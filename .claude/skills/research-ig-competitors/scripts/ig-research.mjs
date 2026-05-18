#!/usr/bin/env node
import { chromium } from "playwright-core";
import fs from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const PROJECT_ROOT = path.resolve(new URL("../../../../", import.meta.url).pathname);
const DEFAULT_OUTPUT_DIR = path.join(PROJECT_ROOT, "research");

const args = parseArgs(process.argv.slice(2));
if (args.help) {
  console.log(`Usage:
  npm run research:ig
  npm run research:ig -- nick_saraev minolee.mp4 chase.h.ai
  npm run research:ig -- --all
  npm run research:ig -- --handles 5 --top 3 --scan 12

Options:
  --all                 Scrape every Instagram handle in competitor-list.md
  --handles <n>         Number of competitor-list handles to scrape. Default: 3
  --top <n>             Reels per handle to hydrate/report. Default: 3
  --scan <n>            Recent non-pinned grid reels to consider. Default: 12
  --profile-dir <path>  Optional Chrome profile for debugging. Default: ephemeral session
  --output <path>       Report path. Default: research/IG-Competitor-Research_YYYY-MM-DD.md
`);
  process.exit(0);
}
const today = new Date().toISOString().slice(0, 10);
const outputPath = path.resolve(
  args.output || path.join(DEFAULT_OUTPUT_DIR, `IG-Competitor-Research_${today}.md`),
);

const config = {
  top: numberArg(args.top, 3),
  scan: numberArg(args.scan, 12),
  profileDir: optionalPath(args.profileDir || process.env.IG_CHROME_PROFILE),
  outputPath,
  handles: await resolveHandles(args),
};

if (!config.handles.length) {
  throw new Error("No Instagram handles found. Add handles to competitor-list.md or pass them as args.");
}

await fs.mkdir(path.dirname(config.outputPath), { recursive: true });

const browser = config.profileDir ? null : await chromium.launch(chromeLaunchOptions());
const context = config.profileDir
  ? await launchPersistentContext(config.profileDir)
  : await browser.newContext({ viewport: { width: 1280, height: 900 } });

try {
  const page = context.pages()[0] || await context.newPage();
  await page.bringToFront();

  const results = [];
  for (const handle of config.handles) {
    console.log(`\n== @${handle}: scanning reels grid`);
    try {
      const gridReels = await scrapeGrid(page, handle, config.scan, config.top);
      console.log(`   found ${gridReels.length} candidate reels`);

      const reels = [];
      for (const reel of gridReels) {
        console.log(`   hydrating ${reel.url}`);
        reels.push(await hydrateReel(page, handle, reel));
      }
      results.push({ handle, reels });
    } catch (error) {
      results.push({ handle, error: error.message });
      console.warn(`   failed: ${error.message}`);
    }
  }

  const report = buildReport(results);
  await fs.writeFile(config.outputPath, report, "utf8");
  console.log(`\nWrote ${config.outputPath}`);
} finally {
  await context.close();
  if (browser) await browser.close();
}

function parseArgs(argv) {
  const parsed = { _: [] };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (!arg.startsWith("--")) {
      parsed._.push(cleanHandle(arg));
      continue;
    }
    const [rawKey, inlineValue] = arg.slice(2).split("=", 2);
    const key = rawKey.replace(/-([a-z])/g, (_, c) => c.toUpperCase());
    if (inlineValue !== undefined) {
      parsed[key] = inlineValue;
    } else if (["all", "help"].includes(key)) {
      parsed[key] = true;
    } else {
      parsed[key] = argv[i + 1];
      i += 1;
    }
  }
  return parsed;
}

function numberArg(value, fallback) {
  const n = Number.parseInt(value, 10);
  return Number.isFinite(n) && n > 0 ? n : fallback;
}

function optionalPath(value) {
  return value ? path.resolve(value) : null;
}

async function resolveHandles(args) {
  if (args._.length) return dedupe(args._.map(cleanHandle).filter(Boolean));

  const competitorList = await fs.readFile(path.join(PROJECT_ROOT, "competitor-list.md"), "utf8");
  const instagramSection = competitorList.split(/^##\s+/m)
    .find((section) => section.trimStart().startsWith("Instagram"));
  if (!instagramSection) return [];

  const handles = dedupe(
    [...instagramSection.matchAll(/instagram\.com\/([A-Za-z0-9._]+)/g)]
      .map((match) => cleanHandle(match[1])),
  );

  return args.all ? handles : handles.slice(0, numberArg(args.handles, 3));
}

function cleanHandle(value) {
  return String(value || "")
    .trim()
    .replace(/^@/, "")
    .replace(/^https?:\/\/(?:www\.)?instagram\.com\//, "")
    .replace(/\/.*$/, "");
}

function dedupe(values) {
  return [...new Set(values)];
}

function chromeLaunchOptions() {
  return {
    channel: "chrome",
    headless: false,
    args: ["--disable-blink-features=AutomationControlled"],
  };
}

async function launchPersistentContext(profileDir) {
  await fs.mkdir(profileDir, { recursive: true });
  return chromium.launchPersistentContext(profileDir, {
    ...chromeLaunchOptions(),
    viewport: { width: 1280, height: 900 },
  });
}

async function scrapeGrid(page, handle, scanCount, topCount) {
  const url = `https://www.instagram.com/${handle}/reels/`;
  await page.goto(url, { waitUntil: "domcontentloaded", timeout: 60000 });
  await page.bringToFront();
  await page.waitForTimeout(8000);

  const reels = await page.evaluate((limit) => {
    const parseViews = (raw) => {
      const compact = String(raw || "").replace(/,/g, "").match(/(\d+(?:\.\d+)?)\s*([KMB])\b/i);
      if (compact) {
        return Number.parseFloat(compact[1]) * ({ K: 1e3, M: 1e6, B: 1e9 }[compact[2].toUpperCase()]);
      }
      const plain = String(raw || "").replace(/,/g, "").match(/\b(\d{3,})\b/);
      return plain ? Number.parseInt(plain[1], 10) : null;
    };

    const seen = new Set();
    return [...document.querySelectorAll('a[href*="/reel/"]')]
      .map((a) => {
        const href = new URL(a.getAttribute("href"), location.origin).href;
        const shortcode = href.match(/\/reel\/([^/?#]+)/)?.[1] || href;
        const text = a.innerText.trim();
        return {
          shortcode,
          url: href,
          text,
          views: parseViews(text),
          pinned: Boolean(a.querySelector('svg[aria-label="Pinned post icon"]')),
        };
      })
      .filter((reel) => {
        if (seen.has(reel.shortcode)) return false;
        seen.add(reel.shortcode);
        return !reel.pinned;
      })
      .slice(0, limit);
  }, scanCount);

  if (reels.length < topCount) {
    throw new Error(`Only found ${reels.length} non-pinned reels on @${handle}; IG may not have hydrated.`);
  }

  const withViews = reels.filter((reel) => Number.isFinite(reel.views));
  if (withViews.length >= topCount) {
    return withViews.sort((a, b) => b.views - a.views).slice(0, topCount);
  }

  console.warn(`   only ${withViews.length} grid items had visible view counts; falling back to recent order`);
  return reels.slice(0, topCount);
}

async function hydrateReel(page, handle, reel) {
  await page.goto(reel.url, { waitUntil: "domcontentloaded", timeout: 60000 });
  await page.waitForTimeout(3000);

  const data = await page.evaluate(() => {
    const meta = (selector) => document.querySelector(selector)?.content || "";
    const ogTitle = meta('meta[property="og:title"]');
    const ogDescription = meta('meta[property="og:description"]');
    const titleCaption = ogTitle.match(/: "([\s\S]*)"$/)?.[1] || "";
    const article = document.querySelector("article")?.innerText || "";
    const caption = titleCaption || article.split("\n").filter(Boolean).slice(0, 12).join("\n");

    return {
      ogTitle,
      ogDescription,
      caption,
      likes: extractMetric(ogDescription, "likes"),
      comments: extractMetric(ogDescription, "comments"),
      date: ogDescription.match(/\bon\s+([A-Z][a-z]+\s+\d{1,2},\s+\d{4})/)?.[1] || null,
    };

    function extractMetric(text, label) {
      return text.match(new RegExp(`([\\d.,]+\\s*[KMB]?)\\s+${label}?`, "i"))?.[1]?.replace(/\s+/g, "") || null;
    }
  });

  return {
    handle,
    url: reel.url,
    views: reel.views,
    viewsText: humanNumber(reel.views) || reel.text,
    likes: data.likes,
    comments: data.comments,
    date: data.date,
    caption: data.caption || reel.url,
    hook: firstLine(data.caption || reel.url),
  };
}

function buildReport(results) {
  const scraped = results.filter((r) => r.reels?.length);
  const errors = results.filter((r) => r.error);
  const allReels = scraped.flatMap((r) => r.reels.map((reel) => ({ ...reel, handle: r.handle })))
    .sort((a, b) => (b.views || 0) - (a.views || 0));

  const pattern = [
    `Scraped ${allReels.length} reels across ${scraped.length} accounts with a headed logged-out Chrome session.`,
    errors.length ? `Errors: ${errors.map((e) => `@${e.handle} (${e.error})`).join(", ")}.` : "No scrape errors.",
    "Look for repeated hook mechanics, comment-keyword CTAs, named-tool stacking, and formats with unusually high like/comment rates.",
  ].join(" ");

  const lines = [
    "# Competitor Research — Top Reels",
    "",
    `**Generated:** ${today} | **Accounts scraped:** ${scraped.length} | **Reels in report:** ${allReels.length} (top ${config.top} by views per handle)`,
    "",
    `> **Pattern:** ${pattern}`,
    "",
    "---",
    "",
  ];

  allReels.forEach((reel, index) => {
    const likes = parseMetric(reel.likes);
    const comments = parseMetric(reel.comments);
    const likeRate = rate(likes, reel.views);
    const commentRate = rate(comments, reel.views);
    const topic = classifyTopic(reel.caption);
    const cta = classifyCta(reel.caption);

    lines.push(
      `### ${index + 1}. [${escapeLinkText(reel.hook)}](${reel.url}) — @${reel.handle}`,
      "",
      `\`${humanNumber(reel.views) || "unknown"} views · ${reel.likes || "unknown"} likes · ${reel.comments || "unknown"} comments\` · ${likeRate} like rate · ${commentRate} comment rate · posted ${reel.date || "unknown"}`,
      "",
      `**Topic:** ${topic} · **CTA:** ${cta}`,
      "",
      `**Why it worked:** ${whyItWorked(reel.caption, topic, cta)}`,
      "",
      blockquote(reel.caption),
      "",
      "---",
      "",
    );
  });

  return `${lines.join("\n").trim()}\n`;
}

function firstLine(text) {
  return String(text || "").split(/\n+/).map((line) => line.trim()).find(Boolean)?.slice(0, 120) || "Instagram reel";
}

function blockquote(text) {
  return String(text || "")
    .split("\n")
    .map((line) => `> ${line}`)
    .join("\n");
}

function parseMetric(value) {
  if (!value) return null;
  const match = String(value).replace(/,/g, "").match(/([\d.]+)\s*([KMB])?/i);
  if (!match) return null;
  return Number.parseFloat(match[1]) * ({ K: 1e3, M: 1e6, B: 1e9 }[match[2]?.toUpperCase()] || 1);
}

function humanNumber(value) {
  if (!Number.isFinite(value)) return null;
  if (value >= 1e9) return `${trim(value / 1e9)}B`;
  if (value >= 1e6) return `${trim(value / 1e6)}M`;
  if (value >= 1e3) return `${trim(value / 1e3)}K`;
  return String(Math.round(value));
}

function trim(value) {
  return Number(value.toFixed(1)).toString();
}

function rate(numerator, denominator) {
  if (!Number.isFinite(numerator) || !Number.isFinite(denominator) || denominator <= 0) return "unknown";
  return `${((numerator / denominator) * 100).toFixed(1)}%`;
}

function classifyTopic(caption) {
  const text = caption.toLowerCase();
  if (/tutorial|guide|how to|step|build|using|tools?/.test(text)) return "Tutorial";
  if (/hot take|truth|nobody|everyone|wrong|mistake/.test(text)) return "Hot take";
  if (/day in|behind|business|doing w|building/.test(text)) return "Build-in-public";
  if (/story|i used to|when i|my first/.test(text)) return "Story";
  if (/comment|free|access|get/.test(text)) return "Education";
  return "Education";
}

function classifyCta(caption) {
  const text = caption.toLowerCase();
  if (/comment\s+["'“”‘’]?[\w. -]+["'“”‘’]?|drop .*comment/.test(text)) return "Comment-bait";
  if (/\bdm\b|message me|send me/.test(text)) return "DM";
  if (/save this|save/.test(text)) return "Save-bait";
  if (/follow/.test(text)) return "Follow-bait";
  return "None";
}

function whyItWorked(caption, topic, cta) {
  const hook = firstLine(caption);
  if (cta === "Comment-bait") {
    return `Comment-keyword CTA turns interest into an immediate action, while the hook promises a specific resource: "${hook}".`;
  }
  if (topic === "Tutorial") {
    return `Specific named tools and a clear how-to promise make it feel save-worthy from the first line: "${hook}".`;
  }
  if (topic === "Hot take") {
    return `Contrarian framing creates curiosity before the viewer knows the full argument: "${hook}".`;
  }
  return `The hook creates an open loop and gives viewers a concrete reason to keep watching: "${hook}".`;
}

function escapeLinkText(text) {
  return String(text).replace(/[[\]]/g, "");
}
