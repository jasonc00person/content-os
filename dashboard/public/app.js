// ═════════════════════════════════════════════════════════════════════════════
// CONTENT OS · DASHBOARD · CLIENT
// ═════════════════════════════════════════════════════════════════════════════

const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => Array.from(document.querySelectorAll(sel));

// ─── helpers ───────────────────────────────────────────────────────────────
const fmtNum = (n) => {
  if (n >= 1_000_000) return (n / 1_000_000).toFixed(1).replace(/\.0$/, "") + "M";
  if (n >= 1_000) return (n / 1_000).toFixed(1).replace(/\.0$/, "") + "K";
  return n.toString();
};

const fmtPct = (n) => n.toFixed(1) + "%";

const levelFor = (count) => {
  if (count <= 0) return 0;
  if (count === 1) return 1;
  if (count === 2) return 2;
  if (count === 3) return 3;
  return 4;
};

// animated counter (uses setInterval — RAF is throttled in non-focused tabs)
function animateCount(el, target, duration = 900, suffix = "") {
  if (!el) return;
  const start = Date.now();
  const isFloat = !Number.isInteger(target);
  const step = 16;
  const id = setInterval(() => {
    const p = Math.min(1, (Date.now() - start) / duration);
    const eased = 1 - Math.pow(1 - p, 3);
    const v = target * eased;
    el.textContent = (isFloat ? v.toFixed(1) : Math.round(v).toLocaleString()) + suffix;
    if (p >= 1) clearInterval(id);
  }, step);
}

// ─── topbar clock ──────────────────────────────────────────────────────────
function updateTopbar() {
  const now = new Date();
  const weekday = now.toLocaleDateString("en-US", { weekday: "short" }).toUpperCase();
  const month = now.toLocaleDateString("en-US", { month: "short" }).toUpperCase();
  const day = now.getDate();
  $("#topbar-date").textContent = `${weekday} · ${month} ${day}`;

  const startOfYear = new Date(now.getFullYear(), 0, 1);
  const dayOfYear = Math.floor((now - startOfYear) / 86400000);
  const week = Math.ceil((dayOfYear + startOfYear.getDay() + 1) / 7);
  $("#topbar-week").textContent = `WK ${week.toString().padStart(2, "0")}`;

  const hh = String(now.getHours()).padStart(2, "0");
  const mm = String(now.getMinutes()).padStart(2, "0");
  const ss = String(now.getSeconds()).padStart(2, "0");
  $("#topbar-time").textContent = `${hh}:${mm}:${ss}`;
}
updateTopbar();
setInterval(updateTopbar, 1000);

// ─── HEATMAP ───────────────────────────────────────────────────────────────
async function renderHeatmap() {
  const data = await fetch("/api/heatmap").then((r) => r.json());

  const container = $("#heatmap-container");
  container.innerHTML = "";

  // Layout: pad the start so first column aligns to Sunday (day 0).
  // We render 53 columns of 7 cells each.
  const firstDate = new Date(data[0].date);
  const padStart = firstDate.getDay(); // 0=Sun, 6=Sat
  const cells = [...Array(padStart).fill(null), ...data];

  // wrap with row labels
  const wrap = document.createElement("div");
  wrap.className = "heatmap-wrap";

  const rowLabels = document.createElement("div");
  rowLabels.className = "heatmap-row-labels";
  rowLabels.innerHTML = `
    <span></span><span>MON</span><span></span><span>WED</span>
    <span></span><span>FRI</span><span></span>
  `;
  wrap.appendChild(rowLabels);

  // grid + month labels stacked
  const gridWrap = document.createElement("div");
  gridWrap.style.flex = "1";

  // month labels — derive from data: find each month's first appearance, position by column
  const monthLabels = document.createElement("div");
  monthLabels.className = "heatmap-month-labels";
  const monthMap = {};
  const parseLocalDate = (s) => {
    const [y, m, day] = s.split("-").map(Number);
    return new Date(y, m - 1, day);
  };

  cells.forEach((c, i) => {
    if (!c) return;
    const d = parseLocalDate(c.date);
    const colIdx = Math.floor(i / 7);
    const monthKey = `${d.getFullYear()}-${d.getMonth()}`;
    if (!(monthKey in monthMap)) {
      monthMap[monthKey] = { col: colIdx, label: d.toLocaleDateString("en-US", { month: "short" }).toUpperCase() };
    }
  });

  // Build month label row using flex with proportional widths based on col positions
  const months = Object.values(monthMap);
  const totalCols = Math.ceil(cells.length / 7);
  let lastCol = 0;
  months.forEach((m, idx) => {
    const span = document.createElement("span");
    span.textContent = m.label;
    const nextCol = months[idx + 1] ? months[idx + 1].col : totalCols;
    span.style.flex = `${nextCol - m.col}`;
    monthLabels.appendChild(span);
  });
  gridWrap.appendChild(monthLabels);

  // grid
  const grid = document.createElement("div");
  grid.className = "heatmap-grid";
  const todayStr = new Date().toISOString().split("T")[0];

  cells.forEach((c, i) => {
    const cell = document.createElement("div");
    cell.className = "heatmap-cell";
    if (c) {
      cell.dataset.level = levelFor(c.count);
      cell.dataset.date = c.date;
      cell.dataset.count = c.count;
      if (c.date === todayStr) cell.classList.add("today");
    } else {
      cell.style.visibility = "hidden";
    }
    cell.style.animationDelay = `${(i / cells.length) * 0.5}s`;
    grid.appendChild(cell);
  });

  // tooltip handlers
  const tip = $("#heatmap-tooltip");
  grid.addEventListener("mouseover", (e) => {
    if (!e.target.classList.contains("heatmap-cell") || !e.target.dataset.date) return;
    const { date, count } = e.target.dataset;
    const d = parseLocalDate(date);
    const fmt = d.toLocaleDateString("en-US", { weekday: "short", month: "short", day: "numeric" }).toUpperCase();
    tip.textContent = `${count} POST${count == 1 ? "" : "S"} · ${fmt}`;
    tip.classList.add("visible");
  });
  grid.addEventListener("mousemove", (e) => {
    if (!e.target.classList.contains("heatmap-cell") || !e.target.dataset.date) return;
    const rect = e.target.getBoundingClientRect();
    tip.style.left = `${rect.left + rect.width / 2}px`;
    tip.style.top = `${rect.top}px`;
  });
  grid.addEventListener("mouseleave", () => tip.classList.remove("visible"));

  gridWrap.appendChild(grid);
  wrap.appendChild(gridWrap);
  container.appendChild(wrap);
}

// ─── STANDUP ───────────────────────────────────────────────────────────────
async function renderStandup() {
  const s = await fetch("/api/standup").then((r) => r.json());

  animateCount($("#stat-streak"), s.currentStreak);
  $("#stat-longest").textContent = s.longestStreak;
  animateCount($("#stat-total"), s.totalThisYear);
  $("#stat-queue").textContent = s.queueDepth;

  $("#standup-filming-count").textContent = s.todaysTarget.filming;

  const scriptList = $("#standup-scripts");
  scriptList.innerHTML = s.todaysTarget.scripts
    .map(
      (script, i) => `
    <li class="flex items-start gap-3 text-[14px] text-ink/90 leading-snug rise rise-delay-${Math.min(i + 1, 4)}">
      <span class="font-mono text-[10px] text-dim mt-1.5">0${i + 1}</span>
      <span class="flex-1">${script}</span>
    </li>`,
    )
    .join("");

  $("#top-perf-title").textContent = `"${s.topLastWeek.title}"`;
  animateCount($("#top-perf-views"), s.topLastWeek.views);
  $("#top-perf-eng").textContent = fmtPct(s.topLastWeek.engagement);

  const gapsList = $("#standup-gaps");
  gapsList.innerHTML = s.pipelineGaps
    .map((g) => `<li class="flex items-start gap-2"><span class="text-warn mt-0.5">▸</span><span>${g}</span></li>`)
    .join("");
}

// ─── PIPELINE ──────────────────────────────────────────────────────────────
async function renderPipeline() {
  const p = await fetch("/api/pipeline").then((r) => r.json());

  // Active stages — POSTED rendered separately as a lifetime stat
  const active = p.stages.filter((s) => s.name !== "POSTED");
  const posted = p.stages.find((s) => s.name === "POSTED");
  const max = Math.max(...active.map((s) => s.count));
  const stages = $("#pipeline-stages");
  stages.innerHTML =
    active
      .map(
        (stage, i) => `
    <div class="pipeline-row rise rise-delay-${Math.min(i + 1, 4)}">
      <span class="text-dim">${stage.name}</span>
      <div class="pipeline-bar">
        <div class="pipeline-bar-fill ${stage.accent}" data-target="${(stage.count / max) * 100}"></div>
      </div>
      <span class="pipeline-count">${stage.count}</span>
    </div>`,
      )
      .join("") +
    `
    <div class="posted-stat">
      <div class="flex items-baseline justify-between">
        <span class="font-mono text-[10px] uppercase tracking-[0.3em] text-dim">SHIPPED · LIFETIME</span>
        <span class="font-serif italic text-4xl text-signal leading-none">${posted.count}</span>
      </div>
    </div>`;

  // Trigger bar fills after a tick (CSS transition handles the animation)
  setTimeout(() => {
    $$(".pipeline-bar-fill").forEach((el) => {
      el.style.width = el.dataset.target + "%";
    });
  }, 50);

  // category mix
  const total = p.categoryMix.TOF + p.categoryMix.MOF + p.categoryMix.BOF;
  const mix = $("#category-mix-bar");
  mix.innerHTML = ["TOF", "MOF", "BOF"]
    .map(
      (c) =>
        `<div class="mix-seg" data-cat="${c}" style="width: ${(p.categoryMix[c] / total) * 100}%"></div>`,
    )
    .join("");

  const legend = $("#category-mix-legend");
  legend.innerHTML = ["TOF", "MOF", "BOF"]
    .map(
      (c) => `
    <div class="mix-legend-item">
      <span class="cat-dot" data-cat="${c}"></span>
      <span>${c}</span>
      <b class="ml-auto">${p.categoryMix[c]}%</b>
    </div>`,
    )
    .join("");
}

// ─── PERFORMANCE ───────────────────────────────────────────────────────────
async function renderPerformance() {
  const perf = await fetch("/api/performance").then((r) => r.json());

  animateCount($("#perf-total-views"), perf.totalViews);
  $("#perf-avg-eng").textContent = fmtPct(perf.avgEngagement);
  $("#perf-best-time").textContent = perf.bestTime.replace(":00", "");

  // line chart
  const ctx = $("#views-chart").getContext("2d");
  const grad = ctx.createLinearGradient(0, 0, 0, 200);
  grad.addColorStop(0, "rgba(52, 211, 153, 0.35)");
  grad.addColorStop(1, "rgba(52, 211, 153, 0)");

  new Chart(ctx, {
    type: "line",
    data: {
      labels: perf.dailyViews.map((d) => d.date.slice(5)),
      datasets: [
        {
          data: perf.dailyViews.map((d) => d.views),
          borderColor: "#34d399",
          borderWidth: 1.5,
          backgroundColor: grad,
          fill: true,
          tension: 0.35,
          pointRadius: 0,
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "#fafafa",
          pointHoverBorderColor: "#34d399",
          pointHoverBorderWidth: 2,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          backgroundColor: "#fafafa",
          titleColor: "#0a0a0c",
          bodyColor: "#0a0a0c",
          titleFont: { family: "JetBrains Mono", size: 10, weight: "600" },
          bodyFont: { family: "JetBrains Mono", size: 11, weight: "700" },
          padding: 8,
          cornerRadius: 0,
          displayColors: false,
          callbacks: {
            title: (items) => items[0].label.toUpperCase(),
            label: (ctx) => fmtNum(ctx.raw) + " VIEWS",
          },
        },
      },
      scales: {
        x: {
          grid: { display: false, drawBorder: false },
          ticks: {
            color: "#52525b",
            font: { family: "JetBrains Mono", size: 9 },
            maxRotation: 0,
            autoSkip: true,
            maxTicksLimit: 8,
          },
        },
        y: {
          grid: { color: "rgba(35,35,42,0.6)", drawBorder: false },
          ticks: {
            color: "#52525b",
            font: { family: "JetBrains Mono", size: 9 },
            callback: (v) => fmtNum(v),
            maxTicksLimit: 5,
          },
        },
      },
    },
  });

  // top reels
  const list = $("#top-reels");
  list.innerHTML = perf.topReels
    .map(
      (r, i) => `
    <li class="reel-row rise rise-delay-${Math.min(i + 1, 4)}">
      <span class="reel-rank">${String(r.rank).padStart(2, "0")}</span>
      <span class="reel-title">
        <span class="cat-dot" data-cat="${r.category}"></span>${r.title}
      </span>
      <span class="reel-views">${fmtNum(r.views)}</span>
      <span class="reel-eng">${fmtPct(r.engagement)}</span>
    </li>`,
    )
    .join("");
}

// ─── INSIGHTS ──────────────────────────────────────────────────────────────
async function renderInsights() {
  const data = await fetch("/api/insights").then((r) => r.json());
  const feed = $("#insights-feed");
  feed.innerHTML = data
    .map(
      (it, i) => `
    <div class="insight-card rise rise-delay-${Math.min(i + 1, 4)}" data-type="${it.type}">
      <div class="insight-meta">
        <span class="text-${it.type === "objection" ? "alert" : it.type === "win" ? "signal" : "warn"}">${it.type.toUpperCase()}</span>
        <span class="text-dimmer">·</span>
        <span>${it.call}</span>
        <span class="text-dimmer">·</span>
        <span>${it.date}</span>
        <span class="ml-auto"><span class="cat-dot" data-cat="${it.category}"></span>${it.category}</span>
      </div>
      <div class="insight-text">"${it.text}"</div>
    </div>`,
    )
    .join("");
}

// ─── RECENT POSTS ──────────────────────────────────────────────────────────
async function renderRecentPosts() {
  const posts = await fetch("/api/recent-posts").then((r) => r.json());
  const wrap = $("#recent-posts");
  wrap.innerHTML = posts
    .map(
      (p, i) => `
    <div class="post-card rise rise-delay-${Math.min(Math.floor(i / 2) + 1, 4)}">
      <span class="platform-tag">${p.platform}</span>
      <div class="font-mono text-[10px] uppercase tracking-widest text-dim mb-3">${p.date}</div>
      <div class="text-[15px] leading-snug font-medium mb-5 min-h-[44px]">${p.title}</div>
      <div class="flex items-center justify-between border-t border-border pt-3">
        <span class="font-mono text-[10px] uppercase tracking-widest text-dim">
          <span class="cat-dot" data-cat="${p.category}"></span>${p.category}
        </span>
        <span class="font-mono text-sm font-bold text-signal">${fmtNum(p.views)}</span>
      </div>
    </div>`,
    )
    .join("");
}

// ─── STAT: BEST DAY pulled from performance ────────────────────────────────
async function renderBestDayStat() {
  const perf = await fetch("/api/performance").then((r) => r.json());
  $("#stat-bestday").textContent = perf.bestDay;
}

// ─── boot ──────────────────────────────────────────────────────────────────
(async function boot() {
  await Promise.all([
    renderHeatmap(),
    renderStandup(),
    renderPipeline(),
    renderPerformance(),
    renderInsights(),
    renderRecentPosts(),
    renderBestDayStat(),
  ]);
})();
