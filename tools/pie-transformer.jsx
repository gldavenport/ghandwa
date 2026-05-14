import { useState } from "react";

// ══════════════════════════════════════════════════════════════════
//  TOKENIZER
// ══════════════════════════════════════════════════════════════════

const PHONEME_PATTERNS = [
  'gʷʰ','ǵʰ','gʷ','kʷ','gʰ','bʰ','dʰ','ǵ','ḱ',
  'h₁','h₂','h₃','H',
  'r̥','l̥','m̥','n̥',
  'β','ð','ɣʷ','ɣ',
  'ā̃','ē̃','ī̃','ō̃','ū̃',
  'ã','ẽ','ĩ','õ','ũ',
  'ā','ē','ī','ō','ū',
  'tː','ˀ',
];

function tokenize(s) {
  const out = []; let i = 0;
  while (i < s.length) {
    let matched = false;
    for (const p of PHONEME_PATTERNS) {
      if (s.slice(i).startsWith(p)) { out.push(p); i += p.length; matched = true; break; }
    }
    if (!matched) { out.push(s[i]); i++; }
  }
  return out;
}
function join(toks) { return toks.join(''); }

// ══════════════════════════════════════════════════════════════════
//  CATEGORIES
// ══════════════════════════════════════════════════════════════════

const LARYNGEALS  = new Set(['h₁','h₂','h₃','H']);
const VOWELS      = new Set(['a','e','i','o','u','ā','ē','ī','ō','ū',
                             'ã','ẽ','ĩ','õ','ũ',
                             'ā̃','ē̃','ī̃','ō̃','ū̃']);
const LONG_V      = new Set(['ā','ē','ī','ō','ū']);
const SYL_RES     = new Set(['r̥','l̥','m̥','n̥']);
const DENTALS     = new Set(['t','d','dʰ']);
const VOICED_C    = new Set(['b','d','g','gʷ','β','ð','ɣ','ɣʷ','m','n','l','r','w','y','j','v','z']);
const LIQUIDS     = new Set(['r','l']);
const NASALS      = new Set(['m','n']);
const GLIDES      = new Set(['w','j','y']);
const DEASPIRATE  = { 'bʰ':'b',  'dʰ':'d',  'gʰ':'g',  'gʷʰ':'gʷ' };
const DEVOICE     = { 'bʰ':'p',  'dʰ':'t',  'gʰ':'k',  'gʷʰ':'kʷ' };
const LENGTHEN    = { a:'ā', e:'ē', i:'ī', o:'ō', u:'ū' };
const SHORTEN     = { 'ā':'a','ē':'e','ī':'i','ō':'o','ū':'u' };

const isVowel     = t => VOWELS.has(t);
const isLaryngeal = t => LARYNGEALS.has(t);
const isGlottal   = t => t === 'ˀ';
const isSylRes    = t => SYL_RES.has(t);
const isDental    = t => DENTALS.has(t);
const isLiquid    = t => LIQUIDS.has(t);
const isNasal     = t => NASALS.has(t);
const isConsonant = t => t !== '-' && !isVowel(t) && !isLaryngeal(t) && !isGlottal(t);
const isVoiced    = t => VOICED_C.has(t) || isVowel(t);
const isLongVowel = t => LONG_V.has(t);
const lengthen    = v => LENGTHEN[v] || v;
const shorten     = v => SHORTEN[v]  || v;
const NASALIZE    = { 'a':'ã','e':'ẽ','i':'ĩ','o':'õ','u':'ũ',
                      'ā':'ā̃','ē':'ē̃','ī':'ī̃','ō':'ō̃','ū':'ū̃' };
const nasalize    = v => NASALIZE[v] || v;

// ══════════════════════════════════════════════════════════════════
//  SYLLABIFICATION  (wékʷos rule 4.4)
// ══════════════════════════════════════════════════════════════════

function getNuclei(toks) {
  const nuclei = []; let i = 0;
  while (i < toks.length) {
    const t = toks[i];
    if (isLongVowel(t)) {
      nuclei.push({ start: i, end: i }); i++;
    } else if (isVowel(t)) {
      const nxt = toks[i+1], afterNxt = toks[i+2];
      const isDiph = nxt && GLIDES.has(nxt) &&
        (!afterNxt || (isConsonant(afterNxt) && !isSylRes(afterNxt)));
      if (isDiph) { nuclei.push({ start: i, end: i+1 }); i += 2; }
      else        { nuclei.push({ start: i, end: i   }); i++;    }
    } else { i++; }
  }
  return nuclei;
}
const isPolysyllabic = toks => getNuclei(toks).length >= 2;

// ══════════════════════════════════════════════════════════════════
//  NORMALIZATION  (shared)
// ══════════════════════════════════════════════════════════════════

function detectAccentPos(raw) {
  const nfd = raw.normalize('NFD');
  const VC = new Set(['a','e','i','o','u','ā','ē','ī','ō','ū']);
  let first = false, firstAcc = false, laterAcc = false;
  for (let i = 0; i < nfd.length; i++) {
    if (VC.has(nfd[i].toLowerCase())) {
      const acc = nfd[i+1] === '\u0301';
      if (!first) { first = true; if (acc) firstAcc = true; }
      else if (acc) laterAcc = true;
    }
  }
  return firstAcc ? 'first' : laterAcc ? 'later' : 'none';
}

function normalize(raw) {
  let s = raw.trim().replace(/^\*/, '');
  s = s.replace(/-/g,'').replace(/\./g,'');
  s = s.normalize('NFD').replace(/[\u0301\u0300\u0302]/g,'').normalize('NFC');
  s = s.replace(/a:/g,'ā').replace(/e:/g,'ē').replace(/i:/g,'ī')
       .replace(/o:/g,'ō').replace(/u:/g,'ū');
  s = s.replace(/gʷh|gwh/g,'gʷʰ').replace(/ǵh/g,'ǵʰ')
       .replace(/bh/g,'bʰ').replace(/dh/g,'dʰ')
       .replace(/gh(?![₁₂₃123])/g,'gʰ');
  s = s.replace(/[Hh]1(?![₂₃23])|[Hh]₁/g,'h₁')
       .replace(/[Hh]2(?![₃3])|[Hh]₂/g,'h₂')
       .replace(/[Hh]3|[Hh]₃/g,'h₃');
  s = s.replace(/g[´'`]h/g,'ǵʰ').replace(/g[´'`](?!ʰ)/g,'ǵ')
       .replace(/k[´'`]/g,'ḱ').replace(/kw/g,'kʷ').replace(/gw(?!ʰ)/g,'gʷ');
  s = s.replace(/r_/g,'r̥').replace(/l_/g,'l̥')
       .replace(/m_/g,'m̥').replace(/n_/g,'n̥');
  return s;
}

// ══════════════════════════════════════════════════════════════════
//  SCAN HELPER
// ══════════════════════════════════════════════════════════════════

function scan(toks, fn) {
  const out = [];
  for (let i = 0; i < toks.length; i++) {
    const r = fn(toks[i], i, toks);
    if (r === null) continue;
    if (Array.isArray(r)) out.push(...r); else out.push(r);
  }
  return out;
}

// ══════════════════════════════════════════════════════════════════
//  LARYNGEAL UTILITIES  (shared)
// ══════════════════════════════════════════════════════════════════

function laryngealColor(h, v) {
  if (v !== 'e') return v;
  if (h === 'h₂') return 'a';
  if (h === 'h₃') return 'o';
  return v;
}

const RULE_H_COLOR = {
  name: "H-A: Laryngeal coloring — h₂/h₃ color adjacent e",
  apply: toks => {
    const t = [...toks];
    for (let i = 0; i < t.length-1; i++)
      if (isLaryngeal(t[i]) && isVowel(t[i+1])) t[i+1] = laryngealColor(t[i], t[i+1]);
    for (let i = t.length-1; i > 0; i--)
      if (isLaryngeal(t[i]) && isVowel(t[i-1])) t[i-1] = laryngealColor(t[i], t[i-1]);
    return t;
  }
};

const RULE_VHV = {
  name: "H-B1: VHV → V̄ — identical vowels across laryngeal contract",
  apply: toks => {
    const out = []; let i = 0;
    while (i < toks.length) {
      const tok = toks[i];
      if (isLaryngeal(tok) && out.length > 0 && toks[i+1]) {
        const prev = out[out.length-1], nxt = toks[i+1];
        if (isVowel(prev) && isVowel(nxt) && prev === nxt) {
          out.pop(); out.push(lengthen(prev)); i += 2; continue;
        }
      }
      out.push(tok); i++;
    }
    return out;
  }
};

const RULE_VH = {
  name: "H-B2: VH → V̄ — vowel before laryngeal (before C or #) lengthens",
  apply: toks => {
    const out = []; let i = 0;
    while (i < toks.length) {
      const tok = toks[i];
      if (isLaryngeal(tok) && out.length > 0) {
        const prev = out[out.length-1], nxt = toks[i+1];
        if (isVowel(prev) && (!nxt || !isVowel(nxt))) {
          out.pop(); out.push(lengthen(prev)); i++; continue;
        }
      }
      out.push(tok); i++;
    }
    return out;
  }
};

// ══════════════════════════════════════════════════════════════════
//  PRE-STAGE — shared across all languages
// ══════════════════════════════════════════════════════════════════

const SHARED_PRE = [
  { name: "Centumization: ḱ→k, ǵ→g, ǵʰ→gʰ",
    apply: t => scan(t, tok => tok==='ḱ'?'k': tok==='ǵ'?'g': tok==='ǵʰ'?'gʰ': tok)
  },
  { name: "Labiovelarization: K+w → Kʷ",
    apply: t => {
      const out=[]; let i=0;
      while (i<t.length) {
        const [c,n]=[t[i],t[i+1]];
        if      (c==='k'  && n==='w') { out.push('kʷ');  i+=2; }
        else if (c==='g'  && n==='w') { out.push('gʷ');  i+=2; }
        else if (c==='gʰ' && n==='w') { out.push('gʷʰ'); i+=2; }
        else { out.push(c); i++; }
      }
      return out;
    }
  },
  { name: "Boukólos: Kʷ → K adjacent to u/ū/w",
    apply: t => {
      const out=[]; let i=0;
      const uuw = x => x==='u'||x==='ū'||x==='w';
      while (i<t.length) {
        const tok=t[i], prev=out[out.length-1], nxt=t[i+1];
        if ((tok==='kʷ'||tok==='gʷ'||tok==='gʷʰ') && ((prev&&uuw(prev))||(nxt&&uuw(nxt)))) {
          out.push(tok==='kʷ'?'k': tok==='gʷ'?'g': 'gʰ');
        } else out.push(tok);
        i++;
      }
      return out;
    }
  },
];

// Ghandwa-only: delabialization before consonants
const GH_PRE_EXTRA = [
  { name: "KʷC → K: labiovelar delabializes before consonant",
    apply: t => scan(t, (tok,i,ts) => {
      const n=ts[i+1];
      if (n && isConsonant(n) && !isSylRes(n)) {
        if (tok==='kʷ') return 'k';
        if (tok==='gʷ') return 'g';
        if (tok==='gʷʰ') return 'gʰ';
      }
      return tok;
    })
  },
];

function applyPre(toks, ghandwa=false) {
  const rules = ghandwa ? [...SHARED_PRE, ...GH_PRE_EXTRA] : SHARED_PRE;
  for (const r of rules) toks = r.apply(toks);
  return toks;
}

// ══════════════════════════════════════════════════════════════════
//  GHANDWA RULES
// ══════════════════════════════════════════════════════════════════

const GH_S1 = [
  { name: "T{T,s}→ss: dental+dental/s → geminate ss",
    apply: t => { const out=[]; let i=0;
      while(i<t.length){ const[c,n]=[t[i],t[i+1]];
        if(isDental(c)&&n&&(isDental(n)||n==='s')){out.push('s','s');i+=2;}
        else{out.push(c);i++;}
      } return out; }
  },
  { name: "ssC→sC: geminate simplifies before consonant",
    apply: t => { const out=[]; let i=0;
      while(i<t.length){ if(t[i]==='s'&&t[i+1]==='s'&&t[i+2]&&isConsonant(t[i+2])){out.push('s');i+=2;}
        else{out.push(t[i]);i++;} } return out; }
  },
  { name: "Thorn metathesis: TK→KT word-internally",
    apply: t => { const PV=new Set(['k','g','gʰ']); const out=[]; let i=0;
      while(i<t.length){ const[c,n]=[t[i],t[i+1]];
        if(i!==0&&isDental(c)&&n&&PV.has(n)){out.push(n,c);i+=2;}else{out.push(c);i++;} }
      return out; }
  },
  RULE_H_COLOR, RULE_VHV, RULE_VH,
  { name: "H-B3: H adjacent to vowel → ∅",
    apply: t => { const out=[]; let i=0;
      while(i<t.length){ const tok=t[i];
        if(isLaryngeal(tok)){const prev=out[out.length-1],nxt=t[i+1];
          if((prev&&isVowel(prev))||(nxt&&isVowel(nxt))){i++;continue;}}
        out.push(tok);i++; } return out; }
  },
  { name: "H-B4: #H before consonant → ∅",
    apply: t => (t.length>1&&isLaryngeal(t[0]))?t.slice(1):t
  },
  { name: "H-B5: H between consonants → a (initial) / ∅",
    apply: t => { const out=[]; let i=0;
      while(i<t.length){ const tok=t[i];
        if(isLaryngeal(tok)){const prev=t[i-1],nxt=t[i+1];
          if(prev&&isConsonant(prev)&&!isSylRes(prev)&&nxt&&isConsonant(nxt)&&!isSylRes(nxt)){
            if(!out.some(x=>isVowel(x))) out.push('a'); i++;continue;}}
        out.push(tok);i++; } return out; }
  },
  { name: "H → ˀ: surviving laryngeals marked",
    apply: t => scan(t, tok => isLaryngeal(tok)?'ˀ':tok)
  },
  { name: "Voiced obstruent → voiceless before t/s",
    apply: t => scan(t,(tok,i,ts)=>{const n=ts[i+1];
      if(!n||(n!=='t'&&n!=='s'))return tok;
      if(tok==='b'||tok==='bʰ')return 'p';
      if(tok==='g'||tok==='gʰ')return 'k';
      if(tok==='gʷ'||tok==='gʷʰ')return 'kʷ';
      return tok;})
  },
  { name: "Osthoff's Law: V̄RC → VRC",
    apply: t => { const SON=new Set(['r','l','m','n','w','y']);
      return scan(t,(tok,i,ts)=>{
        const s1=ts[i+1],s2=ts[i+2];
        if(SHORTEN[tok]&&s1&&SON.has(s1)&&s2&&isConsonant(s2))return shorten(tok);
        return tok;});}
  },
  { name: "ew→ow: tautosyllabic e+w in coda",
    apply: t => { const out=[...t];
      for(let i=0;i<out.length-1;i++){
        if(out[i]==='e'&&out[i+1]==='w'){
          const after=out[i+2];
          if(!after||(isConsonant(after)&&!isSylRes(after)))out[i]='o';}}
      return out; }
  },
];

const GH_S2 = [
  { name: "Syllabic resonants → aR: r̥→ar, l̥→al, m̥→am, n̥→an",
    apply: t => { const R={'r̥':'r','l̥':'l','m̥':'m','n̥':'n'};
      const out=[]; let i=0;
      while(i<t.length){ const tok=t[i];
        if(isSylRes(tok)){const res=R[tok],prev=out[out.length-1],nxt=t[i+1];
          if(isGlottal(prev))out.pop(); else if(nxt&&isGlottal(nxt))i++;
          out.push('a',res);i++;}else{out.push(tok);i++;}}
      return out; }
  },
  { name: "ū→uw before vowel (Juwankos rule)",
    apply: t => { const out=[]; let i=0;
      while(i<t.length){
        if(t[i]==='ū'&&t[i+1]&&isVowel(t[i+1]))out.push('u','w');
        else out.push(t[i]); i++; } return out; }
  },
  { name: "Aspirates → voiced fricatives: bʰ→β, dʰ→ð, gʰ→ɣ, gʷʰ→ɣʷ",
    apply: t => scan(t, tok => tok==='bʰ'?'β': tok==='dʰ'?'ð': tok==='gʰ'?'ɣ': tok==='gʷʰ'?'ɣʷ': tok)
  },
  { name: "s → z between voiced sounds",
    apply: t => scan(t,(tok,i,ts)=>{
      if(tok!=='s')return tok;
      const p=ts[i-1],n=ts[i+1];
      return (p&&isVoiced(p)&&n&&isVoiced(n))?'z':'s';})
  },
  { name: "y → j: palatal glide respelled",
    apply: t => scan(t, tok => tok==='y'?'j':tok)
  },
];

const GH_STANDING = [
  { apply: t => { const out=[]; let i=0;
      while(i<t.length){ const[c,n]=[t[i],t[i+1]];
        if(c==='k'&&n==='w'){out.push('kʷ');i+=2;}
        else if(c==='g'&&n==='w'){out.push('gʷ');i+=2;}
        else if(c==='gʰ'&&n==='w'){out.push('gʷʰ');i+=2;}
        else{out.push(c);i++;}} return out; }},
  { apply: t => scan(t,(tok,i,ts)=>{const n=ts[i+1];
      if(n&&isConsonant(n)&&!isSylRes(n)){
        if(tok==='kʷ')return 'k'; if(tok==='gʷ')return 'g'; if(tok==='gʷʰ')return 'gʰ';}
      return tok;})},
  { apply: t => { const out=[]; let i=0; const uuw=x=>x==='u'||x==='ū'||x==='w';
      while(i<t.length){ const tok=t[i],prev=out[out.length-1],nxt=t[i+1];
        if((tok==='kʷ'||tok==='gʷ'||tok==='gʷʰ')&&((prev&&uuw(prev))||(nxt&&uuw(nxt)))){
          out.push(tok==='kʷ'?'k':tok==='gʷ'?'g':'gʰ');}else out.push(tok); i++;} return out; }},
];

function applyStanding(toks) {
  const MAX=10; let prev, n=0;
  do { prev=join(toks); for(const r of GH_STANDING) toks=r.apply(toks); n++; }
  while(join(toks)!==prev && n<MAX);
  return toks;
}

// ══════════════════════════════════════════════════════════════════
//  WÉKʷOS OLD RULES
// ══════════════════════════════════════════════════════════════════

const WK_OLD = [
  // ── Stage 2: Laryngeals ──────────────────────────────────────────
  RULE_H_COLOR, RULE_VHV, RULE_VH,
  { name: "H-C: Pre-vocalic h₂/h₃ → x (laryngeal coloring residue)",
    apply: t => { const out=[]; let i=0;
      while(i<t.length){ const tok=t[i];
        if((tok==='h₂'||tok==='h₃')&&t[i+1]&&isVowel(t[i+1])){out.push('x');i++;}
        else{out.push(tok);i++;}} return out; }
  },
  { name: "H-D: Pre-vocalic h₁/H → ∅ (no residue)",
    apply: t => { const out=[]; let i=0;
      while(i<t.length){ const tok=t[i];
        if((tok==='h₁'||tok==='H')&&t[i+1]&&isVowel(t[i+1])){i++;}
        else{out.push(tok);i++;}} return out; }
  },
  { name: "Old 2.2: CHC > CaC — laryngeal between consonants vocalizes as a",
    apply: t => { const out=[]; let i=0;
      while(i<t.length){ const tok=t[i];
        if(isLaryngeal(tok)){const prev=out[out.length-1],nxt=t[i+1];
          if(prev&&isConsonant(prev)&&!isSylRes(prev)&&nxt&&isConsonant(nxt)&&!isSylRes(nxt)){
            out.push('a');i++;continue;}}
        out.push(tok);i++;} return out; }
  },
  { name: "Old 2.4: #HC > #C — initial laryngeal before consonant deleted",
    apply: t => (t.length>1&&isLaryngeal(t[0])&&isConsonant(t[1]))?t.slice(1):t
  },
  { name: "Remaining H → x (coloring residue)",
    apply: t => scan(t, tok => isLaryngeal(tok)?'x':tok)
  },
  // ── Stage 3: Syllabic resonants ──────────────────────────────────
  { name: "Syllabic resonants → aR: r̥→ar, l̥→al, m̥→am, n̥→an",
    apply: t => { const R={'r̥':'r','l̥':'l','m̥':'m','n̥':'n'};
      const out=[]; let i=0;
      while(i<t.length){ const tok=t[i];
        if(isSylRes(tok)){out.push('a',R[tok]);i++;}else{out.push(tok);i++;}}
      return out; }
  },
  // ── Stage 4: Aspirate devoicing ──────────────────────────────────
  { name: "Old 4.1: DʰL > DL — aspirate before liquid loses aspiration",
    apply: t => scan(t,(tok,i,ts)=>{
      const n=ts[i+1];
      return (n&&isLiquid(n)&&DEASPIRATE[tok])?DEASPIRATE[tok]:tok;})
  },
  { name: "Old 4.2: Dʰ > T — remaining voiced aspirates devoice",
    apply: t => scan(t, tok => DEVOICE[tok]||tok)
  },
  // ── Stage 5: Substrate phonology ─────────────────────────────────
  { name: "Old 5.1: CVLC > CLVC — liquid metathesis",
    apply: t => { const out=[]; let i=0;
      while(i<t.length){
        const[a,b,c,d]=[t[i],t[i+1],t[i+2],t[i+3]];
        if(a&&isConsonant(a)&&!isLiquid(a)&&b&&isVowel(b)&&c&&isLiquid(c)&&d&&isConsonant(d)){
          out.push(a,c,b);i+=3;}else{out.push(t[i]);i++;}}
      return out; }
  },
  { name: "5.1: VTNV > VNDV — voiceless stop before nasal voices to D; aspirates resolved by 3.2",
    apply: t => { const VS={'p':'b','t':'d','k':'g','kʷ':'gʷ'};
      const out=[]; let i=0;
      while(i<t.length){
        const[a,b,c,d]=[t[i],t[i+1],t[i+2],t[i+3]];
        if(a&&isVowel(a)&&b&&VS[b]&&c&&isNasal(c)&&d&&isVowel(d)){
          out.push(a,c,VS[b]);i+=3;}else{out.push(t[i]);i++;}}
      return out; }
  },
  { name: "Old 5.3: #pr > #br — initial labial+r voices (dental fortis pending notation)",
    apply: t => (t[0]==='p'&&t[1]==='r')?['b',...t.slice(1)]:t
  },
];

// ══════════════════════════════════════════════════════════════════
//  WÉKʷOS NEO RULES
// ══════════════════════════════════════════════════════════════════

const WK_NEO = [
  { name: "Neo 4.1: Barytonesis — stress retracts to initial syllable",
    apply: t => t  // no token-level change; feeds 4.4 by demoting final-syllable prominence
  },
  { name: "Neo: #xLV > #kLV — initial laryngeal residue fortifies before liquid+vowel",
    apply: t => (t[0]==='x' && t[1] && isLiquid(t[1]) && t[2] && isVowel(t[2]))
      ? ['k', ...t.slice(1)] : t
  },
  { name: "Neo 4.2: Collapse of homorganic diphthongs — ey/ej > ī, ow > ū",
    apply: t => { const out=[]; let i=0;
      while(i<t.length){ const[c,n]=[t[i],t[i+1]];
        if(c==='e'&&(n==='y'||n==='j')){out.push('ī');i+=2;}
        else if(c==='o'&&n==='w'){out.push('ū');i+=2;}
        else{out.push(c);i++;}} return out; }
  },
  { name: "Neo 4.3: Harmonization of heterorganic diphthongs — ew > ow, oy > ey",
    apply: t => { const out=[]; let i=0;
      while(i<t.length){ const[c,n]=[t[i],t[i+1]];
        if(c==='e'&&n==='w'){out.push('o','w');i+=2;}
        else if(c==='o'&&(n==='y'||n==='j')){out.push('e','y');i+=2;}
        else{out.push(c);i++;}} return out; }
  },
  { name: "Neo 4.4: Long vowels in final syllable shorten (polysyllables only)",
    apply: t => { if(!isPolysyllabic(t))return t;
      const nuc=getNuclei(t); if(!nuc.length)return t;
      const last=nuc[nuc.length-1]; const out=[...t];
      for(let i=last.start;i<=last.end;i++) if(SHORTEN[out[i]])out[i]=shorten(out[i]);
      return out; }
  },
  { name: "Neo 4.5: o > a (short only) — vowel merger",
    apply: t => scan(t, tok => tok==='o'?'a':tok)
  },
  { name: "10.3: s > z / {V,R}_{V,R} — intervocalic voicing, ordered after o > a",
    apply: t => scan(t, (tok,i,ts) => {
      if (tok!=='s') return tok;
      const vr = x => x && (isVowel(x) || isNasal(x) || isLiquid(x));
      return (vr(ts[i-1]) && vr(ts[i+1])) ? 'z' : 's';
    })
  },
  { name: "10.4: VN# > Ṽ# — final nasal nasalizes preceding vowel, nasal drops",
    apply: t => {
      if (t.length < 2) return t;
      const last = t[t.length-1];
      if (!isNasal(last)) return t;
      const prev = t[t.length-2];
      if (!isVowel(prev)) return t;
      const nas = nasalize(prev);
      if (nas === prev) return t;
      return [...t.slice(0, t.length-2), nas];
    }
  },
  { name: "11.1: word-final obstruent voicing — p,t,k,kʷ,s > b,d,g,gʷ,z",
    apply: t => {
      if (!t.length) return t;
      const VF = {'p':'b','t':'d','k':'g','kʷ':'gʷ','s':'z'};
      const out = [...t];
      if (VF[out[out.length-1]]) out[out.length-1] = VF[out[out.length-1]];
      return out;
    }
  },
  { name: "11.2: Kʷ > K — labiovelar delabialization, ordered after 11.1",
    apply: t => scan(t, tok => tok==='kʷ'?'k': tok==='gʷ'?'g': tok)
  },
  { name: "11.3: l > r / _# — final lateral rhotacism",
    apply: t => {
      if (!t.length) return t;
      const out = [...t];
      if (out[out.length-1] === 'l') out[out.length-1] = 'r';
      return out;
    }
  },
];

// ══════════════════════════════════════════════════════════════════
//  PIPELINE FUNCTIONS
// ══════════════════════════════════════════════════════════════════

function stageOf(name) {
  if (/H-[ABCD]|2\.[24]|Remaining H/.test(name)) return 'Laryngeals';
  if (/Syllabic/.test(name))  return 'Syllabic resonants';
  if (/4\.[12]/.test(name))   return 'Aspirates';
  if (/5\./.test(name))       return 'Substrate';
  if (/Neo/.test(name))       return 'Neo-wékʷos';
  return 'Pre-stage';
}

function runSteps(toks, rules, stageLabel) {
  const steps = [];
  for (const rule of rules) {
    const next = rule.apply(toks);
    const after = join(next);
    if (after !== join(toks)) steps.push({ stage: stageLabel||stageOf(rule.name), label: rule.name, form: after });
    toks = next;
  }
  return { toks, steps };
}

function transformGhandwa(raw) {
  const accentPos = detectAccentPos(raw);
  let toks = tokenize(normalize(raw));
  toks = applyPre(toks, true);
  const steps = [{ stage:'Input', label:'Normalized', form:join(toks) }];

  const s1 = runSteps(toks, GH_S1, 'Stage 1');
  steps.push(...s1.steps); toks = s1.toks;

  const stood = applyStanding(toks);
  if (join(stood)!==join(toks)) steps.push({ stage:'Standing', label:'Labiovelar standing filter', form:join(stood) });
  toks = stood;

  if (accentPos==='later') {
    const out=[...toks];
    for(let i=0;i<out.length;i++){if(isVowel(out[i])){if(SHORTEN[out[i]])out[i]=shorten(out[i]);break;}}
    if(join(out)!==join(toks)){steps.push({stage:'Stage 1',label:'Pretonic shortening',form:join(out)});toks=out;}
  }

  const s2 = runSteps(toks, GH_S2, 'Stage 2');
  steps.push(...s2.steps); toks = s2.toks;

  const stood2 = applyStanding(toks);
  if (join(stood2)!==join(toks)) steps.push({ stage:'Standing', label:'Labiovelar standing filter', form:join(stood2) });
  toks = stood2;

  return { steps, final: join(toks) };
}

function transformOldWekwos(raw) {
  let toks = tokenize(normalize(raw));
  toks = applyPre(toks, false);
  const steps = [{ stage:'Input', label:'Normalized', form:join(toks) }];
  const r = runSteps(toks, WK_OLD, null);
  steps.push(...r.steps);
  return { steps, final: join(r.toks) };
}

function transformNeoWekwos(raw) {
  const old = transformOldWekwos(raw);
  let toks = tokenize(old.final);
  const steps = [...old.steps];
  const r = runSteps(toks, WK_NEO, 'Neo-wékʷos');
  steps.push(...r.steps);
  return { steps, final: join(r.toks) };
}

function transformAll(raw, langs) {
  const out = {};
  if (langs.includes('ghandwa')) out.ghandwa = transformGhandwa(raw);
  if (langs.includes('old'))     out.old     = transformOldWekwos(raw);
  if (langs.includes('neo'))     out.neo     = transformNeoWekwos(raw);
  return out;
}

// ══════════════════════════════════════════════════════════════════
//  WARNINGS
// ══════════════════════════════════════════════════════════════════

function getWarnings(form) {
  const w = [];
  if (form.includes('ˀ')) w.push('unresolved ˀ');
  const toks = tokenize(form); let run=0;
  for (const t of toks) {
    if ((isConsonant(t)||isGlottal(t))&&!isLaryngeal(t)){run++;if(run>=3){w.push('CCC');break;}}
    else run=0;
  }
  return w;
}

// ══════════════════════════════════════════════════════════════════
//  UI
// ══════════════════════════════════════════════════════════════════

const LANG_DEFS = [
  { id:'ghandwa', label:'Ghandwa',     color:'#7bc49b', dimColor:'#3a6a4a' },
  { id:'old',     label:'Old wékʷos',  color:'#c49b7b', dimColor:'#6a4a3a' },
  { id:'neo',     label:'Neo-wékʷos',  color:'#7b96c4', dimColor:'#3a4a6a' },
];

const STAGE_DOT = {
  'Input':               '#4a5568',
  'Stage 1':             '#c4a07b',
  'Stage 2':             '#7bc49b',
  'Standing':            '#a07bc4',
  'Laryngeals':          '#c4c47b',
  'Syllabic resonants':  '#7b96c4',
  'Aspirates':           '#c47b7b',
  'Substrate':           '#7bc4c4',
  'Neo-wékʷos':          '#c47bc4',
  'Pre-stage':           '#4a5568',
};

const EXAMPLES = [
  { label:'*dn̥ǵʰwéh₂s', note:'tongue (1)' },
  { label:'*ǵʰn̥dwéh₂s', note:'tongue (2)' },
  { label:'*ph₂tér',     note:'father' },
  { label:'*bʰreh₂tēr',  note:'brother' },
  { label:'*wĺ̥kʷos',    note:'wolf' },
  { label:'*h₂ékʷeh₂',  note:'water' },
  { label:'*gʷeneh₂',   note:'woman' },
  { label:'*h₃reǵ-',    note:'rule' },
  { label:'*perkʷus',   note:'oak' },
];

function groupSteps(steps) {
  const map = {}; const order = [];
  for (const s of steps) {
    if (!map[s.stage]) { map[s.stage]=[]; order.push(s.stage); }
    map[s.stage].push(s);
  }
  return order.map(st => ({ stage:st, steps:map[st] }));
}

const css = `
  @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=JetBrains+Mono:wght@400;500&display=swap');
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:#0d1117;color:#c8d0db;font-family:'EB Garamond',Georgia,serif;min-height:100vh}
  .app{max-width:900px;margin:0 auto;padding:2rem 1.5rem 4rem}
  h1{font-family:'Cinzel',serif;font-size:1.35rem;letter-spacing:.1em;color:#e8e0cc;
     font-weight:400;margin-bottom:.2rem}
  .sub{font-size:.82rem;color:#3a4a5a;letter-spacing:.04em;margin-bottom:1.5rem}
  .examples{display:flex;flex-wrap:wrap;gap:.3rem;margin-bottom:1rem}
  .ex-btn{background:#0f1620;border:1px solid #202c38;color:#7a9db8;padding:3px 9px;
    cursor:pointer;font-family:'EB Garamond',serif;font-size:.95rem;border-radius:3px;
    display:flex;flex-direction:column;align-items:center;transition:all .12s}
  .ex-btn:hover{background:#192433;border-color:#3a6080}
  .ex-note{font-size:.58rem;color:#3a5060;font-style:italic}
  .lang-row{display:flex;gap:1rem;margin-bottom:.8rem;flex-wrap:wrap}
  .lcheck{display:flex;align-items:center;gap:.35rem;cursor:pointer;font-size:.88rem;color:#6a8090}
  .lcheck input{cursor:pointer;accent-color:#4a7090}
  .ldot{width:7px;height:7px;border-radius:50%;flex-shrink:0}
  .ctrl{display:flex;gap:.4rem;margin-bottom:1rem}
  .inp{flex:1;background:#0f1720;border:1px solid #1e2e3e;color:#d8eeff;
    padding:.55rem .8rem;font-family:'EB Garamond',serif;font-size:1.15rem;
    border-radius:4px;outline:none;transition:border-color .2s}
  .inp:focus{border-color:#3a6080}
  .inp::placeholder{color:#243040}
  .go{background:#172a40;border:1px solid #1e4060;color:#6aaace;padding:.55rem 1rem;
    font-family:'Cinzel',serif;font-size:.8rem;letter-spacing:.07em;cursor:pointer;
    border-radius:4px;white-space:nowrap;transition:all .12s}
  .go:hover{background:#1e3850}
  .cols{display:grid;gap:1px;background:#141e28;border:1px solid #1e2e3e;
    border-radius:5px;overflow:hidden;margin-bottom:.6rem}
  .cols-1{grid-template-columns:1fr}
  .cols-2{grid-template-columns:1fr 1fr}
  .cols-3{grid-template-columns:1fr 1fr 1fr}
  .col{background:#0f1820;padding:.7rem 1rem}
  .col-lbl{font-family:'JetBrains Mono',monospace;font-size:.62rem;letter-spacing:.12em;
    text-transform:uppercase;margin-bottom:.3rem}
  .col-form{font-size:1.9rem;color:#e8ddc8;letter-spacing:.04em;min-height:2.3rem;
    font-family:'EB Garamond',serif}
  .col-warn{font-size:.65rem;color:#c8902a;font-family:'JetBrains Mono',monospace;margin-top:.15rem}
  .step-ctrl{display:flex;gap:.4rem;margin-bottom:.4rem}
  .tog{background:none;border:1px solid #1e2e3e;color:#3a5068;padding:3px 9px;
    font-size:.72rem;font-family:'JetBrains Mono',monospace;cursor:pointer;border-radius:3px;
    transition:all .12s}
  .tog:hover{border-color:#3a5068;color:#6a8090}
  .tabs{display:flex;gap:.2rem;margin-bottom:0}
  .tab{background:#0f1820;border:1px solid #1e2e3e;border-bottom:none;color:#3a5068;
    padding:4px 11px;font-size:.77rem;cursor:pointer;border-radius:3px 3px 0 0;
    font-family:'JetBrains Mono',monospace;transition:all .12s}
  .tab.on{background:#131e2a;color:#8aaabb;border-color:#2a4050}
  .steps-box{background:#0f1820;border:1px solid #1e2e3e;border-radius:0 4px 4px 4px;overflow:hidden}
  .shdr{font-family:'JetBrains Mono',monospace;font-size:.6rem;letter-spacing:.13em;
    text-transform:uppercase;padding:.35rem 1rem .1rem}
  .srow{display:flex;align-items:center;padding:.28rem 1rem;gap:.6rem;
    border-top:1px solid #111820}
  .srow:hover{background:#111c26}
  .sdot{width:5px;height:5px;border-radius:50%;flex-shrink:0}
  .srule{flex:1;font-size:.8rem;color:#3a5060;font-family:'EB Garamond',serif}
  .sform{font-size:1rem;color:#b8c8d0;letter-spacing:.03em;font-family:'EB Garamond',serif}
  .final-row{display:flex;align-items:center;padding:.5rem 1rem;gap:.6rem;
    border-top:1px solid #1e2e3e;background:#0c1520}
  .final-lbl{font-family:'JetBrains Mono',monospace;font-size:.6rem;letter-spacing:.12em;
    text-transform:uppercase;color:#2a4050;flex:1}
  .final-form{font-family:'EB Garamond',serif;font-size:1.3rem;color:#e8ddc8;letter-spacing:.04em}
  .help{margin-top:1.5rem;padding:.8rem 1rem;background:#0c1520;border:1px solid #1a2630;
    border-radius:4px;font-size:.82rem;color:#2e4050;line-height:1.7}
  .help code{font-family:'JetBrains Mono',monospace;font-size:.8em;color:#3a6070}
`;

export default function App() {
  const [input, setInput] = useState('');
  const [results, setResults] = useState(null);
  const [showSteps, setShowSteps] = useState(false);
  const [activeTab, setActiveTab] = useState('ghandwa');
  const [selLangs, setSelLangs] = useState(['ghandwa','old','neo']);

  function run(val) {
    const v = (val ?? input).trim();
    if (!v) return;
    const r = transformAll(v, selLangs);
    setResults(r);
    setShowSteps(false);
    if (!selLangs.includes(activeTab) && selLangs.length > 0) setActiveTab(selLangs[0]);
  }

  function clickEx(label) {
    setInput(label);
    setResults(transformAll(label, selLangs));
    setShowSteps(false);
  }

  function toggleLang(id) {
    setSelLangs(prev => prev.includes(id) ? prev.filter(x=>x!==id) : [...prev,id]);
    setResults(null);
  }

  const activeLangs = LANG_DEFS.filter(l => selLangs.includes(l.id));
  const colCls = `cols cols-${activeLangs.length||1}`;
  const activeResult = results?.[activeTab];
  const activeGroups = activeResult ? groupSteps(activeResult.steps) : [];

  return (
    <>
      <style>{css}</style>
      <div className="app">
        <h1>PIE Multi-Language Transformer</h1>
        <p className="sub">Ghandwa · Old wékʷos · Neo-wékʷos</p>

        <div className="examples">
          {EXAMPLES.map(ex => (
            <button key={ex.label} className="ex-btn" onClick={() => clickEx(ex.label)}>
              {ex.label}
              {ex.note && <span className="ex-note">{ex.note}</span>}
            </button>
          ))}
        </div>

        <div className="lang-row">
          {LANG_DEFS.map(l => (
            <label key={l.id} className="lcheck">
              <input type="checkbox" checked={selLangs.includes(l.id)} onChange={() => toggleLang(l.id)} />
              <span className="ldot" style={{background: l.color}} />
              {l.label}
            </label>
          ))}
        </div>

        <div className="ctrl">
          <input className="inp" value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={e => e.key==='Enter' && run()}
            placeholder="*ph₂tér · bher- · dn̥ǵʰwéh₂s · kw=kʷ · bh=bʰ · H2=h₂"
            spellCheck={false} />
          <button className="go" onClick={() => run()}>Transform</button>
        </div>

        {results && activeLangs.length > 0 && (
          <>
            <div className={colCls}>
              {activeLangs.map(lang => {
                const r = results[lang.id]; if (!r) return null;
                const warns = getWarnings(r.final);
                return (
                  <div key={lang.id} className="col">
                    <div className="col-lbl" style={{color:lang.color}}>{lang.label}</div>
                    <div className="col-form">{r.final||'—'}</div>
                    {warns.length > 0 && <div className="col-warn">⚠ {warns.join(' · ')}</div>}
                  </div>
                );
              })}
            </div>

            <div className="step-ctrl">
              <button className="tog" onClick={() => setShowSteps(v=>!v)}>
                {showSteps ? '▲ hide steps' : '▼ show steps'}
              </button>
            </div>

            {showSteps && (
              <>
                <div className="tabs">
                  {activeLangs.map(lang => results[lang.id] && (
                    <button key={lang.id}
                      className={`tab${activeTab===lang.id?' on':''}`}
                      style={activeTab===lang.id?{borderColor:lang.dimColor,color:lang.color}:{}}
                      onClick={() => setActiveTab(lang.id)}>
                      {lang.label}
                    </button>
                  ))}
                </div>

                <div className="steps-box">
                  {activeGroups.map(({ stage, steps }) => (
                    <div key={stage}>
                      <div className="shdr" style={{color:STAGE_DOT[stage]||'#3a4a5a'}}>{stage}</div>
                      {steps.map((step, idx) => (
                        <div key={idx} className="srow">
                          <div className="sdot" style={{background:STAGE_DOT[stage]||'#3a4a5a'}} />
                          <span className="srule">{step.label}</span>
                          <span className="sform">{step.form}</span>
                        </div>
                      ))}
                    </div>
                  ))}
                  <div className="final-row">
                    <span className="final-lbl">final output</span>
                    <span className="final-form">{activeResult?.final}</span>
                  </div>
                </div>
              </>
            )}
          </>
        )}

        <div className="help">
          <strong style={{color:'#3a6070'}}>Input shortcuts:</strong>&nbsp;
          <code>bh</code>→<code>bʰ</code> &nbsp;<code>dh</code>→<code>dʰ</code> &nbsp;
          <code>gh</code>→<code>gʰ</code> &nbsp;<code>kw</code>→<code>kʷ</code> &nbsp;
          <code>H2/h2</code>→<code>h₂</code> &nbsp;<code>n.</code>→<code>n̥</code> &nbsp;
          <code>e:</code>→<code>ē</code> &nbsp;·&nbsp; Leading <code>*</code> and stress marks stripped.
        </div>
      </div>
    </>
  );
}
