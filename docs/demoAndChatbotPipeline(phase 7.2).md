## 1. Purpose of This Phase

The purpose of Phase 7.2 is to transform the hybrid NER system into a **user-facing, explainable AI demo** that can be accessed through a chatbot-style interface.

This phase does **not** introduce new models or learning mechanisms.  
Instead, it focuses on:

- System integration
- Explainable outputs
- Human-readable interaction
- Practical deployment readiness

This phase demonstrates how NLP models are used in real-world applications beyond raw prediction.

---

## 2. System Position in the Overall Pipeline

Phase 7.2 sits **on top of all previous phases** and consumes their final outputs.

End-to-end pipeline:

1. Raw user input (fashion description)
2. Transformer-based NER inference (Phase 5)
3. Hybrid post-processing with rules and n-grams (Phase 6)
4. Canonical structured output (Phase 7.1)
5. Conversational interface and demo logic (Phase 7.2)

No retraining or re-labeling occurs in this phase.

---

## 3. Input to the Demo System

The demo system accepts **free-form natural language descriptions**, such as:

- `oversized leather logo print midi dress`
- `floral print maxi dress`
- `shoulder bag in leather`

The input format is intentionally flexible to simulate real user behavior.

---

## 4. Canonical Output Format

All chatbot responses are grounded in a **single canonical output schema** defined in Phase 7.1.

Each response includes:

- Extracted attributes
- Attribute source (rule, model, or hybrid)
- Confidence level
- Textual evidence
- A generated, human-readable product title

Example (conceptual):

- PRODUCT_TYPE → dress
- MATERIAL → leather
- PATTERN → logo print
- FIT → oversized
- LENGTH → midi

This structure ensures transparency and traceability.

---

## 5. Explainability and Trust

The demo explicitly exposes:

- **Where each attribute came from**
- **Why it was selected**
- **How confident the system is**

This aligns with explainable AI principles and allows the chatbot to justify its responses instead of acting as a black box.

---

## 6. Role of the Chatbot Interface

The chatbot acts as a **presentation layer**, not an intelligence layer.

It performs the following tasks:

- Receives user input
- Calls the hybrid extraction pipeline
- Formats structured output into natural language responses
- Presents extracted attributes and generated titles

All reasoning and extraction logic remains unchanged.

---

## 7. Why a Chatbot Interface Is Appropriate

A chatbot interface is chosen because:

- Fashion descriptions are naturally conversational
- Users expect explanations and suggestions
- The system supports interactive exploration of attributes
- It demonstrates practical deployment skills

This mirrors how AI-powered fashion assistants operate in real e-commerce platforms.

---

## 8. Limitations

This phase intentionally does not include:

- Dialogue state tracking
- Multi-turn memory
- Personalization
- Recommendation ranking

The focus is on **clarity, correctness, and explainability**, not conversational complexity.

---

## 9. Outcome of Phase 7.2

At the end of this phase, the project includes:

- A fully functional chatbot demo
- Explainable attribute extraction
- Structured AI outputs suitable for UI integration
- A deployment-ready interface using Streamlit

This completes the transition from research prototype to applied NLP system.