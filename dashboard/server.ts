import { Hono } from "hono";
import { serveStatic } from "hono/bun";

const app = new Hono();

// ─────────────────────────────────────────────────────────────────────────────
// MOCK DATA GENERATORS
// Replace these with real Notion / Apify / git calls when ready.
// Data shapes match what the real APIs will return so the swap is trivial.
// ─────────────────────────────────────────────────────────────────────────────

function pad(n: number) {
  return n.toString().padStart(2, "0");
}

function fmtDate(d: Date) {
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
}

// Seeded random so the heatmap is stable between reloads
function seeded(seed: number) {
  let s = seed;
  return () => {
    s = (s * 9301 + 49297) % 233280;
    return s / 233280;
  };
}

function generateHeatmap() {
  const rand = seeded(424242);
  const today = new Date();
  const data: { date: string; count: number }[] = [];

  for (let i = 364; i >= 0; i--) {
    const d = new Date(today);
    d.setDate(d.getDate() - i);
    const r = rand();
    let count = 0;

    if (i < 28) {
      // Last 28 days: hot streak
      count = r < 0.92 ? (r < 0.25 ? 3 : r < 0.55 ? 2 : 1) : 0;
    } else if (i < 90) {
      // Past 90: solid consistency
      count = r < 0.7 ? (r < 0.2 ? 2 : 1) : 0;
    } else if (i < 200) {
      // Mid-year: ramping up
      count = r < 0.5 ? 1 : 0;
    } else {
      // Beginning of year: sparse
      count = r < 0.25 ? 1 : 0;
    }

    data.push({ date: fmtDate(d), count });
  }

  return data;
}

function computeStreak(heatmap: { date: string; count: number }[]) {
  let current = 0;
  let longest = 0;
  let running = 0;
  for (const day of heatmap) {
    if (day.count > 0) {
      running++;
      longest = Math.max(longest, running);
    } else {
      running = 0;
    }
  }
  // current streak — count from end backwards
  for (let i = heatmap.length - 1; i >= 0; i--) {
    if (heatmap[i].count > 0) current++;
    else break;
  }
  const total = heatmap.reduce((sum, d) => sum + d.count, 0);
  return { current, longest, total };
}

function generateStandup() {
  const today = new Date();
  const heatmap = generateHeatmap();
  const { current, longest, total } = computeStreak(heatmap);

  return {
    date: fmtDate(today),
    dayOfWeek: today.toLocaleDateString("en-US", { weekday: "long" }).toUpperCase(),
    weekNumber: Math.ceil(
      (today.getDate() + new Date(today.getFullYear(), today.getMonth(), 1).getDay()) / 7,
    ),
    currentStreak: current,
    longestStreak: longest,
    totalThisYear: total,
    queueDepth: 8,
    todaysTarget: {
      filming: 3,
      scripts: ["Why 95% of creators stay in 200-view jail", "The $0 → $10k creator path", "Why I fired my editor"],
    },
    topLastWeek: {
      title: "The 3 things broke creators get wrong",
      views: 47318,
      engagement: 8.4,
      postedDate: "2026-04-24",
    },
    pipelineGaps: ["Need 4 more BOF scripts", "No reels filmed for Friday"],
  };
}

function generatePipeline() {
  return {
    stages: [
      { name: "IDEA", count: 24, accent: "dim" },
      { name: "SCRIPTED", count: 11, accent: "dim" },
      { name: "FILMED", count: 6, accent: "warn" },
      { name: "EDITED", count: 4, accent: "warn" },
      { name: "SCHEDULED", count: 9, accent: "primary" },
      { name: "POSTED", count: 247, accent: "primary" },
    ],
    categoryMix: { TOF: 42, MOF: 31, BOF: 27 },
  };
}

function generatePerformance() {
  const rand = seeded(1337);
  const today = new Date();
  const dailyViews: { date: string; views: number }[] = [];

  for (let i = 29; i >= 0; i--) {
    const d = new Date(today);
    d.setDate(d.getDate() - i);
    const base = 8000 + rand() * 12000;
    const spike = rand() < 0.1 ? rand() * 40000 : 0;
    dailyViews.push({ date: fmtDate(d), views: Math.round(base + spike) });
  }

  return {
    dailyViews,
    topReels: [
      { rank: 1, title: "Why broke creators stay in 200-view jail", views: 84210, engagement: 11.2, category: "TOF", postedDate: "2026-04-12" },
      { rank: 2, title: "The 3 reasons your reels flop (it's not the algorithm)", views: 67882, engagement: 9.8, category: "TOF", postedDate: "2026-04-19" },
      { rank: 3, title: "I made $0 from content for 2 years. Then I did this.", views: 53104, engagement: 12.1, category: "MOF", postedDate: "2026-04-08" },
      { rank: 4, title: "Why I fired my editor and replaced him with Claude", views: 47318, engagement: 8.4, category: "MOF", postedDate: "2026-04-24" },
      { rank: 5, title: "How Albert went from 800 followers to 47k in 90 days", views: 42007, engagement: 10.7, category: "BOF", postedDate: "2026-04-22" },
    ],
    totalViews: 1284902,
    avgEngagement: 9.2,
    bestDay: "TUE",
    bestTime: "11:00 AM",
  };
}

function generateInsights() {
  return [
    { type: "objection", text: "I don't have time to post every day — I'm running my actual business.", call: "Cole Baker", date: "2026-04-02", category: "MOF" },
    { type: "win", text: "Albert went from 800 to 47k followers in 90 days using the system.", call: "Internal note", date: "2026-04-15", category: "BOF" },
    { type: "pain", text: "I've been stuck at 200 views for 8 months. I don't know what's broken.", call: "Conaugh & McKenna", date: "2026-04-17", category: "TOF" },
    { type: "objection", text: "$6k feels steep. Why not start with the Skool community?", call: "Albert Wang", date: "2026-03-12", category: "BOF" },
    { type: "pain", text: "All my revenue is from ads. If Meta sneezes, I'm done.", call: "Cole Baker", date: "2026-04-02", category: "MOF" },
    { type: "win", text: "Closed 3 calls last week — all from a single MOF reel.", call: "Internal note", date: "2026-04-28", category: "BOF" },
  ];
}

function generateRecentPosts() {
  const today = new Date();
  const titles = [
    { title: "Why 95% of creators stay broke", category: "TOF", platform: "IG" },
    { title: "I quit my agency to do this full-time", category: "MOF", platform: "IG" },
    { title: "The Creator Accelerator just hit 10 spots", category: "BOF", platform: "IG" },
    { title: "Stop posting 3x a day. Do this instead.", category: "TOF", platform: "YT" },
    { title: "My exact AI content workflow", category: "MOF", platform: "IG" },
    { title: "Albert's 90-day transformation", category: "BOF", platform: "IG" },
    { title: "Why your hooks are dead on arrival", category: "TOF", platform: "IG" },
    { title: "The $0 organic playbook", category: "MOF", platform: "TT" },
    { title: "I built this dashboard in one night", category: "MOF", platform: "IG" },
    { title: "Behind the scenes: filming day prep", category: "MOF", platform: "IG" },
  ];

  const rand = seeded(99);
  return titles.map((t, i) => {
    const d = new Date(today);
    d.setDate(d.getDate() - i);
    return {
      date: fmtDate(d),
      slug: t.title.toLowerCase().replace(/[^a-z0-9]+/g, "-").slice(0, 40),
      title: t.title,
      category: t.category,
      platform: t.platform,
      views: Math.round(5000 + rand() * 80000),
    };
  });
}

// ─────────────────────────────────────────────────────────────────────────────
// API ROUTES
// ─────────────────────────────────────────────────────────────────────────────

app.get("/api/heatmap", (c) => c.json(generateHeatmap()));
app.get("/api/standup", (c) => c.json(generateStandup()));
app.get("/api/pipeline", (c) => c.json(generatePipeline()));
app.get("/api/performance", (c) => c.json(generatePerformance()));
app.get("/api/insights", (c) => c.json(generateInsights()));
app.get("/api/recent-posts", (c) => c.json(generateRecentPosts()));

// ─────────────────────────────────────────────────────────────────────────────
// STATIC
// ─────────────────────────────────────────────────────────────────────────────

app.use("/*", serveStatic({ root: "./public" }));
app.get("/", serveStatic({ path: "./public/index.html" }));

const port = 3000;
console.log(`╭─────────────────────────────────────────╮`);
console.log(`│  CONTENT OS · DASHBOARD                 │`);
console.log(`│  → http://localhost:${port}                │`);
console.log(`╰─────────────────────────────────────────╯`);

export default {
  port,
  fetch: app.fetch,
};
