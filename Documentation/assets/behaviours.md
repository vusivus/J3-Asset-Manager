# AI behaviour system

This page introduces how an AI character can decide what to do. It describes the design model in the *Ultimate Bounty Hunter* GDD and how the proposed J3 assets fit together. Some parts are design direction and may not yet be implemented as complete editor or runtime features.

## From goal to concrete movement

An AI system can be understood as a short chain:

```text
Agent profile → Behaviour → State → Action
```

- An **agent profile** describes what kind of character this is and what options it has.
- A **behaviour** is the current goal, such as patrol, investigate, fight, flee, or recover.
- A **state** is the current phase of that goal, such as approach, attack, defend, or recover.
- An **action** is a concrete instruction, such as turn, walk, reload, or use a particular attack.

In plain terms: the profile defines what the character knows how to do; the behaviour chooses the goal; the state decides what phase comes next; and an action does a specific piece of work.

## Example: an enemy with a rifle

1. The agent profile allows the character to use combat and rifle attacks.
2. The combat behaviour identifies a target from what the enemy can currently perceive and remember.
3. The enemy enters an approach state and moves toward a useful firing position.
4. The attack state checks range, line of sight, ammunition, cooldown, nearby allies, and safety.
5. An action faces the target and fires an allowed attack.
6. The enemy recovers or repositions, continues attacking, or changes behaviour if the situation changes.

This keeps the broad goal (fight) separate from the moment-to-moment phase (approach or attack) and the actual operation (fire a weapon).

## Thinking and context

The GDD describes **Thinking** as the quality and style of an agent's decisions. It can affect how many options an agent evaluates, how well it judges risk, whether it coordinates with allies, and how quickly it reacts. A lower Thinking level should make understandable mistakes; it should not break movement or make decisions purely random.

Thinking is not another level in the profile → behaviour → state → action chain. It influences decisions across the chain. Likewise, **behaviour context** is temporary runtime information, such as the current target, last-known position, equipped weapon, ammunition, route, and nearby danger. It is not necessarily a saved asset.

An agent should make decisions from available perception and memory. It should not know a hidden player's exact position without seeing, hearing, or otherwise learning about it.

## How the proposed J3 assets fit

The GDD proposes these reusable configuration assets:

| Asset | Purpose |
| --- | --- |
| `.j3agent` | Agent profile: permitted behaviours, perception, thinking, and role-specific settings. |
| `.j3behaviour` | Goal-level logic such as patrol or combat. |
| `.j3state` | A phase inside a behaviour, with actions and transitions. |
| `.j3action` | A configured instruction selected by a state, such as turn, walk, attack, reload, or throw. |

The GDD's expected hierarchy allows profiles to reuse behaviours and behaviours to reuse states and actions. Parameters can tune the shared logic for different character roles without copying an entire behavior for every enemy type.

![Behaviour hierarchy](../images/behaviour-hierarchy.png)

*Screenshot placeholder: show the agent profile referencing behaviours, one behaviour containing states, and a selected state listing actions and transitions. The image should make the profile → behaviour → state → action hierarchy understandable.*

## Behaviours described in the game design

The GDD outlines several goal-level behaviours:

- **Patrol:** follow a route, guard a location, interact with the gang, or observe the area.
- **Investigate:** orient toward a suspicious sound or sight, approach carefully, inspect the area, and confirm or clear the threat.
- **Warning and intimidation:** communicate a boundary or demand, wait for a response, and escalate only when conditions justify it.
- **Combat:** select a target, approach an appropriate position, check whether an attack is safe and available, defend, recover, reposition, or disengage.
- **Pursuit and search:** use the last known location when the target is no longer visible, coordinate a search, and stop when the search budget expires.
- **Reinforcement, retreat, or surrender:** respond to danger, morale, role, and encounter conditions.

These are design concepts, not a checklist of finished AI behavior in the editor. Their detailed state flows are maintained in the game design documents and will need matching runtime implementations.

## Weapon-specific behaviour

Combat can share common decisions—choose a target, find a useful position, and avoid unsafe attacks—while delegating the move itself to a behavior suited to the equipped weapon.

| Weapon | Example decision priority |
| --- | --- |
| Bare fists | Close distance, wait for a safe opening, use quick strikes or attempt an eligible grapple. |
| Bat | Maintain swing range, commit to a strong strike, then manage the recovery window. |
| Chain | Preserve space for a sweep and avoid swinging through blocked geometry. |
| Shinobi sword | Maintain disciplined blade distance and use precise attacks or counters. |
| Firearm | Seek line of sight and useful range, monitor ammunition, reload or reposition when threatened. |
| Grenade | Choose a valid throw, warn nearby characters, and avoid unsafe blasts around allies or civilians. |

The weapon influences preferred range, movement, attack choices, and risk. The agent profile, current context, and Thinking determine which option it selects. This is why a shared Combat Behaviour can lead two characters with different weapons or profiles to act differently.

## Current J3 Asset Manager status

The repository currently includes editor and core concepts for enemy, social, memory, inventory, level, and wave assets. The GDD's `.j3agent`, `.j3behaviour`, `.j3state`, and `.j3action` hierarchy is the proposed direction for reusable behavior authoring. Do not assume those proposed extensions are fully available just because they appear in the design documentation.

## Design source

This page is based on *Ultimate Bounty Hunter* GDD, Revision 2, especially *Behaviours* and *J3 Asset Manager Software*. It summarizes the design for an editor user and does not claim the AI design is complete in the current runtime.
