# states.py
# Valid start and end states for the chronicle generator.

START_STATES = {
    "rich": "Born into wealth. Merchant family. Full granaries. Silk at birth.",
    "poor": "Born into poverty. Tenant farmer stock. Debt before first breath.",
}

END_STATES = {
    "rich": {
        "gout": "Died of gout. Excess crystallised in the joints. Wealth turned inward against the body.",
        "apoplexy": "Died of apoplexy. A burst vessel in the brain during a feast.",
        "poison": "Died of slow poison. A rival merchant's gift, laced, mistaken for illness.",
        "heart_failure": "Heart gave out. Decades of indulgence left it too weak to pump.",
        "robbery_murder": "Beaten to death by bandits on the trade road. They took everything.",
        "family_betrayal": "Murdered in his bed. An heir, impatient, took the estate early.",
        "execution": "Executed by the magistrate. His wealth bought influence, then bought the scaffold.",
    },
    "poor": {
        "malnutrition": "Died of malnutrition. The body consumed itself. Scarcity made total.",
        "plague": "Died of the sweating plague. Swept through the slums where he could not flee.",
        "war_death": "Killed in a sect skirmish. A stray arrow meant for a cultivator found his back.",
        "exhaustion": "Died of exhaustion. Worked until the body simply stopped, in a field or a mill.",
        "flogging": "Flogged to death for stealing grain. Justice for the poor is quick and final.",
        "winter_freeze": "Froze to death outside the city walls. No fuel, no blanket, no one.",
    },
}

def validate(start: str, end: str) -> tuple[str, str]:
    if start not in START_STATES:
        raise ValueError(f"Invalid start state '{start}'. Choose from: {list(START_STATES)}")
    if end not in END_STATES[start]:
        raise ValueError(f"Invalid end state '{end}' for start '{start}'. Choose from: {list(END_STATES[start])}")
    return START_STATES[start], END_STATES[start][end]


def default_ends(start: str) -> list[str]:
    """Return all possible end keys for a given start."""
    return list(END_STATES[start].keys())
