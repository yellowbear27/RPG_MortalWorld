# RPG MortalWorld

Generate mortal life chronicles in a xianxia world.
One life. Two events. Born into a condition. Dies into another.

---

## Setup

No external dependencies. Python 3.8+ only.

```bash
git clone https://github.com/yourname/RPG_MortalWorld
cd RPG_MortalWorld
cp .env.example .env
```

Edit `.env` to set your Ollama model and URL.

---

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com) running locally with a model pulled

```bash
ollama pull qwen2.5:1.5b
ollama serve
```

---

## Run

**With Ollama:**
```bash
python main.py --start rich --end gout --event1 "lost the family business in a flood"
```

**With mock output (no Ollama needed):**
```bash
python main.py --start rich --end gout --event1 "lost the family business in a flood" --mock
```

**Other examples:**
```bash
python main.py --start poor --end malnutrition --event1 "drafted into a sect war as a porter"
python main.py --start rich --end malnutrition --event1 "cheated by a business partner at forty"
```

---

## Arguments

| Argument | Required | Values | Description |
|---|---|---|---|
| `--start` | yes | `rich`, `poor` | Starting life condition |
| `--end` | yes | `gout`, `malnutrition` | Cause of death |
| `--event1` | yes | any string | First major turning point |
| `--mock` | no | flag | Skip Ollama, return hardcoded output |
| `--model` | no | model name | Overrides OLLAMA_MODEL in .env |
| `--base-url` | no | URL | Overrides OLLAMA_BASE_URL in .env |

---

## Output

Chronicles are saved to `outputs/` as markdown files.
Filename format: `chronicle_{start}_{end}_{timestamp}.md`

---

## Structure

```
RPG_MortalWorld/
├── main.py          # CLI entry point
├── states.py        # Valid start and end states
├── prompts.py       # Prompt construction
├── llm_client.py    # Ollama communication
├── .env.example     # Environment variable template
├── requirements.txt # No external deps for V0
├── README.md        # This file
├── LORE.md          # World background and roadmap
└── outputs/         # Generated chronicles
```
