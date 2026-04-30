# RPG MortalWorld

Generate mortal life chronicles in a xianxia world. One life per invocation. A birth condition, a user-defined turning point, and a hidden death — shaped by an authentic I Ching birth fate. No game loop yet. The chronicle is the artefact.

---

## Roadmap

| Version | Status       | What                                          |
|---------|--------------|-----------------------------------------------|
| V0      | Shipped      | Proof-of-concept: `--start`, `--end`, `--event1` → 300–400 word chronicle via local Ollama |
| V1.0    | Current      | Birth Fate engine. Hidden death. Classical Chinese canonical texts injected into prompt. 500–800 word chronicle. |
| V2      | Planned      | Interview layer. Speak with the dead character after the chronicle is generated. |
| V3      | Planned      | Intergenerational karma. One chronicle's death seeds the next. Parent hexagram → child trigram. |
| V4+     | Planned      | Parallel bloodlines. Autonomous agents living simultaneous lives. Player reads chronicles after elapsed time. |

---

## What This Is Trying to Achieve

A mechanically legible fate system for mortal lives in a xianxia world. The I Ching is not flavour. It is the seed. The Five Elements and trigrams are structural cause, woven into the Causal Spine. The AI reads Classical Chinese source texts directly — one interpretive layer between canon and chronicle. No translation. No modern gloss.

End goal: an idle RPG where characters live, encounter each other, die, and leave legacies — across generations, across bloodlines — while the player only reads the chronicles after the fact. V1.0 is the first engine component that earns trust in the underlying structure.

---

## Mechanics

### The Birth Fate

Every mortal is born under a random Five Element and I Ching trigram. The system constrains the mapping:

| Element | Trigram | Binary  | Aspect    |
|---------|---------|---------|-----------|
| 火 (Fire) | 離 (Li) | 101101  | 陰火 (Yin Fire) |
| 水 (Water) | 坎 (Kan) | 010010 | 陽水 (Yang Water) |
| 木 (Wood) | 震 (Zhen) or 巽 (Xun) | 100100 / 011011 | 陽木 / 陰木 |
| 金 (Metal) | 乾 (Qian) or 兌 (Dui) | 111111 / 110110 | 陽金 / 陰金 |
| 土 (Earth) | 艮 (Gen) or 坤 (Kun) | 001001 / 000000 | 陽土 / 陰土 |

Fire and Water each have exactly one trigram. Wood, Metal, and Earth each have two (Yin and Yang aspects). This constraint is enforced by data, not by prompt.

The 6-bit binary represents the doubled trigram (lower trigram + upper trigram, lines read bottom-up: 0 = Yin, 1 = Yang).

### Canonical Texts Injected Into Prompt

Two source texts are passed to the AI, in Classical Chinese, without translation:

- **Bai Hu Tong** (白虎通, Eastern Han, compiled by Ban Gu): describes the cosmological nature of the mortal's element.
- **Shuogua** (說卦傳, from the received Zhouyi): lists the attributes, images, and associations of the mortal's trigram.

The AI interprets these directly. The prompt does not explain them. The instruction is: "This cosmic signature shapes the character's innate temperament, strengths, weaknesses, and the underlying pattern of their life. It is not a prophecy, but a compass."

### Randomness

Two layers, both fully random, no user selection:

1. **Birth Fate**: `roll_fate()` in `fate.py` picks a random Five Element, then a random trigram from that element's pool.
2. **Hidden Death**: `main.py` picks a random end from a pool of 6–7 thematically appropriate deaths for the start condition.

| Start | Possible Deaths |
|-------|-----------------|
| rich  | gout, apoplexy, poison, heart failure, robbery murder, family betrayal, execution |
| poor  | malnutrition, plague, war death, exhaustion, flogging, winter freeze |

The death is never shown in the terminal summary or the output filename.

### Causal Spine

Every chronicle ends with a forced causal chain: a dry, logical summary of how the birth fate, start condition, turning point, and hidden death connect. This enforces structural coherence. The narrative can be organic; the spine must be honest.

---

## Sources

| Text | Date | Authority | Used For |
|------|------|-----------|----------|
| 尚書·洪範 (Shang Shu, Hong Fan) | ~6th–4th c. BCE | Seminal Five Elements definition, attributed to Ji Zi | Reference, not injected |
| 白虎通·五行 (Bai Hu Tong) | 79 CE | Han dynasty imperial canon by Ban Gu | Element nature injected into prompt |
| 說卦傳 (Shuogua) | Received Zhouyi | One of the Ten Wings | Trigram attributes injected into prompt |
| 周易 (Zhouyi) | Western Zhou | King Wen hexagram judgments | Stored in `hexagram_data.py` for future use |

---

## Files

### Active Modules

**`main.py`** — CLI entry point. Parses `--start` and `--event1`. Calls `validate()`, `roll_fate()`, `build()`, and `generate()`. Hides the death. Prints the birth fate summary. Saves output.

**`states.py`** — Houses `START_STATES` (2 entries) and `END_STATES` (7 rich, 6 poor). Provides `validate()` and `default_ends()`.

**`prompts.py`** — `build()` constructs the system prompt with COSMIC SIGNATURE block (Bai Hu Tong + Shuogua) and the user prompt with start, event, hidden end, and format instructions (500–800 words, Title/Chronicle/Causal Spine).

**`llm_client.py`** — `generate()` sends the prompt to Ollama via HTTP, or returns a hardcoded mock chronicle if `--mock` is set. Timeout: 300 seconds.

**`fate.py`** — `roll_fate()` picks a random element and trigram, merges data from `five_elements_data` and `bagua_data`, returns a unified fate dict.

### Data Files

**`five_elements_data.py`** — `FIVE_ELEMENTS` dict keyed by Chinese element character. Each entry contains `name_en`, `baihutong_zh`, and a list of `trigrams` (each with `binary`, `name_zh`, `name_en`, `element_aspect`).

**`bagua_data.py`** — `TRIGRAMS` dict keyed by 6-bit binary string. Each entry contains `name_zh`, `name_en`, `element`, `element_aspect`, and `shuogua_zh`.

**`hexagram_data.py`** — Full 64 hexagrams in Shao Yong binary order (000000–111111), each with `name_zh`, `name_en`, and `judgment_zh`. Reserved for future use.

### Documentation

**`LORE.md`** — World setting, design constraints, tone rules, and long-term roadmap.

**`README.md`** — This file.

---

## Current State

V1.0 is live. The pipeline runs end-to-end on a Dell Latitude 7490 running Ubuntu, using Ollama with `qwen2.5:1.5b`. No cloud dependencies. No external Python packages. The fate engine injects authentic Classical Chinese source texts into every chronicle. The death is hidden. The Causal Spine links everything. The chronicle length is 500–800 words.

---

## Pending

- **Event weighting logic.** Currently, the birth fate influences the chronicle only through the AI's interpretation of canonical texts. The turning point (`--event1`) is still user-supplied. V2/V3 will need a system where fate biases what events can occur, not just how they are narrated.
- **Interview layer (V2).** Speaking with the dead character post-chronicle.
- **Intergenerational karma (V3).** One chronicle's death seeds the next.
- **Parallel lives (V4).** Autonomous agents, elapsed time, legacy loops.
- **Hexagram integration.** The full 64 hexagrams in `hexagram_data.py` are stored but unused. They are the natural bridge from single-life trigram fate to multi-generational hexagram patterns.
