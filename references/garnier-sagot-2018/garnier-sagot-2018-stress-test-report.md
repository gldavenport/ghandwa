---
source_title: "New results on a centum substratum in Greek: the Lydian connection"
source_file_name: "garnier-sagot-2018.pdf"
stress_test_date: "2026-05-06"
pass_status: "complete"
---

# Stress-test report — Garnier & Sagot 2018

## Tests run

### Artifact scan

Searched the Markdown extraction for:

- replacement character `�`
- private-use characters
- `U+FFFF`
- raw micro sign `µ`
- obvious page-layout hyphenation residues from HAL cover text
- unresolved `[unclear]` markers
- malformed Markdown emphasis around reconstructed starred forms

### Character-sensitive search tests

Confirmed searchable strings in the final Markdown:

- `μόλυβδος`
- `mariwda-`
- `/marǝwđa/`
- `*morgʷiyo-`
- `Λῡδός`
- `λύγδος`
- `κίβδος`
- `σίβδη`
- `ἄχερδος`
- `αὐτοκάβδαλος`
- `καλύϐη`
- `κολοϐός`
- `Κύρβαντες`
- `λυκάβαντ-`
- `Inschrifensammlung`

## Results

- No replacement characters found.
- No private-use characters found.
- No `U+FFFF` found.
- No raw micro sign `µ` remains.
- No `[unclear]` markers remain.
- The key Greek and reconstructed forms are searchable.
- Markdown emphasis around starred reconstructed forms was protected with escaped asterisks where needed or encoded as italicized whole forms where unambiguous.

## Repairs applied during stress testing

- Corrected raw-extraction `µόλυβδος` to `μόλυβδος`.
- Corrected `*morgwiyo-` to `*morgʷiyo-`.
- Preserved `καλύϐη` and `κολοϐός` with Greek beta-symbol `ϐ`.
- Rejoined HAL cover-page hyphenation: `re-search`, `pri-vate`, `des-tinée`, `scien-tifiques`.
- Rebuilt the page-2 linguistic core as paragraphs and a list rather than preserving source line wrapping.

## Assessment

This extraction is character-authoritative for the short source within the limits of rendered-page inspection. Further useful work would be limited to external bibliographic normalization, not source transcription accuracy.
