import { useState } from "react";

// ══════════════════════════════════════════════════════════════════
//  TOKENIZER
// ══════════════════════════════════════════════════════════════════

const PHONEME_PATTERNS = [
  'gʷʰ','ǵʰ','gʷ','kʷ','gʰ','bʰ','dʰ','ǵ','ḱ',
  'h₁','h₂','h₃','H',
  'r̥','l̥','m̥','n̥',
  'β','ð','ɣʷ','ɣ',
  'ā','ē','ī','ō','ū',
  'ˀ',
];

function tokenize(s) {
  const tokens = [];
  let i = 0;
  while (i < s.length) {
    let matched = false;
    for (const p of PHONEME_PATTERNS) {
      if (s.slice(i).startsWith(p)) {
        tokens.push(p); i += p.length; matched = true; break;
      }
    }
    if (!matched) { tokens.push(s[i]); i++; }
  }
  return tokens;
}

function join(tokens) { return tokens.join(''); }

// ══════════════════════════════════════════════════════════════════
//  CATEGORIES
// ══════════════════════════════════════════════════════════════════

const LARYNGEALS = new Set(['h₁','h₂','h₃','H']);
const VOWELS     = new Set(['a','e','i','o','u','ā','ē','ī','ō','ū']);
const SYL_RES    = new Set(['r̥','l̥','m̥','n̥']);
const DENTALS    = new Set(['t','d','dʰ']);
const VELARS     = new Set(['k','g','gʰ','kʷ','gʷ','gʷʰ']);
const VOICED_C   = new Set(['b','d','g','gʷ','β','ð','ɣ','ɣʷ','m','n','l','r','w','y','j','v','z']);

const isVowel     = t => VOWELS.has(t);
const isLaryngeal = t => LARYNGEALS.has(t);
const isGlottal   = t => t === 'ˀ';
const isSylRes    = t => SYL_RES.has(t);
const isDental    = t => DENTALS.has(t);
const isVelar     = t => VELARS.has(t);
const isConsonant = t => t !== '-' && !isVowel(t) && !isLaryngeal(t) && !isGlottal(t);
const isVoiced    = t => VOICED_C.has(t) || isVowel(t);

const LENGTHEN = { a:'ā', e:'ē', i:'ī', o:'ō', u:'ū' };
const lengthen = v => LENGTHEN[v] || v;

const SHORTEN = { 'ā':'a', 'ē':'e', 'ī':'i', 'ō':'o', 'ū':'u' };
const shorten = v => SHORTEN[v] || v;

// Detect whether accent falls on first syllable, a later syllable, or nowhere
// Returns: 'first' | 'later' | 'none'
function detectAccentPosition(raw) {
  const nfd = raw.normalize('NFD');
  const VOWEL_CHARS = new Set(['a','e','i','o','u','ā','ē','ī','ō','ū']);
  let firstVowelSeen = false;
  let firstVowelAccented = false;
  let laterAccent = false;
  for (let i = 0; i < nfd.length; i++) {
    const ch = nfd[i].toLowerCase();
    if (VOWEL_CHARS.has(ch)) {
      const accented = nfd[i+1] === '\u0301';
      if (!firstVowelSeen) {
        firstVowelSeen = true;
        if (accented) firstVowelAccented = true;
      } else {
        if (accented) laterAccent = true;
      }
    }
  }
  if (firstVowelAccented) return 'first';
  if (laterAccent) return 'later';
  return 'none';
}

// Pretonic shortening: shorten long vowel on first syllable if accent falls later
// Only fires when accentPos === 'later'; indeterminate ('none') is flagged, not applied
function applyPretonicShorten(tokens) {
  const out = [...tokens];
  for (let i = 0; i < out.length; i++) {
    if (isVowel(out[i])) {
      if (SHORTEN[out[i]]) out[i] = shorten(out[i]);
      break; // only first vowel = first syllable
    }
  }
  return out;
}

function laryngealColor(h, v) {
  // coloring only affects *e*; high vowels (i, u) and already-colored (a, o) are immune
  if (v !== 'e') return v;
  if (h === 'h₂') return 'a';
  if (h === 'h₃') return 'o';
  return v; // h₁ and H are neutral
}

// ══════════════════════════════════════════════════════════════════
//  NORMALIZATION
// ══════════════════════════════════════════════════════════════════

function normalize(raw) {
  let s = raw.trim().replace(/^\*/, '');
  // Strip morpheme and syllable boundary markers
  s = s.replace(/-/g, '').replace(/\./g, '');
  // Strip stress marks (precomposed via NFD decomposition, and combining)
  s = s.normalize('NFD').replace(/[\u0301\u0300\u0302]/g,'').normalize('NFC');
  s = s.replace(/a:/g,'ā').replace(/e:/g,'ē').replace(/i:/g,'ī')
       .replace(/o:/g,'ō').replace(/u:/g,'ū');
  s = s.replace(/gʷh|gwh/g,'gʷʰ');
  s = s.replace(/ǵh/g,'ǵʰ');
  s = s.replace(/bh/g,'bʰ');
  s = s.replace(/dh/g,'dʰ');
  s = s.replace(/gh(?![₁₂₃123])/g,'gʰ');
  s = s.replace(/[Hh]1(?![₂₃23])|[Hh]₁/g,'h₁');
  s = s.replace(/[Hh]2(?![₃3])|[Hh]₂/g,'h₂');
  s = s.replace(/[Hh]3|[Hh]₃/g,'h₃');
  // Bare H (unspecified laryngeal) — treated as neutral laryngeal, no coloring; passes through as 'H'
  s = s.replace(/g[´'`]h/g,'ǵʰ');
  s = s.replace(/g[´'`](?!ʰ)/g,'ǵ');
  s = s.replace(/k[´'`]/g,'ḱ');
  s = s.replace(/kw/g,'kʷ');
  s = s.replace(/gw(?!ʰ)/g,'gʷ');
  s = s.replace(/r_/g,'r̥').replace(/l_/g,'l̥')
       .replace(/m_/g,'m̥').replace(/n_/g,'n̥');
  return s;
}

// ══════════════════════════════════════════════════════════════════
//  SCAN HELPER
// ══════════════════════════════════════════════════════════════════

function scan(tokens, fn) {
  const out = [];
  for (let i = 0; i < tokens.length; i++) {
    const r = fn(tokens[i], i, tokens);
    if (r === null) continue;
    if (Array.isArray(r)) out.push(...r);
    else out.push(r);
  }
  return out;
}

// ══════════════════════════════════════════════════════════════════
//  STAGE 0: run once before Stage 1
// ══════════════════════════════════════════════════════════════════

const preStageRules = [
  {
    name: "Centumization: ḱ→k, ǵ→g, ǵʰ→gʰ",
    apply: tokens => scan(tokens, tok => {
      if (tok === 'ḱ')  return 'k';
      if (tok === 'ǵ')  return 'g';
      if (tok === 'ǵʰ') return 'gʰ';
      return tok;
    })
  },
  {
    name: "labiovelarization: Kw→kʷ",
    apply: tokens => {
      const out = []; let i = 0;
      while (i < tokens.length) {
        const tok = tokens[i], nxt = tokens[i+1];
        if      (tok === 'k'  && nxt === 'w') { out.push('kʷ');  i += 2; }
        else if (tok === 'g'  && nxt === 'w') { out.push('gʷ');  i += 2; }
        else if (tok === 'gʰ' && nxt === 'w') { out.push('gʷʰ'); i += 2; }
        else { out.push(tok); i++; }
      }
      return out;
    }
  },
  {
    name: "Boukólos rule: Kʷ → K adjacent to u, ū, or w",
    apply: tokens => {
      const out = []; let i = 0;
      while (i < tokens.length) {
        const tok = tokens[i];
        const prev = out[out.length-1], next = tokens[i+1];
        const adjUW = t => t === 'u' || t === 'ū' || t === 'w';
        if ((tok === 'kʷ' || tok === 'gʷ' || tok === 'gʷʰ') &&
            ((prev && adjUW(prev)) || (next && adjUW(next)))) {
          if (tok === 'kʷ')       out.push('k');
          else if (tok === 'gʷ')  out.push('g');
          else if (tok === 'gʷʰ') out.push('gʰ');
        } else {
          out.push(tok);
        }
        i++;
      }
      return out;
    }
  },
  {
    name: "KʷC→K: labiovelar delabializes before any consonant",
    apply: tokens => scan(tokens, (tok, i, toks) => {
      const nxt = toks[i+1];
      if (nxt && isConsonant(nxt) && !isSylRes(nxt)) {
        if (tok === 'kʷ')  return 'k';
        if (tok === 'gʷ')  return 'g';
        if (tok === 'gʷʰ') return 'gʰ';
      }
      return tok;
    })
  },
];

// ══════════════════════════════════════════════════════════════════
//  STAGE 1: PIE → Late Western IE (after Ringe 2017, with divergences)
// ══════════════════════════════════════════════════════════════════

const stage1Rules = [
  {
    name: "T{T,s}→ss: dental before dental or s → geminate ss",
    apply: tokens => {
      const out = []; let i = 0;
      while (i < tokens.length) {
        const tok = tokens[i], nxt = tokens[i+1];
        if (isDental(tok) && nxt && (isDental(nxt) || nxt === 's')) {
          out.push('s','s'); i += 2;
        } else { out.push(tok); i++; }
      }
      return out;
    }
  },
  {
    name: "ssC→sC: geminate ss simplifies before consonant",
    apply: tokens => {
      const out = []; let i = 0;
      while (i < tokens.length) {
        if (tokens[i] === 's' && tokens[i+1] === 's' &&
            tokens[i+2] && isConsonant(tokens[i+2])) {
          out.push('s'); i += 2;
        } else { out.push(tokens[i]); i++; }
      }
      return out;
    }
  },
  {
    name: "Thorn metathesis: TK→KT word-internally (labiovelars excluded; voicing preserved)",
    apply: tokens => {
      // Dental+velar → velar+dental, preserving voicing of each segment.
      // Voicing classes:
      //   voiceless:  t + k → k + t
      //   voiced:     d + g → g + d
      //   aspirated:  dʰ + gʰ → gʰ + dʰ
      // Mixed pairs handled by straightforward swap.
      // Word-initial position is excluded (pre-resolved in PIE to bare K-).
      const PLAIN_VELARS = new Set(['k','g','gʰ']);
      const out = []; let i = 0;
      while (i < tokens.length) {
        const tok = tokens[i], nxt = tokens[i+1];
        const isWordInitial = i === 0;
        if (!isWordInitial && isDental(tok) && nxt && PLAIN_VELARS.has(nxt)) {
          out.push(nxt, tok); i += 2;
        } else { out.push(tok); i++; }
      }
      return out;
    }
  },
  // ── LARYNGEAL RULES: Phase A (color) then Phase B (delete) ──────────────
  {
    name: "H-A: Laryngeal coloring — h₂/h₃ color adjacent vowels; h₁/H neutral",
    apply: tokens => {
      const t = [...tokens];
      for (let i = 0; i < t.length - 1; i++)
        if (isLaryngeal(t[i]) && isVowel(t[i+1]))
          t[i+1] = laryngealColor(t[i], t[i+1]);
      for (let i = t.length - 1; i > 0; i--)
        if (isLaryngeal(t[i]) && isVowel(t[i-1]))
          t[i-1] = laryngealColor(t[i], t[i-1]);
      return t;
    }
  },
  {
    name: "H-B1: VHV → V̄ — identical vowels across laryngeal contract; laryngeal lost",
    apply: tokens => {
      const out = []; let i = 0;
      while (i < tokens.length) {
        const tok = tokens[i];
        if (isLaryngeal(tok) && out.length > 0 && tokens[i+1] !== undefined) {
          const prev = out[out.length-1], next = tokens[i+1];
          if (isVowel(prev) && isVowel(next) && prev === next) {
            out.pop(); out.push(lengthen(prev)); i += 2; continue;
          }
        }
        out.push(tok); i++;
      }
      return out;
    }
  },
  {
    name: "H-B2: VH → V̄ — vowel before laryngeal (before C or #) lengthens; laryngeal lost",
    apply: tokens => {
      const out = []; let i = 0;
      while (i < tokens.length) {
        const tok = tokens[i];
        if (isLaryngeal(tok) && out.length > 0) {
          const prev = out[out.length-1];
          const next = tokens[i+1];
          if (isVowel(prev) && (!next || !isVowel(next))) {
            out.pop(); out.push(lengthen(prev)); i++; continue;
          }
        }
        out.push(tok); i++;
      }
      return out;
    }
  },
  {
    name: "H-B3: H adjacent to vowel → ∅ — covers #HV and CHV (coloring already fired)",
    apply: tokens => {
      const out = []; let i = 0;
      while (i < tokens.length) {
        const tok = tokens[i];
        if (isLaryngeal(tok)) {
          const prev = out[out.length-1], next = tokens[i+1];
          if ((prev && isVowel(prev)) || (next && isVowel(next))) {
            i++; continue;
          }
        }
        out.push(tok); i++;
      }
      return out;
    }
  },
  {
    name: "H-B4: H → ∅ word-initially (before consonant)",
    apply: tokens => {
      if (tokens.length > 1 && isLaryngeal(tokens[0])) return tokens.slice(1);
      return tokens;
    }
  },
  {
    name: "H-B5: H between consonants → a (initial syllable) / ∅ (elsewhere)",
    apply: tokens => {
      const out = []; let i = 0;
      while (i < tokens.length) {
        const tok = tokens[i];
        if (isLaryngeal(tok)) {
          const prev = tokens[i-1], next = tokens[i+1];
          if (prev && isConsonant(prev) && !isSylRes(prev) &&
              next && isConsonant(next) && !isSylRes(next)) {
            const hasVowelBefore = out.some(t => isVowel(t));
            if (!hasVowelBefore) out.push('a');
            i++; continue;
          }
        }
        out.push(tok); i++;
      }
      return out;
    }
  },
  {
    name: "H → ˀ: surviving laryngeals become glottal stop (diagnostic)",
    apply: tokens => scan(tokens, tok => isLaryngeal(tok) ? 'ˀ' : tok)
  },
  {
    name: "Voiced obstruent → voiceless before t or s (Core IE)",
    apply: tokens => scan(tokens, (tok, i, toks) => {
      const nxt = toks[i+1];
      if (!nxt || (nxt !== 't' && nxt !== 's')) return tok;
      if (tok === 'b'   || tok === 'bʰ')  return 'p';
      if (tok === 'g'   || tok === 'gʰ')  return 'k';
      if (tok === 'gʷ'  || tok === 'gʷʰ') return 'kʷ';
      return tok;
    })
  },
  {
    name: "Osthoff's Law: V̄RC → VRC (long vowel shortens before sonorant + consonant)",
    apply: tokens => {
      const SONORANTS = new Set(['r','l','m','n','w','y']);
      return scan(tokens, (tok, i, toks) => {
        const s1 = toks[i+1], s2 = toks[i+2];
        if (SHORTEN[tok] && s1 && SONORANTS.has(s1) && s2 && isConsonant(s2)) {
          return shorten(tok);
        }
        return tok;
      });
    }
  },
  {
    name: "Tautosyllabic ew → ow: e+w in coda (w before consonant or word-finally)",
    apply: tokens => {
      const out = [...tokens];
      for (let i = 0; i < out.length - 1; i++) {
        if (out[i] === 'e' && out[i+1] === 'w') {
          const after = out[i+2];
          // tautosyllabic: w is in coda = followed by consonant, word boundary, or nothing
          const wInCoda = !after || (isConsonant(after) && !isSylRes(after));
          if (wInCoda) out[i] = 'o';
        }
      }
      return out;
    }
  },
];

// ══════════════════════════════════════════════════════════════════
//  STAGE 2: Late Western PIE → Conlang
// ══════════════════════════════════════════════════════════════════

const stage2Rules = [
  {
    name: "Syllabic resonants vocalize: r̥→ar, l̥→al, m̥→am, n̥→an (adjacent ˀ consumed)",
    apply: tokens => {
      const RES = { 'r̥':'r', 'l̥':'l', 'm̥':'m', 'n̥':'n' };
      const out = []; let i = 0;
      while (i < tokens.length) {
        const tok = tokens[i];
        if (isSylRes(tok)) {
          const res = RES[tok];
          const prev = out[out.length-1], next = tokens[i+1];
          if (isGlottal(prev))            { out.pop(); }
          else if (next && isGlottal(next)) { i++; }
          out.push('a', res); i++;
        } else { out.push(tok); i++; }
      }
      return out;
    }
  },
  {
    name: "Juwankos rule: ū → uw before vowel",
    apply: tokens => {
      const out = []; let i = 0;
      while (i < tokens.length) {
        const tok = tokens[i];
        if (tok === 'ū' && tokens[i+1] && isVowel(tokens[i+1])) {
          out.push('u', 'w');
        } else {
          out.push(tok);
        }
        i++;
      }
      return out;
    }
  },
  {
    name: "Aspirates → voiced fricatives: bʰ→β, dʰ→ð, gʰ→ɣ, gʷʰ→ɣʷ",
    apply: tokens => scan(tokens, tok => {
      if (tok === 'bʰ')  return 'β';
      if (tok === 'dʰ')  return 'ð';
      if (tok === 'gʰ')  return 'ɣ';
      if (tok === 'gʷʰ') return 'ɣʷ';
      return tok;
    })
  },
  {
    name: "s → z between voiced sounds",
    apply: tokens => scan(tokens, (tok, i, toks) => {
      if (tok !== 's') return tok;
      const prev = toks[i-1], next = toks[i+1];
      if (prev && isVoiced(prev) && next && isVoiced(next)) return 'z';
      return tok;
    })
  },
  {
    name: "y → j: palatal glide respelled in Ghandwa orthography",
    apply: tokens => scan(tokens, tok => tok === 'y' ? 'j' : tok)
  },
];

// ══════════════════════════════════════════════════════════════════
//  STANDING RULES: synchronic filter, run to stability after each stage
// ══════════════════════════════════════════════════════════════════

const standingRules = [
  {
    name: "labiovelarization: Kw→kʷ (standing filter)",
    apply: tokens => {
      const out = []; let i = 0;
      while (i < tokens.length) {
        const tok = tokens[i], nxt = tokens[i+1];
        if      (tok === 'k'  && nxt === 'w') { out.push('kʷ');  i += 2; }
        else if (tok === 'g'  && nxt === 'w') { out.push('gʷ');  i += 2; }
        else if (tok === 'gʰ' && nxt === 'w') { out.push('gʷʰ'); i += 2; }
        else { out.push(tok); i++; }
      }
      return out;
    }
  },
  {
    name: "KʷC→K: labiovelar delabializes before any consonant (standing filter)",
    apply: tokens => scan(tokens, (tok, i, toks) => {
      const nxt = toks[i+1];
      if (nxt && isConsonant(nxt) && !isSylRes(nxt)) {
        if (tok === 'kʷ')  return 'k';
        if (tok === 'gʷ')  return 'g';
        if (tok === 'gʷʰ') return 'gʰ';
      }
      return tok;
    })
  },
  {
    name: "Boukólos: Kʷ → K adjacent to u or w (standing filter)",
    apply: tokens => {
      const out = []; let i = 0;
      while (i < tokens.length) {
        const tok = tokens[i];
        const prev = out[out.length-1], next = tokens[i+1];
        const adjUW = t => t === 'u' || t === 'ū' || t === 'w';
        if ((tok === 'kʷ' || tok === 'gʷ' || tok === 'gʷʰ') &&
            ((prev && adjUW(prev)) || (next && adjUW(next)))) {
          if (tok === 'kʷ')       out.push('k');
          else if (tok === 'gʷ')  out.push('g');
          else if (tok === 'gʷʰ') out.push('gʰ');
        } else {
          out.push(tok);
        }
        i++;
      }
      return out;
    }
  },
];

function applyStanding(tokens) {
  const MAX = 10;
  let prev, passes = 0;
  do {
    prev = join(tokens);
    for (const rule of standingRules) tokens = rule.apply(tokens);
    passes++;
  } while (join(tokens) !== prev && passes < MAX);
  return tokens;
}

// ══════════════════════════════════════════════════════════════════
//  PIPELINE
// ══════════════════════════════════════════════════════════════════

function transformSingle(raw) {
  const steps = [];
  const accentPos = detectAccentPosition(raw);
  const normed = normalize(raw);
  let tokens = tokenize(normed);

  // Stage 0: labiovelar normalization (run once)
  for (const rule of preStageRules) tokens = rule.apply(tokens);
  steps.push({ stage: 'Input', label: 'Normalized', form: join(tokens) });

  for (const rule of stage1Rules) {
    const next = rule.apply(tokens);
    const after = join(next);
    if (after !== join(tokens)) steps.push({ stage: 'Stage 1', label: rule.name, form: after });
    tokens = next;
  }

  // Standing after Stage 1
  const afterS1 = applyStanding(tokens);
  if (join(afterS1) !== join(tokens))
    steps.push({ stage: 'Standing', label: 'Kw→kʷ (post Stage 1)', form: join(afterS1) });
  tokens = afterS1;

  // Pretonic shortening: long vowel in unaccented first syllable shortens
  if (accentPos === 'later') {
    const shortened = applyPretonicShorten(tokens);
    if (join(shortened) !== join(tokens))
      steps.push({ stage: 'Stage 1', label: 'Pretonic shortening: long vowel in unaccented first syllable → short', form: join(shortened) });
    tokens = shortened;
  } else if (accentPos === 'none') {
    const firstLong = (() => { for (const t of tokens) { if (isVowel(t)) return !!SHORTEN[t]; } return false; })();
    if (firstLong) steps.push({ stage: 'Stage 1', label: '⚠ Pretonic shortening: accent not marked — indeterminate (long vowel in first syllable preserved)', form: join(tokens) });
  }

  for (const rule of stage2Rules) {
    const next = rule.apply(tokens);
    const after = join(next);
    if (after !== join(tokens)) steps.push({ stage: 'Stage 2', label: rule.name, form: after });
    tokens = next;
  }

  // Standing after Stage 2
  const afterS2 = applyStanding(tokens);
  if (join(afterS2) !== join(tokens))
    steps.push({ stage: 'Standing', label: 'Kw→kʷ (post Stage 2)', form: join(afterS2) });
  tokens = afterS2;

  return { steps, final: join(tokens) };
}

function transform(raw) {
  const stripped = raw.trim().replace(/^\*/, '');
  const tildeIdx = stripped.indexOf('~');

  if (tildeIdx === -1) {
    const r = transformSingle(raw);
    return { mode: 'single', steps: r.steps, final: r.final };
  }

  const nomRaw = stripped.slice(0, tildeIdx).trim();
  const genRaw = stripped.slice(tildeIdx + 1).trim();
  const nomR = transformSingle(nomRaw);
  const genR = transformSingle(genRaw);

  const steps = [];
  steps.push({
    stage: 'Input', label: 'Normalized',
    formNom: nomR.steps[0]?.form ?? nomRaw,
    formGen: genR.steps[0]?.form ?? genRaw,
  });

  const allRules = [...preStageRules, ...stage1Rules, ...stage2Rules];
  const nomByRule = new Map(nomR.steps.slice(1).map(s => [s.label, s.form]));
  const genByRule = new Map(genR.steps.slice(1).map(s => [s.label, s.form]));
  let nomCur = nomR.steps[0]?.form ?? nomRaw;
  let genCur = genR.steps[0]?.form ?? genRaw;

  for (const rule of allRules) {
    const nomNext = nomByRule.get(rule.name) ?? null;
    const genNext = genByRule.get(rule.name) ?? null;
    if (nomNext) nomCur = nomNext;
    if (genNext) genCur = genNext;
    if (nomNext || genNext) {
      const stage = preStageRules.includes(rule) ? 'Stage 0' : stage1Rules.includes(rule) ? 'Stage 1' : 'Stage 2';
      steps.push({ stage, label: rule.name, formNom: nomCur, formGen: genCur });
    }
  }

  return { mode: 'pair', steps, finalNom: nomR.final, finalGen: genR.final };
}

// ══════════════════════════════════════════════════════════════════
//  WARNING DETECTION
// ══════════════════════════════════════════════════════════════════

function hasGlottal(form) {
  return form.includes('ˀ');
}

function hasCCC(form) {
  // Tokenize and check for 3+ consecutive consonants (including glides/resonants)
  // Laryngeals not counted — they should have been consumed
  const tokens = tokenize(form);
  let run = 0;
  for (const t of tokens) {
    if (t === '-') { run = 0; continue; }
    if ((isConsonant(t) || isGlottal(t)) && !isLaryngeal(t)) { run++; if (run >= 3) return true; }
    else run = 0;
  }
  return false;
}

function getWarnings(form) {
  const w = [];
  if (hasGlottal(form)) w.push('unresolved ˀ');
  if (hasCCC(form))     w.push('CCC cluster');
  return w;
}

const EXAMPLES = [
  { label: 'wirós ~ wirózjo',           note: 'man (o-stem)' },
  { label: 'wih₁rós'},
  { label: 'h₂ŕ̥tḱos ~ h₂ŕ̥tḱozjo',    note: 'bear' },
  { label: 'wĺ̥kʷos ~ wĺ̥kʷozjo',       note: 'wolf' },
  { label: 'ḱr̥h₂nóm',                  note: 'horn (acc.)' },
  { label: '*ph₂tér',                   note: 'father' },
  { label: '*bʰer-',                    note: 'carry' },
  { label: '*h₁esti',                   note: 'is' },
  { label: '*dʰeǵʰom ~ *dʰeǵʰonós',    note: 'earth' },
  { label: '*h₃rḗǵs ~ h₃reǵes',           note: 'king' },
  { label: '*h₃reǵ-',                   note: 'rule' },
  { label: '*h₁nḗh₃mn̥',                note: 'name (Osthoff)' },
  { label: '*h₂wéh₁n̥ts',               note: 'wind (Osthoff)' },
  { label: 'h₂yúHn̥ḱos',               note: 'young (Osthoff)' },
  { label: '*kʷekʷlos ~ *kʷekʷlozjo',  note: 'wheel' },
  { label: 'h₂ŕ̥tḱos ~ h₂ŕ̥tḱozjo',      note: 'bear (thorn metathesis)' },
  { label: 'wésonts ~ wésn̥tés',          note: 'being (ptcp. nom. ~ gen.)' },
  { label: 'h₂ékʷeh₂ ~ h₂ékʷeh₂s',     note: 'water (nom. ~ gen.sg.)' },
  { label: 'h₂ékʷeh₂m ~ h₂ékʷeh₂ns',   note: 'water (acc.sg. ~ acc.pl.)' },
  { label: 'h₂ékʷeh₂ay ~ h₂ékʷeh₂mos', note: 'water (dat.sg. ~ dat.pl.)' },
  { label: 'h₂ékʷeh₂su',                note: 'water (loc.pl.)' },
];

const DOT = { 'Input':'#7b96c4', 'Stage 0':'#c4c47b', 'Stage 1':'#c49b7b', 'Standing':'#a07bc4', 'Stage 2':'#7bc49b' };

const css = `
  @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=JetBrains+Mono:wght@400;500&display=swap');
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:#0d1117;color:#c8d0db;font-family:'EB Garamond',Georgia,serif;min-height:100vh}
  .app{max-width:840px;margin:0 auto;padding:2.5rem 1.5rem 4rem}
  .header{border-bottom:1px solid #2a3040;padding-bottom:1.25rem;margin-bottom:2rem}
  .header h1{font-family:'Cinzel',serif;font-size:1.5rem;letter-spacing:.12em;color:#e8e0cc;font-weight:400;margin-bottom:.35rem}
  .header p{font-size:.9rem;color:#6a7585;letter-spacing:.03em}
  .ex-label{font-family:'JetBrains Mono',monospace;font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:#4a5568;margin-bottom:.5rem}
  .examples{display:flex;flex-wrap:wrap;gap:.4rem;margin-bottom:1.5rem}
  .ex-btn{background:#151b25;border:1px solid #2a3545;color:#9aadbe;padding:4px 10px;cursor:pointer;font-family:'EB Garamond',serif;font-size:1rem;border-radius:3px;transition:all .15s;display:flex;flex-direction:column;align-items:center;line-height:1.2}
  .ex-btn:hover{background:#1e2a38;border-color:#4a6080;color:#c8d8e8}
  .ex-note{font-size:.65rem;color:#4a5568;font-style:italic}
  .input-row{display:flex;gap:.5rem;margin-bottom:1.5rem}
  .pie-input{flex:1;background:#111720;border:1px solid #2a3a4a;color:#ddeeff;padding:.6rem .9rem;font-family:'EB Garamond',serif;font-size:1.25rem;border-radius:4px;outline:none;transition:border-color .2s}
  .pie-input:focus{border-color:#4a7aaa}
  .pie-input::placeholder{color:#2e3d4e}
  .run-btn{background:#1e3a5a;border:1px solid #2a5078;color:#88bbdd;padding:.6rem 1.25rem;font-family:'Cinzel',serif;font-size:.85rem;letter-spacing:.08em;cursor:pointer;border-radius:4px;transition:all .15s}
  .run-btn:hover{background:#264870;color:#aad4ee}
  .result-box{background:#111820;border:1px solid #2a3a4a;border-radius:6px;overflow:hidden}
  .result-top{display:flex;align-items:center;padding:1rem 1.25rem;gap:1rem;border-bottom:1px solid #1e2a38;flex-wrap:wrap}
  .result-in{color:#5a7090;font-family:'EB Garamond',serif;font-size:1.1rem;font-style:italic;flex-shrink:0}
  .result-arrow{color:#3a5070;flex-shrink:0}
  .result-out{color:#e8e0cc;font-family:'EB Garamond',serif;font-size:2rem;flex:1;letter-spacing:.04em}
  .result-tilde{color:#4a6070;margin:0 .35rem}
  .toggle-btn{background:none;border:1px solid #2a3a4a;color:#5a7090;padding:4px 10px;font-size:.75rem;font-family:'JetBrains Mono',monospace;cursor:pointer;border-radius:3px;transition:all .15s;white-space:nowrap;flex-shrink:0}
  .toggle-btn:hover{border-color:#4a6080;color:#8aaabb}
  .steps{padding:.5rem 0}
  .stage-hdr{font-family:'JetBrains Mono',monospace;font-size:.65rem;letter-spacing:.14em;text-transform:uppercase;padding:.4rem 1.25rem .15rem;color:#3a4a5a}
  .step-row{display:flex;align-items:center;padding:.3rem 1.25rem;gap:.75rem;border-top:1px solid #161e28}
  .step-row:hover{background:#141c26}
  .dot{width:6px;height:6px;border-radius:50%;flex-shrink:0}
  .step-rule{flex:1;font-size:.87rem;color:#5a7080;font-family:'EB Garamond',serif}
  .step-forms{display:flex;gap:.5rem;align-items:center;min-width:160px;justify-content:flex-end}
  .step-form{font-family:'EB Garamond',serif;font-size:1.1rem;color:#c8d8e0;letter-spacing:.02em}
  .step-sep{color:#3a5060;font-size:.9rem}
  .final-row{display:flex;align-items:center;padding:.6rem 1.25rem;gap:.75rem;border-top:1px solid #2a3a4a;background:#0f1820}
  .final-lbl{font-family:'JetBrains Mono',monospace;font-size:.65rem;letter-spacing:.12em;text-transform:uppercase;color:#4a6a8a;flex:1}
  .final-form{font-family:'EB Garamond',serif;font-size:1.4rem;color:#e8ddc8;letter-spacing:.04em}
  .help{margin-top:2rem;padding:1rem 1.25rem;background:#0f1520;border:1px solid #1e2838;border-radius:4px;font-size:.87rem;color:#4a5a6a;line-height:1.75}
  .help strong{color:#6a8a9a;font-weight:500}
  .help code{font-family:'JetBrains Mono',monospace;font-size:.82em;color:#7a9aaa}
  .warn{display:inline-flex;align-items:center;gap:.4rem;margin-top:.35rem;font-family:'JetBrains Mono',monospace;font-size:.7rem;color:#c8902a;letter-spacing:.06em}
  .warn-dot{width:6px;height:6px;border-radius:50%;background:#c8902a;flex-shrink:0}
  .result-out.has-warn{color:#c8d0a0}
`;

function groupByStage(steps) {
  const out = {};
  for (const s of steps) {
    if (!out[s.stage]) out[s.stage] = [];
    out[s.stage].push(s);
  }
  return out;
}

export default function App() {
  const [input, setInput] = useState('');
  const [result, setResult] = useState(null);
  const [showSteps, setShowSteps] = useState(false);

  function run(val) {
    const v = (val ?? input).trim();
    if (v) { setResult(transform(v)); setShowSteps(false); }
  }

  function clickExample(label) {
    setInput(label);
    setResult(transform(label));
    setShowSteps(false);
  }

  const isPair = result?.mode === 'pair';
  const grouped = result ? groupByStage(result.steps) : {};

  return (
    <>
      <style>{css}</style>
      <div className="app">
        <div className="header">
          <h1>PIE → Conlang Transformer</h1>
          <p>Pre-Anatolian PIE → Late Western PIE → Daughter language &nbsp;·&nbsp; Use <strong>~</strong> for nom ~ gen pairs</p>
        </div>

        <div className="ex-label">Examples</div>
        <div className="examples">
          {EXAMPLES.map(ex => (
            <button key={ex.label} className="ex-btn" onClick={() => clickExample(ex.label)}>
              {ex.label}
              <span className="ex-note">{ex.note}</span>
            </button>
          ))}
        </div>

        <div className="input-row">
          <input
            className="pie-input"
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && run()}
            placeholder="wirós ~ wirózjo  ·  *ph₂tér  ·  bher-  ·  ph2ter"
            spellCheck={false}
          />
          <button className="run-btn" onClick={() => run()}>Transform</button>
        </div>

        {result && (
          <div className="result-box">
            <div className="result-top">
              <span className="result-in">{input}</span>
              <span className="result-arrow">→</span>
              <span className={`result-out${(() => {
                const forms = isPair ? [result.finalNom, result.finalGen] : [result.final];
                return forms.some(f => getWarnings(f).length > 0) ? ' has-warn' : '';
              })()}`}>
                {isPair
                  ? <>{result.finalNom}<span className="result-tilde">~</span>{result.finalGen}</>
                  : result.final}
              </span>
              {(() => {
                const forms = isPair ? [result.finalNom, result.finalGen] : [result.final];
                const warns = [...new Set(forms.flatMap(f => getWarnings(f)))];
                return warns.length > 0 ? (
                  <span className="warn">
                    <span className="warn-dot" />
                    {warns.join(' · ')}
                  </span>
                ) : null;
              })()}
              <button className="toggle-btn" onClick={() => setShowSteps(v => !v)}>
                {showSteps ? '▲ hide steps' : '▼ show steps'}
              </button>
            </div>

            {showSteps && (
              <div className="steps">
                {Object.entries(grouped).map(([stage, steps]) => (
                  <div key={stage}>
                    <div className="stage-hdr">{stage}</div>
                    {steps.map((step, idx) => (
                      <div key={idx} className="step-row">
                        <div className="dot" style={{ background: DOT[stage] }} />
                        <span className="step-rule">{step.label}</span>
                        <span className="step-forms">
                          {isPair ? (
                            <>
                              <span className="step-form">{step.formNom}</span>
                              <span className="step-sep">~</span>
                              <span className="step-form">{step.formGen}</span>
                            </>
                          ) : (
                            <span className="step-form">{step.form}</span>
                          )}
                        </span>
                      </div>
                    ))}
                  </div>
                ))}
                <div className="final-row">
                  <span className="final-lbl">Final output</span>
                  <span className="final-form">
                    {isPair
                      ? <>{result.finalNom}<span style={{color:'#4a6070',margin:'0 .35rem'}}>~</span>{result.finalGen}</>
                      : result.final}
                  </span>
                </div>
              </div>
            )}
          </div>
        )}

        <div className="help">
          <strong>Pairs:</strong> <code>wirós ~ wirózjo</code> &nbsp;·&nbsp;
          <strong>Flexible input:</strong> <code>bh</code>→<code>bʰ</code> &nbsp;
          <code>n.</code>→<code>n̥</code> &nbsp;
          <code>e:</code>→<code>ē</code> &nbsp;
          <code>H2</code>/<code>h2</code>→<code>h₂</code> &nbsp;
          <code>kw</code>→<code>kʷ</code> &nbsp;·&nbsp;
          Leading <code>*</code> and stress marks stripped automatically. &nbsp;·&nbsp;
          Surviving <code>ˀ</code> in output = unaccounted-for laryngeal environment.
        </div>
      </div>
    </>
  );
}
