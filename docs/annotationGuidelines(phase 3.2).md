## 1. Purpose of This Phase

The purpose of Phase 3.2 is to define **how product descriptions are annotated** using the BIO tagging scheme based on the attribute schema defined in Phase 3.1.

This phase establishes clear and consistent rules for labeling text, ensuring reproducibility and alignment before any automated labeling or model training is performed.

No modeling or weak supervision logic is implemented in this phase.

---

## 2. BIO Tagging Scheme

This project uses the standard **BIO (Begin–Inside–Outside)** tagging format:

- **B-ATTRIBUTE**: the first token of an attribute entity
- **I-ATTRIBUTE**: subsequent tokens belonging to the same entity
- **O**: tokens that are not part of any attribute

The BIO scheme allows precise identification of multi-word attributes within short text spans.

---

## 3. General Annotation Rules

The following rules apply to all annotations:

- Attributes must align with exact token boundaries
- Multi-word attributes are labeled as a single entity span
- Attributes must not overlap
- Only attributes explicitly present in text are labeled
- Tokens not belonging to any attribute are labeled as `O`

---

## 4. Attribute-Specific Annotation Rules

Annotations follow the attribute schema defined in Phase 3.1.

---

### 4.1 PRODUCT_TYPE

**Definition:**  
The main noun phrase describing what the product is.

**Annotation rules:**
- Exactly one PRODUCT_TYPE is labeled per description
- The most specific product term is selected
- Multi-word product types are labeled as one entity

**Examples:**
- shoulder bag
- midi dress
- ankle boots

---

### 4.2 PATTERN

**Definition:**  
Surface design or print-related descriptors.

**Annotation rules:**
- All tokens forming the pattern phrase are labeled
- Pattern terms often appear as bigrams
- Generic descriptive words not tied to a pattern are excluded

**Examples:**
- logo print
- floral print
- leopard print

---

### 4.3 FIT / SHAPE

**Definition:**  
Descriptors related to garment fit or silhouette.

**Annotation rules:**
- Only explicit fit-related terms are labeled
- Fit descriptors are distinct from length descriptors
- Single-token attributes are common

**Examples:**
- oversized
- skinny
- slim

---

### 4.4 LENGTH

**Definition:**  
Descriptors related to garment length.

**Annotation rules:**
- Length terms are labeled independently of product type
- Overlapping with FIT is avoided
- Cropped is labeled as LENGTH, not FIT

**Examples:**
- mini
- midi
- maxi
- cropped

---

### 4.5 MATERIAL

**Definition:**  
Explicit mentions of fabric or material composition.

**Annotation rules:**
- Only materials explicitly stated in text are labeled
- Multi-word materials are labeled as a single entity
- Implied materials are not labeled

**Examples:**
- leather
- denim
- knit
- silk

---

### 4.6 BRAND

**Definition:**  
Brand names explicitly mentioned in the description text.

**Annotation rules:**
- Brand metadata is not used for labeling
- Multi-word brand names are labeled as one entity
- Capitalization is ignored

**Examples:**
- Gucci
- Fendi
- Valentino Garavani

---

## 5. Handling Multi-Attribute Descriptions

Multiple attributes may appear in a single description.

**Example description:**  
logo print midi dress

**Annotation breakdown:**
- logo print → B-PATTERN I-PATTERN
- midi → B-LENGTH
- dress → B-PRODUCT_TYPE

---

## 6. Edge Cases and Special Considerations

### 6.1 Brand Names Embedded in Product Names

Brand names that appear as part of a longer product name are labeled only for the brand span.

Example:  
Valentino Garavani Open sneakers

- Valentino Garavani → BRAND
- sneakers → PRODUCT_TYPE

---

### 6.2 Overlapping Attribute Candidates

If a token could plausibly belong to multiple attributes, the label is chosen based on semantic role:

- Fit and length are treated as separate attributes
- Cropped is labeled as LENGTH, not FIT

---

### 6.3 Non-Informative Tokens

Words such as:
- style
- design
- collection

are labeled as `O` and excluded from annotation.

---

### 6.4 Pricing, Stock, and Metadata

Numbers, prices, and stock-related terms are never annotated, even if present in the text.

---

## 7. Fully Labeled Examples

### Example 1

**Text:**  
Gucci logo print tote bag

**Token-level labels:**
- Gucci → B-BRAND
- logo → B-PATTERN
- print → I-PATTERN
- tote → B-PRODUCT_TYPE
- bag → I-PRODUCT_TYPE

---

### Example 2

**Text:**  
oversized leather jacket

**Token-level labels:**
- oversized → B-FIT
- leather → B-MATERIAL
- jacket → B-PRODUCT_TYPE

---

### Example 3

**Text:**  
unisex floral midi dress

**Token-level labels:**
- unisex → O
- floral → B-PATTERN
- midi → B-LENGTH
- dress → B-PRODUCT_TYPE

---

## 8. Annotation Consistency and Quality

To ensure consistent annotations:

- The same phrase should always receive the same label
- Ambiguous cases should be resolved conservatively
- Annotation decisions must adhere strictly to the schema

This consistency is critical for effective weak supervision and model training.

---

## 9. Role of These Guidelines in the Pipeline

These annotation guidelines serve as:

- The operational interpretation of the attribute schema
- The reference for automatic label generation (Phase 4)
- The basis for evaluating labeling quality

No automated labeling occurs until these rules are finalized.

---

## 10. Transition to Next Phase

With annotation guidelines established, the project proceeds to:

- **Phase 4:** Weakly supervised label generation

This phase will convert raw product descriptions into labeled training data.
