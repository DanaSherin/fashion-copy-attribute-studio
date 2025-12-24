## 1. Objective

The objective of this phase is to define a canonical, explainable output schema for the
hybrid fashion attribute extraction system.

This schema serves as the contract between:
- The hybrid extraction engine
- The chatbot interface
- Downstream applications such as title generation

No new modeling or extraction logic is introduced in this phase.

---

## 2. Design Principles

The output schema was designed according to the following principles:

- **Explainability:** Every extracted attribute must be traceable
- **Consistency:** All system outputs follow the same structure
- **Minimalism:** Only information required for demonstration and reasoning is included
- **Extensibility:** The schema can support future attributes without breaking compatibility

---

## 3. High-Level Structure

The hybrid system outputs a single structured object per input description.

At a high level, the output contains:
- The original input text
- A dictionary of extracted attributes
- A generated product title derived from those attributes

---

## 4. Canonical Output Schema

```json
{
  "input_text": "<original product description>",

  "attributes": {
    "<ATTRIBUTE_NAME>": {
      "value": "<normalized attribute value>",
      "source": "<rule | model | hybrid>",
      "confidence": "<high | medium>",
      "evidence": "<text span supporting extraction>"
    }
  },

  "generated_title": "<generated product title>"
}

## 5. Output example for phase 7
```json
{
  "input_text": "oversized leather logo print midi dress",

  "attributes": {
    "PRODUCT_TYPE": {
      "value": "dress",
      "source": "hybrid",
      "confidence": "high",
      "evidence": "midi dress"
    },
    "MATERIAL": {
      "value": "leather",
      "source": "rule",
      "confidence": "high",
      "evidence": "leather"
    },
    "PATTERN": {
      "value": "logo print",
      "source": "hybrid",
      "confidence": "high",
      "evidence": "logo print"
    },
    "FIT": {
      "value": "oversized",
      "source": "hybrid",
      "confidence": "medium",
      "evidence": "oversized"
    },
    "LENGTH": {
      "value": "midi",
      "source": "rule",
      "confidence": "high",
      "evidence": "midi"
    }
  },

  "generated_title": "Oversized Leather Logo Print Midi Dress"
}
