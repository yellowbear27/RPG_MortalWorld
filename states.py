# states.py
# Valid start and end states for the chronicle generator.
# These are placeholders. The state system will expand in later versions.

START_STATES = {
    "rich": "Born into wealth. Merchant family. Full granaries. Silk at birth.",
    "poor": "Born into poverty. Tenant farmer stock. Debt before first breath.",
}

END_STATES = {
    "gout":         "Died of gout. Excess crystallised in the joints. Wealth turned inward against the body.",
    "malnutrition": "Died of malnutrition. The body consumed itself. Scarcity made total.",
}


def validate(start: str, end: str) -> tuple:
    if start not in START_STATES:
        raise ValueError(f"Invalid start state '{start}'. Choose from: {list(START_STATES)}")
    if end not in END_STATES:
        raise ValueError(f"Invalid end state '{end}'. Choose from: {list(END_STATES)}")
    return START_STATES[start], END_STATES[end]
