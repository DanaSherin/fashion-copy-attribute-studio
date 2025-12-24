## 1. Purpose of This Phase

The purpose of Phase 3.1 is to define the attribute schema used for Named Entity Recognition (NER) in this project.

This schema specifies what information the system is designed to extract from text, based strictly on empirical observations from the dataset explored in Phase 2.

No annotation rules or modeling decisions are made in this phase.

---

## 2. Schema Design Principles

The attribute schema was designed according to the following principles:

- Data-driven: attributes are derived from patterns observed in `shortDescription`
- Text-only: only attributes explicitly present in text are included
- Phrase-level: multi-word expressions are treated as single entities
- Minimal but expressive: only high-signal attributes are included
- NER-suitable: each attribute can be localized to a text span

This avoids over-engineering and ensures annotation feasibility.

---

## 3. Scope of the Schema

### Included

- Attributes that frequently appear as words or phrases in product descriptions
- Attributes that are clearly separable at the token level

### Excluded

- Attributes only present in metadata (e.g., price, stock)
- Attributes requiring visual inference (e.g., colors from images)
- Attributes not reliably or consistently present in the dataset text

---

## 4. Final Attribute Set

Based on the dataset analysis, six attributes are included in the schema.

---

### 4.1 PRODUCT_TYPE

**Definition:**  
The core category describing what the product is.

**Examples from the dataset:**
- dress
- bag
- sneakers
- jacket
- trousers
- sunglasses

**Notes:**
- Exactly one PRODUCT_TYPE is expected per description
- Multi-word product types are treated as a single entity (e.g., shoulder bag)

---

### 4.2 PATTERN

**Definition:**  
Surface design or print-related descriptors.

**Examples from the dataset:**
- logo print
- floral print
- leopard print
- graphic print

**Notes:**
- Pattern terms frequently appear as multi-word phrases
- All tokens in the phrase belong to the same entity

---

### 4.3 FIT / SHAPE

**Definition:**  
Descriptors related to garment fit or silhouette.

**Examples from the dataset:**
- oversized
- skinny
- slim
- cropped

**Notes:**
- Only explicit fit-related terms are included
- Fit descriptors are distinct from length descriptors

---

### 4.4 LENGTH

**Definition:**  
Descriptors related to garment length.

**Examples from the dataset:**
- mini
- midi
- maxi
- cropped

**Notes:**
- Length terms frequently co-occur with product types (e.g., midi dress)
- Treated as separate from fit attributes

---

### 4.5 MATERIAL

**Definition:**  
Explicit mentions of fabric or material composition.

**Examples from the dataset:**
- leather
- denim
- knit
- silk

**Notes:**
- Only materials explicitly mentioned in text are included
- Implicit or inferred materials are excluded

---

### 4.6 BRAND

**Definition:**  
Brand names explicitly mentioned in the product description text.

**Examples from the dataset:**
- Gucci
- Fendi
- Valentino Garavani

**Notes:**
- Brand metadata is not used for labeling
- Brand entities support interpretability and conversational responses

---

## 5. Attribute Relationships

Multiple attributes may appear in a single description, and attributes do not overlap in token spans.

**Example description:**  
logo print midi dress

**Attribute interpretation:**
- logo print → PATTERN  
- midi → LENGTH  
- dress → PRODUCT_TYPE  

---

## 6. Justification for Schema Size

The schema is intentionally limited to six attributes in order to:

- Reduce annotation noise
- Improve label consistency
- Enable reliable weak supervision
- Support clear chatbot explanations

Adding more attributes without strong textual evidence would reduce extraction quality and increase ambiguity.

---

## 7. Role of This Schema in the Pipeline

This attribute schema serves as:

- The foundation for annotation guidelines (Phase 3.2)
- The target label set for weak supervision (Phase 4)
- The output structure for the chatbot demo (Phase 7)

No extraction logic is implemented at this stage.

---

## 8. Transition to Next Phase

With the attribute schema finalized, the project proceeds to Phase 3.2: annotation guidelines and BIO tagging rules.

This ensures that how attributes are labeled is fully aligned with what attributes exist.
The final attribute set was refined after exploratory data analysis and frequency-based pattern discovery.