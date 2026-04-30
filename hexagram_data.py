# hexagram_data.py
# I Ching hexagrams in Shao Yong (Fu Xi) binary order.
# Lines read bottom-up: 0 = Yin, 1 = Yang.
# Keys are 6-character strings from "000000" to "111111".
# name_zh  : single-character Chinese hexagram name
# name_en  : conventional English translation (not sent to the AI)
# judgment_zh : King Wen's 卦辞 in Classical Chinese

HEXAGRAMS = {
    # ----- 000000 – 001111 -----
    "000000": {
        "name_zh": "坤",
        "name_en": "The Receptive",
        "judgment_zh": "坤，元亨，利牝馬之貞。君子有攸往，先迷後得主，利。西南得朋，東北喪朋。安貞吉。",
    },
    "000001": {
        "name_zh": "剝",
        "name_en": "Splitting Apart",
        "judgment_zh": "剝，不利有攸往。",
    },
    "000010": {
        "name_zh": "比",
        "name_en": "Holding Together",
        "judgment_zh": "比，吉。原筮，元永貞，无咎。不寧方來，後夫凶。",
    },
    "000011": {
        "name_zh": "觀",
        "name_en": "Contemplation",
        "judgment_zh": "觀，盥而不薦，有孚顒若。",
    },
    "000100": {
        "name_zh": "豫",
        "name_en": "Enthusiasm",
        "judgment_zh": "豫，利建侯行師。",
    },
    "000101": {
        "name_zh": "晉",
        "name_en": "Progress",
        "judgment_zh": "晉，康侯用錫馬蕃庶，晝日三接。",
    },
    "000110": {
        "name_zh": "萃",
        "name_en": "Gathering Together",
        "judgment_zh": "萃，亨。王假有廟，利見大人，亨，利貞。用大牲吉，利有攸往。",
    },
    "000111": {
        "name_zh": "否",
        "name_en": "Standstill",
        "judgment_zh": "否之匪人，不利君子貞。大往小來。",
    },
    # ----- 001000 – 001111 -----
    "001000": {
        "name_zh": "謙",
        "name_en": "Modesty",
        "judgment_zh": "謙，亨，君子有終。",
    },
    "001001": {
        "name_zh": "艮",
        "name_en": "Keeping Still",
        "judgment_zh": "艮其背，不獲其身，行其庭，不見其人，无咎。",
    },
    "001010": {
        "name_zh": "蹇",
        "name_en": "Obstruction",
        "judgment_zh": "蹇，利西南，不利東北，利見大人，貞吉。",
    },
    "001011": {
        "name_zh": "漸",
        "name_en": "Development",
        "judgment_zh": "漸，女歸吉，利貞。",
    },
    "001100": {
        "name_zh": "小過",
        "name_en": "Preponderance of the Small",
        "judgment_zh": "小過，亨，利貞。可小事，不可大事。飛鳥遺之音，不宜上，宜下，大吉。",
    },
    "001101": {
        "name_zh": "旅",
        "name_en": "The Wanderer",
        "judgment_zh": "旅，小亨，旅貞吉。",
    },
    "001110": {
        "name_zh": "咸",
        "name_en": "Influence",
        "judgment_zh": "咸，亨，利貞，取女吉。",
    },
    "001111": {
        "name_zh": "遯",
        "name_en": "Retreat",
        "judgment_zh": "遯，亨，小利貞。",
    },
    # ----- 010000 – 010111 -----
    "010000": {
        "name_zh": "師",
        "name_en": "The Army",
        "judgment_zh": "師，貞，丈人吉，无咎。",
    },
    "010001": {
        "name_zh": "蒙",
        "name_en": "Youthful Folly",
        "judgment_zh": "蒙，亨。匪我求童蒙，童蒙求我。初筮告，再三瀆，瀆則不告。利貞。",
    },
    "010010": {
        "name_zh": "坎",
        "name_en": "The Abysmal",
        "judgment_zh": "習坎，有孚，維心亨，行有尚。",
    },
    "010011": {
        "name_zh": "渙",
        "name_en": "Dispersion",
        "judgment_zh": "渙，亨。王假有廟，利涉大川，利貞。",
    },
    "010100": {
        "name_zh": "解",
        "name_en": "Deliverance",
        "judgment_zh": "解，利西南，无所往，其來復吉。有攸往，夙吉。",
    },
    "010101": {
        "name_zh": "未濟",
        "name_en": "Before Completion",
        "judgment_zh": "未濟，亨，小狐汔濟，濡其尾，无攸利。",
    },
    "010110": {
        "name_zh": "困",
        "name_en": "Oppression",
        "judgment_zh": "困，亨，貞，大人吉，无咎，有言不信。",
    },
    "010111": {
        "name_zh": "訟",
        "name_en": "Conflict",
        "judgment_zh": "訟，有孚，窒惕，中吉，終凶。利見大人，不利涉大川。",
    },
    # ----- 011000 – 011111 -----
    "011000": {
        "name_zh": "升",
        "name_en": "Pushing Upward",
        "judgment_zh": "升，元亨，用見大人，勿恤，南征吉。",
    },
    "011001": {
        "name_zh": "蠱",
        "name_en": "Decay",
        "judgment_zh": "蠱，元亨，利涉大川。先甲三日，後甲三日。",
    },
    "011010": {
        "name_zh": "井",
        "name_en": "The Well",
        "judgment_zh": "井，改邑不改井，无喪无得，往來井井。汔至，亦未繘井，羸其瓶，凶。",
    },
    "011011": {
        "name_zh": "巽",
        "name_en": "The Gentle",
        "judgment_zh": "巽，小亨，利有攸往，利見大人。",
    },
    "011100": {
        "name_zh": "恆",
        "name_en": "Duration",
        "judgment_zh": "恆，亨，无咎，利貞，利有攸往。",
    },
    "011101": {
        "name_zh": "鼎",
        "name_en": "The Cauldron",
        "judgment_zh": "鼎，元吉，亨。",
    },
    "011110": {
        "name_zh": "大過",
        "name_en": "Preponderance of the Great",
        "judgment_zh": "大過，棟橈，利有攸往，亨。",
    },
    "011111": {
        "name_zh": "姤",
        "name_en": "Coming to Meet",
        "judgment_zh": "姤，女壯，勿用取女。",
    },
    # ----- 100000 – 101111 -----
    "100000": {
        "name_zh": "復",
        "name_en": "Return",
        "judgment_zh": "復，亨。出入无疾，朋來无咎。反復其道，七日來復，利有攸往。",
    },
    "100001": {
        "name_zh": "頤",
        "name_en": "Nourishment",
        "judgment_zh": "頤，貞吉。觀頤，自求口實。",
    },
    "100010": {
        "name_zh": "屯",
        "name_en": "Difficulty at the Beginning",
        "judgment_zh": "屯，元亨利貞。勿用有攸往，利建侯。",
    },
    "100011": {
        "name_zh": "益",
        "name_en": "Increase",
        "judgment_zh": "益，利有攸往，利涉大川。",
    },
    "100100": {
        "name_zh": "震",
        "name_en": "The Arousing",
        "judgment_zh": "震，亨。震來虩虩，笑言啞啞。震驚百里，不喪匕鬯。",
    },
    "100101": {
        "name_zh": "噬嗑",
        "name_en": "Biting Through",
        "judgment_zh": "噬嗑，亨，利用獄。",
    },
    "100110": {
        "name_zh": "隨",
        "name_en": "Following",
        "judgment_zh": "隨，元亨利貞，无咎。",
    },
    "100111": {
        "name_zh": "無妄",
        "name_en": "Innocence",
        "judgment_zh": "無妄，元亨利貞。其匪正有眚，不利有攸往。",
    },
    # ----- 101000 – 101111 -----
    "101000": {
        "name_zh": "明夷",
        "name_en": "Darkening of the Light",
        "judgment_zh": "明夷，利艱貞。",
    },
    "101001": {
        "name_zh": "賁",
        "name_en": "Grace",
        "judgment_zh": "賁，亨。小利有攸往。",
    },
    "101010": {
        "name_zh": "既濟",
        "name_en": "After Completion",
        "judgment_zh": "既濟，亨小，利貞。初吉終亂。",
    },
    "101011": {
        "name_zh": "家人",
        "name_en": "The Family",
        "judgment_zh": "家人，利女貞。",
    },
    "101100": {
        "name_zh": "豐",
        "name_en": "Abundance",
        "judgment_zh": "豐，亨，王假之，勿憂，宜日中。",
    },
    "101101": {
        "name_zh": "離",
        "name_en": "The Clinging",
        "judgment_zh": "離，利貞，亨。畜牝牛，吉。",
    },
    "101110": {
        "name_zh": "革",
        "name_en": "Revolution",
        "judgment_zh": "革，巳日乃孚，元亨利貞，悔亡。",
    },
    "101111": {
        "name_zh": "同人",
        "name_en": "Fellowship with Men",
        "judgment_zh": "同人于野，亨。利涉大川，利君子貞。",
    },
    # ----- 110000 – 111111 -----
    "110000": {
        "name_zh": "臨",
        "name_en": "Approach",
        "judgment_zh": "臨，元亨利貞。至于八月有凶。",
    },
    "110001": {
        "name_zh": "損",
        "name_en": "Decrease",
        "judgment_zh": "損，有孚，元吉，无咎，可貞，利有攸往。曷之用，二簋可用享。",
    },
    "110010": {
        "name_zh": "節",
        "name_en": "Limitation",
        "judgment_zh": "節，亨。苦節不可貞。",
    },
    "110011": {
        "name_zh": "中孚",
        "name_en": "Inner Truth",
        "judgment_zh": "中孚，豚魚吉，利涉大川，利貞。",
    },
    "110100": {
        "name_zh": "歸妹",
        "name_en": "The Marrying Maiden",
        "judgment_zh": "歸妹，征凶，无攸利。",
    },
    "110101": {
        "name_zh": "睽",
        "name_en": "Opposition",
        "judgment_zh": "睽，小事吉。",
    },
    "110110": {
        "name_zh": "兌",
        "name_en": "The Joyous",
        "judgment_zh": "兌，亨，利貞。",
    },
    "110111": {
        "name_zh": "履",
        "name_en": "Treading",
        "judgment_zh": "履虎尾，不咥人，亨。",
    },
    # ----- 111000 – 111111 -----
    "111000": {
        "name_zh": "泰",
        "name_en": "Peace",
        "judgment_zh": "泰，小往大來，吉亨。",
    },
    "111001": {
        "name_zh": "大畜",
        "name_en": "The Taming Power of the Great",
        "judgment_zh": "大畜，利貞，不家食吉，利涉大川。",
    },
    "111010": {
        "name_zh": "需",
        "name_en": "Waiting",
        "judgment_zh": "需，有孚，光亨，貞吉。利涉大川。",
    },
    "111011": {
        "name_zh": "小畜",
        "name_en": "The Taming Power of the Small",
        "judgment_zh": "小畜，亨。密雲不雨，自我西郊。",
    },
    "111100": {
        "name_zh": "大壯",
        "name_en": "The Power of the Great",
        "judgment_zh": "大壯，利貞。",
    },
    "111101": {
        "name_zh": "大有",
        "name_en": "Possession in Great Measure",
        "judgment_zh": "大有，元亨。",
    },
    "111110": {
        "name_zh": "夬",
        "name_en": "Breakthrough",
        "judgment_zh": "夬，揚于王庭，孚號有厲，告自邑，不利即戎，利有攸往。",
    },
    "111111": {
        "name_zh": "乾",
        "name_en": "The Creative",
        "judgment_zh": "乾，元亨利貞。",
    },
}
