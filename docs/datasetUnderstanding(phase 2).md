## 1. Purpose of This Phase

The goal of Phase 2 is to **understand the structure and linguistic characteristics of the dataset** in order to determine:

- Which columns are relevant for NLP
- What type of NLP task is most appropriate
- What attributes can realistically be extracted from text

This phase directly informs the design decisions made in later phases, including attribute schema definition and annotation strategy.

---

## 2. Dataset Overview

- **Dataset:** Farfetch product listings  
- **Source:** Kaggle  
- **Format:** CSV  
- **Domain:** Luxury fashion e-commerce  

The dataset contains both structured metadata and short textual descriptions of products.  
For this project, the focus is **exclusively on textual NLP signals**, not images or pricing prediction.

---

## 3. Column Selection Rationale

After inspecting all columns, the analysis focused on **three columns only**.

### 3.1 `shortDescription` (Primary NLP Signal)

- Contains concise product descriptions such as:
  - *“logo print strap sandals”*
  - *“embroidered midi dress”*
  - *“cropped skinny jeans”*
- Descriptions are:
  - Short
  - Phrase-based
  - Rich in fashion attributes

This column is the **core input** for all NLP tasks in the project.

---

### 3.2 `brand.name`

- Represents the fashion brand associated with each product
- Shows a highly skewed distribution toward luxury brands
- Used to:
  - Analyze brand dominance
  - Study brand–gender relationships
  - Support contextual chatbot responses later

---

### 3.3 `gender`

- Categories observed:
  - `women`
  - `unisex`
- The dataset is strongly skewed toward women’s fashion
- Unisex items are brand-dependent rather than evenly distributed

Gender is treated as **contextual metadata**, not a prediction target.

---

## 4. Data Integrity Checks

- Duplicate rows were checked and **none were found**
- Missing values in `shortDescription` were checked and **none were present**
- Minimal safety checks were still applied during preprocessing

This confirms the dataset is **clean and reliable** for downstream NLP tasks.

---

## 5. Brand Distribution Analysis

Brand frequency analysis revealed:

- A small number of brands dominate the dataset (e.g., Prada, Gucci, Fendi)
- A long-tail distribution of smaller brands
- Certain brands show a higher proportion of unisex items

This indicates that:
- Brand bias is present
- Brand-aware interpretation is important
- Brand information can enhance conversational explanations

---

## 6. Gender Distribution Analysis

- The majority of items are labeled `women`
- A smaller but meaningful subset is labeled `unisex`
- Unisex products are concentrated in specific brands

This suggests that:
- Gender should be used as a **filter or context**
- It is not suitable as a standalone NLP prediction task

---

## 7. Linguistic Analysis of `shortDescription`

### 7.1 Description Length and Structure

- Descriptions are short noun phrases
- They rarely form complete sentences
- They typically contain:
  - A product type
  - One or more descriptive modifiers

This structure favors **sequence labeling** rather than document-level classification.

---

### 7.2 Frequent Unigrams

Commonly occurring tokens include:

- `dress`
- `bag`
- `print`
- `trousers`
- `logo`
- `skirt`
- `sunglasses`
- `jacket`
- `sneakers`

These tokens strongly indicate **product category and attributes**.

---

### 7.3 Frequent Bigrams

Examples of high-frequency bigrams include:

- `midi dress`
- `mini dress`
- `logo print`
- `floral print`
- `cropped trousers`
- `shoulder bag`
- `tote bag`

These patterns clearly encode **multi-word fashion attributes**, making them ideal candidates for Named Entity Recognition (NER).

---

## 8. Implications for NLP Task Selection

Based on the analysis:

- The text is **attribute-rich but short**
- Information is localized to specific word spans
- Multiple attributes often appear in a single description

Therefore:

> **Named Entity Recognition (sequence labeling) is the most suitable NLP task for this dataset.**

Document-level classification would lose important fine-grained information.

---

## 9. Key Takeaways from Phase 2

- The dataset is well-suited for **attribute extraction**
- `shortDescription` is the primary NLP input
- Brand and gender provide useful contextual signals
- The linguistic structure supports BIO-style labeling
- All subsequent design decisions should be grounded in these findings

---

## 10. Transition to Next Phase

The insights from this phase directly inform:

- **Phase 2.5:** Preprocessing decisions  
- **Phase 3.1:** Attribute schema design  
- **Phase 3.2:** Annotation guidelines  

No modeling or labeling is performed at this stage.
Insights from Phase 2 directly informed the attribute schema and lexicon expansion in later phases.