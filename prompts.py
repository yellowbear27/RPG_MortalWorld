# prompts.py
# Builds the system and user prompts for the LLM.
# Now incorporates a birth fate (element + trigram + canonical texts).

def build(start_desc: str, event1: str, end_desc: str, fate: dict) -> tuple[str, str]:
    """
    fate is the dict from roll_fate(), containing:
      - element, element_en
      - baihutong_zh
      - trigram_name_zh, trigram_name_en
      - element_aspect
      - shuogua_zh
      - binary
    """

    # System prompt: sets the tone, world, and now the birth fate
    system = (
        "You are a chronicler of mortal lives in a xianxia world. "
        "The world is indifferent, not cruel. Keep the story human in scale. "
        "Write in a dry, precise style. Your chronicle must include a Title, "
        "a Chronicle (700–1000 words, divided naturally into scenes), "
        "and a Causal Spine.\n\n"
        "--- COSMIC SIGNATURE ---\n"
        f"The mortal is born under the Five Element {fate['element']} ({fate['element_en']}). "
        f"The Bai Hu Tong describes its nature: {fate['baihutong_zh']}\n"
        f"The mortal's trigram is {fate['trigram_name_zh']} ({fate['trigram_name_en']}), "
        f"aspect {fate['element_aspect']} (binary {fate['binary']}). "
        f"The Shuogua reveals its attributes: {fate['shuogua_zh']}\n"
        "This cosmic signature shapes the character's innate temperament, strengths, "
        "weaknesses, and the underlying pattern of their life. It is not a prophecy, "
        "but a compass. The events of the life must feel as if they arise from this nature.\n"
        "--- END COSMIC SIGNATURE ---\n\n"
        "Do not explain the signature. Let it quietly influence the narrative."
    )

    # User prompt: now requests 600–1000 words
    user_prompt = (
        f"Write a mortal life chronicle.\n"
        f"Starting condition: {start_desc}\n"
        f"First major turning point: {event1}\n"
        f"Ending condition (cause of death): {end_desc}\n\n"
        "The Chronicle must be 600–1000 words long, told in natural scenes.\n\n"
        "Return the chronicle in this exact format:\n"
        "## Title\n\n## Chronicle\n\n## Causal Spine"
    )

    return system, user_prompt
