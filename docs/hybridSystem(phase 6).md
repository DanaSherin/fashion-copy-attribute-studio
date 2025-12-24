## 1. Objective

The objective of this phase is to formalize a hybrid inference system that combines a trained Named Entity Recognition (NER) model with rule-based and phrase-level constraints.

The hybrid system is designed to improve semantic correctness while preserving the model’s ability to generalize beyond explicit rule matches. This phase focuses on system integration and inference-time reasoning rather than additional model training.

---

## 2. Motivation for a Hybrid Approach

Results from earlier phases highlight complementary strengths and weaknesses across extraction methods.

- Rule-based extraction provides high precision for known patterns and is fully explainable, but suffers from limited coverage and poor generalization.
- Model-based NER generalizes better to unseen combinations but exhibits semantic confusion due to weak supervision and overlapping fashion terminology.

A hybrid approach is therefore required to balance precision, coverage, and robustness.

---

## 3. Hybrid System Design Principles

The hybrid system is guided by three core principles.

### 3.1 Attribute-Aware Trust

Different attributes exhibit different reliability characteristics. Certain attributes, such as PRODUCT_TYPE and PATTERN phrases, are more reliably identified using deterministic rules, while others benefit from contextual modeling.

### 3.2 Phrase-Level Priority

Multi-token fashion phrases such as `logo print`, `midi dress`, and `shoulder bag` are resolved using n-gram rules that take priority over conflicting model predictions.

### 3.3 Conservative Correction

Rules are applied only to correct clear semantic errors. The system does not introduce new attributes unless they are supported by either the model or known domain patterns.

---

## 4. Hybrid Inference Pipeline

The hybrid inference process follows a fixed and deterministic sequence:

1. Input text is passed to the trained NER model
2. Model predictions are generated at the token level
3. Token-level post-processing corrects systematic misclassifications
4. Phrase-level n-gram rules resolve multi-token attributes
5. Conflicts between rules and model outputs are resolved deterministically
6. Final attribute labels are produced

This design ensures reproducibility, explainability, and stable downstream behavior.

---

## 5. Conflict Resolution Strategy

When rule-based and model-based predictions disagree, the following logic is applied:

- If a known phrase is detected, the rule-based label overrides the model prediction
- If the model predicts an invalid attribute, the rule corrects it
- If the model predicts a valid unseen span, the model prediction is retained
- If no rule signal is present, the model output is preserved

This strategy avoids degeneration into a purely rule-based system while preventing systematic semantic errors.

---

## 6. Qualitative Evaluation

Qualitative evaluation was conducted using controlled fashion description examples.

For example, given the input `oversized leather logo print midi dress`, the model-only system exhibited misclassification of MATERIAL and LENGTH attributes and fragmented phrase labeling. The hybrid system correctly identified FIT, MATERIAL, PATTERN, LENGTH, and PRODUCT_TYPE with coherent phrase-level spans.

Across multiple test cases, the hybrid system consistently outperformed both rule-only and model-only approaches.

---

## 7. Advantages of the Hybrid System

The hybrid system provides:

- Improved semantic accuracy
- Stronger phrase coherence
- Robust handling of compressed fashion language
- Fully explainable correction logic

It represents the best trade-off between precision and generalization for weakly supervised NER in the fashion domain.

---

## 8. Limitations

Despite improvements, the system remains limited by:

- Ambiguous natural language constructs (e.g., `cropped t-shirt`)
- Finite rule coverage
- Absence of gold-standard annotations

These limitations are explicitly acknowledged and retained for transparency and discussion.

---

## 9. Role of Phase 6 in the Overall Project

Phase 6 establishes a stable and reliable attribute extraction layer. This layer enables structured querying, explainable outputs, and safe downstream usage.

It serves as the final extraction system used by subsequent components.

---

## 10. Transition to Next Phase

With the hybrid inference system finalized, the project proceeds to **Phase 7 — Interactive Chatbot and Demonstration**.

In the final phase, extracted attributes are used for user interaction, explanation, and controlled generation.