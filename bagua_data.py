# bagua_data.py
# Eight Trigrams (八卦) as birth fates, with Shuogua attributes.
# Binary lines read bottom-up: 0 = Yin, 1 = Yang.
# The 6‑digit binary is the doubled trigram (e.g., Li = 101 repeated).
#
# Source: Shuogua (說卦傳), from the received Zhouyi.

TRIGRAMS = {
    "111111": {
        "name_zh": "乾",
        "name_en": "Heaven",
        "element": "金",
        "element_aspect": "陽金 (Yang Metal)",
        "shuogua_zh": "乾爲天，爲圜，爲君，爲父，爲玉，爲金，爲寒，爲冰，爲大赤，爲良馬，爲老馬，爲瘠馬，爲駁馬，爲木果。"
    },
    "000000": {
        "name_zh": "坤",
        "name_en": "Earth",
        "element": "土",
        "element_aspect": "陰土 (Yin Earth)",
        "shuogua_zh": "坤爲地，爲母，爲布，爲釜，爲吝嗇，爲均，爲子母牛，爲大輿，爲文，爲衆，爲柄。其於地也，爲黑。"
    },
    "100100": {
        "name_zh": "震",
        "name_en": "Thunder",
        "element": "木",
        "element_aspect": "陽木 (Yang Wood)",
        "shuogua_zh": "震爲雷，爲龍，爲玄黃，爲旉，爲大塗，爲長子，爲決躁，爲蒼筤竹，爲萑葦。其於馬也，爲善鳴，爲馵足，爲作足，爲的顙。其於稼也，爲反生。其究爲健，爲蕃鮮。"
    },
    "011011": {
        "name_zh": "巽",
        "name_en": "Wind",
        "element": "木",
        "element_aspect": "陰木 (Yin Wood)",
        "shuogua_zh": "巽爲木，爲風，爲長女，爲繩直，爲工，爲白，爲長，爲高，爲進退，爲不果，爲臭。其於人也，爲寡髮，爲廣顙，爲多白眼，爲近利市三倍。其究爲躁卦。"
    },
    "010010": {
        "name_zh": "坎",
        "name_en": "Water",
        "element": "水",
        "element_aspect": "陽水 (Yang Water)",
        "shuogua_zh": "坎爲水，爲溝瀆，爲隱伏，爲矯輮，爲弓輪。其於人也，爲加憂，爲心病，爲耳痛，爲血卦，爲赤。其於馬也，爲美脊，爲亟心，爲下首，爲薄蹄，爲曳。其於輿也，爲多眚，爲通，爲月，爲盜。其於木也，爲堅多心。"
    },
    "101101": {
        "name_zh": "離",
        "name_en": "Fire",
        "element": "火",
        "element_aspect": "陰火 (Yin Fire)",
        "shuogua_zh": "離爲火，爲日，爲電，爲中女，爲甲胄，爲戈兵。其於人也，爲大腹，爲乾卦，爲鱉，爲蟹，爲蠃，爲蚌，爲龜。其於木也，爲科上槁。"
    },
    "001001": {
        "name_zh": "艮",
        "name_en": "Mountain",
        "element": "土",
        "element_aspect": "陽土 (Yang Earth)",
        "shuogua_zh": "艮爲山，爲徑路，爲小石，爲門闕，爲果蓏，爲閽寺，爲指，爲狗，爲鼠，爲黔喙之屬。其於木也，爲堅多節。"
    },
    "110110": {
        "name_zh": "兌",
        "name_en": "Lake",
        "element": "金",
        "element_aspect": "陰金 (Yin Metal)",
        "shuogua_zh": "兌爲澤，爲少女，爲巫，爲口舌，爲毁折，爲附决。其於地也，爲剛鹵，爲妾，爲羊。"
    }
}
