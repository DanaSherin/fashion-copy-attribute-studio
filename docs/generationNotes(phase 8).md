## Objective

The objective of Phase 8 is to extend the hybrid fashion attribute extraction system with a controlled and explainable generative component. This phase demonstrates how structured NLP outputs can be consumed by a Large Language Model (LLM) to generate fashion-related text such as product copy and captions while preserving attribute grounding, stylistic control, explainability, and system modularity.

This phase does not replace or modify the extraction pipeline. All generation is strictly downstream of the canonical structured output defined in Phase 7.

---

## Position in the Overall Pipeline

Phase 8 operates after hybrid extraction and canonical output construction.

End-to-end pipeline flow:

1. Raw product description input  
2. Weak supervision and NER modeling (Phases 3–5)  
3. Hybrid rule–model correction (Phase 6)  
4. Canonical structured output (Phase 7.1)  
5. Attribute-conditioned controlled generation (Phase 8)

At no point does the generation module consume raw input text directly.

---

## Design Principles

The generative component is designed according to the following principles:

- Separation of concerns between extraction and generation  
- Attribute grounding for all generated text  
- Prompt-based control instead of learned generation logic  
- Explainability through explicit attribute usage  
- Replaceability of the LLM backend without system changes  

---

## Input Contract

The generation module accepts only the canonical structured output produced in Phase 7.1.

The input consists of the original text and a normalized set of extracted attributes such as product type, material, pattern, fit, and length.

Raw text alone is never used as input to the generation component.

---

## Generation Modes

The system supports multiple explicit generation modes, each serving a distinct purpose:

- SEO Description for search-optimized product copy  
- Social Media Caption for short marketing text  
- Brand Copy for brand-aligned promotional content  

Each mode is implemented through prompt constraints rather than learned behavior.

---

## Style Profiles

To ensure stylistic consistency and controllability, generation is conditioned on explicit style profiles.

Each style profile defines tone, preferred adjectives, forbidden vocabulary, sentence length preferences, and emoji usage rules.

Examples include luxury minimal, streetwear, modern casual, editorial fashion, and sustainable conscious.

Style profiles are external to the extraction pipeline and can be extended without retraining any models.

---

## Prompt Engineering Strategy

All generation is performed using deterministic prompt templates composed of:

- System role definition  
- Task specification  
- Explicit attribute listing  
- Style constraints  
- Forbidden vocabulary  
- Hard generation rules  

This structured prompt design ensures attribute coverage, style consistency, minimal hallucination, and reproducibility.

---

## Large Language Model Integration

Generation is performed using an external Large Language Model accessed via API.

No fine-tuning or weight updates are performed. The LLM is used purely as a language realizer rather than a reasoning engine.

All semantic control originates from structured inputs and prompt design, and the backend model is treated as a replaceable component.

---

## Output Structure

The generation module returns generated text along with metadata describing the generation mode, style profile, attributes used, and model identifier.

This structure preserves explainability and supports qualitative evaluation.

---

## Explainability and Control

Explainability is preserved through explicit attribute-to-text grounding, transparent prompt construction, and clear separation between extraction and generation.

The system never invents attributes or performs implicit inference.

---

## Limitations

Output quality depends on the completeness of extracted attributes. Style enforcement relies on prompt compliance, and subtle tone variation may occur across different LLM versions.

These limitations are inherent to prompt-based generation.

---

## Role of Phase 8 in the Overall Project

Phase 8 demonstrates how structured and explainable NLP outputs can safely enable downstream generative applications.

The core philosophy of the project is reinforced: attribute extraction is the primary contribution, and generation is a controlled extension.