## 1. Purpose of This Phase

The purpose of Phase 4 is to generate **token-level BIO labels** for product descriptions using **weak supervision**, based on the attribute schema defined in Phase 3.1 and the annotation guidelines defined in Phase 3.2.

This phase transforms raw text into a labeled dataset suitable for training a Named Entity Recognition (NER) model, without relying on manual annotation.

---

## 2. Motivation for Weak Supervision

Manual annotation of large-scale fashion datasets is expensive, time-consuming, and prone to inconsistency. Given the size of the Farfetch listings dataset, weak supervision provides a scalable and reproducible alternative.

Weak supervision enables:

- Systematic label generation from explicit rules
- Alignment between schema design and training data
- Full transparency of label provenance
- Reproducibility suitable for an academic NLP project

---

## 3. Inputs to the Weak Supervision Pipeline

Weak label generation relies on three inputs:

### 3.1 Raw Text Data

- Source column: `shortDescription`
- Text type: short noun-phrase product descriptions
- Only textual data is used (no images, prices, or stock metadata)

### 3.2 Attribute Schema (Phase 3.1)

The following **six attributes** are used as label targets:

- PRODUCT_TYPE  
- PATTERN  
- LENGTH  
- FIT  
- MATERIAL  
- BRAND  

The schema is intentionally limited to attributes that are explicitly and consistently expressed in text.

### 3.3 Annotation Guidelines (Phase 3.2)

BIO tagging rules, span boundaries, and conflict resolution strategies guide how labels are assigned.

---

## 4. Lexicon-Based Weak Supervision Strategy

Weak supervision is implemented using **lexicon-driven, rule-based matching**.

For each attribute, a controlled vocabulary (lexicon) is defined. These lexicons specify which words or phrases may trigger labels during annotation.

Key design principles:

- Only explicit textual expressions are included
- Lexicons are conservative to reduce noise
- Multi-word phrases are preferred when they represent true product categories

---

## 5. Semi-Automatic Lexicon Expansion

Initial lexicons were expanded using **corpus-driven pattern discovery**, based on frequency analysis of unigrams and bigrams extracted from `shortDescription`.

This process involved:

1. Extracting frequent n-grams from the dataset
2. Identifying high-frequency candidates per attribute
3. Manually validating candidates against the schema
4. Selectively promoting valid phrases into lexicons

This **human-in-the-loop approach** improves coverage while preserving interpretability.

Examples of promoted phrases include:

- PRODUCT_TYPE: `shoulder bag`, `bucket bag`, `bomber jacket`
- PATTERN: `paisley print`, `zebra print`
- FIT: normalization of `slim-fit` → `slim`

No automatic lexicon growth was performed.

---

## 6. Rule-Based Span Matching

Each product description is tokenized using simple whitespace tokenization, followed by light normalization (e.g., removing `-fit` suffixes).

The labeling process:

1. Scans tokens for lexicon matches
2. Matches longer phrases before shorter ones
3. Assigns BIO labels to matched spans
4. Prevents overlapping entity assignments

Attribute matching follows a fixed priority order:

1. BRAND  
2. PATTERN  
3. MATERIAL  
4. LENGTH  
5. FIT  
6. PRODUCT_TYPE  

This priority ensures consistent resolution of potential conflicts.

---

## 7. BIO Label Assignment

For each description:

- Tokens are assigned one BIO label
- Multi-word attributes receive `B-` and `I-` tags
- Tokens not belonging to any attribute are labeled `O`

The result is a complete token–label sequence for every description.

---

## 8. Validation and Sanity Checks

Labeling rules were validated using manually constructed sanity-check examples.

Example validation confirmed that:

- Length terms (e.g., `midi`) are labeled as LENGTH
- Product nouns (e.g., `dress`) are labeled as PRODUCT_TYPE
- Composite phrases do demonstrate correct span detection
- Normalization enables correct FIT labeling (e.g., `slim-fit` → `slim`)

Only after these checks passed was the weakly labeled dataset considered final.

---

## 9. Limitations of Weak Supervision

Despite careful design, weak supervision has inherent limitations:

- Lexicons cannot capture all possible valid expressions
- Rare or novel phrases may remain unlabeled
- Exact phrase matching does not leverage broader context

To mitigate these issues, this project:

- Uses conservative, schema-aligned lexicons
- Applies human validation during lexicon expansion
- Avoids automatic model-driven label propagation

More advanced approaches, such as model-based bootstrapping, are intentionally excluded to preserve interpretability and avoid feedback-loop bias.

---

## 10. Role of This Phase in the Overall Pipeline

Phase 4 bridges the gap between:

- Conceptual design (Phases 3.1 and 3.2)
- Statistical modeling (Phase 5)

It ensures that training data is:

- Reproducible
- Interpretable
- Directly traceable to explicit design decisions

---

## 11. Transition to the Next Phase

With weakly supervised labels finalized and validated, the project proceeds to:

- **Phase 5:** NER model training and fine-tuning

At this stage, the labeling pipeline is considered frozen.

---