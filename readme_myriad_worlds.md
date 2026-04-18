# Myriad Worlds — 三千大千世界

**A xianxia universe built on real physics, Chinese cosmology, and the question of what it actually costs to survive under heaven.**

Status: Active worldbuilding — physics engine in early development
Language: Python (prototyping), potentially Rust (performance layer)
Author: Building in public from first principles

---

## What This Repository Is

This repository has two layers that share the same foundation.

The first is a physics engine — a Python system implementing real physical laws as the underlying mechanics of a fantasy world. Force, momentum, mass, energy propagation, environmental consequence. The spectacle emerges from the rules. The rules are not invented for convenience.

The second is the xianxia universe those rules govern — a world called Myriad Worlds (三千大千世界), currently being expressed as a novel and as an RPG. The novel is titled *The Unluckiest Cultivator*. The RPG is a separate artifact built on the same cosmological foundation.

This repository documents the physics engine build. The worldbuilding canon lives elsewhere and is referenced here only where it directly informs engine design.

---

## Origin: Why Physics

I came to physics through an unusual route.

Twenty years in finance gave me a particular way of thinking about systems: incentives, flows, leverage points, the gap between how a structure is described and how it actually behaves. When I began seriously studying mathematics and physics in my fifties — working through Spivak's Calculus from first principles, engaging with tensor field theory, studying classical mechanics — I found that the same structural thinking applied. Physics is not a collection of facts. It is a language for describing how things actually behave, as opposed to how we imagine they should.

The xianxia genre — Chinese fantasy cultivation fiction — has always fascinated me for its ambition: a cosmology, a hierarchy of power, a metaphysics of energy. But the genre almost universally treats its physics as decoration. Qi is a word. Cultivation is a narrative device. Impact is an animation trigger.

I wanted to ask: what if it were real? What if the physics of a xianxia world were as internally consistent as the physics of our own? What if the energy that a cultivator channels obeyed conservation laws? What if an impact from a being of extraordinary mass and force produced real shockwaves, real environmental consequence, real effects on bystanders?

That question became a design principle. The physics engine is its implementation.

---

## The Physics of This World

In Myriad Worlds, Qi is a rank-2 tensor field. It transforms correctly under coordinate changes. It obeys conservation laws. Its behaviour is governed by a 64-hexagram framework derived from the I Ching, with the eight primary hexagrams holding foundational authority.

This is not flavour text. It is the actual structure of the world's energy system, and it has consequences for how the engine must behave.

The physics engine does not simulate our universe. It simulates a universe whose laws are coherent, internally consistent, and rooted in real mathematical structure — but whose constants and field behaviours differ from ours in specific, defined ways.

Building this engine is therefore simultaneously a programming project, a physics education, and an act of worldbuilding. The three cannot be separated.

---

## Design Philosophy

**Consequence over spectacle.** A heavy impact creates a shockwave. The shockwave has effects on terrain, structures, and bodies within range. Those effects are calculated from the force involved, not selected from a menu of pre-authored animations. Spectacle emerges from the physics. The physics is not adjusted to produce the desired spectacle.

**Rules before implementation.** Before a line of engine code is written for a given phenomenon, the physical principles governing that phenomenon are understood. The mathematics precede the model. The model precedes the code.

**Pragmatism over purity.** This is not a project to write every engine subsystem from scratch. Existing tools — Unity, Unreal, or other frameworks — may serve as infrastructure layers where appropriate. The engine is the physics and simulation logic, not necessarily the rendering pipeline. Goalposts will move as knowledge deepens. That is expected and healthy.

**Realism as respect.** A world whose physics are taken seriously respects the intelligence of the reader and the player. It also produces better stories — because consequence is real, and real consequence creates genuine stakes.

---

## The Novel: The Unluckiest Cultivator

The novel set in this world is not a power fantasy.

It follows a protagonist who is autistic, cursed, and exiled — carrying a burden he did not choose, accompanied by a fellowship of outcasts who are not heroes by the world's definition. The story begins in the register of dark comedy and picaresque absurdity. It ends in tragedy.

The deepest thematic engine is this: ordinary suffering matters more than elite transcendence. The world of cultivation fiction usually celebrates the extraordinary individual who escapes the common fate. This novel asks what the common fate actually costs, and who pays for the transcendence of the exceptional.

The worldbuilding is rooted in the I Ching, Chinese cosmology, and the symbolic logic of ritual and hierarchy. The four clans — Dong Chen, Nan Yan, Xi Yue, Bei Yuan — are not aesthetic houses. They are civilisational archetypes representing different corrupted or partial relationships to power, order, and survival.

The mythic objects — the Hundun Egg, the Taotie Axe, the Dongfang Coliseum — carry precise symbolic weight derived from Chinese mythology and cosmological tradition. They are not decorative.

This repository does not contain novel text. The canon of the novel is held separately and precisely. What the engine inherits from the novel is its physical laws and its cosmological structure.

---

## The RPG

The RPG built on this world is a separate project documented in a separate repository. Its design philosophy inherits the same commitment to physical consequence and real simulation weight.

The short version: it is a game where fantasy combat obeys physical logic. Where force matters, mass matters, momentum matters, environmental response matters. Where the player must understand the system to play it well, not merely memorise the animations.

---

## Current Study Path

The engine cannot be built without understanding the physics it is meant to implement. The study path and the build path are the same path.

Current curriculum:

- Calculus: Spivak's *Calculus*, Chapter One. Formal proofs, not computation. Deliberately difficult. Deliberately correct.
- Linear algebra and tensor theory: tensors as multilinear maps invariant under coordinate transformation. Not arrays. Not numbers. Maps. This is essential for the Qi field system and for General Relativity, which is a longer horizon.
- Classical mechanics: Newtonian dynamics, impulse, energy propagation, rigid body behaviour.
- Numerical methods: how to implement continuous physical systems in discrete computational steps.

The 3Blue1Brown reference point: one person built Manim — a mathematical animation engine in Python — to visualise concepts he was studying. The scope of that project was defined by what the builder understood and needed. This engine is being built the same way.

---

## Learning Objectives

This project is engineered to teach:

- Python simulation and numerical methods
- Physics implementation (Newton's laws, impulse, momentum, energy, waves)
- Tensor operations in code
- Mathematical modelling — translating physical equations into computational models
- Eventually: performance optimisation, possibly Rust

The engine is the curriculum. The curriculum is the engine.

---

## Why This Is Public

Because building something this ambitious in public creates accountability. Because the commit history of someone learning physics and mathematics while building the system those subjects describe is an unusual and honest record.

Because the question at the centre of this project — what does a xianxia world look like if its physics are taken seriously — deserves to be asked in a place where others can engage with it.

And because this portfolio, taken as a whole, is the argument that it is not too late to build something real. That a finance career does not foreclose a technical one. That genuine curiosity, pursued with discipline, produces genuine capability regardless of when it starts.

---

## A Note on Scope

This is a long project. Possibly a decade-long project, if it is pursued with the seriousness it deserves.

The MVP is not a full engine. The MVP is a Python simulation that correctly implements a small set of physical interactions — impact, force propagation, environmental response — within the defined laws of Myriad Worlds.

Each commit is a step. The steps accumulate. The engine grows with the understanding that makes it possible.

That is the only way to build something that will last.
