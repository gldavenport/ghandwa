---
source_title: "A shared substrate between Greek and Italic"
author_creator: "Romain Garnier; Benoît Sagot"
date_year: 2017
source_type: "journal article / HAL open-access PDF"
journal: "Indogermanische Forschungen"
volume_issue_pages: "122(1): 29-60"
doi: "10.1515/if-2017-0002"
hal_id: "hal-01621467"
source_file_name: "garnier-2017.pdf"
extraction_date: "2026-05-06"
extraction_method: "PyMuPDF text extraction with rendered-page spot checks; cleaned to Markdown"
pass_status: "first extraction plus targeted character/structure QA pass plus second character-authority pass plus stress-test repair pass"
notes: "Page anchors preserve PDF page and article page alignment. U+E727 extraction artifact normalized to u̯ after rendered-page verification. Second character pass repaired superscript/citation collisions, DLG² misreadings, broken technical-form joins, and selected Greek/PIE spacing artifacts. Footnotes preserved as Markdown footnotes; italics are not exhaustively encoded. Stress-test pass repaired residual page-break word splits, U+00B4 accent artifact, hₓ notation, and one Sanskrit stem hyphen."
---

# A shared substrate between Greek and Italic

**Authors:** Romain Garnier and Benoît Sagot

**Citation supplied by HAL:** Romain Garnier, Benoît Sagot. A shared substrate between Greek and Italic. *Indogermanische Forschungen*, 2017, 122(1), pp. 29–60. DOI: 10.1515/if-2017-0002. HAL Id: hal-01621467.

**HAL URL:** https://inria.hal.science/hal-01621467v1

**Submitted to HAL:** 6 Jun 2020

**Source note:** The PDF includes a HAL cover page with logo and bilingual archive boilerplate before the article text. The article proper begins on PDF page 2 / article page 29.

<!-- pdf-page: 1 | HAL cover page -->

## HAL cover-page boilerplate

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L’archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d’enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

<!-- pdf-page: 2 | article-page: 29 -->

## Abstract

The Greek lexicon is known for its significant proportion of words lacking a clear etymology. Previous attempts to explain these words range from the so-called “Pelasgian” hypotheses, which resort to an unattested satem Indo-European language, to Beekes’s (2010; 2014) non-Indo-European “Pre-Greek”. In this paper, we reconsider this long-disputed question, and adduce Latin and even Proto-Romance data to unveil a centum language which possibly served as the basis for borrowing in both Common Greek and, at a later date, Common Italic. We analyse several dozen difficult Greek and Italic words as borrowings from this newly identified language, for which we provide a set of phonetic laws that model its development from Proto-Indo-European. Important methodological strengths of our proposal include the systematic correspondence between Greek and Italic forms, the semantic plausibility of our etymologies, and their consistency with what is known about Proto-Indo-European word-formation patterns. Moreover, a computer implementation of these phonetic laws ensures its formal consistency and validates the chronological ordering we put forward. This is all the more important since most of our etymologies involve more than one of these phonetic laws, which is an additional confirmation of the plausibility of our proposal.

**Keywords:** Greek, Italic, Latin, Mediterranean Substrate, Pre-Greek

## 1 Introduction

Greek and Latin have developed from their common Proto-Indo-European (PIE) ancestor in distinct ways, resulting in two languages that exhibit very different features, in particular regarding phonology and word-formation. Moreover, the Greek lexicon has long been recognised for its huge proportion of non-inherited words, among which it is difficult to draw a clear distinction between substrate words and loanwords. Several of the languages that have contributed to shaping the Greek lexicon are Indo-European (IE) languages, including Latin, Anatolian languages, Indo-Iranian languages, Phrygian, and Thracian. Among the IE contributors to the non-inherited Greek lexicon, we identify a new language that also provided substrate elements to Italic languages. Starting from an initial set of semantically plausible and formally coherent correspondences

## Author affiliations and DOI

Romain Garnier: Université de Limoges & Institut Universitaire de France; garromain@gmail.com Benoît Sagot: Inria, France; benoit.sagot@inria.fr

DOI: 10.1515/if-2017-0002

<!-- pdf-page: 3 | article-page: 30 -->

between Greek and/or Latin and PIE, we propose a set of phonetic laws that describe the development from PIE to this new language, a source language for early borrowings in Common Greek and/or Common Italic. This set of laws allows us to suggest etymologies for a few dozen previously unexplained or poorly explained Greek and Latin words. In the remainder of this paper, we shall qualify this newly identified donor language as ‘Substratic’ and indicate reconstructed words in this language by the prefix Substr. This is not to be understood as a statement about the substrate nature of this language — for example, it could actually have played the role of an adstrate rather than a substrate for Common Greek and/or for Common Italic — but rather as a convenient and temporary way to name it. As we shall see, some of the phonetic laws that describe the evolution from PIE to our substrate language are reminiscent of phenomena attested for example in Germanic (Verner-like voice alternations) and Tocharian (voiceless reflexes of voiced aspirated consonants). Contrary to earlier proposals often referred to as Pelasgian, our substrate language appears to be a centum language. The correspondence between Greek and Italic forms, the better semantic plausibility of our etymologies, and the attention paid to being consistent with what is known about PIE word-formation patterns constitute an important methodological improvement over Pelasgian theories. In fact, many of our etymologies concern words that were not studied by “Pelasgianists”; standard “Pelasgic” candidates (e.g. words in -νθ- and -σσ-) do not seem to originate from the substrate language unveiled in this paper. Moreover, we have tested the systematic validity of the suggested phonetic evolution from PIE to our substrate language on all our examples using a computer implementation. Such an implementation also makes it easier to chronologically order the different phonetic laws involved. This paper is organised as follows. We first briefly discuss previous attempts to study the non-inherited component of the Greek lexicon, and, to a lesser extent, of the Latin and Slavic lexica (Section 2). Next, we briefly describe the methodology we followed (Section 3). In the main section of the paper (Section 5), we discuss several dozen Greek and Italic words and word families, which we explain as borrowings from our substrate language, thereby gradually introducing the reduced set of phonetic laws that we propose as a (simplified) model of its phonetic evolution from PIE. In Section 6 we summarise our findings and propose a suitably chosen name for our substrate language.

<!-- pdf-page: 4 | article-page: 31 -->

## 2 Previous work

### 2.1 Pelasgian theories

The most well-known yet generally unconvincing attempts to identify an IE substrate in Greek are the Pelasgian theories mentioned in the introduction. They are centered around the definition of a new substrate IE language often called “Pelasgian”. This hypothetical language was introduced and defined as the single IE substrate language in Greek by a number of scholars (Kretschmer 1925; Georgiev 1941–1945; Carnoy 1955; Budimir 1969; van Windekens 1952); see Katičić 1976 for a critical survey. Their starting point was toponymic evidence, especially from the eastern part of Greece. The most prominent features are suffixes such as -ανθ-/-ινθ-/-υνθ- and -σσ-/-ττ-. These suffixes (as well as some toponyms) seem to have cognates in Anatolia. Many lexical items were also adduced, including words containing the same suffixes.[^1]

The set of laws proposed for modelling the phonetic changes between PIE and Pelasgian vary from one author to the next, but there is a general consensus among defenders of Pelasgian on several points. In particular, Pelasgian is said to be a satem language; PIE aspirated voiced stops are reflected as voiced stops; PIE resonant vowels *-R̥- would be vocalised as *-uR- or *-oR-. Pelasgian theories are now widely rejected. This is because many of the suggested Pelasgian etymologies are virtually unprovable, semantically unconvincing, and/or formally irregular with respect to the set of phonetic laws postulated by their authors (Katičić 1976). A few authors have attempted to explain these formal irregularities by assuming borrowings at different stages of the history of Pelasgian. This is not fully satisfactory, and even less so when more than one hypothetical and non-attested IE language is postulated (see e.g. Haas 1959; Merlingen 1967; Hester 1968). Another difficulty was already noted by Lejeune (1947: 32) and clearly formalised by Katičić (1976: 76), following Hester (1968: 348): “Most of [Georgiev’s] Pelasgian words show only one of the characteristic Pelasgian sound changes. There are only a few words that attest the coherent coexistence of the Pelasgian sound changes in one language and there coincidence by chance is not to be excluded.” Finally, many of the suggested Pelasgian etyma do not conform to standard PIE word-formation patterns. Some of them are just root etymologies (cf. Messing 1958: 87–88 in his review of Carnoy 1955).

<!-- pdf-page: 5 | article-page: 32 -->

### 2.2 Beekes’s homogeneous non-IE Pre-Greek

In his etymological dictionary of the Greek language and follow-up monograph, Beekes (2010) and Beekes (2014), expanding on data from Furnée (1972), defends a different point of view: for him, most non-inherited words in the Greek lexicon are to be interpreted as reflecting a (single) non-IE substrate language, which he names Pre-Greek. This analysis starts from the fact that many non-inherited Greek words are attested in several variants. Important is the fact that these alternations do not seem to be random. For example, Gr. δάφνη ‘laurel’ is also attested as Gr. δαύχν-, which illustrates an alternation of the form -Vφ- ∼ -Vυχ-, which is also attested in other words. Based on such alternations, Beekes draws several conclusions about Pre-Greek. For example, alternations such as φ ∼ π ∼ β lead him to conclude that there is no aspiration or voice opposition. He also identifies pre-nasalisation as a frequent phenomenon (see for example σαλαμβή ∼ σαλαβή ‘vent-hole’). Concerning the -Vφ- ∼ -Vυχ- alternation illustrated by Gr. δάφνη ∼ Gr. δαύχν(α)-, he interprets these forms as reflecting Pre-Greek *dakʷn-. Such a substrate form could be reflected as δαπν-, as the result of the regular treatment of Com. Gr. *kʷ, or as δαυχν-, resulting from the anticipation of the labial component and the lack of an opposition between aspirated and non-aspirated consonants. Such alternations allow Beekes to tentatively reconstruct the Pre-Greek phonological system as a complex one involving palatalised and labialised counterparts for 9 plain consonants out of 10. Although not typologically impossible, extracting such a complex phonological system solely from alternations between loanword variants is not very convincing (Garnier 2015). Beekes insists on Pre-Greek being a single, non-IE language: “[…] we can in some cases say that an IE reconstruction is impossible. A good example is the word γνάτος. […] Another example is the word κρημνός […] The conclusion is that no IE proto-form can be reconstructed, and that the word cannot be IE.” We believe that this line of reasoning does not hold. What Beekes demonstrates is that γνάτος ‘jaw’ and κρημνός ‘overhanging bank’ cannot be inherited IE words, but there is no reason for such words not to have come from another IE language and/or from more than one language, possibly both IE and non-IE (Garnier 2015).

### 2.3 Substrate theories for Latin and Balto-Slavic

Szemerényi (1991) defends the idea of an IE substrate in Italic, which he calls “Ausonian”. His three most interesting examples are the following. First, Lat. Alpēs, -ium ‘Alps’ is interpreted as reflecting *h₁albʰ-éi̯-es ‘white mountains (vel sim.)’ from

<!-- pdf-page: 6 | article-page: 33 -->

PIE *h₁al-bʰ- ‘(to be) white’. Second, he connects Lat. Rutulī ‘Rutulians’ with Lat. rutilus [adj.] ‘red’, interpreted as reflecting *h₁rudʰ-ró- from PIE *h₁rudʰ- ‘(to be) red’. Finally, he suggests that Lat. Tiberis ‘the river Tiber’ comes from Com. It. *tub-rí- < *dʰub-rí- ‘ravine’, from the PIE root *dʰeu̯bʰ- ‘(to be) deep’. We shall come back to this last example in Section 5.5.3. Holzer (1989) proposes the existence of an IE substrate layer in Balto-Slavic (Slavic only for 34 out of 45 etymologies) which he names “Temematic”. Holzer’s proposal is not often discussed but has been positively reviewed (Kortlandt 2003; Matasović 2013: 77–82). In our opinion, the two most promising Temematic etymologies are (1) Com. Sl. *proso [n.] ‘millet’, which Holzer analyses as the expected Temematic reflex of a nominal etymon *bʰr̥so- based on the PIE root *bʰers- ‘burst, bud’,[^2] and (2) Com. Sl. *trǫtŭ [m.] ‘drone’, which he interprets as a borrowing from Temematic *tron- < PIE *dʰrōn- (cf. Eng. drone, Gr. θρῶναξ ‘id.’). In both proposals, the IE substrate language is posited as centum, and PIE aspirated voiced stops are reflected as voiceless stops. These features are two important differences from the hypothetical Pelasgian, and we also find them in the substrate language identified and described in this paper.

## 3 Methodology

Greek and Latin lexica contain many words long recognised as non-inherited, most probably substrate. Several such words are similar in Latin (or Proto-Romance) and Greek, and are often postulated as stemming from a Mediterranean substrate or, for some of the Latin words, as reflecting borrowings from (non-inherited) Greek words via Etruscan, in order to account for phonetic irregularities. Examples of such ‘Mediterranean’ correspondences include Gr. κέλῡφος [n.] ‘husk, shell or skin of fruit’ vs. Proto Romance *kalŭppo- [m.] ‘id.’; Gr. λείβω ‘to pour a libation’ vs. Lat. lībāre ‘id.’; Gr. μίνθη [f.] ‘mint’ vs. Lat. menta [f.] ‘id.’ (cf. Alb. mendër ‘id.’); Gr. πράσον [n.] ‘leek’ vs. Lat. porrum [n.] ‘id.’; Gr. σῦκον [n.] ‘fig’ vs. Lat. fīca [f.] ‘id.’ (cf. Arm. tʿuz ‘id.’); Gr. σφενδόνη [f.] ‘sling’ vs. Lat. funda [f.] ‘id.’; Gr. τύρβη [f.] ‘confusion, tumult’ vs. Lat. turba [f.] ‘id.’. Our first working hypothesis is that some of these word pairs could be explained as borrowings from a single language. This requires the reconstruction, at least for some of the word pairs mentioned above, of substrate words that could explain both the Greek and the Latin (or Proto-Romance) forms. Let us illustrate this preliminary investigation with four examples. By backwardly applying the

<!-- pdf-page: 7 | article-page: 34 -->

well-known phonetic laws relevant to Greek and to Latin, we posit a proto-form *pr̥so- which, if borrowed into Common Italic and Common Greek, would regularly yield the attested Gr. πράσον and Lat. porrum. Similarly, Gr. κέλῡφος and Proto Romance *kalŭppo- call for a common proto-form of the shape *kVlū̆pp-. The case for Gr. λείβω and Lat. lībāre is more complex, since the Greek form is a secondary formation, as we shall see later on. For now, we propose a temporary proto-form *lVi̯b-. Finally, Gr. τύρβη (with its unexpected barytone stress) and Lat. turba call for a proto-form *turba, possibly stressed on the first syllable. We shall come back to these examples in Section 5. Remarkably, it is possible to identify well-known PIE roots that are formally and semantically close to these tentative proto-forms and their meanings. This is the basis of our second working hypothesis, namely that some of our word pairs can be explained as borrowings from a single Indo-European language. However, in order to substantiate this hypothesis, adequate PIE etyma must be proposed that match known IE word-formation patterns and, ideally, have reflexes in other IE languages with similar meanings. In the case of *pr̥so- ‘leek’, a natural candidate is the PIE root *bʰers- ‘to point, burst, bud’ (Pokorny 1959: 109), in the form of a zero-grade noun *bʰr̥s-o-. The zero-grade of this root is attested for example in Com. Celt. *barsos > OIr. barr ‘point, top’ (Matasović 2009: 58) (more on this word in Section 5.5.1). The semantic side of this correspondence is straightforward, since leeks can be thought of as bursting out of the soil. Turning now to *kVlū̆pp- ‘husk, shell or skin of fruit’, the PIE root *ḱel- ‘to cover’ (LIV²: 322) immediately comes to mind. The word formation pattern is ambiguous, as *kVlū̆pp- could, at this stage of the reasoning, reflect a suffix *-bʰo- or a suffix *-po- (see Section 4) based on a nominal u-stem. Next, the temporary proto-form *lVi̯b- ‘libation’ is difficult to separate from the PIE root *lei̯H- ‘to pour’ (LIV²: 405), also with a labial suffix, this time reflected as a *-b-. Finally, the proto-form *turba ‘confusion’ is reminiscent of the PIE root *tu̯er- ‘to stir’ (LIV²: 655), once again with a labial suffix. Of course, no previously unidentified IE language should be reconstructed on the sole basis of these four correspondences. Yet they may serve as a starting point to posit a preliminary set of underspecified phonetic laws that would have applied during the evolution from PIE to our hypothetical substrate language, should our working hypotheses prove tractable. Obviously, only the consistent and systematic recurrence of the same set of laws in a much wider set of etymological proposals can significantly increase the probability of our hypothesis (see Section 5). If we analyse the four abovementioned sets of correspondences, we can draw a few preliminary conclusions: 1. our substrate language would be a centum language; 2. voiced aspirated consonants (at least PIE *bʰ) would be reflected as non-aspirated voiceless consonants, at least in certain contexts;

<!-- pdf-page: 8 | article-page: 35 -->

3. our substrate language would have syllabic sonorants (at least *r̥ ); 4. it would have fortis consonants of some kind, approximated above as *-pp-; 5. it could have undergone some sort of stress regression (cf. Gr. τύρβη).

Such hypotheses are much more reminiscent of Holzer’s Temematic and Szemérenyi’s Ausonian substrate theories than of Pelasgian hypotheses. Our preliminary conclusions have no value per se. However, they have allowed us to identify dozens of additional correspondences between Latin (or Proto-Romance) and/or Greek words on the one hand and PIE roots and well-known formation patterns on the other hand. The preliminary and underspecified inventory of phonetic developments suggested for describing the evolution from PIE to this substrate language will be refined and extended accordingly, resulting in a consistent set of partially chronologically ordered laws, all of which apply with no exceptions to all substrate proto-forms we reconstruct. Moreover, contrasting with one of the aforementioned issues with Pelasgian theories, most of our proto-forms are the result of the application of several of these laws. These characteristics of our work, together with the large number of suggested etymologies — not all of which could be included in this paper —, their semantic precision, and the exclusive use of well-known IE formation patterns, lead us to believe that the material presented in Section 5 constitutes a strong case in favour of the reconstruction of our new IE substrate language.

## 4 Excursus on the PIE nominal morph *-p-

Before discussing our etymological proposals and identifying the phonetic laws we postulate between PIE and our substrate language, we must strengthen the case for a poorly attested deverbal morph, the PIE labial morph *-p-. This is because our substrate language seems to use this morph more often than others. A *-p- nominal morph can be found in derivatives of at least seven roots: PIE root *ḱerh₂- ‘to shatter, smash’ (LIV²: 327): an athematic noun *ḱrṓp-s, *ḱrép-s < PIE *ḱór(h₂)-p-s, with application of the Saussure-effect and the metathesis studied by Griepentrog (1995: 198), has served as a base for creating a secondary root *ḱrep- ‘to rattle, crack’ (cf. Lat. crepāre ‘to crack (something)’).[^3]

<!-- pdf-page: 9 | article-page: 36 -->

PIE root *(s)gʷesh₂- ‘to become extinct’ (LIV²: 541): PIE *kʷsṓp-s, *kʷsép-s [f.] ‘night’ (Skt kṣáp- ‘id.’, YAv. xšap- ‘id.’, cf. also Hitt. išpant- [c.] ‘id.’) reflects an earlier PIE *gʷṓs-p-s < *gʷṓs(h₂)-p-s ‘extinction’. PIE root *(s)ḱel- ‘to be bent, curved; to bend, curve’:[^4] We reconstruct a PIE ḱl-óu̯-p-o- [m.] ‘limp’, hence a Lithuanian neo-root √klup- ‘to kneel (down)’ (cf. Lith. klùbas ∼Lith. šlùbas ‘limping’, klùmpti ‘to walk awkwardly, clumsily’, klumpus [deverbal adj.] ‘stumbling, limping’ (LEW: 275–276, s. v. klùpti)). PIE root *ḱel- ‘to cover, hide’ (LIV²: 322): We can start from a PIE *ḱól-p- [f.] ‘hiding place, theft’, hence PIE *ḱlṓp-s (gén. *ḱlép-s) [f.] ‘theft’. It was used as a second compound member based on the e-grade (cf. PIE *gʷou̯-ḱlép-s > Gr. βοῦκλεψ ‘stealer of oxen’), hence a secondary masculine agent name *ḱlṓp-s (gen. *ḱlép-s) ‘stealer’ reflected by Gr. κλώψ [m.] ‘thief’.[^5] From the same root, note Hitt. kalŭppa- ‘petticoat (vel sim.)’ (HED: H, 32–33). PIE root *(s)ker- ‘to cut’ (LIV²: 556): This root is the basis for an o-grade derivative PIE *(s)kór-u [n.] ‘sharp stone fragment, splinter’, whence a secondary derivative PIE *(s)kr-óu̯-p-o- > Lat. scrūpus [m.] ‘sharp stone’. PIE root *seu̯- ‘to sleep’: Next to the PIE root *su̯ep- ‘to sleep’ (LIV²: 612), Gr. εὕδω ‘id.’ points to a PIE etymon *séu̯-d-e/o- ‘to fall asleep’, a perfective derivative of a primary durative root *seu̯- ‘to sleep, rest, lie down’[^6] Skt sas- ‘to sleep’, and Av. hah- ‘id.’ (EDHIL: 746–747), whose unusual structure could result from the simplification of an earlier initial cluster PIE *su̯-, and which could derive from an s-stem *séu̯-s (oblique stem *su̯-és-) ‘bed (vel sim.)’ based on the same primary root *seu̯-. This root could be the basis for an athematic noun *su̯ṓp-s, *su̯ép-s < PIE *sṓu̯-p-s, *séu̯-p-s ‘sleep’, hence the secondary verbal root *su̯ep-. PIE root *u̯es- ‘to be dressed (with/in something)’ (LIV²: 692): this root underlies Hitt. u̯ašpa- ‘clothing (in a funerary context)’ and its probable cognate CLuw. u̯ašpant- ‘wearing shrouds (?)’. For these words, (EDHIL: 984–985) tentatively prefers an etymon PIE *u̯os-bʰo- However, Lat. uespillō ‘undertaker,

<!-- pdf-page: 10 | article-page: 37 -->

dresser of dead bodies’ is certainly a direct cognate, which seems to reinforce the reconstruction by Watkins (1969) of an etymon PIE *u̯os-po-.[^7]

## 5 Etymological proposals and phonetic laws

In this section, we shall gradually introduce a reduced set of phonetic laws which we believe to constitute a reasonable approximation of the phonetic changes from PIE to our substrate language. Each of the major treatments we postulate, which can be expressed either by a single law or by a set of two complementary laws, is dealt with in a separate section. With each section, new etymological proposals are introduced via our substrate language for several dozen Greek, Latin, and Proto-Romance words or word families. The sections have been ordered and the examples selected in such a way that, in almost all cases, all laws required to explain the etymology of a particular example have already been introduced. All etymologies proposed here strictly respect our set of phonetic laws, as checked by dedicated computer software. At the beginning of the next section, we sum up our proposal in the form of a table listing all phonetic laws we introduce in this section, in an order that is compatible with all examples discussed.[^8]

### 5.1 Voice alternations akin to Verner’s Law in Germanic

Introducing phonetic laws in a progressive way requires starting with substrate words whose evolution from their PIE etymon involves a single phonetic law. Such examples are difficult to come by, since most of our etymologies involve more than one of the phonetic laws we postulate, something which reflects the usual situation

<!-- pdf-page: 11 | article-page: 38 -->

in IE etymological discussions in general. Examples in this section will become more convincing once further examples are provided. We have decided to begin with a treatment which was not suggested in Section 3. The first reason is that it is a widespread phenomenon, which is, however, very specific to our substrate language, except for parallels in Germanic in the form of Verner’s Law. It will be applied to many other words described in the remainder of this paper. The second reason is that we were able to find three word families that illustrate this treatment and do not require any further law.

#### 5.1.1 Lat. lībāre ‘to pour out, spill; to libate’, Gr. λείβω ‘to let flow; to pour; to libate’ and related words

Lat. lībāre ‘to pour out, spill; to libate’ is sometimes analysed as a borrowing from Greek (LIV²: 405–406, s. v. *lei̯H-), which is not very probable given the semantic field involved. De Vaan (2008: 339), following Steinbauer, derives Lat. lībāre from the PIE root *h₂libʰ- ‘to anoint’ as a denominative of Com. It. *le/oifo- ‘sacrificial cake’ ( > Lat. lībum ‘id.’) and relates it to a Com. It. *lifu- ‘greasy’ (cf. Lat. dēlībāre ‘to remove, take a small piece from’, dēlibūtus ‘thickly smeared, imbued’). This is unlikely; the derivation of lībum from lībāre — perhaps via *lībātum (Garnier 2016: 3.2.19) — is usually admitted, rather than the other way round. Lat. dēlĭbūtus is likely to be unrelated.[^9]

Gr. λείβω ‘to let flow, shed; to pour, drip’ hence ‘to pour a libation’, whose formal and semantic similarity to Lat. lībāre is striking, is sometimes analysed as reflecting the same root as OCS liti (1sg. lьjǫ, lějǫ) ‘to pour’, Lith. líeti (1sg. líeju) ‘id.’, assuming that the Greek -β- is secondary, possibly after εἴβω ‘to drip’. The relevant PIE root is then *lei̯H- ‘to drip (intr.); to pour (tr.)’ (LIV²: 405). We too believe that it is legitimate to connect Gr. λείβω, Lat. lībāre, and the PIE root *lei̯H-. Note also the related Greek forms Gr. λιβάζω ‘λείβω’, Gr. λίβος [n.] (var. Gr. λιβάς) ‘anything that drops or trickles, drop’, Gr. λίψ ‘drop, libation’ and Gr. λοιβή ‘libation’. We start from a PIE action noun PIE *lói̯(H)-p-o- built on the same pattern as Hitt. u̯ašpa- ‘clothing (in a funerary context)’ < PIE *u̯ós-p-o(cf. Section 4).[^10] The meaning of this noun could have been specialised in our

<!-- pdf-page: 12 | article-page: 39 -->

substrate language to denote the action of pouring or dripping a liquid for religious purposes, for instance onto a sacrificial cake. It serves as the basis for a denominative stem *loi̯-p-eh₂-i̯é/ó- ‘to pour a libation’. We now introduce our first phonetic law, namely a lenition of intervocalic stops in pretonic position, akin to Verner’s law in Germanic. According to this lenition law, *loi̯-p-eh₂-i̯é/ó- is reflected as *loiβā́-.[^11] A secondary effect of this pretonic lenition and its counterpart, the posttonic fortition discussed below in Section 5.1.3, is a systematic barytonesis (or stress retraction).[^12] Applying this systematic barytonesis, we obtain Substr. *lóiβā-. This verb would have been borrowed on the one hand as Com. Gr. *loibáo (cf. the Hesychian gloss λοιβᾶται ‘libates’), hence a deverbal Gr. λοιβή ‘libation’ and a secondary productive thematic present Gr. λείβω, and on the other hand as Com. It. *loibāi̯e/o-, hence Lat. lībāre (Lat. lībum being, as usually assumed, a deverbal noun).

#### 5.1.2 Gr. ὕβρις ‘arrogance, haughtiness, etc.’

Gr. ὕβρις [f.] ‘arrogance, haughtiness, exorbitance, violence, offence, abuse’, attested from Homer on, is mentioned by Chantraine et al. (2009: 1110) as being without etymology and by Beekes (2010: 1524–1525) as having “no certain explanation”.[^13] Yet Chantraine indicates that “some Hellenists have probably thought of comparing this word with ὑπέρ, which would be semantically satisfactory but remains impossible.” We believe this comparison actually holds. We start from the PIE adverb *(h₁)upér-i ‘above’ (cf. Ved. upári ‘id.’ and Ger. über < Com. Germ. *uβeri ‘id.’). Applying the Verner-like lenition followed by the systematic barytonesis, such an

<!-- pdf-page: 13 | article-page: 40 -->

adverb would yield Substr. *úβeri. Once borrowed as Com. Gr. *húberi, this adverb could have served as the basis for the Hom. Gr. present participle ὑβρίζων, -οντος ‘who exhibits an overbearing spirit or demeanour’ after dactylisation, whence Classical Gr. ὑβρίζω ‘to outrage, insult, maltreat’. In turn, this participle could have yielded a derived noun ὑβριστής ‘arrogant person’. Gr. ὑβρίζων, -οντος would also have served as the basis for the back-formed noun ὕβρις.[^14]

#### 5.1.3 δρύπτω ‘to scratch’, Hom. Gr. ἀποδρύπτω and related words

Gr. δρύπτω ‘to scratch (especially in sign of mourning)’ is attested from Homer on, in particular in the form of the compound Hom. Gr. ἀποδρύπτω ‘to tear off the skin, lacerate’ (act. aor. ἀποδρύφοι Ψ 187, Ω 21 and ἀποδρύψωσι ρ 480, pass. aor. ἀπέδρυφθεν ε 435).[^15]

We believe that all these forms can be explained as reflecting the PIE root *der- ‘to tear’ (LIV²: 119). Let us start from the well-attested acrostatic noun PIE *dór-u- ‘chopped (piece of) wood, chip of wood’. A holokinetic derived noun PIE *dér-ou̯-/*dr-óu̯-/*dr̥-u̯-és ‘graze, scrape (vel sim.)’ could have served as the basis for a thematic action noun *dr-óu̯-p-o- [m.] ‘action of flaying’ and an associated collective *dr-u-p-éh₂ ‘grazes, scrapes’. An analogical levelling between these two forms could have resulted in a *dr-ú-p-o- ‘action of flaying (initially, wood)’, either within PIE or in the history of our substrate language. We then posit a fortition law in posttonic position, which will also be confirmed by numerous further examples below. This fortition law is the counterpart of the pretonic (Verner-like) lenition law posited in the previous section. With this law, *drúpo- would result in Substr. *drúPo-, the *P denoting a fortis consonant. As we shall see in several examples, this Substr. *P is often borrowed in Greek as pʰ, sometimes as p,[^16] and in Italic as *pp or *pᶠ.[^17]

<!-- pdf-page: 14 | article-page: 41 -->

In our case, Substr. *drúPo- ‘action of flaying (initially, wood)’ would have been borrowed in Com. Gr. as *drúpʰos [m.] ‘id.’, hence a Greek-internal denominal verb *drúpʰ-i̯o > Gr. δρύπτω (cf. τύφος vs. τύπτω rather than \*\*τυπέω). Note also Hesychian glosses that probably also reflect this borrowing process: δρυφόμενοι· φθειρόμενοι ‘destroyed’ and δρυφάδες· ὄνυχες ‘nails’.[^18]

### 5.2 *#(s)klV- > *#(s)kəlV-

#### 5.2.1 Gr. καλύβη ‘hut, cabin, tent’

The Verner-like lenition introduced in the previous section is also attested via non-inherited Gr. καλύβη [f.] ‘hut, cabin, tent’ (with variants καλυβός, κολυβός [m.]) and non-inherited Gr. κέλῡφος [secondary n.] ‘fruit shell, eggshell’, two words that are difficult to separate from the PIE root *ḱel- ‘to cover’ (LIV²: 322) (cf. Lat. oc-cŭl-ĕrĕ ‘hide’ < PIE *ḱél-e/o-). Gr. κέλῡφος could reflect a Substratic noun *kəlū́Po- ‘covering’ (probably /kə́lūppo-/ ∼ /kə́lūpfo-/, see below), the result of the posttonic fortition law on PIE *ḱl-óu-p-o- ‘id.’ with monophthongisation *ou > *ū and systematic barytonesis. Yet this Substratic reflex requires positing an additional law, namely the introduction of an anaptyctic schwa in word-initial clusters *#(s)kl, hence *#(s)kəl.[^19] In the case of Gr. κέλῡφος, this schwa is reflected as Gr. ε. The old PIE zero-grade collective *ḱl-u-p-éh₂ ‘set of huts (vel sim.)’ resulted in *kluβā̆́, with Verner-like lenition in posttonic position, which was reinterpreted as a singular word for ‘hut’. With the epenthetic schwa introduced in word-initial *klV- and the systematic barytonesis, the expected result is Substr. *kə́luβa. This

<!-- pdf-page: 15 | article-page: 42 -->

Substratic form is directly reflected as Com. Gr. *kalúbā > Gr. καλύβη ‘hut, cabin, tent’, with a Greek-internal stress shift due to the three-mora law.[^20][^21]

The apophonic system involving Substr. *kə́lūppo- ∼ *kə́lūpfo- and Substr. *kə́luβa was levelled in several different ways, most probably within the borrowing languages. Firstly, the feminine stem with the masculine ending resulted in the Greek masculine variants καλυβός and κόλυβος of the feminine Gr. καλύβη, as if from a Substratic \*\*kəluβo- (the stress is admittedly unexpected, but these forms are poorly and lately attested and the stress might not be reliable). Secondly, the masculine stem with the feminine ending provided the source for Proto-Romance *káluppa ∼ *káluffa ‘nutshell, (vel sim.)’ (REW: 381), as if from a Substratic \*\*kə́lūppa- ∼ \*\*kə́lūpfa- — which motivates the realisation *pp/*pf suggested above.[^22] This proto-form is reflected for example by Provencal caloufo ‘nut hull’ and Old Occit. calupa ‘*nutshell; boat’ (hence Fr. (dial.) chalo(u)ppe ‘nutshell; boat hull’). Thirdly, more speculatively, the masculine stem with the feminine ending, but this time with the lenited *β, could have provided the source for a Substratic form borrowed as Com. Sl. *kolyba ‘hut’, as if from a Substratic *kə́lūβa-.[^23]

Note that this series requires that our substrate language be a centum language, since PIE *ḱ is reflected as k.

#### 5.2.2 Gr. κολοβός ‘mutilated’, Gr. σκόλοψ ‘pointed pole’

Gr. κολοβός ‘mutilated’ is formally and semantically close to the PIE root *(s)kelh₂- ‘to chop (wood)’ (LIV²: 350 and 553, s. v. *kelH- and *skelh₂-). We assume a Substratic adjective inherited from PIE *kol(h₂)-p-ó- ‘chopped, mutilated (vel sim.)’ resulting in *klo-p-ó- after application of the Saussure effect (Nussbaum 1997) followed by

<!-- pdf-page: 16 | article-page: 43 -->

the anticipation of the *-l- described later on in Section 5.6. Our law *#(s)kl- > *#(s)kəl-, the Verner-like lenition and the systematic barytonesis yields *kə́loβos, borrowed as Gr. κολοβός.[^24]

It is our second example of a Greek word borrowed from our substrate language that does not have a barytone stress. As above, it is very likely the outcome of Greek-internal levelling, since most adjectives, especially those with a passive meaning as is the case here, have an oxytone stress.[^25]

Related to this set of words is Gr. κολούω ‘cut short, dock, curtail’, possibly a Greek denominal ye/o-present on a variant *κολοϝός of Gr. κολοβός. This β ∼ ϝ alternation, together with a case of a phonetic realisation as *-f- in Proto-Romance (see Section 5.5.3), lead us to suggest the reconstruction Substr. *β for the lenited counterpart of an earlier Substratic *p.[^26]

These words are also clearly related to Gr. κόλος ‘mutilated’, whose stress on the first syllable is unexpected in Greek. We analyse it as simply reflecting a Substratic adjective *kólo- < *kol-ó- < PIE *kol(h₂)-ó- with application of the systematic barytonesis. Numerous other related words are attested — see for example those listed in (Chantraine et al. 2009), among which Gr. κόλουρος ‘dock-tailed, stump-tailed’ or Gr. κολοβόω ‘κολούω’.[^27]

<!-- pdf-page: 17 | article-page: 44 -->

### 5.3 *Cu̯r̥C > *CurC

#### 5.3.1 Lat. corbis ‘basket’, Gr. κύρβεις and related words

We believe that the PIE root *ku̯erp- ‘to turn towards something/somebody, spin, twist’ (LIVAdd: 50)[^28] could explain, via our subtratic language, several yet unexplained forms in both Greek and Latin. Let us begin with Gr. κύρβεις [m. f. pl.], whose remarkably specific meaning is ‘at Athens, triangular tablets forming a three-sided pyramid and turning on a pivot, upon which the early laws of Solon were inscribed’. We start from an etymon *ku̯r̥p-í- [m.] ‘pivoting, twisting object’ forming a system with an adjective *ku̯r̥p-ó- ‘spinning, pivoting’, which is reflected by inherited Gr. καρπός ‘wrist’. We then posit a resyllabification rule of the form *Cu̯r̥C > *CurC, which has parallels in Anatolian, Tocharian, and Albanian. From the same root, see for example To. B kurp- ‘to be busy with’ < PIE *ku̯r̥p- (Adams 2013: 196) or Alb. (Gheg) kurpën [m.] < *ku̯r̥p-Vnā ‘tendril, clematis’, borrowed as Rom. curpen ‘clematis’ (LIVAdd: 50). Together with the Verner-like lenition and the systematic barytonesis, we thus obtain Substr. *kúrβi- ‘pivoting, twisting object’, borrowed as *kúrbis, from which Gr. κύρβεις is then a direct derivative.[^29]

The same Substr. *kúrβi- could also be the basis for a reduplicated derived form attested in Lat. cucurbita ‘gourd (which grows on plants characterised by their tendrils)’ (cf. the Gheg word mentioned above).[^30] With a similar semantic specialisation, this time applied to wicker, an o-grade Substr. *kórβi-, resulting from the delabialisation of a previous *kʷórβi < *ku̯orβí and borrowed as Com. It. *kórβi- ‘id.’, could be the origin for Lat. corbis, -is [m., f.] ‘basket’. The same semantic specialisation is also found in reflexes of various forms based on the primary root root *ku̯er- that is the basis for the (secondary root) *ku̯erp-. A zero-grade adjective *kur-tó- is attested in inherited Gr. κυρτός ‘vaulted’,[^31] with several secondary formations (κύρτος [m., n.] ‘bird-cage’, κύρτη ‘sieve, cage’, and κυρτία ‘wickerwork’), and probably, as a secondary derivative, in Hitt. kurtal(l)i- ‘basket (of wicker)’.

<!-- pdf-page: 18 | article-page: 45 -->

Finally, a zero-grade abstract noun *kur-tí- could be reflected by Com. Germ. *χurđíz > OHG hurd ‘trellis’.

#### 5.3.2 Gr. τύρβη ‘confusion, tumult’, Lat. turba ‘id.’

An interesting Greek-Latin doublet that has no commonly accepted etymology is Gr. τύρβη ‘confusion, tumult’ and Lat. turba ‘id.’ Although it has been suggested that the Latin word is a loanword from Greek, this is far from certain and does not, in any case, shed light on the etymology of the Greek word. It would require a borrowing from a non-Attic-Ionic dialect, most probably Doric, from which the expected outcome, however, would have probably led to a borrowed word \*\*tiurba. We analyse Gr. τύρβη and Lat. turba as deriving from more concrete words built on the PIE root *tu̯er- (LIV²: 655) ‘to stir’. We start from a PIE feminine action noun *tu̯r̥-p-éh₂ ‘stirring (vel sim.)’. After application of the Verner-like lenition, the law *Cu̯r̥C > *CurC and of the systematic barytonesis, this results in Substr. *túrβa, which had probably already acquired its abstract meaning ‘trouble (vel sim.)’. It is directly reflected as Classical Gr. τύρβη and probably Lat. turba.[^32]

### 5.4 Anticipation of nasals: *VPNV > *VNBV

#### 5.4.1 Gr. κράμβος ‘dried up’

Gr. κράμβος ‘dried up’ is most likely related to Gr. κραῦρος ‘id.’, as suggested by Furnée (1972: 238). Both words are sometimes connected with Germanic and Baltic forms such as ON skorpinn ‘shrivelled up’ < *skurppana-, a regrammaticalisation of Com. Germ. *skurppa- < PIE *skr̥bʰ-nó- based on the PIE root *(s)kerbʰ- ‘to shrivel’ (Pokorny 1959: 948–949).[^33]

We believe this connection to be valid. We start from a variant of the same etymon without the s-mobile, namely PIE *kr̥bʰ-nó- ‘shrivelled up, dried up (vel sim.)’. We then posit a treatment of sequences *VCNV akin to the lex unda in Latin (Meiser 1998: 121), namely a lenition of a stop followed by a nasal and a (probably subsequent) anticipation of the nasal.

<!-- pdf-page: 19 | article-page: 46 -->

The lex unda in Latin only applies to dental stops. As illustrated here (for the labial stop) and in other forms discussed in the remainder of this paper, this treatment applies in our substrate language to any stop. Starting from PIE *kr̥bʰ-nó-, this law yields Substr. *kŕ̥mβο- after application of the systematic barytonesis. This Substr. *kŕ̥mβο- was then borrowed in Com. Gr. as *kŕ̥mbos, whence Gr. κράμβος.[^34]

Gr. κραῦρος reflects another treatment of Substratic *β in intervocalic position; we analyse it as reflecting a Com. Gr. *kŕ̥u̯ros ‘dried up’ borrowed from a Substratic *kŕ̥βro- < PIE *kr̥bʰ-ró- ‘id.’. It is therefore another example of the two possible treatments of Substr. *β during the borrowing process in Com. Gr., namely Com. Gr. *b and, sometimes, Com. Gr. *u̯.[^35]

Inherited counterparts based on the same root are found in Hom. Gr. κάρφω ‘to dry up’ < PIE *kr̥bʰ-é/ó- ‘id.’ and the secondary noun Gr. κάρφος [n.] ‘any small dry body, esp. dry stalk’ (Hdt.+).

#### 5.4.2 Gr. κρέμβαλα ‘clappers, castanets’

Another example of this law of nasal anticipation (with lenition) is Gr. κρέμβαλα [n. pl.] ‘clappers, castanets’. We analyse it as a diminutive built on a Substr. *krémbo- reflecting PIE *ḱrép-no-, itself derived from a PIE verb *ḱrép- ‘to rattle, crack’ (cf. Lat. crepāre ‘to crack [something]’ and Lat. crepitāculum ‘rattle’, semantically identical to Gr. κρέμβαλα; cf. also Section 4). The underlying PIE root is *ḱerh₂-, reflected for example in inherited Gr. κέραυνος [m.] ‘lightning’.[^36] The PIE verb *ḱrép- is the result of the following developments. First, a derived noun *ḱrṓp-s was created by metathesis of a -p- ‘extension’ of the root’s o-grade, with application of the metathesis described by Griepentrog (1995: 198). Then a metanalysis of this noun resulted in the neo-root *ḱrep-, whence a verb *ḱrép-. From this verb, a ‘primary’ derivation led to PIE *ḱrép-no-, whence Substr. *krémβo- via the law *VPNV > *VNBV discussed in this section. Secondarily,

<!-- pdf-page: 20 | article-page: 47 -->

a (probably Greek-internal) *-l- diminutive was formed, hence Gr. κρέμβαλα [n. pl.] ‘clapper, castanets’.[^37]

Note that this hypothesis confirms that we are dealing with a centum language, as here as well PIE *ḱ is reflected as k.

### 5.5 Dʰ > T, at least word-initially

#### 5.5.1 Lat. porrum, Gr. πράσον

The correspondence between Lat. porrum ‘leek’ and Gr. πράσον ‘id.’ already mentioned in Section 3 is not new. Beekes (2010: 1229) quotes the usual reconstruction *pr̥s-o-. For him, the preservation of the -σ- between a resonant and a vowel is an indication that πράσον could be Pre-Greek, which is probably not a valid argument (on which see below). More importantly, no semantically adequate PIE root can formally account for an inherited etymon PIE *pr̥s-o-. We analyse these words as derived from the PIE root *bʰers- ‘to point, burst, bud’ (Pokorny 1959: 109).[^38] This root is attested at the o-grade, for instance by the noun PIE *bʰórs-o- > PGmc *bársaz > Ger. Barsch ‘perch’ and the adjective PIE *bʰors-ó- > PGmc *barzáz ‘breaking through, piercing, pointing (vel sim.)’, hence PGmc *barzǣ́janan > OHG parrên ‘to stand upright’. A zero-grade noun can be found in PIE *bʰr̥s-tí- > PGmc *burs-tiz (cf. Ger. Bürste ‘brush’), reinterpreted as PGmc *burst-iz, hence a neo-strong verb PGmc *burstanan seen in OE brust > Eng. burst and in Ger. bersten ‘id.’[^39] The zero-grade *bʰr̥s- is attested in Skt bhr̥ṣṭi- ‘point, summit’ and in Com. Celt. *barsos > OIr. barr ‘point, top’. Given the meanings of these forms, the original meaning of the PIE root *bʰers- is ‘to break into pieces’ and specialised in several daughter languages as ‘to break through the ground upwards (especially speaking of a plant)’. Our interpretation of Lat. porrum ‘leek’ and Gr. πράσον ‘id.’ is then as follows. We start from a zero-grade adjective PIE *bʰr̥s-ó- ‘bursting’ nominalised with the

<!-- pdf-page: 21 | article-page: 48 -->

meaning ‘leek’ either in PIE or in our substrate language, where we reconstruct it as Substr. *pŕ̥so-, with application of the systematic barytonesis and the effect of a new law PIE *#Dʰ > Substr. *#T, which applies here to PIE *bʰ.[^40] Substr. *pŕ̥so-, once borrowed as such in both Com. Gr. and in Com. It., regularly resulted in Lat. porrum and Gr. πράσον.[^41]

#### 5.5.2 Gr. πύνδᾰξ ‘bottom of a jar’

We analyse Gr. πύνδᾰξ [m.] ‘bottom of a jar’ as reflecting Substr. *púndo- ‘bottom’ < *pundó- < PIE *bʰudʰ-nó- ‘id.’, thus illustrating once again the rule PIE *#bʰ > Substr. *#p, together with the lex-unda-like nasal anticipation law and the systematic barytonesis. Note that in Latin, the exact same etymon PIE *bʰudʰ-nó- is attested as (inherited) fundus ‘bottom’, after application of the lex unda.

#### 5.5.3 Lat. Tĭbĕris ‘the river Tiber’, Lat. tŭbus ‘tube’

Similar to the suggestion by Szemerényi (1991: 675–681), but without resorting to a dubious PIE *b, we believe that Lat. Tĭbĕris, -is [m.] ‘the river Tiber’ < Com. It. *tŭbris reflects Substr. *túβri- < PIE *dʰubʰ-rí- ‘ravine’, which we identify with our substrate language, as it exhibits a treatment PIE *#dʰ > *#t, which is another instance of the more general law PIE *#Dʰ > Substr. *#T. It is built on a PIE root *dʰeu̯bʰ- ‘to sink, go deep’ (LIVAdd: 24).[^42] Words with similar meanings and based on the same root are attested, such as Lith. daubà ‘ravine, hole, burrow’ < PIE *dʰoubʰ-éh₂ and To. B taupe ‘mine’ < PIE *dʰóu̯bʰ-o-.[^43]

<!-- pdf-page: 22 | article-page: 49 -->

Starting from the same root, we posit a PIE adjective *dʰubʰ-ó- reflected as Substr. *túβo-, borrowed as Com. It. *túβo- > Lat. tŭbus and Sabellic and Proto-Romance *tŭfus ‘underground pipe (for conducting water)’[^44] attested for example in Logudorian tuva ‘hole in the mill stone’ (REW: 746).[^45]

#### 5.5.4 Gr. τύμβος ‘tomb’

We analyse Gr. τύμβος ‘tomb’ as a borrowing from a Substratic *túmβo-, the nominalisation of an earlier PIE adjective *dʰubʰ-nó- ‘deep’ > Substr. *túmβo- ‘id.’ based on the PIE root *dʰeu̯bʰ- ‘to sink, go deep’ already mentioned in Section 5.5.3. A cognate of Substr. *túmβo- could be Gaul. *dubno- ‘underworld’[^46] attested in compounds such as the personal name Dubno-rix ‘king of the underworld’ (DLG²: 150). There also exists a dialectal variant τῡμος of Gr. τύμβος.[^47] We interpret it as a reflex of Com. Gr. *túmu̯os, another rendering of Substr. *túmβo- together with Com. Gr. *túmbos.[^48]

### 5.6 Metathesis of liquids: *CVRC > *CRVC

#### 5.6.1 Gr. στρέφω ‘to twist’, Gr. στρεβλός ‘turned, twisted’, Gr. στρόμβος ‘spinning-top, whirlwind’

The Greek verb στρέφω ‘to twist’, which according to Beekes (2010: 1413) is Pre-Greek, is formally and semantically close to the PIE root *terkʷ- ‘turn oneself’ (LIV²: 635).[^49] This root is reflected by inherited Lat. torqueō ‘to turn, twist’ < PIE *torkʷ-éi̯-e/o-.

<!-- pdf-page: 23 | article-page: 50 -->

However, relating στρέφω to *terkʷ- requires: (i) a spurious s- which can be analysed as an s-mobile; (ii) a metathesis of the *r of the form *CVrC > *CrVC. We therefore posit a Post-PIE form *sterkʷ-e/o- > Substr. *stréKʷ-e/o- borrowed as Com. Gr. *strékʷʰō > Gr. στρέφω, with the Verner-like post-stress fortition PIE *-kʷ- > Substr. *Kʷ reflected by Com. Gr. *-kʷʰ- > Gr. -pʰ-. On the other hand, Gr. στρόμβος ‘spinning-top (Ξ 413); whirlwind’ reflects Substr. *stróngʷo- < *strókʷ-no- and illustrates once more the nasal anticipation rule.[^50] A lenited counterpart is actually attested, namely Gr. στρεβλός ‘turned, twisted’ < Com. Gr. *stregʷ-lό-, a borrowing from Substr. *strégʷ-lo- < PIE *(s)trekʷ-ló-. The labiovelar underlying this word family is ascertained by Gr. στρογγύλος ‘round, spherical, compact’, a Com. Gr. diminutive of an adjective *strongʷ-ú-, with the expected delabialisation of *gʷ before *u. This adjective can have been created either in the substrate language or in Com. Gr. based on the noun Substr. *stróngʷo- introduced above or its Com. Gr. counterpart *stróngʷo-.

### 5.7 Substr. *#trV- is reflected as Gr. #θρV-

We suspect several Greek words with the anlaut #θρ- to be borrowings from our substrate language and to reflect an earlier *#tr-:

1. Gr. θρῖψ ‘woodworm’, from Substr. *Trī́ps < PIE *trih₁-p- < *trh₁-i-p- (PIE root *terh₁- ‘to drill’);
2. Substr. *Trisno- < PIE *tri-s-nó- ‘ternary (vel sim.)’, attested in Gr. θρῖναξ ‘three-pronged fork, trident’, together with other words in Gr. θρι- with semantics related to the number three, the most convincing one being Gr. θρῖον ‘fig leaf’ (which has three lobes);
3. Gr. θρύον ‘reed, rush’, for which the connection with OCS trъstъ [f.] ‘reed, cane’ and Lith. tr(i)ušìs ‘id.’ < Com. BSl. *trus- (Derksen 2008: 499) is rejected by Beekes (2010) because of the anlaut, but is perfectly consistent with our substrate analysis, via a Substr. *Trúso- < *trus-ó-.

Conversely, we have found no examples of Greek words that have an anlaut Gr. τρ- and are likely candidates for having been borrowed from our substrate language.

<!-- pdf-page: 24 | article-page: 51 -->

This does not constitute a definitive argument, but it seems that a systematic correspondence between PIE *tr- and Gr. θρ- via Substr. *Tr- is a reasonable hypothesis.[^51]

### 5.8 PIE *bʰR > Substr. *bR and PIE #pr- > Substr. #br-

#### 5.8.1 Gr. βροῦκος ‘edible locust’

The Greek group βροῦκος/*βρεῦκος/βρύκος [m.] ‘edible locust’ has been examined by Furnée (1972: 128–129). The Hesychian gloss βροῦκος· ἀττέλεβος indicates a ‘locust larva’ (LXX: Na. 3, 17). It has a late doublet βροῦχος [m.] ‘locust, larva of a non-winged locust’. We suggest a Substratic apophonic series Substr. *brówko-/*bréwko-/*brúko- ‘jumping animal’, which would stem from the (secondary) PIE root *(s)preu̯g- ‘to jump’ (Pokorny 1959: 995),[^52] where the fortition of PIE *g is expected because of the Verner-like treatment (cf. Section 5.1). There exist interesting Slavic, Tocharian, and Germanic reflexes that also lack the s mobile. For Slavic we can cite Com. Sl. *pryg- ‘to jump’ ( < Com. BSl. *prū́g-), attested by Ru. прыгать ‘to jump’ (post-verbal прыг ‘jump’) and Com. Sl. *prǫg- ‘jump’ ( < Com. BSl. *prū́ng-) (LEW: 883). For Tocharian, see To. B pruk- glossed by Adams (2013: 449) as ‘to make a leap, get away from, overlook, neglect’ (presumably a secondary zero-grade). Related Germanic forms include for example ON froskr ‘frog’, OHG frosc ‘id.’, OE frosċ ‘id.’, all from Com. Germ. *fruska- < PIE *prug-sḱó- and ON fraukr ‘id.’ < Com. Germ. *frauka- < PIE *prou̯g-ó-. However, deriving βροῦκος/*βρεῦκος/βρύκος from PIE *preu̯g-ó-, the same etymon we just posited for ON froskr, assumes a Substratic treatment *#pr- > *#br-. Since PIE *bʰ > Substr. *p as seen in Section 5.5.1, the law *#pr- > *#br-, if it is

<!-- pdf-page: 25 | article-page: 52 -->

posterior to the law *bʰ > *p, must result in PIE *#bʰr > Substr. *#br. This is exactly what we observe, as illustrated in the remainder of this section.[^53][^54]

#### 5.8.2 Gr. βρέτας ‘wooden idol’

The meaning of Gr. βρέτας, -εος [n.] is ‘wooden idol, wooden image of a god’.[^55]

We analyse it as the reflex of a Com. Gr. *brétar borrowed from Substr. *brétar < *prétar < *pértar < PIE *bʰér-dʰ-r̥,[^56] based on a secondary denominal PIE root *bʰerdʰ- resulting from the reanalysis of PIE *bʰordʰ-ó- < PIE *bʰor(H).dʰh₁-ó- ‘bored, carved’, with application of the Saussure effect.[^57] The underlying primary root is PIE *bʰerH- ‘to bore, work (wood) with a sharp tool’ (LIV²: 80), attested for example in Eng. bore < Com. Germ. *burōjan-an ‘id.’ (cf. also Ger. bohren ‘id.’), Lat. forō ‘id.’ and, interestingly, Eng. burin borrowed from Fr. burin ‘chisel, burin’ borrowed from It. burino ‘id.’, itself from Langobardic *boro ‘(drill) bit’.

#### 5.8.3 Gr. βρέμω ‘to roar, grumble’

Another example of a PIE *#bʰr- reflected in Greek by #βρ- after borrowing from Substr. *#br- is Gr. βρέμω ‘to roar, grumble’. Indeed, as mentioned by Beekes (2010: 237, s. v.), this word “resembles Lat. fremō ‘to rumble, roar’, OHG breman ‘buzz’, and MW brefu ‘roar’.” But Beekes’s conclusion reflects his rejection of any PIE substrate in Greek: “these cannot be connected, since they derive from *bʰrem-, whereas Greek has β-. Therefore, it is rather an onomatopoeic word.” Our substrate language provides a direct way to connect all these words in a regular way, by reconstructing a Substr. *brém-e/o-, which is the expected outcome

<!-- pdf-page: 26 | article-page: 53 -->

of the PIE present *bʰrém-e/o- reflected for example in Lat. fremō and Welsh bref- ‘to low, bleat, bray’.

#### 5.8.4 Gr. βλέπω ‘to look’ and Gr. βλέφαρον ‘eyelid’

Gr. βλέπω (+acc.) ‘to look’ is probably a late pseudo-verb created on the basis of Gr. βλέπων, βλέποντος ‘looking’, interpreted as a participle. This pseudo-participle is likely to have resulted from an older nasal theme Gr. *βλέπων, -ονος.[^58] It would have derived from Com. Gr. *bléku̯on reflecting Substr. *bléKwon- < PIE *bʰléǵ-u̯-on- with application of the posttonic fortition introduced above. The underlying root is PIE *bʰleǵ- ‘sparkle, shine’ (LIV²: 86), attested for example in Lat. fulgeō ‘glitter’, in inherited Gr. φλέγω ‘to burn, light’ and, interestingly from a semantic point of view, To. B palyka/To. A pälkāt [pret.] ‘saw’ (Hackstein 1995: 112–113¹⁵). Note also βλέφαρον [n.] ‘eyelid’, a singulative from plural βλέφαρα, itself probably from an older athematic singular *βλέφαρ < Com. Gr. *blékʰu̯ar from Substr. *bléKwr̥ < PIE *bʰléǵ-u̯-r̥ ‘wink’.[^59]

These etymologies suggest that the treatment PIE *#bʰr- > Substr. *#br- also applies to liquids (PIE *#bʰl- > Substr. *#bl-). Therefore, we postulate a more general law of the form PIE *#bʰR- > Substr. *#bR- (*R = *r or *l).

### 5.9 PIE *CHC > Substr. *CăC

#### 5.9.1 Gr. μέλαθρον ‘vault of a roof, roof (beam)’ and Gr. κμέλεθρον ‘(vault of a) roof’

Hom. Gr. μέλαθρον [n.] ‘vault of a roof, roof-beam, roof’ (plural: ‘dwelling, house’) cannot be directly compared to the adjective βλωθρός ‘high’ ( < Com. Gr. μλωθρός), which shows the expected outcome of a PIE etymon *ml̥h₃-dʰ-r-ó-, with the expected outcome -λω- of the long sonorant inherited from PIE *-l̥h₃- (Beekes 2010: 923, s. v. μέλαθρον). We do however believe that both words belong to the PIE root *melh₃- ‘to emerge from, come out from’ (LIV²: 433–434). We rely on a PIE etymon

<!-- pdf-page: 27 | article-page: 54 -->

*mélh₃-tr̥ [n.] ‘beam holding the roof (vel sim.)’ reflected as Substr. *mélaTr̥, with vocalisation of PIE *h₃ as Substr. *ă (Com. Gr. *mélatʰar). Note also the by-form κμέλεθρον with a spurious κ- and progressive assimilation of vowels *e—a > ε—ε.[^60] This prothetic velar stop could be the reflex of a Substratic morpheme *ki ( < PIE *ḱi), cognate of Hitt. ki ‘that’, Luw. zi ‘id.’. Therefore, a Substratic *ki=mélatar ‘that roof, the roof’, syncopated as *k(i)=mélatar, could have been borrowed as Com. Gr. *kmélatʰar [n.] ‘roof’, hence dialectal κμέλεθρον.

#### 5.9.2 Gr. πλέθρον vs. Hom. Gr. πέλεθρον ‘measure of length of 100 feet’

On the same pattern, the odd doublet Attic πλέθρον vs. Homeric πέλεθρον [n.] ‘measure of length of 100 feet’ could be accounted for as the reflex of an inherited Substratic paradigm combining Substr. *pela-Tr̥ [n. sg.] ‘flatness, length’ (borrowed as Com. Gr. *péla-tʰar) vs. Substr. *plé-Trā̆ [n. pl.] ‘measures of length’ (borrowed as Com. Gr. *plé-tʰra). This points to a PIE etymon based on the widely attested PIE root *pelh₂- ‘(to be) flat, wide’, namely a noun *pélh₂-tr̥ [n.] ‘flatness, length’, endowed with a plural stem *pél.tr-eh₂ > *pél(h₂).tr-eh₂, with the PIE-internal rule *CH.CC > *C.CC (Hackstein 2002). From Com. Gr. *péla-tʰar/Com. Gr. *plé-tʰra, a separate intraparadigmatic analogical levelling can explain Hom. Gr. πέλε-θρον [sg.], πέλε-θρα [pl.] as well as Attic πλέ-θρον [sg.], πλέ-θρα [pl.]. To sum up, we may assume a law PIE *CeRH.C > Substr. *CeRă.C with regular vocalisation of PIE *H as Substr. *ă (see Sections 5.9.4 and 5.9.1). On the other hand, PIE *CeR.C ( < PIE *CeR(H).C) yields Substr. *CRe.C (via *CeR.C). This would provide a clue as to the origin of the classical PIE pattern of thematic instrument nouns *CéC-tro-m (plural *CéC-tr-eh₂) as the outcome of an earlier pattern *CéC-tr̥ (plural *CéC-tr-eh₂) with stress on the root.

#### 5.9.3 Gr. (σ)πέλεθος ‘dung’

Beekes (2010: p. 1380, s. v.) suggests two different possibilities for Gr. σπέλεθος [m.] ‘dung’. The first one is a connection with the same PIE root *(s)pelH- ‘to split’ (LIV²: 576–577). Under this hypothesis, the -ε- indicates that the laryngeal was h₁. The second possibility, according to Beekes, is that the word is Pre-Greek (which, for Beekes, means non-Indo-European). He reconstructs a Pre-Greek *(s)paly- in

<!-- pdf-page: 28 | article-page: 55 -->

view of variants with -λλ- and variants in π- instead of σπ- (Furnée 1972: 390). We believe that the word is indeed not inherited, but that the connection with the PIE root *(s)pelH- holds. We start from a PIE neutral substantive *(s)pélH-tr̥ ‘splitting, defecation’, with the same well-known word-formation pattern as suggested above for Gr. μέλαθρον.[^61] This would have yielded Substr. *spélaTr̥ ‘dung’ borrowed as Com. Gr. *spélatʰar ‘id.’. The regressive vowel assimilation *e—a > e—e already mentioned in the previous section would have resulted in *spéletʰar.[^62] The attested masculine Gr. σπελεθος could then result from the influence of Gr. (σ)πύραθοι [m. pl.] ‘droppings of goats and sheep’ (obscure) and Hom. Gr. ὄνθος [m.] ‘dung, excrement of animals’ (Ψ 775, 777), from PIE *son-dʰh₁-ó- ‘set apart’.

#### 5.9.4 Gr. βάραθρον ‘cleft, abyss’

Gr. βάραθρον [n.] ‘cleft, abyss’ is an obscure form which is related to Hom. Gr. βέρεθρον, Arc. ζέρεθρον and the Hesychian gloss βέθρον [Euphorio]· βάθος, δεσμωτήριον ‘pit, prison’. According to Beekes (2010: 200, s. v. βάραθρον), in view of these variants, the word is Pre-Greek and the connection with βιβρώσκω ‘devour’ cannot be maintained. Indeed, PIE *gʷerh₃-/*gʷr̥h₃- ‘devour’ (cf. Lat. uorāre ‘id.’) would yield Gr. \*\*δερο-/βρω- (< Com. Gr. *gʷero-/*gʷro-). The odd variant βέθρον is explained as a shortened variant of βέρεθρον by Szemerényi (1964: 261), who assumes that a former *brétʰron underwent a dissimilation, *brétʰron itself being syncopated from βέρεθρον, following the same pattern as Gr. πλέθρον vs. Hom. Gr. πέλεθρον [n.] (cf. Section 5.9.2). The problem with this series is that the long sonorant should have yielded Gr. βρω- instead of Gr. βάρα- as found in βάρα-θρον < Com. Gr. *gʷéra-tʰron (cf. Semerényi 1964: 215⁵ and Kuryłowicz 1956: 208⁵⁶), with a regressive vowel assimilation *e—a > a—a that is also attested in Greek, next to the progressive assimilation *e—a > e—e previously mentioned.[^63] Another problem is that the laryngeal *h₃ is reflected as Gr. ă, which can no longer be accepted as a valid Greek treatment. Yet such a treatment, with a-vocalisation of laryngeals, is attested in many Indo-European languages, including our substrate language as discussed above for Gr. μέλαθρον. We assume a PIE etymon *gʷérh₃-tr̥ [n.] ‘swallowing’, with a secondary plural *gʷér(h₃).tr-eh₂ ‘clefts, abysses’ endowed with a concrete meaning, and exemplifying the PIE-internal rule *CH.CC > *C.CC (Hackstein 2002). The substrate language

<!-- pdf-page: 29 | article-page: 56 -->

would have inherited a stem such as *gʷéra-Tr̥ [n.] ‘abyss, pit’ with a plural of the form *gʷré-Trā̆ ( < *gʷér-Trā̆ ), with the expected metathesis of liquids. These forms were borrowed as Com. Gr. *gʷéra-tʰar and *gʷré-tʰra and later thematised as *gʷéra-tʰron, the form mentioned above. On the one hand, an assimilated variant *gʷéretʰron would have yielded dialectal *δέρε-θρον (> spirantised Arc. ζέρε-θρον) and ‘Aeolic’ βέρε-θρον. On the other hand Attic βάρα-θρον reflects an early assimilation *gʷéra-tʰron > *gʷára-tʰron, which predates the alternation of labiovelar stops before front vowels. The by-form βέθρον ‘pit, prison’ would be the reflex of an inherited plural stem *b(r)é-tʰra < Com. Gr. *gʷré-tʰra.

## 6 Conclusion

We believe we have identified a new IE centum language that has served as a substrate for both Greek and Latin. Borrowings seem to date back to Common Greek on the one hand and to the (much later) Common Italic stage on the other hand. This substrate language is very different from the hypothetical IE satem substrate language investigated by several defenders of the “Pelasgian” theories.[^64] Our substrate language has more in common with Szemerényi’s (1991) “Ausonian” and Holzer’s (1989) “Temematic” substrate layers in Italic and (Balto-)Slavic, respectively (see Section 2.3). One of the chronological orderings of the above-discussed laws that is compatible with the data we have discussed — as well as a few dozen more candidate loan words or word families not discussed in this paper — is given in Table 1 (p. 57). This sequence of laws allows us to suggest etymologies for approximately 100 non-inherited Greek words and 20 non-inherited Latin or Proto-Romance words — not all of them discussed in this paper —, which we all analyse as borrowings from our substrate language. These etymologies are semantically convincing and rely on standard IE word formation patterns. This sequence of laws suggests that our substrate language could share with Germanic and Tocharian some characteristics of what is sometimes called Northwest Indo-European. An interesting similarity between our substrate language and Germanic is the post-stress lenition (Verner’s Law in Germanic), although our language seems also to undergo a pre-stress fortition that is not paralleled in Germanic. Our substrate language also seems to have

<!-- pdf-page: 30 | article-page: 57 -->

several treatments in common with Hittite ((#)Dʰ > (#)T, Cu̯r̥C > CurC) and even more so with Tocharian, besides the fact that all these languages are centum.

**Table 1. Suggested chronologically ordered sequence of phonetic laws that models the evolution from PIE to our substrate language.**

| Step | Phonetic law |
|---:|---|
| 1 | Centum treatment: Ḱ > K |
| 2 | Laryngeal treatment: CHC > CăC |
| 3 | bʰR > bR (before step 4 because of βλέπω vs. πλέθρον) |
| 4 | Treatment of voiced aspirated consonants: (#)Dʰ > (#)T |
| 5 | Metathesis of non-syllabic liquids: CVRC > CRVC (before step 10 because of Lat. corbis; before step 11 because of Gr. βρέτας) |
| 6 | Schwa epenthesis of the form #(s)klV- > #(s)kəlV- |
| 7 | Verner-like lenition and fortition rules: P > Pː/V́(R)(s)_ and P > B/_(R)(s)V́, where P denotes any stop, Pː resp. B its fortis resp. lenis counterpart |
| 8 | Systematic barytonesis |
| 9 | Nasal anticipation: VPNV > VNBV |
| 10 | Resyllabification: Cu̯r̥C > CurC |
| 11 | Word-initial treatments: #pr > #br and #tr > #Tr |
| 12 | Monophthongisation ow > ū |

We would like to conclude with an admittedly speculative hypothesis. A PIE noun *gʰórdʰ-o- ‘fence, enclosure’, which later acquired the meaning ‘town’ in several IE daughter languages, is reconstructed on the basis of words such as OCS gradъ ‘town’ and the Phrygian city name Γόρδιον. An etymon PIE *gʰórdʰ-o-on-, with the well-known PIE characterising suffix -on-, would necessarily mean something like ‘that which is enclosed, city’, a good candidate for a city name. By applying to this hypothetical etymon the sequence of phonetic laws summarised in Table 1, we obtain the following derivation (step numbers refer to those in Table 1): PIE *gʰórdʰōn- > *kórtōn- (step 4) > *krótōn- (step 5) > *króTōn- (step 7). This matches the town name Κρότων ‘Crotone’ located in Calabria, Southern Italy. The following scenario can therefore be suggested. First, ancestors of Greek (i.e. speakers of Common Greek, 3rd millennium BC) could have been in contact with speakers of our substrate language, most probably before entering Greece. Later on, (some of) the speakers of our substrate language could have reached Southern Italy, founding cities such as Crotone, and (later?) have been there in contact with speakers of Italic languages as they spread over the Italian peninsula (end of the 2nd millennium BC). This would account for the borrowings in both (Common) Greek and (Late Common) Italic as well as for our suggestion regarding the etymology of the city name Κρότων. Based on this formal, semantic, and geographic match, and despite

<!-- pdf-page: 31 | article-page: 58 -->

the lack of definitive evidence, we suggest the name “Crotonian” for our newly identified language.

## Abbreviations

**DLG²** Xavier Delamarre (2003). *Dictionnaire de la langue gauloise. Une approche linguistique du vieux-celtique continental*. 2nd ed. Paris: Errance.

**EDHIL** Alwin Kloekhorst (2008). *Etymological Dictionary of the Hittite Inherited Lexicon*. Leiden & Boston: Brill.

**ESSJ** Oleg N. Trubačev et al., ed. (1974ff.). *Ėtimologičeskij slovar’ slavjanskich jazykov*. Moskva: Nauka.

**GEW** Hjalmar Frisk (1960–1972). *Griechisches etymologisches Wörterbuch*. 3 vols. Heidelberg: Winter.

**HED** Jaan Puhvel (1984–). *Hittite Etymological Dictionary*. 9 vols. Berlin & New York: Mouton.

**LEW** Ernst Fraenkel (1962–1965). *Litauisches etymologisches Wörterbuch*. 2 vols. Göttingen & Heidelberg: Vandenhoeck & Ruprecht, Winter.

**LIV²** Helmut Rix (2001). *Lexikon der indogermanischen Verben. Die Wurzeln und ihre Primärstammbildungen*. Unter Leitung von Helmut Rix bearbeitet von Martin J. Kümmel, Thomas Zehnder, Reiner Lipp, Brigitte Schirmer. 2nd ed. Wiesbaden: Reichert.

**LIVAdd** Martin J. Kümmel (2015). Addenda und Corrigenda zu LIV². url: http://www.martinkuemmel.de/liv2add.html.

**REW** Wilhelm Meyer-Lübke (1935). *Romanisches etymologisches Wörterbuch*. 6th ed. Heidelberg: Winter.

## Bibliography

Adams, Douglas Q. (2013). *A Dictionary of Tocharian B. Revised and greatly enlarged*. 2 vols. Amsterdam & Atlanta: Rodopi.

Beekes, Robert S. P. (2010). *Etymological Dictionary of Greek*. With the assistance of Lucien van Beek. 2 vols. Leiden & Boston: Brill.

Beekes, Robert S. P. (2014). *Pre-Greek. Phonology, Morphology, Lexicon*. Leiden: Brill.

Budimir, Milan (1969). *Sa balkanskih istočnika*. Belgrade: Srpska knjiievna zadruga.

Carnoy, Albert (1955). *Dictionnaire étymologique du Proto-Indo-Européen*. Louvain: Publications Universitaires.

Chantraine, Pierre et al. (2009). *Dictionnaire étymologique de la langue grecque. Histoire des mots*. Paris: Klincksieck.

De Vaan, Michiel A. C. (2008). *Etymological Dictionary of Latin and the Other Italic Languages*. Leiden & Boston: Brill.

Derksen, Rick H. (2008). *Etymological Dictionary of the Slavic Inherited Lexicon*. Leiden & Boston: Brill.

<!-- pdf-page: 32 | article-page: 59 -->

Furnée, Edzard J. (1972). *Die wichtigsten konsonantischen Erscheinungen des Vorgriechischen*. The Hague: Mouton.

Garnier, Romain (2015). Rev. of Beekes 2014. In: *Journal Asiatique* 303.2, 332–334.

Garnier, Romain (2016). *La dérivation inverse en latin*. Innsbruck: Institut für Sprachen und Literaturen.

Georgiev, Wladimir (1941–1945). *Vorgriechische Sprachwissenschaft*. Sofia: Sofijski Universitet Kliment Ochridski.

Griepentrog, Wolfgang (1995). *Die Wurzelnomina des Germanischen und ihre Vorgeschichte*. Innsbruck: Institut für Sprachwissenschaft der Universität Innsbruck.

Haas, Otto (1959). “Die Lehre von den indogermanischen Substraten in Griechenland”. In: *Linguistique Balkanique* 1, 29–56.

Hackstein, Olav (1995). *Untersuchungen zu den sigmatischen Präsensstammbildungen des Tocharischen*. Göttingen: Vandenhoeck & Ruprecht.

Hackstein, Olav (2002). “Uridg. *CH.CC > *C.CC”. In: *Historische Sprachforschung* 115, 1–22.

Hester, David A. (1968). “Recent developments in mediterranean «substrate» studies”. In: *Minos* 9.1, 219–235.

Holzer, Georg (1989). *Entlehnungen aus einer bisher unbekannten indogermanischen Sprache im Urslavischen und Urbaltischen*. Wien: Akademie der Wissenschaften.

Katičić, Radoslav (1976). *Ancient languages of the Balkans*. Paris: Mouton.

Katz, Joshua T. (2000). “Evening dress: The metaphorical background of Latin uesper and Greek ἕσπερος”. In: *Proceedings of the 11th Annual UCLA Indo-European Conference*. Washington, DC: Institute for the Study of Man, 69–93.

Kortlandt, Frederik H. H. (2003). “An Indo-European substratum in Slavic?” In: *Languages in Prehistoric Europe*. Ed. by Alfred Bammesberger & Theo Vennemann. Heidelberg: Winter, 253–260.

Kretschmer, Paul (1925). “Die protindogermanische Schicht”. In: *Glotta* 14, 300–319.

Kroonen, Guus (2013). *Etymological Dictionary of Proto-Germanic*. Leiden & Boston: Brill.

Kuryłowicz, Jerzy (1956). *L’apophonie en indo-européen*. Wrocław: Zakład Imiena Ossolińskich.

Lejeune, Michel (1947). “Linguistique préhellénique”. In: *Revue des Études Anciennes* 49.1, 25–37.

Matasović, Ranko (2009). *Etymological Dictionary of Proto-Celtic*. Leiden & Boston: Brill.

Matasović, Ranko (2013). “Substratum words in Balto-Slavic”. In: *Filologija* 60, 75–102.

Meiser, Gerhard (1998). *Historische Laut- und Formenlehre der lateinischen Sprache*. Darmstadt: Wissenschaftliche Buchgesellschaft.

Merlingen, Weriand (1967). “Fair play for ‘Pelasgian’”. In: *Lingua* 18, 144–167.

Messing, Gordon M. (1958). Rev. of Carnoy 1955. In: *The American Journal of Philology* 79.1, 85–90.

Nikolaev, Alexander S. (2004). “Die Etymologie von altgriechischem ὕβρις”. In: *Glotta* 80, 114–125.

Nikolaev, Alexander S. (2007). “The name of Achilles”. In: *Cambridge Classical Journal* 32, 162–173.

Nussbaum, Alan J. (1997). “The ‘Saussure Effect’ in Latin and Italic”. In: *Sound Law and Analogy. Papers in honor of Robert S. P. Beekes on the occasion of his 60th birthday*. Ed. by Alexander M. Lubotsky. Amsterdam & Atlanta: Rodopi, 181–203.

Pokorny, Julius (1959). *Indogermanisches etymologisches Wörterbuch*. Vol. 1. Bern & München: Francke.

<!-- pdf-page: 33 | article-page: 60 -->

Szemerényi, Oswald (1964). *Syncope in Greek and Indo-European and the nature of Indo-European accent*. Naples: Istituto Universitario Orientale di Napoli.

Szemerényi, Oswald (1991). “The development of the Indo-European mediae aspiratae in Latin and Italic”. In: *Scripta minora. Selected essays in Indo-European, Greek and Latin*. Ed. by John T. Hooker & Patrick Considine. Innsbruck: Institut für Sprachwissenschaft, 628–693.

Van Windekens, Albert J. (1952). *Le pélasgique. Essai sur une langue indo-européenne préhellénique*. Louvain: Publications Universitaires et Institut Orientaliste.

Watkins, Calvert (1969). “A Latin-Hittite Etymology”. In: *Language* 45.2, 235–242.

Weiss, Michael (1994). “On the non-verbal origin of the Greek verb νήφειν ‘be sober’”. In: *Historische Sprachforschung* 107, 91–98.

## Footnotes

[^1]: A few examples: τέρμινθος ∼ τερέβινθος ‘terbinth tree’, ἀσάμινθος ‘bath-tub’, ἐρέβινθος ‘chick-pea’, λαβύρινθος ‘labyrinth (vel sim.)’, νάρκισσος ‘narcissus’, and κυπάρισσος ‘cypress’.

[^2]: We shall come back to this root and, in fact, to this very same nominal etymon in Section 5.5.1.

[^3]: There is therefore no need for a PIE root *KrepH- (LIV²: 370).

[^4]: This root is not included in LIV². Yet it is attested in several formations. An i-stem noun PIE *(s)ḱól-i- reflected by Gr. σκολιός ‘curved, unright’ was paralleled by a u-stem noun PIE *(s)ḱól-u-, the starting point for a secondary adjective PIE *ḱl-ou̯-ó- ‘inclined, limping’ seen in Lat. *clăuus, hence *claueō ‘to limp’, whose quasi-participle *clauidus is attested in the syncopated form claudus ‘lame, limping’. Cf. also PIE *ḱl-ou̯-ní- [f.] ‘hip’, cf. Franconian *hanka [f.] ‘id.’ (hence Fr. hanche ‘id.’) based on *hinkan ‘to limp’.

[^5]: This noun has served as a basis for the denominative verb Gr. κλέπτω < Com. Gr. *klép-i̯o.

[^6]: This primary root could also be (indirectly) reflected in OE swodrian ‘to sleep, be half asleep’ < Com. Germ. *sweðrōjan, a denominative of an instrument name *sweþran ‘bed (vel sim.)’ < *su̯é-tro- < PIE *séu̯-tro-. See also Hitt. šeš-zi / šaš-.

[^7]: In fact, the original meaning of the PIE root *u̯es- is likely to be something like ‘wrap, swaddle (vel sim.)’, hence a general meaning ‘cover’ specialised as ‘to dress, to be dressed’, further specialised in Hittite and Latin for funerary contexts. Note also the proposal by Katz (2000: 82), according to whom Gr. ἕσπερος ‘evening’ and Lat. uesper ‘id.’ reflect an *-eró- derivative with “locatival meaning” of a stem *u̯ósp-/u̯ésp- ‘covering’. This analysis is incompatible with a *-bh- extension of the root as assumed by Kloekhorst, and is a further argument in favour of our *-p-extension. (We thank Ben Fortson for the reference to Katz’s article.)

[^8]: The chronological ordering of our laws cannot be completely established based on our examples. Certain relative orderings can be determined based on specific words. They will be mentioned whenever applicable. The total ordering we propose at the end of this section is therefore one possible order amongst several that are compatible with our data.

[^9]: In fact, dēlĭbūtus (with a short -ĭ-) is the only Latin word cited by de Vaan (2008) that (indirectly) reflects PIE *h₂libʰ- ‘to anoint’. It is a secondary “blend of dēlĭtus (from dēlĭno) and imbūtus” (Szemerényi 1991: 1030).

[^10]: As we shall see later, an etymon loi̯(H)-bʰó- ‘rainy, wet (vel sim.)’ could also serve as a starting point for deriving the same words via our substrate language. However, we believe that a nominal scheme in *CóC-p-o- is a more natural candidate.

[^11]: For the choice of the symbol β to note the lenited labial, see the discussion in Section 5.4.1.

[^12]: As in Germanic, voice oppositions resulting from stress oppositions, as introduced here for the pretonic lenition law and in the next section with a posttonic fortition law, make stress oppositions superfluous, thus enabling a simplification of the stress patterns as they lose their morphological value.

[^13]: Although formally ingenious, the suggestion made by Nikolaev (2004), namely a derivation from *hₓi̯ó/é(h₂)gʷ-ri- ‘power’, internally derived from *hₓi̯á(h₂)gʷ-ro- ‘mighty’, should be rejected on semantic grounds. In Greek, Nikolaev connects ἥβη ‘youthful power’ and ἁβρός ‘graceful, delicate, pretty, esp. of young ladies’ < *hₓi̯á(h₂)gʷ-ro- to the same PIE root *hₓi̯e(h₂)gʷ- (note that both Chantraine et al. (2009) and Beekes (2010) reject the connection between the two Greek words). This root is therefore related to the notion of youthful strength (see also Lith. jėgà ‘strength, force, power, understanding, intelligence’ and Latv. ję̃ga ‘strength, reflection, sense, idea’). This semantic value is difficult to equate with that of ὕβρις, which is typically associated with older men, sometimes even imposing their arrogance, violence or abuse on younger people.

[^14]: The semantic sketch is paralleled by Lat. superbus ‘who thinks himself above others, arrogant, insolent, discourteous, uncivil, rude’, by Got. ubils ‘bad, evil’, and by MIr. fel [o] ‘id.’, both from PIE *up-eló-.

[^15]: For further attestations and derivatives, see for example Chantraine et al. 2009: 286 and Beekes 2010: 356. Chantraine et al. (2009) connects these forms with the IE root of inherited Gr. δέρω ‘to skin, flay’ and Gr. δρέπω ‘to pluck, cut off’, namely PIE *der- ‘to tear, flay’ (LIV²: 119), with, according to us, a *-p- extension of this root in δρέπω (cf. related forms and discussion in Beekes 2010: 353). However, he admits the vocalism remains unexplained, and resorts to classing δρύπτω and its derivative as an expressive group. On the other hand, Beekes (2010: 356) rejects this connection, in view of the forms in δρύφ-/δρύψ- and by adducing δρυμάσσω, primarily ‘to tear up, crush’. His conclusion is that δρύπτω, together with its variants and derivatives, is “clearly […] Pre-Greek,” and that “therefore it is improbable that it derives from IE δέρω.”

[^16]: This is to be expected as our substrate language seems to exhibit a bipartite opposition between lenis and fortis plosives, as we shall illustrate throughout the paper. This dual system had to be mapped during the borrowing process to the Com. Gr. tripartite opposition between voiced, voiceless, and voiceless aspirated plosives (e.g. *b/*p/*pʰ).

[^17]: This points to a geminated and/or affricate realisation *pp ∼ *pᶠ (cf. Section 5.2.1).

[^18]: Concerning δρυμάσσω ‘to tear up, crush’, there is probably no need for a phonetic explanation for the -μ-. Following Chantraine et al. (2009: 286), it is better analysed as a portmanteau form based on δρύπτω and (ἰ)μάσσω.

[^19]: See below for an example with s-mobile.

[^20]: Cf. also first-millennium Gr. καλύπτω ‘to hide’ (with a short ῠ as can be deduced from the infinitive aorist καλύψαι), which takes the place of the expected e-grade root present \*\*κέλω < PIE *ḱel-e/o- attested in several other languages (OE helan ‘to hide’, Lat. oc-cŭl-ĕrĕ < Com. It. *óp-kel-e/o-).

[^21]: Note that Hitt. kalŭppa- ‘petticoat (vel sim.)’ is probably based on the same root with the same nominal formation pattern. It could be the result of analogical levelling based on both PIE *ḱl-óu̯-p-o- and PIE *ḱl-u-p-éh₂ into a masculine stem *ḱl-ú-p-o-, which would parallel what we have posited in section 5.1.3 when discussing Gr. δρύπτω.

[^22]: The shortening of the *ū before a following fortis *pp/*pf is regular in (Vulgar) Latin.

[^23]: Com. Sl. *kolyba cannot be borrowed from Gr. καλύβη because of its short ŭ. Forms in h- such as Croat. halupa (Kastav), Slovenian halúpa, Russ. dial. халу́па, Pol. chałupa, Cz. chalupa (dial. chalpa) from a Com. Sl. *xalupa, are probably borrowed from a Germanic source *halaupa (Matasović 2013; ESSJ: 8, 15–16 and 10, 162–164.)

[^24]: In this case, the schwa seems to be homothetically ‘coloured’ as *o in the borrowed Greek form.

[^25]: We also analyse Gr. σκόλοψ [m.] ‘pointed pole, palisade, prickle’ as a borrowing from our substrate language based on the same PIE root. We start again from *skól(h₂)-p-, a nominal formation using the labial morph, but this time in the o-grade. The Saussure effect and the metathesis described by Griepentrog (1995: 198) yield *sklóps for the nominative form, which is then generalised, as posited in our analysis of Gr. κολοβός. The systematic schwa epenthesis in word-initial *#(s)klV- applies, hence Substr. *skə́lop-. With the same homothetic schwa colouring as postulated for Gr. κολοβός, this substrate word is reflected as Gr. σκόλοψ. Note that this word can be related to the Hesychian glosses σκόλοφρον· θρανίον ‘bench’ and σκολύψαι· κολοῦσαι, κολοβῶσαι ‘cut short, mutilate’.

[^26]: Two other examples of this β ∼ ϝ alternation in (Common) Greek reflecting Substr. *β will be discussed below in Sections 5.4.1 and 5.5.4.

[^27]: Note that under our analysis, Gr. κολοβός is a direct cognate of Com. Germ. *χalƀáz ‘half’ > Eng. half, and Got. halbs ‘id.’.

[^28]: This is a correction of a PIE root \*\*kʷerpH- proposed earlier (LIV²: 392–393).

[^29]: In Section 5.6, we shall introduce another law, namely the metathesis CVRC > CRVC. Gr. κύρβεις provides an important clue about the relative chronology of the treatment *Cu̯r̥C > *CurC and this metathesis: the metathesis must have applied before the rule *Cu̯r̥C > *CurC, as otherwise we would find words such as κρύβις, with a metathesised r.

[^30]: See also Ger. Kurbis from non-reduplicated Vulgar Latin *curbita.

[^31]: This adjective could be related to the intransitive present Gr. κῡ́ρω ‘to reach, meet, be located/situated, be’ < PIE *kúr-i̯e/o- ‘to turn to/towards; be located/situated’ (for the semantics, cf. Lat. uersārī ‘be located/situated’, frequentative of Lat. uersor ‘to dwell, leave, remain, stay, be’ vs. active Lat. uersō ‘to turn’).

[^32]: Note also that a Greek variant Gr. σύρβη is attested with the same meaning, and derived words in both τ- and σ- exist (cf. Chantraine et al. 2009: 1106). The variants in σ- can be explained by a Greek-internal phenomenon also seen in Com. Gr. *tú > Ion. Att. σύ ‘you (sg.)’ next to other dialectal forms τύ. This change is only attested when the υ is short, which is the case here.

[^33]: This root is reconstructed by Rix (LIV²: 557) as †(s)kreb-, a result of not taking Kluge’s Law into account.

[^34]: Note also for example the derived nouns Gr. κράμβος [m.] ‘disease that dries up grapes’, derived from this adjective, and κράμβη [f.] ‘cabbage, Brassica cretica’.

[^35]: See other examples in Sections 5.2.2 and 5.5.4.

[^36]: The PIE root *kʷRepH- ‘to lament’ (LIV²: 370) is semantically more divergent. Rix (LIV²: 370) also suggests a PIE root *KrepH- ‘crack’ for Lat. crepāre (perf. crepuī, sup. crepitum) ‘to crack’, which is to be explained differently as a back-formation from the frequentative crepitāre ‘id.’ of an older crepāre/*crepuī ‘id.’ (Garnier 2016: 11.1.4).

[^37]: The same kind of derivation pattern can be seen in PIE *kʷsṓp-s, *kʷsép-s [f.] ‘night’, reflecting PIE *gʷṓs-p-s < *gʷṓs(h₂)-p- ‘extinction’ (cf. Section 4).

[^38]: This root is not \*\*pers- pace Kümmel (LIVAdd: 67). As Kümmel himself discusses, a PIE root *bʰers-, but not \*\*pers-, can explain Gr. φάρσος ‘fragment’ from *φαρσύς, from PIE *bʰr̥s- (cf. Luw. parsul- [n.] ‘fragment’). Both \*\*pers- and *bʰers- can explain the forms of Hitt. parši-a(ri), parš-a(ri) ‘to break’ adduced by Kümmel (EDHIL: 642). The only problematic form is Arm. pʿeṙeke- ‘to split’, which cannot result recto itinere either from \*\*pers- or from *bʰers-, and whose velar enlargement is unclear. It might be explainable from a root variant of *bʰers- with s-mobile, namely *spʰers-.

[^39]: There is no need for an “obscure Pre-Gm. root *bʰrest-” as proposed by Kroonen (2013: 75).

[^40]: Note that the Verner-like lenition law and its fortition counterpart prevent us from directly observing the result of this law if it also applied word-internally. However, we are inclined to believe that this treatment PIE *Dʰ > Substr. *T was systematic in all positions but the effect of this treatment word-internally was masked by the later lenition and fortition laws.

[^41]: The intervocalic -s- is regular in reflexes of Pre-Com. Gr. Cr̥sV leading (phonetically or by analogical levelling) to Gr. CrasV, see θρασύς ‘audacious, courageous, bold’ < *dʰr̥séu̯-. Compare the treatment *CN̥ sV > CasV seen in δασύς ‘hairy’ < *dn̥séu̯- and maybe in ἄσις ‘slime, mud’ < *h₂m̥ si- (Nikolaev 2007). As a result, πράσον does not shed any light on whether the borrowings to our substrate language occurred before of after the loss of intervocalic *-s-.

[^42]: Cf. OCS dьbrь ‘id.’

[^43]: And not from \*\*dʰóu̯b-o- pace Adams 2013: 330. See also, with an unexpected p, Sln. dúpa ‘hole, burrow’ and Cz. (arch.) doupa ‘hollow, burrow’, Slk. dúpa ‘id.’ < Com. Sl. *dupa [f.], maybe a loan word from a Germanic *daupa < Com. Germ. *daup-ō ‘id.’.

[^44]: For the meaning, cf. OFr. tou ‘underground pipe’, (REW: 746 (8968)).

[^45]: Gr. τοῦφος ‘grave, tomb’, attested in the Hesychian gloss τοῦφος· τάφος, is an inherited word based on a nominal stem *dʰóu̯bʰ-o- via Pre-Com. Gr. *tʰoūpʰos and Grassmann’s Law.

[^46]: The synchronic meaning of Gaulish *dubno-/*dumno- is ‘world’. However, this meaning is derived from an etymological meaning ‘underworld’, as can be seen for instance from the meaning of W dwfn ‘deep’ < Com. Celt. *dubnos and OIr. domain ‘id.’ < Com. Celt. *dubnis.

[^47]: This variant futher discredits the explanation by Georgiev via a supposedly “Pelasgian” *dʰm̥ bʰo- > *dm̥ bʰo- > *tm̥ bʰo- > *tumbʰo- > *tumbo- (see Katičić 1976: 71).

[^48]: On this alternation, see also Sections 5.2.2 and 5.4.1.

[^49]: Rather than a PIE root such as *strebʰ- (LIV²: 603) posited exclusively because of the Greek verb στρέφω. The update provided by Kümmel (LIVAdd: 75) based on Myc. Gr. ku-su-to-ro-ka /ksustrokʷʰā́/ ‘sum total’, namely a root of the form *stregʷʰ-, is no less ad hoc and should be abandoned unless evidence from other languages is adduced.

[^50]: The suggestion by Kümmel (LIVAdd: 75) that Gr. στρόμβος is based on a stem *stramb- < PIE *str̥-né/n-gʷʰ- is not convincing, not least because it is based on a virtually unattested root (see previous footnote).

[^51]: The reason for this correspondence is unclear. It could be the result of a shift within the substrate language before the time of borrowing. It could also result from a Substratic articulation of initial Substr. *Tr- that, according to the ancestors of the Classical Greeks, sounded more like the predecessor to Gr. θρ- than to Gr. τρ-. In particular, forms with ternary semantics are sometimes also attested with an initial *tr-, but this might result from a folk-etymological contamination of inherited Gr. τρι- ‘three-, triple’.

[^52]: Cf. Lith. sprū́g-ti ‘to rise, spring, escape from something’, present sprū́gstu < *sprug-sḱ-é/ó-, with PIE *sprug.C- > Com. BSl. *sprū́g.C- via Winter’s Law (LEW: 883).

[^53]: This rule does not apply if the *r is vocalic, as illustrated by Lat. porrum and Gr. πράσον reflecting Substr. *pŕ̥so- < PIE *bʰr̥s-ó- (see Section 5.5.1).

[^54]: Contrary to the lenited counterpart of a previous *p as produced by the Verner-like effect in pretonic position, we have no evidence for a treatment *bʰr > *βr instead of *bʰr > *br. The *b in such clusters could rather be a conditioned allophone of Substr. *p in this specific environment. The same holds for the result of the treatment PIE *#pr- > Substr. *#br- (see below).

[^55]: It is probably a Doric equivalent of ξόανον, which has the same meaning (Chantraine et al. 2009: 195, s. v. βρέτας).

[^56]: The expected metathesis of *r (cf. Section 5.6) must therefore have occurred beforehand.

[^57]: The family of Gr. πέρθω (Hom.+) ‘to destroy, devastate’ should be kept separate on semantic grounds, and be analysed as reflecting the PIE root *per- ‘to hit’ (LIV²: 473) (cf. Arm. ehar ‘hit’, Com. Sl. *perǫ ‘id.’).

[^58]: For a parallel, see the pseudo-verb νήφω ‘to be sober’ created from its participle νήφων, -οντος, together with the dative plural form νήφοσι in Theognis (Weiss 1994).

[^59]: Forms with an initial γ- are also attested, namely the optative ποτιγλέποι (Alcman) and the noun γλέφαρον (Alcman, Pindar). Both are dialectal (Doric) forms, which probably exhibit a dissimilation b—p > g—p, rather than the often assumed dissimilation gʷ—p > g—p (GEW: 1, 243).

[^60]: Cf. Att. μέγεθος vs. Ion. μέγαθος ‘magnitude’ and μέγας ‘great’, all from PIE *meǵh₂-, or τέμαχος ‘slice’ vs. τέμενος ‘piece of land resulting from a partition’, both from PIE *temh₂-.

[^61]: As a semantic parallel, GEW: 2, 763, s. v. σπέλεθος mentions Ger. scheißen ‘to defecate’ < *‘to separate’ (cf. PIE root *sḱʰei̯d- ‘to cut, separate’).

[^62]: Cf. Gr. μέγεθος ‘greatness’ next to Gr. μέγας ‘great’ from PIE *méǵ-h₂, already cited above.

[^63]: Cf. Hom. Gr. πλαταμών [m.] ‘flat stone’ if from *πλεταμών (Ved. prathimán- ‘wideness’).

[^64]: In fact, if Greek has borrowed words both from a centum and from a satem language, it explains why “Pelasgic” studies have failed, as two distinct sets of phonetic laws and two distinct borrowing chronologies would be required.
