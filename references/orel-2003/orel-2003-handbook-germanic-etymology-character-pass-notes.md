---
source_title: "A Handbook of Germanic Etymology"
author: "Vladimir Orel"
date: "2003"
publisher: "Brill"
source_type: "PDF book; etymological dictionary"
section: "extraction notes"
extraction_date: "2026-04-28"
notes:
  - "Fourth-pass character-context notes for clean Markdown extraction."
---

# Character-Fidelity Fourth-Pass Notes

This pass targeted the specific residual issues noted after the third pass: polytonic Greek, Baltic/Slavic special characters, and overprinted/legacy-font vowel marks.

## What changed

- Converted Greek spans extracted from the PDF's custom `KadmosNieuw` font into Unicode Greek where the span contained distinctive Greek-font characters.
- Repaired recurring, context-clear bibliographic artifacts, especially Polish and Slavic names and titles: `Białystok`, `Słownik`, `Gołąb`, `Kuryłowicz`, `Otrębski`, `Mažiulis`, `Gdańsk`, `Poznań`, `języka`, and related forms.
- Repaired a few clear source-language contexts such as Sanskrit `aśáni-`, Lithuanian `úošvis`, Avestan `ašta`, and Slavic `*agnę`.
- Rebuilt the lexical-entry TSV from the corrected dictionary Markdown.

## Limits

The pass deliberately avoided broad global substitutions for ambiguous signs. For example, the same extracted character can represent different values depending on source font and language context. A few very short Greek spans consisting only of ordinary ASCII letters may remain unconverted when they lacked a distinctive Kadmos character.

Further improvement would require manual page-image verification of the remaining ambiguous tokens, not another broad automated pass.

## Replacement count

Greek raw-span replacements available from the PDF font context: 1413.

