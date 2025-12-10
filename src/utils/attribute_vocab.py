"""
Fashion attribute vocabularies and NER label schema.

This file defines:
- Canonical vocabularies for each attribute (colors, materials, etc.)
- Simple synonym maps for normalization
- The list of NER labels used for sequence tagging
"""

# -----------------------------
# Canonical vocabularies
# -----------------------------

GENDER = [
    "women",
    "men",
    "unisex",
    "girls",
    "boys",
]

# High-level categories (you can expand later)
CATEGORY_TOP = [
    "clothing",
    "shoes",
    "bags",
    "accessories",
]

# More specific product categories (partial list, expand as needed)
CATEGORY_SUB = [
    "t-shirt",
    "shirt",
    "blouse",
    "top",
    "dress",
    "skirt",
    "jeans",
    "trousers",
    "pants",
    "shorts",
    "jumpsuit",
    "playsuit",
    "jacket",
    "coat",
    "blazer",
    "hoodie",
    "sweatshirt",
    "sweater",
    "cardigan",
    "sneakers",
    "boots",
    "sandals",
    "heels",
    "loafers",
    "flats",
    "bag",
    "tote",
    "backpack",
    "shoulder bag",
    "crossbody bag",
    "clutch",
]

COLOR = [
    "black",
    "white",
    "grey",
    "red",
    "pink",
    "orange",
    "yellow",
    "green",
    "blue",
    "navy",
    "purple",
    "brown",
    "beige",
    "cream",
    "silver",
    "gold",
    "metallic",
    "multicolor",
]

MATERIAL = [
    "cotton",
    "denim",
    "linen",
    "wool",
    "cashmere",
    "silk",
    "satin",
    "leather",
    "faux leather",
    "suede",
    "polyester",
    "viscose",
    "nylon",
    "acrylic",
    "velvet",
    "lace",
    "jersey",
    "knit",
    "chiffon",
]

PATTERN = [
    "solid",
    "striped",
    "checked",
    "plaid",
    "floral",
    "polka dot",
    "animal print",
    "logo print",
    "graphic",
    "geometric",
    "abstract",
]

FIT = [
    "slim",
    "regular",
    "relaxed",
    "oversized",
    "skinny",
    "wide-leg",
    "straight",
    "tapered",
    "fitted",
    "a-line",
]

LENGTH = [
    "cropped",
    "mini",
    "midi",
    "maxi",
    "ankle-length",
    "knee-length",
    "full-length",
    "hip-length",
    "waist-length",
    "floor-length",
]

SLEEVE = [
    "sleeveless",
    "short-sleeve",
    "3/4-sleeve",
    "long-sleeve",
    "cap sleeve",
    "strapless",
    "one-shoulder",
]

NECKLINE = [
    "crew neck",
    "round neck",
    "v-neck",
    "deep v-neck",
    "turtleneck",
    "halter",
    "off-shoulder",
    "square neck",
    "boat neck",
    "sweetheart",
    "collared",
]

OCCASION = [
    "casual",
    "work",
    "office",
    "evening",
    "party",
    "wedding",
    "streetwear",
    "sports",
    "loungewear",
    "vacation",
]

STYLE = [
    "minimal",
    "classic",
    "sporty",
    "streetwear",
    "boho",
    "romantic",
    "edgy",
    "preppy",
    "elegant",
]

DETAIL = [
    "buttons",
    "zipper",
    "lace trim",
    "ruffles",
    "fringe",
    "embroidery",
    "sequins",
    "belted",
    "cut-out",
    "pleated",
    "studs",
    "buckles",
]

CLOSURE = [
    "zip",
    "button",
    "snap",
    "lace-up",
    "slip-on",
    "hook-and-eye",
    "buckle",
]

# -----------------------------
# Synonym maps for normalization
# (raw text -> canonical value)
# -----------------------------

COLOR_SYNONYMS = {
    "navy blue": "navy",
    "dark blue": "navy",
    "light blue": "blue",
    "off white": "white",
    "off-white": "white",
    "ivory": "cream",
    "ecru": "beige",
    "burgundy": "red",
    "wine": "red",
    "camel": "brown",
    "charcoal": "grey",
    "multi": "multicolor",
    "multicolour": "multicolor",
}

MATERIAL_SYNONYMS = {
    "100% cotton": "cotton",
    "pure cotton": "cotton",
    "denim jeans": "denim",
    "genuine leather": "leather",
    "faux-leather": "faux leather",
    "fake leather": "faux leather",
    "poly": "polyester",
    "polyamide": "nylon",
    "viscose blend": "viscose",
    "wool blend": "wool",
}

PATTERN_SYNONYMS = {
    "animal-print": "animal print",
    "logo-print": "logo print",
    "graphic print": "graphic",
    "printed": "graphic",
    "plain": "solid",
}

FIT_SYNONYMS = {
    "relaxed fit": "relaxed",
    "regular fit": "regular",
    "slim-fit": "slim",
    "skinny fit": "skinny",
    "oversize": "oversized",
}

LENGTH_SYNONYMS = {
    "ankle length": "ankle-length",
    "knee length": "knee-length",
    "full length": "full-length",
    "floor length": "floor-length",
    "cropped length": "cropped",
}

SLEEVE_SYNONYMS = {
    "short sleeve": "short-sleeve",
    "long sleeve": "long-sleeve",
    "3/4 sleeve": "3/4-sleeve",
}

NECKLINE_SYNONYMS = {
    "crewneck": "crew neck",
    "round-neck": "round neck",
    "v neck": "v-neck",
    "deep v neck": "deep v-neck",
    "roll neck": "turtleneck",
    "polo collar": "collared",
}

OCCASION_SYNONYMS = {
    "office wear": "office",
    "workwear": "work",
    "evening wear": "evening",
    "partywear": "party",
    "casualwear": "casual",
    "lounge": "loungewear",
    "vacation wear": "vacation",
}

# Group all synonym maps together for convenience
SYNONYM_MAPS = {
    "color": COLOR_SYNONYMS,
    "material": MATERIAL_SYNONYMS,
    "pattern": PATTERN_SYNONYMS,
    "fit": FIT_SYNONYMS,
    "length": LENGTH_SYNONYMS,
    "sleeve": SLEEVE_SYNONYMS,
    "neckline": NECKLINE_SYNONYMS,
    "occasion": OCCASION_SYNONYMS,
}

# -----------------------------
# NER label schema
# -----------------------------

# Which attributes will appear as NER tags in the text
ATTRIBUTES_FOR_NER = [
    "GENDER",
    "CATEGORY",
    "COLOR",
    "MATERIAL",
    "PATTERN",
    "FIT",
    "LENGTH",
    "NECKLINE",
    "SLEEVE",
    "OCCASION",
    "STYLE",
    "DETAIL",
]

# Build BIO labels automatically: B-ATTR, I-ATTR + "O"
NER_LABELS = ["O"]
for attr in ATTRIBUTES_FOR_NER:
    NER_LABELS.append(f"B-{attr}")
    NER_LABELS.append(f"I-{attr}")

# Mapping helpers (for the model config)
LABEL2ID = {label: i for i, label in enumerate(NER_LABELS)}
ID2LABEL = {i: label for label, i in LABEL2ID.items()}