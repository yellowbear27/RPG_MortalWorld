# fate.py
# Rolls a random birth element and trigram.
# Imports data from five_elements_data.py and bagua_data.py.
# Returns a clean bundle for the prompt.

import random
from five_elements_data import FIVE_ELEMENTS
from bagua_data import TRIGRAMS


def roll_fate():
    """
    Randomly selects a Five Element, then a trigram from that element.
    Returns a dict with all required texts for the AI prompt.
    """
    # 1. Pick a random element
    element_key = random.choice(list(FIVE_ELEMENTS.keys()))
    element_data = FIVE_ELEMENTS[element_key]

    # 2. Pick a random trigram from that element
    trigram = random.choice(element_data["trigrams"])

    # 3. Get the Shuogua text from bagua_data
    full_trigram = TRIGRAMS[trigram["binary"]]

    # 4. Return the combined canonical texts
    return {
        "element": element_key,                    # e.g. "火"
        "element_en": element_data["name_en"],     # "Fire"
        "baihutong_zh": element_data["baihutong_zh"],
        "trigram_name_zh": full_trigram["name_zh"],
        "trigram_name_en": full_trigram["name_en"],
        "element_aspect": trigram["element_aspect"], # e.g. "陰火"
        "shuogua_zh": full_trigram["shuogua_zh"],
        "binary": trigram["binary"],               # 6‑bit string
    }
