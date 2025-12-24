## 1. Objective

The objective of this phase is to train a Named Entity Recognition (NER) model capable of identifying fashion-related attributes in short product descriptions.

The model learns from weakly supervised labels generated in Phase 4 and aims to generalize beyond explicit rule matches.

---

## 2. Model Selection

We use **BERT-base-cased** as the underlying transformer model.

### Justification:
- Strong contextual representation for short text
- Case sensitivity preserves brand name signals
- Widely used baseline for NER tasks
- Suitable for weakly supervised learning

Larger or alternative models were intentionally avoided, as observed errors were driven by label ambiguity rather than model capacity.

---

## 3. Training Data

Training data consists of:
- Tokenized product descriptions
- BIO labels generated via weak supervision
- Six attribute classes:
  - PRODUCT_TYPE
  - PATTERN
  - MATERIAL
  - FIT
  - LENGTH
  - BRAND

No manually annotated data was used.

---

## 4. Training Setup

The model was fine-tuned using the HuggingFace `Trainer` API.

### Key settings:
- Optimizer: AdamW
- Learning rate: 2e-5
- Batch size: 16
- Epochs:
  - Diagnostic run: higher epochs to observe overfitting
  - Final model: reduced epochs (2–3) to improve generalization
- Evaluation strategy: per epoch

Models and checkpoints are saved to Google Drive for reproducibility.

---

## 5. Training Observations

During training, the model demonstrated:
- Rapid convergence
- Low training and validation loss
- Clear signs of overfitting at higher epoch counts

This behavior is expected due to:
- Weak supervision noise
- Limited semantic diversity in compressed fashion descriptions

As a result, a lower epoch count was selected for the final model.

---

## 6. Limitations

While the model learns span structure and contextual relationships, it exhibits:
- Attribute identity confusion
- Sensitivity to overlapping terminology
- Errors driven by noisy weak labels

These limitations motivate the introduction of post-processing and hybrid inference strategies in subsequent phases.

---

## 7. Output of This Phase

The output of Phase 5 is:
- A trained NER model capable of extracting attribute spans
- Saved model checkpoints
- Baseline predictions for comparison with post-processed and hybrid systems

This model serves as the foundation for further refinement rather than a final standalone solution.

## 8. Qualitative Evaluation and Post-Processing Impact

To assess model behavior under weak supervision, we perform a qualitative evaluation using controlled fashion description examples.

### Observations (Model-Only)

The model-only NER system exhibits:
- Frequent attribute identity confusion (e.g., MATERIAL vs FIT)
- Fragmented phrase labeling for multi-token attributes
- Misclassification of compressed fashion descriptors
- Sensitivity to overlapping terminology (e.g., `logo`, `midi`, `leather`)

These errors are consistent with known limitations of weakly supervised NER, where label noise and attribute overlap affect semantic precision.

### Impact of Post-Processing

After applying post-processing with domain constraints and phrase-level (n-gram) rules:
(Phrase-level rules were derived from high-frequency n-gram analysis of the dataset)
- Multi-token attributes such as `logo print` and `midi dress` are correctly resolved
- Token-level ambiguities (e.g., `leather`, `denim`) are consistently normalized
- Span coherence and attribute identity are significantly improved

Qualitative comparisons demonstrate that post-processing corrects systematic semantic errors while preserving the model’s ability to generalize to unseen combinations.

### Remaining Limitations

Some ambiguous cases (e.g., `cropped t-shirt`) remain partially unresolved due to:
- Attribute ambiguity in natural language
- Limited phrase rule coverage
- Inherent uncertainty in weak supervision

These cases are intentionally retained for analysis in subsequent phases rather than force-corrected.

---

This evaluation motivates the transition to a hybrid rule–model system in the next phase.