# West 2007 Extraction Notes — Additional Passes

## Pass status

This package contains a third-pass working Markdown extraction of M. L. West, *Indo-European Poetry and Myth* (2007), derived from the first-pass extraction and the original PDF.

## Second pass performed

- Removed duplicated all-caps source headings where the same heading had already been inserted as Markdown from the PDF outline.
- Added a `# Preface` heading.
- Added an accessible description of the stemmatic diagram on PDF page 35.
- Joined obvious line-break hyphenation in prose.
- Cleaned common ligature-spacing artifacts such as `di fferent`, `o ffer`, `identi fied`, `in fluence`, and related forms.
- Normalized some front-matter spacing artifacts such as `New Y ork`, `Cape T own`, and `V erse`.

## Third-pass character audit performed

- Converted the high-frequency Greek final-sigma artifact `δΖi˜maa;t` to `ς`.
- Converted the Greek digamma artifact `δGammaa;t` to `ϝ`.
- Converted Greek micro-sign mu `µ` to Greek `μ`.
- Converted high-confidence PIE font artifacts such as `/hooktopk` to `ḱ`, `/superh` to `ʰ`, `/superw` to `ʷ`, and `/subarchg` to `ǵ`.
- Converted many spacing diacritic sequences to Unicode characters or combining sequences, including macron, acute, breve, tilde, caron, cedilla, ogonek, ring below, and Indic/Avestan-style dot below.
- Spot-checked PDF page 6 for `saṃhitā`, PDF page 35 for the stemmatic diagram, and PDF page 99 for a dense mixed Vedic/Greek passage.

## Remaining known limitations

This is materially better than the first pass, but it is not a fully hand-verified scholarly edition. Greek polytonic breathing/accents and some specialized PIE typography still contain unresolved extraction artifacts. The remaining artifacts are concentrated in dense Greek quotations, PIE reconstructions, and the index.

## Remaining artifact counts after cleanup

- final-sigma artifact δΖi˜maa;t: 0
- digamma artifact δGammaa;t: 0
- /hooktop: 0
- /superh: 0
- /superw: 0
- /subarch: 21
- upΖ: 5
- Ζ: 101
- spacing macron ¯: 111
- spacing acute ´: 54
- spacing dot ˙: 115
- spacing caron ˇ: 13
- spacing breve ˘: 10
- spacing tilde ˜: 4
- spacing ogonek ˛: 10
- spacing ring ˚: 0

## Sample unresolved contexts

- `/subarch`: `. 15, / 9. 10, Isth. 8. 62; fr. 341 μνα<μο>νόοι Μοι / /subarch / σαι; Theoc. 16. 42–5. According to Plutarch, Quae`
- `/subarch`: `nd. Isth. 1. 14, / al.; Nünlist (1998), 86 f. ποιει / /subarch / ν: Solon 20. 3, Theognidea 771, etc. On the whole`
- `/subarch`: `es the Muse to / direct or strengthen the songs’ οὐ / /subarch / ρος, the following wind that helps a ship on / its `
- `/subarch`: `but is shortened by correption. The semivowels / i/i/subarch and u/ u/subarch, as the second element of a diph`
- `/subarch`: `by correption. The semivowels / i/i/subarch and u/ u/subarch, as the second element of a diphthong, are treate`
- `/subarch`: `y instance is / Hes. Op. 25 f. καὶ κεραμεὺς κεραμει / /subarch /  κοτέει καὶ τέκτονι τέκτων, | καὶ πτωχὸς πτωχῶι φ`
- `/subarch`: `ulkes; Skáldsk. 3. / 50 Hes. Th. 69 ἀμβροσίηι μολπη / /subarch / ι (cf. 43 ἄμβροτον ὄσσαν); Hymn. Hom. 27. 18 / ἀμβρ`
- `/subarch`: `rom every / citizen of Thebes, ἀνὴρ γυνή τε χὤτι τω /subarchν μεταίχμιον, ‘man and woman / and whatever is in th`
- `upΖ`: `he bardoi as poets who sang praises: ποιηταὶ δὲ οδupΖi;onti;deaΖperτοι τυγχάνουσι μετ’ / ὠιδῆς ἐπαίνους λ`
- `upΖ`: `edians: / Soph. Aj. 1237 ποῦ βάντος ἢ ποῦ στάντος οδupΖi;onti;deaΖperπερ οὐκ ἐγώ; ‘where did he step, / whe`
- `upΖ`: ` but auditory: / κνήμηι νεκρὸς ὄνος με κερασφόρωι οδupΖi;onti;de;eniΖας ἔκρουσεν. / A dead ass struck my ea`
- `upΖ`: `cal renewal: in Homer κλέος ἐσθλόν (replacing * ἐδupΖi;oñravediereΖiΖ κλέος), in Avestan / vohu sravō (Y.`
- `upΖ`: `tation of the Homeric formula ὀδὰξ ἕλον ἄσπετον οδupΖi;onti;de;eniΖδας (Il. 19. 61, / al.) as ‘bit the du`
- `Ζ`: ` as ‘songs’ or ‘words’, for / example: / δetati;de;eniΖ σὺν Χαρίτεσσι βαθυζώνοις ὑφάνας ὕμνον ἀπὸ ζαθέας / `
- `Ζ`: `th. 3. 113 ἐπέων κελαδεννῶν, τέκτονες οδiotati;deaΖperα σοφοί | α῞ρμοσαν, ‘resounding / verses such as `
- `Ζ`: ` bardoi as poets who sang praises: ποιηταὶ δὲ οδupΖi;onti;deaΖperτοι τυγχάνουσι μετ’ / ὠιδῆς ἐπαίνους λ`
- `Ζ`: `poets who sang praises: ποιηταὶ δὲ οδupΖi;onti;deaΖperτοι τυγχάνουσι μετ’ / ὠιδῆς ἐπαίνους λέγοντες. He`
- `Ζ`: `ρις‘Ill-Paris’, in the Odyssey ΚακοδiotaacutediereΖiΖλιος‘evil Troy’, in Alcman / Αἰνόπαρις, in Euripid`
- `Ζ`: `ς‘Ill-Paris’, in the Odyssey ΚακοδiotaacutediereΖiΖλιος‘evil Troy’, in Alcman / Αἰνόπαρις, in Euripides`
- `Ζ`: `e a heart of / bronze or iron, χάλκεον δetati;de;eniΖτορIl. 2. 490; σιδήρεος θυμός 22. 357, δetati;de;e`
- `Ζ`: `ρIl. 2. 490; σιδήρεος θυμός 22. 357, δetati;de;eniΖτορ 24. 205, / 521, κραδίηOd. 4. 293; ἀδάμαντος θυμό`
- `etati;de;eni`: `objects such as ‘songs’ or ‘words’, for / example: / δetati;de;eniΖ σὺν Χαρίτεσσι βαθυζώνοις ὑφάνας ὕμνον ἀπὸ ζαθέας`
- `etati;de;eni`: `Homer to have a heart of / bronze or iron, χάλκεον δetati;de;eniΖτορIl. 2. 490; σιδήρεος θυμός 22. 357, δetati;de;`
- `etati;de;eni`: `ti;de;eniΖτορIl. 2. 490; σιδήρεος θυμός 22. 357, δetati;de;eniΖτορ 24. 205, / 521, κραδίηOd. 4. 293; ἀδάμαντος θυμ`
- `etati;de;eni`: `striking Homeric expression ἐγέλασσε δέ οἱ φίλον δetati;de;eniΖτορ (Il. 21. / 389), ἐμὸν δ’ ἐγέλασσε φίλον κῆρ (Od`
- `etati;de;eni`: `ng; the same structure appears in Od. 20. 287 f. δetati;de;eniΖν δέ τις ἐν μνηστῆρσιν ἀνὴρ ἀθεμίστια / εἰδώς, Κτήσ`
- `etati;de;eni`: `light variations. / Thus in Greek, Alcman, PMGF 74 δetati;de;eniΖσκέ τις Καφεὺς ϝανάσσων; Xenophon of Ephesus 1. 1`
- `etati;de;eni`: `κέ τις Καφεὺς ϝανάσσων; Xenophon of Ephesus 1. 1 δetati;de;eniΖν ἐν’Εφέσωι ἀνὴρ τῶν τα `  πρῶτα ἐκεῖ δυναμένων, / `
- `etati;de;eni`: `be’ (Y. 33. 10, cf. 45. 7, 51. 22); πάνθ’ ὅσα τ’ / δetati;de;eniΖν ὅσα τ’ ἐστὶ καὶ ἔσται ‘everything that was and `
- `ravediere`: `ewal: in Homer κλέος ἐσθλόν (replacing * ἐδupΖi;oñravediereΖiΖ κλέος), in Avestan / vohu sravō (Y. 30. 10, al.)`

## Further-pass recommendation

A fourth pass would add value only if targeted at Greek/polytonic passages, PIE reconstructions, or index entries. For ordinary corpus search and reading, this third-pass file is the recommended working copy. For quotation of Greek, Vedic, Avestan, or reconstructed forms, verify the local passage against the PDF page image.

## Postscript cleanup

After the pass log above was generated, a small exact-match cleanup corrected `saṃ hitā`, `blackbelt`, and several high-frequency Sanskrit proper-name spacing artifacts such as `Droṇ a`, `Pāṇ ḍavas`, and `Purāṇ as`. The artifact-count list above should be read as a conservative diagnostic snapshot from just before that final exact-match cleanup.
