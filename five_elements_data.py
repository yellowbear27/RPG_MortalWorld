# five_elements.py
# Five Elements with Bai Hu Tong canonical text and birth trigram mappings.
# Binary lines read bottom-up: 0 = Yin, 1 = Yang. 6‑digit doubled trigram.
#
# Source: Bai Hu Tong (白虎通·卷三·五行), Eastern Han, compiled by Ban Gu.

FIVE_ELEMENTS = {
    "火": {
        "name_en": "Fire",
        "baihutong_zh": "火者，陽也，尊，故上。火之為言化也，陽氣用事，萬物變化也。",
        "trigrams": [
            {
                "binary": "101101",
                "name_zh": "離",
                "name_en": "Fire / Clinging",
                "element_aspect": "陰火 (Yin Fire)"
            }
        ]
    },
    "水": {
        "name_en": "Water",
        "baihutong_zh": "水者，陰也，卑，故下。水之為言準也，養物平均，有準則也。",
        "trigrams": [
            {
                "binary": "010010",
                "name_zh": "坎",
                "name_en": "Water / Abyss",
                "element_aspect": "陽水 (Yang Water)"
            }
        ]
    },
    "木": {
        "name_en": "Wood",
        "baihutong_zh": "木者，少陽，有中和之性，故可曲直。木之為言觸也，陽氣動躍，觸地而出也。",
        "trigrams": [
            {
                "binary": "100100",
                "name_zh": "震",
                "name_en": "Thunder",
                "element_aspect": "陽木 (Yang Wood)"
            },
            {
                "binary": "011011",
                "name_zh": "巽",
                "name_en": "Wind",
                "element_aspect": "陰木 (Yin Wood)"
            }
        ]
    },
    "金": {
        "name_en": "Metal",
        "baihutong_zh": "金者，少陰，有中和之性，故可從革。金之為言禁也。西方者，陰始起，萬物禁止。",
        "trigrams": [
            {
                "binary": "111111",
                "name_zh": "乾",
                "name_en": "Heaven",
                "element_aspect": "陽金 (Yang Metal)"
            },
            {
                "binary": "110110",
                "name_zh": "兌",
                "name_en": "Lake",
                "element_aspect": "陰金 (Yin Metal)"
            }
        ]
    },
    "土": {
        "name_en": "Earth",
        "baihutong_zh": "土者最大，苞含物，將生者出者，將歸者，不嫌清濁為萬物。土之為言吐也。",
        "trigrams": [
            {
                "binary": "001001",
                "name_zh": "艮",
                "name_en": "Mountain",
                "element_aspect": "陽土 (Yang Earth)"
            },
            {
                "binary": "000000",
                "name_zh": "坤",
                "name_en": "Earth",
                "element_aspect": "陰土 (Yin Earth)"
            }
        ]
    }
}

