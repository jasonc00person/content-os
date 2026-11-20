// ig-feed-research page helpers — home-feed loop (re-calibrated live 2026-11-02).
// Paste this WHOLE file into one javascript_tool call after EVERY navigation
// (page loads wipe window.* state). Then call the helpers in later calls.
//
//   __feed()               -> one row per article currently in the DOM, cached on window.__rows:
//                             "user | SUGGESTED|followed|AD | reel|carousel|post | L<likes> C<comments> | flags | caption"
//                             flags: fav (account is a favorite), saved (post already saved)
//   __more(px)             -> scroll the feed down by px (default 1400), for the lazy loader
//   __feedDismiss(key,mode)-> 'post' = Not interested; 'account' = Not interested, then
//                             "Don't suggest posts from <user>" on the hidden-post card
//   __save(key)            -> click the post's Save bookmark (positive signal)
//   __favorite(key)        -> menu -> "Add to favorites" (followed accounts only)
//   every action returns  'key:ok' | 'key:ok-account' | 'key:already' | 'key:no-item'
//                          | 'key:ad' (refused) | 'key:no-btn' | 'key:no-entry'
//
// key = the username, or "user|caption words" when the same account has two posts
// loaded. The feed VIRTUALIZES: articles leave the DOM as you scroll and indexes shift,
// so actions resolve the post by key at call time, never by index.
//
// IG class names are minified and rotate — every selector here is structural:
// article/svg aria-label/innerText. Menus are NOT role=dialog — entries are found by
// scanning visible childless text leaves OUTSIDE any article. The hidden-post card
// ("Post hidden" + "Don't suggest posts from X") also renders outside the article now.
// NEVER return raw hrefs/query strings/innerHTML, and never return "a=1 b=2"-shaped
// text either — the harness safety filter blocks the whole result. Cleaned text only.

const clean = s => (s||'').replace(/[^\w\s.,:'&()!?$%+@#/|-]/g,'').trim();
const vis = e => { const r = e.getBoundingClientRect(); return r.width>0 && r.height>0 && r.top < innerHeight && r.bottom > 0; };
const wait = ms => new Promise(r=>setTimeout(r,ms));

// The page scrolls on <body> (2026-11 layout), not documentElement; pick whichever
// one actually overflows so this survives IG flipping it back.
const scroller = () => [document.body, document.documentElement]
  .find(e => e.scrollHeight > e.clientHeight + 50 && /(auto|scroll)/.test(getComputedStyle(e).overflowY))
  || document.scrollingElement;

const lines = el => (el.innerText||'').split('\n').map(clean).filter(Boolean);
const userOf = el => (lines(el)[0]||'?').slice(0,30);

// Counts sit in the sibling right after each action button's wrapper span.
const count = (el, label) => {
  let p = el.querySelector(`svg[aria-label="${label}"]`);
  for (let i = 0; i < 6 && p; i++) {
    p = p.parentElement;
    const n = p && p.nextElementSibling && (p.nextElementSibling.innerText||'').trim();
    if (n && /^[\d.,]+[KM]?$/.test(n)) return n;
  }
  return '?';
};

const status = el => {
  const head = lines(el).slice(0,6);
  if (head.includes('Ad') || head.includes('Sponsored')) return 'AD';
  // Suggested posts carry the "Suggested for you" line or a bare Follow button in the header.
  if ((el.innerText||'').includes('Suggested for you') || head.includes('Follow')) return 'SUGGESTED';
  return 'followed';
};

const kindOf = el => el.querySelector('svg[aria-label="Next"], button[aria-label="Next"]') ? 'carousel'
                   : el.querySelector('video') ? 'reel' : 'post';

window.__feed = () => {
  window.__rows = [...document.querySelectorAll('article')].map(el => {
    const liked = !!el.querySelector('svg[aria-label="Unlike"]');
    const flags = [el.querySelector('svg[aria-label="Favorited"]') && 'fav',
                   el.querySelector('svg[aria-label="Remove"]') && 'saved'].filter(Boolean).join(',') || '-';
    const cap = lines(el).slice(1)
      .filter(l => !/^(Follow|Following|Suggested for you|Original audio|AI content|Verified|more|\d+[dhwm]|1x|[\d.,]+[KM]?)$/i.test(l))
      .join(' ').slice(0,140);
    return [userOf(el), status(el), kindOf(el), 'L'+count(el, liked ? 'Unlike' : 'Like')+' C'+count(el,'Comment'), flags, cap].join(' | ');
  });
  return window.__rows.join('\n');
};

window.__more = async (px) => {
  const s = scroller();
  s.scrollTop += (px || 1400);
  await wait(2000);
  return 'articles ' + document.querySelectorAll('article').length + ', scrolled ' + Math.round(s.scrollTop);
};

const find = key => {
  const [user, words] = key.split('|');
  return [...document.querySelectorAll('article')]
    .find(el => userOf(el) === user && (!words || (el.innerText||'').includes(words)));
};

// No root = scan the document but skip anything inside an <article> (menu entries).
const findEntry = re => {
  const leaf = [...document.querySelectorAll('button, [role="button"], [role="menuitem"], div, span')]
    .find(e => vis(e) && e.children.length === 0 && re.test(clean(e.innerText)) && !e.closest('article'));
  return leaf ? (leaf.closest('[role="button"]') || leaf.closest('button') || leaf) : null;
};

const closeMenu = async () => {
  const c = findEntry(/^Cancel$/);
  if (c) c.click(); else document.dispatchEvent(new KeyboardEvent('keydown', {key:'Escape', bubbles:true}));
  await wait(500);
};

const openMenu = async el => {
  const svg = el.querySelector('svg[aria-label="More options"], svg[aria-label="More"]');
  const btn = svg && (svg.closest('[role="button"]') || svg.closest('button') || svg.parentElement);
  if (!btn) return false;
  el.scrollIntoView({block:'center'});
  await wait(500);
  btn.click();
  await wait(1000);
  return true;
};

window.__feedDismiss = async (key, mode) => {
  const el = find(key);
  if (!el) return key+':no-item';        // already hidden posts leave the article list
  if (status(el) === 'AD') return key+':ad';
  const user = userOf(el);
  if (!await openMenu(el)) return key+':no-btn';
  // "Not interested" = suggested posts (any kind) + followed REELS. Followed
  // carousels/images don't have it: close and move on.
  const entry = findEntry(/^not interested$/i);
  if (!entry) { await closeMenu(); return key+':no-entry'; }
  entry.click();
  await wait(1500);
  if (mode !== 'account') return key+':ok';
  // The hidden-post card offers "Don't suggest posts from <user>" (curly apostrophe
  // stripped by clean -> don.?t). Match the exact username so a neighbouring hidden
  // card for a different account can't be clicked. Never touch its other offer,
  // "Snooze all suggested posts in feed for 30 days": that kills the research surface.
  const esc = user.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const block = findEntry(new RegExp('^don.?t suggest posts from ' + esc + '$', 'i'));
  if (!block) return key+':ok';          // post-level landed; account option absent (followed account)
  block.click();
  await wait(800);
  return key+':ok-account';
};

window.__save = async (key) => {
  const el = find(key);
  if (!el) return key+':no-item';
  if (status(el) === 'AD') return key+':ad';
  if (el.querySelector('svg[aria-label="Remove"]')) return key+':already';
  const svg = el.querySelector('svg[aria-label="Save"]');
  const btn = svg && (svg.closest('[role="button"]') || svg.closest('button') || svg.parentElement);
  if (!btn) return key+':no-btn';
  el.scrollIntoView({block:'center'});
  await wait(500);
  btn.click();
  await wait(1200);
  return key + (find(key) && find(key).querySelector('svg[aria-label="Remove"]') ? ':ok' : ':no-entry');
};

window.__favorite = async (key) => {
  const el = find(key);
  if (!el) return key+':no-item';
  if (status(el) !== 'followed') return key+':no-entry';   // favorites = followed accounts only
  if (el.querySelector('svg[aria-label="Favorited"]')) return key+':already';
  if (!await openMenu(el)) return key+':no-btn';
  const entry = findEntry(/^add to favorites$/i);
  if (!entry) { await closeMenu(); return key+':no-entry'; }
  entry.click();
  await wait(1500);
  await closeMenu();                     // a confirmation toast or the menu may linger
  return key+':ok';
};
'helpers injected'
