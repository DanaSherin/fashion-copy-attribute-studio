## 1. Purpose of This Phase

The purpose of Phase 2.5 is to document and justify the **preprocessing decisions** applied to the dataset before any annotation or modeling steps.

This phase ensures that text cleaning supports the downstream **Named Entity Recognition (NER)** task without altering or destroying meaningful linguistic signals.

---

## 2. Guiding Principle

For NER tasks, **minimal and conservative preprocessing** is preferred.

Unlike text classification, NER relies heavily on:
- Token boundaries
- Word order
- Surface forms
- Multi-word expressions

Over-processing can negatively impact label alignment and entity recognition.

---

## 3. Preprocessing Steps Applied

Only the following preprocessing steps were applied.

### 3.1 Handling Missing Values

- Rows with missing values in the `shortDescription` column were dropped.
- In practice, the dataset contained **no missing descriptions**, but this step was retained as a safety check.

This ensures robustness and prevents downstream errors.

---

### 3.2 Whitespace Normalization

The following operations were applied to `shortDescription`:

- Removal of leading and trailing whitespace
- Replacement of multiple consecutive spaces with a single space

This step improves consistency while preserving the original text content.

---

## 4. Preprocessing Steps Intentionally Avoided

The following common preprocessing techniques were **intentionally not applied**:

- Stopword removal
- Lemmatization
- Stemming
- Aggressive regex-based cleaning
- Early lowercasing

---

## 5. Rationale for Avoided Steps

These techniques were avoided because they can:

- Break multi-word fashion attributes (e.g., *“one-shoulder”*, *“logo print”*)
- Alter token boundaries required for BIO tagging
- Remove stylistically meaningful words
- Reduce interpretability of extracted entities

For example, stemming or lemmatization could distort fashion-specific terms that carry semantic meaning.

---

## 6. Impact on Downstream Phases

This minimal preprocessing strategy ensures that:

- Token-level annotations remain aligned with original text
- Attribute boundaries are preserved
- Weak supervision rules can be applied reliably
- Model training receives linguistically intact input

---

## 7. Key Takeaways from Phase 2.5

- Preprocessing was intentionally minimal and task-aware
- Text consistency was improved without semantic loss
- Decisions were guided by the requirements of NER, not generic NLP pipelines
- This phase provides a clean foundation for annotation and labeling

---

## 8. Transition to Next Phase

With preprocessing decisions finalized, the project proceeds to:

- **Phase 3.1:** Attribute schema design  
- **Phase 3.2:** Annotation guidelines and BIO tagging rules  

No annotation or modeling is performed in this phase.