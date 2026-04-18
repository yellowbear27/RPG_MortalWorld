# The Mortal Game

**An idle RPG about fate, randomness, and the roads not taken.**

Status: Conceptual — early development
Language: Python (text-based output)
Author: Building in public from first principles

---

## What This Is

You create a character. You set their attributes, their background, their circumstances.

Then you let go.

You have no further control. Ever. Your character lives their life — encounters unfold, decisions are made, consequences accumulate — entirely without your intervention. After 24 hours you can read what happened. The 24 hours represents the passage of time in their world.

You are not a player. You are something closer to a god who created a mortal being and then stepped back. Involved in creation. Unable to affect destination. Able only to hope.

It is like making a paper airplane and setting it off from a rooftop.

---

## Origin

This project began as a personal question that became a design principle.

What if I had studied harder? What if I had stayed in Singapore instead of leaving? What if I had been less hard on my son when he was young — would he have chosen differently?

These questions have no answers. The roads not taken cannot be walked. But they can be simulated. Not to produce the answer we want — that would be dishonest — but to confront the deeper truth: that even if we had made different choices, randomness would have intervened. Life does not proceed the way we feel it should, even when we try harder, choose better, love more carefully.

The game is a machine for exploring that truth without the cost of living it again.

The thematic parallel is Pachinko — not in mechanics, but in philosophy. One decision walks you down an entirely different path. Fate. The cards you are dealt. The gap between what you intended and what arrived.

---

## The Core Mechanic

A character is created with a set of attributes — background, temperament, social position, starting circumstances. These parameters are the only control the player ever has.

Once the character enters the world, an AI system generates their life story in discrete encounters. Each encounter builds on the previous one. Parameters constrain the impossible — an orphan child in a subsistence farming community will not be homeschooled in particle physics. The system is bounded by what is plausible given the character's actual situation.

The character has a natural lifespan. They will age, struggle, make choices (without player direction), form relationships, succeed in some things, fail in others, and eventually die. The player reads the accumulated story after each 24-hour cycle.

The deeper mechanic is emergence. When multiple characters exist in the same world and begin interacting — forming alliances, competing for resources, influencing each other's trajectories — the system produces outcomes that no one designed. The story becomes genuinely unpredictable. Not random. Emergent.

That distinction matters.

---

## The AI Architecture

Each character is powered by an AI agent with a defined personality, history, and set of goals. The agent does not follow a script. It reasons about its situation and acts accordingly.

The world is governed by a World Soul — an overarching agent that functions as an autonomous dungeon master. The World Soul monitors all character interactions, enforces the physical and social laws of the world, and generates consequences for actions. It cannot be appealed to. It does not take sides. It simply maintains coherence.

Failure modes in AI behaviour — unexpected decisions, surprising interactions, outcomes no one predicted — are not bugs to be eliminated. They are the mechanism of emergence. The system is designed to channel unpredictability into valid, surprising world events rather than suppress it.

This is the most technically interesting problem in the project: designing an AI system that produces emergent narrative complexity from simple, consistent rules — and remains bounded enough to feel real rather than arbitrary.

---

## Why Text-Based

Text is the correct format for this project, for several reasons.

The richness of the experience is cognitive, not visual. Reading a life story — seeing the choices made, the luck encountered, the slow accumulation of consequence — requires language, not graphics. A rendered 3D environment would distract from the thing that actually matters: what happened, and what it means.

Text is also achievable. This project is being built by one person who is learning Python while building it. Starting with text output and a working emergent system is the correct MVP. Visual layers, if they ever come, come later.

---

## What This Project Is Not

It is not a god game in the Populous tradition. There is no city to build, no civilization to direct.

It is not a narrative RPG in the Dragon Age tradition. There are no dialogue choices, no branching trees, no player-authored story.

It is not a simulation in the Dwarf Fortress tradition, though it shares some philosophical DNA. The scale is smaller and the focus is personal rather than systemic.

It is closest to: a life, observed from a distance, by someone who made the life possible and then had to let it go.

---

## Phase 1 MVP

A single character. A single lifespan. A readable text log of the life story, updated every 24 hours.

The technical components:

- Character creation interface (attributes, background parameters)
- Encounter scheduler (triggers at defined intervals)
- LLM integration (generates narrative output from character state and encounter parameters)
- Probability framework for encounter weighting (the statistical heart of the system)
- Text log accumulation
- Read interface unlocking after each 24-hour cycle

The probability framework deserves specific mention. Getting the encounter parameters right — weighted by character background, social position, geographic context, and prior events — is the hardest design problem in the system. Too constrained and the life feels scripted. Too loose and the AI hallucinates nonsense that breaks immersion. Finding the right balance is also a learning project in probability and statistics.

---

## Phase 2 (Not Yet)

Legacy. Inheritance. Reincarnation.

The idea: a character's life generates karma, legacy, and consequence that shapes the starting conditions of the next character. Previous life merit unlocks better beginning circumstances in the next life. Multiple lifetimes accumulate meaning.

This is thematically perfect. It is also a significant engineering challenge. It will wait until Phase 1 is complete and working.

---

## Learning Objectives

This project is engineered to teach:

- Python scheduling and event systems
- LLM API integration (structuring prompts, handling responses, managing state)
- Probability distributions and weighted random selection
- State management across time (character state evolving through a lifespan)
- Emergent systems design
- Text generation and narrative coherence evaluation

The game is the curriculum. The curriculum is the game.

---

## Why This Is Public

Because the idea deserves to be visible. Because the problem it is trying to solve — how to build genuine emergent narrative from AI agents following consistent rules — is a real and interesting technical problem that others may have thoughts about.

And because this repository, like all the others in this portfolio, is a record of a particular kind of transition: from someone who understood systems conceptually to someone who can build them.

Collaboration from people who find the idea interesting is welcome. Especially on the probability framework and the emergent AI architecture.

---

## A Note on the Theme

Every person who has ever made a serious mistake, lost something they should not have lost, or made a choice they cannot unmake — carries some version of the question this game is trying to answer.

What would have happened if I had done it differently?

The honest answer, built into the architecture of this system, is: something different. Not necessarily better. Not necessarily what you imagined. Life has its own momentum. Randomness intervenes. The cards you are dealt matter, but so does the shuffle.

The game does not offer comfort. It offers clarity.

That is enough.
