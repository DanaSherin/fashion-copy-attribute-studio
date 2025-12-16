"""
Reference vocabularies and normalization helpers for fashion attributes.

This file provides:
- Canonical vocabularies (colors, materials, patterns, etc.)
- Synonym maps for normalization and post-processing

NOTE:
This file does NOT define the active NER label schema.
The NER schema is intentionally limited and defined separately
according to Phase 3 (Schema & Annotation Strategy).
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
