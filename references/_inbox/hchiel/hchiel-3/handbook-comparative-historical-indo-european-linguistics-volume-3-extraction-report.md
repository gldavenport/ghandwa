# Extraction report — Handbook of Comparative and Historical Indo-European Linguistics — Volume 3

## Source identification

- Source file: `978-3-11-054052-9.epub.zip`
- Source type treated as: EPUB.
- Primary input: EPUB XHTML/text layer from `OPS/content/*.xhtml` in spine order.
- EPUB internal image directory: `OPS/graphic/`.
- Image handling: all non-metadata files in `OPS/graphic/` were copied as-is to `images/` with kebab-case names. No OCR or visual inference was attempted for image contents.
- Chunking: applied by the source's own article/chapter labels, 80–125, with front matter, per-chapter bibliography/reference files, and a combined index file separated.
- Page ranges: print page markers were not encoded in the EPUB text layer; YAML `pages:` fields and README page ranges therefore use `not encoded in EPUB`.

## Corrections applied

- XHTML entities were decoded into Unicode characters where present.
- Soft hyphen artifacts were removed.
- Empty visual spacer spans were converted to spaces where detected.
- Superscript/subscript spans were converted to Unicode superscript/subscript characters where clear; unsupported or ordinal superscripts were retained as HTML `<sup>...</sup>`.
- Common isolated ASCII laryngeal leakage patterns `h1`, `h2`, `h3` were repaired to `h₁`, `h₂`, `h₃` outside links, image references, source comments, and inline image tags. Approximate affected lines: 18.
- HTML tables were converted to Markdown tables when simple and headered; complex or headerless tables were retained as simplified HTML tables to avoid structural loss.
- EPUB index locator links with artificial visible labels such as `1`, `2`, `3` were removed from index entries; print-style page/page-range references were retained.
- Paragraph boundaries, headings, lists, index entries, bibliography entries, and source-location comments were reconstructed from the EPUB block structure.
- Inline EPUB glyph images with clear Unicode equivalents were substituted directly: `i_Mac.png` → `ī`, `u_Mac.png` → `ū`, `teta.png` → `θ`, `a_dgrave.png` → `ȁ`.
- Inline EPUB glyph images without a clear single Unicode equivalent were preserved as image references with inline `[image-glyph: ...]` annotations.
- Non-glyph image references were inserted for `<img>` locations rather than replacing image-only tables/figures with guessed text.
- Per-chapter references sections removed from chapter content files and written to separate `bibliography-chNN` companion files. Sections separated: 46.

## Chunking and output structure

- `handbook-comparative-historical-indo-european-linguistics-volume-3-front-matter.md` — Front matter (Cover, title page, copyright, contents)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch80.md` — 80. The documentation of Slavic (XIII. Slavic; 80. The documentation of Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch80.md` — Bibliography — 80. The documentation of Slavic (References for 80. The documentation of Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch81.md` — 81. The phonology of Slavic (XIII. Slavic; 81. The phonology of Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch81.md` — Bibliography — 81. The phonology of Slavic (References for 81. The phonology of Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch82.md` — 82. The morphology of Slavic (XIII. Slavic; 82. The morphology of Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch82.md` — Bibliography — 82. The morphology of Slavic (References for 82. The morphology of Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch83.md` — 83. The syntax of Slavic (XIII. Slavic; 83. The syntax of Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch83.md` — Bibliography — 83. The syntax of Slavic (References for 83. The syntax of Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch84.md` — 84. The lexicon of Slavic (XIII. Slavic; 84. The lexicon of Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch84.md` — Bibliography — 84. The lexicon of Slavic (References for 84. The lexicon of Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch85.md` — 85. The dialectology of Slavic (XIII. Slavic; 85. The dialectology of Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch85.md` — Bibliography — 85. The dialectology of Slavic (References for 85. The dialectology of Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch86.md` — 86. The evolution of Slavic (XIII. Slavic; 86. The evolution of Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch86.md` — Bibliography — 86. The evolution of Slavic (References for 86. The evolution of Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch87.md` — 87. The documentation of Baltic (XIV. Baltic; 87. The documentation of Baltic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch87.md` — Bibliography — 87. The documentation of Baltic (References for 87. The documentation of Baltic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch88.md` — 88. The phonology of Baltic (XIV. Baltic; 88. The phonology of Baltic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch88.md` — Bibliography — 88. The phonology of Baltic (References for 88. The phonology of Baltic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch89.md` — 89. The morphology of Baltic (XIV. Baltic; 89. The morphology of Baltic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch89.md` — Bibliography — 89. The morphology of Baltic (References for 89. The morphology of Baltic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch90.md` — 90. The syntax of Baltic (XIV. Baltic; 90. The syntax of Baltic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch90.md` — Bibliography — 90. The syntax of Baltic (References for 90. The syntax of Baltic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch91.md` — 91. The lexicon of Baltic (XIV. Baltic; 91. The lexicon of Baltic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch91.md` — Bibliography — 91. The lexicon of Baltic (References for 91. The lexicon of Baltic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch92.md` — 92. The dialectology of Baltic (XIV. Baltic; 92. The dialectology of Baltic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch92.md` — Bibliography — 92. The dialectology of Baltic (References for 92. The dialectology of Baltic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch93.md` — 93. The evolution of Baltic (XIV. Baltic; 93. The evolution of Baltic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch93.md` — Bibliography — 93. The evolution of Baltic (References for 93. The evolution of Baltic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch94.md` — 94. The documentation of Albanian (XV. Albanian; 94. The documentation of Albanian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch94.md` — Bibliography — 94. The documentation of Albanian (References for 94. The documentation of Albanian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch95.md` — 95. The phonology of Albanian (XV. Albanian; 95. The phonology of Albanian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch95.md` — Bibliography — 95. The phonology of Albanian (References for 95. The phonology of Albanian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch96.md` — 96. The morphology of Albanian (XV. Albanian; 96. The morphology of Albanian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch96.md` — Bibliography — 96. The morphology of Albanian (References for 96. The morphology of Albanian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch97.md` — 97. The syntax of Albanian (XV. Albanian; 97. The syntax of Albanian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch97.md` — Bibliography — 97. The syntax of Albanian (References for 97. The syntax of Albanian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch98.md` — 98. The lexicon of Albanian (XV. Albanian; 98. The lexicon of Albanian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch98.md` — Bibliography — 98. The lexicon of Albanian (References for 98. The lexicon of Albanian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch99.md` — 99. The dialectology of Albanian (XV. Albanian; 99. The dialectology of Albanian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch99.md` — Bibliography — 99. The dialectology of Albanian (References for 99. The dialectology of Albanian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch100.md` — 100. The evolution of Albanian (XV. Albanian; 100. The evolution of Albanian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch100.md` — Bibliography — 100. The evolution of Albanian (References for 100. The evolution of Albanian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch101.md` — 101. Phrygian (XVI. Languages of fragmentary attestation; 101. Phrygian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch101.md` — Bibliography — 101. Phrygian (References for 101. Phrygian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch102.md` — 102. Venetic (XVI. Languages of fragmentary attestation; 102. Venetic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch102.md` — Bibliography — 102. Venetic (References for 102. Venetic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch103.md` — 103. Messapic (XVI. Languages of fragmentary attestation; 103. Messapic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch103.md` — Bibliography — 103. Messapic (References for 103. Messapic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch104.md` — 104. Thracian (XVI. Languages of fragmentary attestation; 104. Thracian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch104.md` — Bibliography — 104. Thracian (References for 104. Thracian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch105.md` — 105. Siculian (XVI. Languages of fragmentary attestation; 105. Siculian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch105.md` — Bibliography — 105. Siculian (References for 105. Siculian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch106.md` — 106. Lusitanian (XVI. Languages of fragmentary attestation; 106. Lusitanian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch106.md` — Bibliography — 106. Lusitanian (References for 106. Lusitanian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch107.md` — 107. Macedonian (XVI. Languages of fragmentary attestation; 107. Macedonian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch107.md` — Bibliography — 107. Macedonian (References for 107. Macedonian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch108.md` — 108. Illyrian (XVI. Languages of fragmentary attestation; 108. Illyrian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch108.md` — Bibliography — 108. Illyrian (References for 108. Illyrian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch109.md` — 109. Pelasgian (XVI. Languages of fragmentary attestation; 109. Pelasgian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch109.md` — Bibliography — 109. Pelasgian (References for 109. Pelasgian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch110.md` — 110. The phonology of Proto-Indo-Iranian (XVII. Indo-Iranian; 110. The phonology of Proto-Indo-Iranian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch110.md` — Bibliography — 110. The phonology of Proto-Indo-Iranian (References for 110. The phonology of Proto-Indo-Iranian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch111.md` — 111. The morphology of Indo-Iranian (XVII. Indo-Iranian; 111. The morphology of Indo-Iranian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch111.md` — Bibliography — 111. The morphology of Indo-Iranian (References for 111. The morphology of Indo-Iranian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch112.md` — 112. The syntax of Indo-Iranian (XVII. Indo-Iranian; 112. The syntax of Indo-Iranian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch112.md` — Bibliography — 112. The syntax of Indo-Iranian (References for 112. The syntax of Indo-Iranian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch113.md` — 113. The lexicon of Indo-Iranian (XVII. Indo-Iranian; 113. The lexicon of Indo-Iranian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch113.md` — Bibliography — 113. The lexicon of Indo-Iranian (References for 113. The lexicon of Indo-Iranian)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch114.md` — 114. Balto-Slavic (XVIII. Balto-Slavic; 114. Balto-Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch114.md` — Bibliography — 114. Balto-Slavic (References for 114. Balto-Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch115.md` — 115. The phonology of Balto-Slavic (XVIII. Balto-Slavic; 115. The phonology of Balto-Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch115.md` — Bibliography — 115. The phonology of Balto-Slavic (References for 115. The phonology of Balto-Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch116.md` — 116. Balto-Slavic morphology (XVIII. Balto-Slavic; 116. Balto-Slavic morphology)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch116.md` — Bibliography — 116. Balto-Slavic morphology (References for 116. Balto-Slavic morphology)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch117.md` — 117. The syntax of Balto-Slavic (XVIII. Balto-Slavic; 117. The syntax of Balto-Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch117.md` — Bibliography — 117. The syntax of Balto-Slavic (References for 117. The syntax of Balto-Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch118.md` — 118. The lexicon of Balto-Slavic (XVIII. Balto-Slavic; 118. The lexicon of Balto-Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch118.md` — Bibliography — 118. The lexicon of Balto-Slavic (References for 118. The lexicon of Balto-Slavic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch119.md` — 119. The shared features of Italic and Celtic (XIX. Wider configurations and contacts; 119. The shared features of Italic and Celtic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch119.md` — Bibliography — 119. The shared features of Italic and Celtic (References for 119. The shared features of Italic and Celtic)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch120.md` — 120. Graeco-Anatolian contacts in the Mycenaean period (XIX. Wider configurations and contacts; 120. Graeco-Anatolian contacts in the Mycenaean period)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch120.md` — Bibliography — 120. Graeco-Anatolian contacts in the Mycenaean period (References for 120. Graeco-Anatolian contacts in the Mycenaean period)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch121.md` — 121. The phonology of Proto-Indo-European (XX. Proto-Indo-European; 121. The phonology of Proto-Indo-European)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch121.md` — Bibliography — 121. The phonology of Proto-Indo-European (References for 121. The phonology of Proto-Indo-European)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch122.md` — 122. The morphology of Proto-Indo-European (XX. Proto-Indo-European; 122. The morphology of Proto-Indo-European)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch122.md` — Bibliography — 122. The morphology of Proto-Indo-European (References for 122. The morphology of Proto-Indo-European)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch123.md` — 123. The syntax of Proto-Indo-European (XX. Proto-Indo-European; 123. The syntax of Proto-Indo-European)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch123.md` — Bibliography — 123. The syntax of Proto-Indo-European (References for 123. The syntax of Proto-Indo-European)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch124.md` — 124. The lexicon of Proto-Indo-European (XX. Proto-Indo-European; 124. The lexicon of Proto-Indo-European)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch124.md` — Bibliography — 124. The lexicon of Proto-Indo-European (References for 124. The lexicon of Proto-Indo-European)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-ch125.md` — 125. More remote relationships of Proto-Indo-European (XXI. Beyond Proto-Indo-European; 125. More remote relationships of Proto-Indo-European)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-bibliography-ch125.md` — Bibliography — 125. More remote relationships of Proto-Indo-European (References for 125. More remote relationships of Proto-Indo-European)
- `handbook-comparative-historical-indo-european-linguistics-volume-3-index.md` — Index (General index and Languages and dialect index)

## Image extraction summary

- Image files copied from `OPS/graphic/`: 383
- Image references inserted in Markdown: 557
- Block image references: 316
- Inline image references: 241
- Inline image-glyph substitutions: 68
- Inline image-glyph unresolved annotations: 117
- `[image-only...]` fallback placeholders used: 0, because binary image copying was available.

Sample image mapping:

- `01_Cover_fig_01.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-cover.png`
- `04_Title_fig_01.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-title-page-image.png`
- `07_chapter01_fig_01.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-001.png`
- `07_chapter01_fig_02.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-002.png`
- `07_chapter01_fig_03.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-003.png`
- `07_chapter01_fig_04.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-004.png`
- `07_chapter01_fig_05.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-005.png`
- `07_chapter01_fig_06.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-006.png`
- `07_chapter01_fig_07.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-007.png`
- `07_chapter01_fig_08.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-008.png`
- `07_chapter01_fig_09.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-009.png`
- `07_chapter01_fig_10.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-010.png`
- `07_chapter01_fig_100.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-100.png`
- `07_chapter01_fig_101.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-101.png`
- `07_chapter01_fig_102.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-102.png`
- `07_chapter01_fig_103.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-103.png`
- `07_chapter01_fig_104.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-104.png`
- `07_chapter01_fig_105.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-105.png`
- `07_chapter01_fig_106.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-106.png`
- `07_chapter01_fig_107.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-107.png`
- `07_chapter01_fig_108.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-108.png`
- `07_chapter01_fig_109.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-109.png`
- `07_chapter01_fig_11.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-011.png`
- `07_chapter01_fig_110.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-110.png`
- `07_chapter01_fig_111.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-111.png`
- `07_chapter01_fig_112.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-112.png`
- `07_chapter01_fig_113.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-113.png`
- `07_chapter01_fig_114.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-114.png`
- `07_chapter01_fig_115.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-115.png`
- `07_chapter01_fig_116.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-116.png`
- `07_chapter01_fig_117.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-117.png`
- `07_chapter01_fig_118.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-118.png`
- `07_chapter01_fig_119.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-119.png`
- `07_chapter01_fig_12.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-012.png`
- `07_chapter01_fig_120.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-120.png`
- `07_chapter01_fig_121.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-121.png`
- `07_chapter01_fig_122.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-122.png`
- `07_chapter01_fig_123.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-123.png`
- `07_chapter01_fig_124.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-124.png`
- `07_chapter01_fig_125.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-125.png`
- `07_chapter01_fig_126.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-126.png`
- `07_chapter01_fig_127.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-127.png`
- `07_chapter01_fig_128.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-128.png`
- `07_chapter01_fig_129.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-129.png`
- `07_chapter01_fig_13.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-013.png`
- `07_chapter01_fig_130.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-130.png`
- `07_chapter01_fig_131.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-131.png`
- `07_chapter01_fig_132.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-132.png`
- `07_chapter01_fig_133.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-133.png`
- `07_chapter01_fig_134.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-134.png`
- `07_chapter01_fig_135.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-135.png`
- `07_chapter01_fig_136.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-136.png`
- `07_chapter01_fig_137.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-137.png`
- `07_chapter01_fig_138.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-138.png`
- `07_chapter01_fig_139.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-139.png`
- `07_chapter01_fig_14.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-014.png`
- `07_chapter01_fig_140.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-140.png`
- `07_chapter01_fig_141.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-141.png`
- `07_chapter01_fig_142.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-142.png`
- `07_chapter01_fig_143.png` → `images/handbook-comparative-historical-indo-european-linguistics-volume-3-fig-chapter01-143.png`
- ... 323 additional image files listed in manifest.json.

## Image-glyph inventory

| Source filename | Status | Output/reference | Description | Occurrences | EPUB XHTML locations |
|---|---|---|---|---:|---|
| `L_Tilde.png` | unresolved | `images/handbook-comparative-historical-indo-european-linguistics-volume-3-img-l-tilde.png` | l with tilde | 29 | 07_chapter01_2.xhtml (1); 07_chapter01_9.xhtml (5); 08_chapter02_2.xhtml (4); 08_chapter02_5.xhtml (9); 12_chapter06_1.xhtml (2); 12_chapter06_2.xhtml (3); 14_chapter08_13.xhtml (2); 14_chapter08_14.xhtml (1); 14_chapter08_2.xhtml (1); 14_chapter08_3.xhtml (1) |
| `O_Tilde.png` | unresolved | `images/handbook-comparative-historical-indo-european-linguistics-volume-3-img-o-tilde.png` | o with macron and tilde | 9 | 07_chapter01_7.xhtml (3); 14_chapter08_3.xhtml (2); 14_chapter08_4.xhtml (2); 14_chapter08_6.xhtml (2) |
| `Reversed_c_Tilde.png` | unresolved | `images/handbook-comparative-historical-indo-european-linguistics-volume-3-img-reversed-c-tilde.png` | open o / reversed c with tilde | 24 | 07_chapter01_3.xhtml (2); 07_chapter01_4.xhtml (18); 07_chapter01_5.xhtml (2); 08_chapter02_6.xhtml (2) |
| `V_Tilde.png` | unresolved | `images/handbook-comparative-historical-indo-european-linguistics-volume-3-img-v-tilde.png` | V with tilde | 1 | 07_chapter01_3.xhtml (1) |
| `a_dgrave.png` | substituted | `ȁ` | Latin small a with double grave | 4 | 07_chapter01_4.xhtml (3); 07_chapter01_6.xhtml (1) |
| `ae_Tilde.png` | unresolved | `images/handbook-comparative-historical-indo-european-linguistics-volume-3-img-ae-tilde.png` | æ with tilde | 20 | 07_chapter01_4.xhtml (20) |
| `epsilon_Tilde.png` | unresolved | `images/handbook-comparative-historical-indo-european-linguistics-volume-3-img-epsilon-tilde.png` | Greek epsilon with tilde | 29 | 07_chapter01_3.xhtml (11); 07_chapter01_4.xhtml (18) |
| `epsilon_hypine.png` | unresolved | `images/handbook-comparative-historical-indo-european-linguistics-volume-3-img-epsilon-hypine.png` | Greek epsilon with overmark/acute-style mark | 1 | 07_chapter01_4.xhtml (1) |
| `i_Mac.png` | substituted | `ī` | Latin small i with macron | 14 | 07_chapter01_2.xhtml (1); 07_chapter01_4.xhtml (1); 08_chapter02_2.xhtml (1); 08_chapter02_3.xhtml (1); 09_chapter03_3.xhtml (1); 11_chapter05_3.xhtml (1); 11_chapter05_5.xhtml (2); 11_chapter05_6.xhtml (3); 12_chapter06_1.xhtml (1); 14_chapter08_1.xhtml (1); 14_chapter08_15.xhtml (1) |
| `r_Tilde.png` | unresolved | `images/handbook-comparative-historical-indo-european-linguistics-volume-3-img-r-tilde.png` | r with tilde | 1 | 07_chapter01_7.xhtml (1) |
| `schwa_breve.png` | unresolved | `images/handbook-comparative-historical-indo-european-linguistics-volume-3-img-schwa-breve.png` | schwa with breve | 3 | 07_chapter01_4.xhtml (2); 07_chapter01_5.xhtml (1) |
| `teta.png` | substituted | `θ` | Greek small theta | 42 | 10_chapter04_3.xhtml (1); 14_chapter08_1.xhtml (14); 14_chapter08_2.xhtml (10); 14_chapter08_3.xhtml (2); 14_chapter08_4.xhtml (1); 14_chapter08_5.xhtml (9); 14_chapter08_6.xhtml (3); 14_chapter08_7.xhtml (2) |
| `u_Mac.png` | substituted | `ū` | Latin small u with macron | 8 | 07_chapter01_2.xhtml (1); 11_chapter05_3.xhtml (1); 11_chapter05_5.xhtml (3); 13_chapter07.xhtml (2); 14_chapter08_1.xhtml (1) |

## Unresolved issues list

1. Image-only tables, paradigms, scripts, and formula blocks are preserved as image references rather than transcribed. This avoids visual guessing but leaves those portions non-searchable as text.
2. Inline glyph images without a clear single Unicode equivalent are preserved with `[image-glyph: ...]` annotations rather than silently guessed.
3. The source does not encode print pagebreak markers in the XHTML layer, so page ranges could not be assigned to chunks.
4. Bibliography/reference sections were separated by automated heading detection. Human review should verify that no late chapter matter after a References heading was intended to remain in the chapter body.
5. Some bibliography entries may remain as separate source paragraphs rather than fully joined citation records where the EPUB split author/year/title across multiple `<p>` elements.
6. The QC pass was automated. It cannot detect errors that were consistently encoded in the EPUB text layer or consistently introduced by conversion rules.

## Confusion-pair report

- h₁ h₂ h₃ vs h1 h2 h3: no obvious automated red-flag pattern found; not fully verified.
- ā ē ī ō ū macrons: automated red-flag pattern(s) present for human review: `a\u0304|e\u0304|i\u0304|o\u0304|u\u0304`: 7.
- ʰ ʷ vs h w: no obvious automated red-flag pattern found; not fully verified.
- ə vs e/9: automated red-flag pattern(s) present for human review: `(?<![A-Za-z])9(?![A-Za-z])`: 17782.
- ṛ ḷ ṃ ṇ underdots: automated red-flag pattern(s) present for human review: `\br\b`: 402; `\bl\b`: 356.
- ǵ ḱ vs g'/k': automated red-flag pattern(s) present for human review: `k'`: 1.
- * before reconstructed forms: automated red-flag pattern(s) present for human review: `×`: 1.
- † dagger vs +: automated red-flag pattern(s) present for human review: `\+`: 292.

## Codepoint inventory

Approximate counts for cross-pass comparison only:

```json
{
  "note": "All counts are approximate and for cross-pass comparison only.",
  "laryngeals": {
    "h1": 541,
    "h2": 885,
    "h3": 158
  },
  "macron_a": 2506,
  "macron_e": 881,
  "macron_i": 893,
  "macron_o": 845,
  "macron_u": 640,
  "schwa": 261,
  "greek_chars": 8588,
  "combining_diacritics": 5765,
  "dagger": 49
}
```

Additional approximate metrics:

- EPUB XHTML files processed: 86
- Markdown tables produced: 0
- Simplified HTML tables produced: 113
- Empty/source anchors removed: 1577
- Empty spacer spans converted: 1298
- Index locator anchors removed: 16231
- `[unclear]` markers in output: 0
- `[?]` inferred-character markers in output: 6
- Inline image-glyph substitutions: 68
- Inline image-glyph unresolved annotations: 117

## Structural integrity check

- Headings were generated from EPUB `h1`–`h6` elements, then shifted within each chunk so the chunk title is H1.
- Chapter/article chunks follow the source's own labels: 80–125.
- References sections were written to separate bibliography files named according to the matching content chunk identifier.
- Both source index sections were combined into `handbook-comparative-historical-indo-european-linguistics-volume-3-index.md`; index-list entries are preserved one per line where EPUB index-list semantics made this detectable.
- Table handling is mixed: simple headered tables are Markdown; complex/headerless tables are simplified HTML.
- Images are stored under `images/` and referenced from Markdown by relative path.
- Footnotes/endnotes were not detected as distinct EPUB footnote structures in this package.
- Continuation text at EPUB XHTML file boundaries was not manually verified against a rendered edition.
- No claim is made that the output is character-authoritative for unresolved image-only material; a pass using a publisher PDF text layer would likely improve image-rendered tables or glyphs if such text exists there.
