# AI Writing Style Extraction, Voice Cloning & Antigravity Style Guide Synthesis

This guide provides research, prompt engineering patterns, analysis frameworks, and specifications for extracting AI writing styles, cloning authorial voices, and synthesizing reusable Antigravity Markdown (`SKILL.md`) rules from sample documents.

---

## 1. Executive Overview & Architectural Philosophy

Large Language Models (LLMs) default to a homogenized, synthetic tone characterized by over-explanation, repetitive structural transitions, balanced hedging, and recognizable cliché vocabulary ("AIsms"). Replicating a specific human author's voice or enforcing corporate brand consistency requires moving beyond surface-level tone descriptors to deterministic, rule-based style extraction.

### Key Architectural Concepts
- **Stylometric Extraction:** Systematic decomposition of prose into measurable lexical, syntactic, structural, and rhetorical parameters.
- **Progressive Disclosure via Antigravity Skills:** Utilizing Google Antigravity's Agent Skills Specification and Agentic Context Profiles to encapsulate style rules in lightweight `SKILL.md` files or workspace rules (`.gemini/config/rules/*.md`).
- **Imperative Rule Encoding (RFC 2119):** Converting subjective stylistic preferences into unambiguous mandates using normative keywords (**MUST**, **SHOULD**, **MUST NOT**, **NEVER**).

---

## 2. Multidimensional Stylometric Extraction Framework

```text
                  ┌─────────────────────────────────────────┐
                  │      6-DIMENSIONAL STYLOMETRICS         │
                  └────────────────────┬────────────────────┘
                                       │
     ┌─────────────────┬───────────────┼───────────────┬─────────────────┐
     ▼                 ▼               ▼               ▼                 ▼
┌─────────┐      ┌───────────┐   ┌───────────┐   ┌───────────┐     ┌───────────┐
│ Lexical │      │ Syntactic │   │ Formatting│   │   Tone &  │     │Rhetorical │
│ Profile │      │ Structure │   │  & Pacing │   │  Cadence  │     │ Devices   │
└─────────┘      └───────────┘   └───────────┘   └───────────┘     └───────────┘
                                       │
                                       ▼
                         ┌───────────────────────────┐
                         │   Anti-AI Purge Matrix    │
                         │   (Eliminating AIsms)     │
                         └───────────────────────────┘
```

### 2.1 Lexical & Vocabulary Profile
- **Type-Token Ratio (TTR):** Measure of vocabulary diversity (unique words / total words).
- **Jargon & Domain Density:** Industry-specific vocabulary vs. layperson equivalents.
- **Discourse Markers & Transitions:** Preferred connective words (e.g., favoring "Conversely," or "That said," over "However," or "Furthermore,").
- **Assertion vs. Hedging:** Frequency of definitive statements vs. qualifying terms ("appears to be", "arguably", "potentially").

### 2.2 Syntactic & Structural Architecture
- **Sentence Length Distribution:** Ratio of short (1–10 words), medium (11–22 words), and long (23+ words) sentences.
- **Clause Complexity:** Preference for hypotaxis (complex subordinate structures) versus parataxis (short, coordinate clauses).
- **Voice Distribution:** Active vs. passive voice ratios.
- **Sentence Openers:** Frequency of adverbial fronting, participle clauses, or direct subject-verb starts.

### 2.3 Formatting, Pacing & Punctuation
- **Punctuation Footprint:** Frequency and usage of em-dashes (—), semicolons, parentheses, and Oxford commas.
- **Paragraph Density:** Average paragraph length (single-sentence line breaks vs. dense multi-sentence blocks).
- **Emphasis Styles:** Selective use of bolding, italics, inline code, or bulleted lists versus continuous narrative prose.

### 2.4 Tone, Stance & Cadence
- **Formality & Distance:** First-person ("I/we"), second-person ("you"), or detached third-person perspective.
- **Emotional Resonance & Energy:** High-energy instructional tone vs. calm, analytical, or dry wit.
- **Pacing Rhythm:** Staccato (rapid-fire assertions) vs. legatist (flowing, balanced prose).

### 2.5 Rhetorical & Argumentation Devices
- **Framing Strategies:** Direct problem-solution loops, storytelling hooks, or empirical data-first starts.
- **Structural Analogies:** Frequent use of metaphors, real-world analogies, or rule-of-three groupings.

### 2.6 Anti-AI Footprint (The "AI-sm" Purge Matrix)

| AI Cliché Category | Overused AI Terms / Patterns | Target Replacement Strategy |
| :--- | :--- | :--- |
| **Overused Verbs** | *delve, foster, harness, illuminate, underscore, showcase, tailor, elevate* | Direct, concrete verbs (*explore, build, use, show, set, improve*) |
| **Overused Nouns** | *tapestry, beacon, landscape, testament, paradigm, synergy, realm* | Specific domain terms or plain language |
| **Structural Tropes** | *"In today's fast-paced world...", "In conclusion...", "It's important to remember that..."* | Direct entry into the topic; immediate thesis statement |
| **Formatting Tropes** | Excessive bolded bullet lists, balanced pros-and-cons in every section | Continuous narrative paragraphs or explicit tables |

---

## 3. Authoring Rule Generation & Synthesis Pipeline

```text
┌──────────────────┐     ┌───────────────────────┐     ┌────────────────────────┐     ┌───────────────────────┐
│ Stage 1:         │     │ Stage 2:              │     │ Stage 3:               │     │ Stage 4:              │
│ Ingestion &      │────>│ Multi-Dimensional     │────>│ Rule Abstraction &     │────>│ SKILL.md Synthesis &  │
│ Normalization    │     │ Stylometric Profiling │     │ Imperative Encoding    │     │ Progressive Packaging │
└──────────────────┘     └───────────────────────┘     └────────────────────────┘     └───────────────────────┘
```

### Stage 1: Ingestion & Normalization
- Strip external metadata, code blocks, and non-prose elements.
- Segment sample text into structural blocks (introductions, body paragraphs, transitions, conclusions).

### Stage 2: Multi-Dimensional Stylometric Profiling
- Calculate lexical metrics (TTR, sentence lengths, punctuation counts).
- Identify recurring structural patterns, sentence openers, and rhetorical devices.

### Stage 3: Rule Abstraction & Imperative Encoding
- Convert qualitative observations into RFC 2119 imperatives (**MUST**, **SHOULD**, **MUST NOT**, **NEVER**).
- Formulate specific negative constraints to block default LLM behaviors.

### Stage 4: SKILL.md / Rule File Synthesis
- Format the rules into an Antigravity-compliant `SKILL.md` document or `.gemini/config/rules/*.md` file with YAML frontmatter, context triggers, voice parameters, and few-shot exemplars.
