# AI Writing Style Extraction, Voice Cloning & Antigravity Style Guide Synthesis (English & Turkish)

This guide provides research, prompt engineering patterns, analysis frameworks, and specifications for extracting AI writing styles, cloning authorial voices, and synthesizing reusable Antigravity Markdown (`SKILL.md`) rules from sample documents in **English** and **Turkish (Türkçe)**.

---

## 1. Executive Overview & Architectural Philosophy

Large Language Models (LLMs) default to homogenized, synthetic tones characterized by over-explanation, repetitive structural transitions, balanced hedging, and recognizable cliché vocabulary ("AIsms" in English; "Yapay Zeka Kalıpları" in Turkish). Replicating a specific human author's voice requires moving beyond surface-level tone descriptors to deterministic, rule-based style extraction.

### Key Architectural Concepts
- **Stylometric Extraction:** Systematic decomposition of prose into measurable lexical, syntactic, structural, and rhetorical parameters.
- **Multi-Lingual Adaptation:** Native handling of agglutinative Turkish morphology, SOV word order (kurallı/devrik cümle), and Turkish LLM clichés alongside English stylometrics.
- **Imperative Rule Encoding (RFC 2119):** Converting subjective stylistic preferences into unambiguous mandates using normative keywords (**MUST**, **SHOULD**, **MUST NOT**, **NEVER** / **ZORUNLUDUR**, **YASAKTIR**).

---

## 2. Multidimensional Stylometric Extraction Framework

### 2.1 Lexical & Morphological Profile
- **English:** Type-Token Ratio (TTR), jargon density, preferred discourse markers (*"Conversely,"*, *"That said,"*).
- **Turkish (Türkçe):** Suffix density (`-dir/-dir`, `-maktadır/-mektedir`, `-acağı/eceği`), modal suffixes (`-miş` vs `-di`), discourse markers (*"Nitekim,"*, *"Öte yandan,"*, *"Dolayısıyla,"*, *"Nihayetinde,"*).

### 2.2 Syntactic & Structural Architecture
- **English:** Active vs. passive voice ratios, clause complexity, sentence length distribution.
- **Turkish (Türkçe):** Sentence word order (Kurallı SOV: Özne-Nesne-Yüklem vs. Devrik cümle), active/passive verb suffix ratio (`-il/-in`), sentence length variation.

### 2.3 Anti-AI Footprint (The AI-sm Purge Matrix)

#### English AI Cliché Purge Table

| AI Cliché Category | Overused AI Terms / Patterns | Target Replacement Strategy |
| :--- | :--- | :--- |
| **Overused Verbs** | *delve, foster, harness, illuminate, underscore, showcase, tailor, elevate* | Direct, concrete verbs (*explore, build, use, show, set, improve*) |
| **Overused Nouns** | *tapestry, beacon, landscape, testament, paradigm, synergy, realm* | Specific domain terms or plain language |
| **Structural Tropes** | *"In today's fast-paced world...", "In conclusion...", "It's important to remember that..."* | Direct entry into the topic; immediate thesis statement |

#### Turkish AI Cliché Purge Table (Türkçe Yapay Zeka Kalıpları Temizleme Tablosu)

| Yapay Zeka Kalıp Kategorisi | Sık Kullanılan Yapay Zeka İfadeleri | Hedef Değişim / Temizleme Stratejisi |
| :--- | :--- | :--- |
| **Aşırı Kullanılan Fiiller/İfadeler** | *derinlemesine incelemek, büyük bir titizlikle, ışık tutmaktadır, harmanlamak, köprü kurmak, çığır açan, ön plana çıkmaktadır, büyük önem taşımaktadır* | Doğrudan, somut fiiller (*incelemek, ele almak, kurmak, göstermek, kullanmak*) |
| **Aşırı Kullanılan İsimler/Sıfatlar** | *mihenk taşı, mozaik, dönüm noktası, kutsal miras, vazgeçilmez, eşsiz* | Alana özgü somut terimler veya sade Türkçe ifadeler |
| **Basmakalıp Giriş/Sonuç İfadeleri** | *"Günümüzün hızlı tempolu dünyasında...", "Sonuç olarak...", "Özetlemek gerekirse...", "Unutulmamalıdır ki...", "Göz önünde bulundurulduğunda..."* | Doğrudan konuya giriş; ilk cümleden net tez sunumu; yapay özet paragraflarını kaldırma |

---

## 3. Turkish-Specific Prompt Engineering Patterns

### Pattern: Turkish Voice Anchor & Morphological Constraints
```markdown
<turkish_voice_anchor>
Yazarın özgün Türkçe üslubu uygulanmaktadır:
- Cümle Yapısı: Kurallı SOV cümleler ile ritmik devrik cümle dengesi.
- Fiil Çekimi: "-mektedir/-maktadır" yapmacıklığı yerine etken "-yor" veya "-di" geçmiş zaman çekimi.
- Yasaklı Kelimeler: "derinlemesine incelemek", "mihenk taşı", "günümüz dünyasında", "sonuç olarak".
</turkish_voice_anchor>
```
