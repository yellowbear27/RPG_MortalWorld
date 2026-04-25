# main.py
# Entry point. Parses CLI args, builds prompt, calls LLM, saves output.
#
# Usage:
#   python main.py --start rich --end gout --event1 "lost the family business in a flood"
#   python main.py --start poor --end malnutrition --event1 "drafted into a sect war as a porter" --mock

import argparse
import os
import datetime

from states import validate
from prompts import build
from llm_client import generate


OUTPUT_DIR = "outputs"


def parse_args():
    parser = argparse.ArgumentParser(
        description="RPG MortalWorld -- mortal life chronicle generator"
    )
    parser.add_argument(
        "--start",
        required=True,
        choices=["rich", "poor"],
        help="Starting life condition.",
    )
    parser.add_argument(
        "--end",
        required=True,
        choices=["gout", "malnutrition"],
        help="Ending life condition (cause of death).",
    )
    parser.add_argument(
        "--event1",
        required=True,
        help='The first major turning point. Example: "lost the family business in a flood"',
    )
    parser.add_argument(
        "--mock",
        action="store_true",
        help="Use mock output instead of calling Ollama. Good for testing.",
    )
    parser.add_argument(
        "--model",
        default=os.getenv("OLLAMA_MODEL", "qwen2.5:1.5b"),
        help="Ollama model name. Defaults to OLLAMA_MODEL env var or qwen2.5:1.5b.",
    )
    parser.add_argument(
        "--base-url",
        default=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        help="Ollama base URL. Defaults to OLLAMA_BASE_URL env var or http://localhost:11434.",
    )
    return parser.parse_args()


def save_output(content: str, start: str, end: str) -> str:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename  = f"{OUTPUT_DIR}/chronicle_{start}_{end}_{timestamp}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return filename


def main():
    args = parse_args()

    # Validate states and get their descriptions.
    start_desc, end_desc = validate(args.start, args.end)

    # Build the prompt.
    system, user_prompt = build(start_desc, args.event1, end_desc)

    # Print a summary of what we are generating.
    print("=" * 60)
    print("RPG MortalWorld -- Chronicle Generator")
    print("=" * 60)
    print(f"  Start:  {args.start} -- {start_desc}")
    print(f"  Event1: {args.event1}")
    print(f"  End:    {args.end} -- {end_desc}")
    print("=" * 60)
    print()

    # Generate the chronicle.
    result = generate(system, user_prompt, args.model, args.base_url, args.mock)

    # Print to terminal.
    print(result)

    # Save to file.
    filepath = save_output(result, args.start, args.end)
    print(f"\n[saved] {filepath}")


if __name__ == "__main__":
    main()
