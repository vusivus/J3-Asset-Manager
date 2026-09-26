# Character (`.j3char`)

A Character asset brings a model and its gameplay modules together. It is the place to say which movement, combat, damage, and agent settings belong to a character. The model provides its appearance; the controller assets provide reusable behavior data.

## Create and edit

Import or prepare a compatible model first. Choose **Assets → Create → Characters → Character** (the exact category follows the character directory configured for this build), name the file, and open it. Choose the model and any optional module assets in the Character inspector. Adjust dimensions and capsule collision to fit the preview, then save.

![Character inspector](../images/character-inspector.png)

*Screenshot placeholder: show a Character asset with its model, movement, combat, damage, and agent references, physical dimensions, and preview. The image should show the character as the hub for other assets.*

## Fields

| Field | Meaning |
| --- | --- |
| `displayName` | Name shown to an author or player-facing system. |
| `model` | `.j3model` reference for the character's visual model. Model import and metadata are separate workflows. |
| `characterType` | `Player`, `Enemy`, or `NPC`; this also changes which archetype choices are offered. |
| `archetype` | Starting statistical profile, such as Balanced for a player or Grunt for an enemy. The inspector displays derived stats; the archetype is not a separate file reference. |
| `heightMeters`, `weightKg` | Physical dimensions of the character. Use values appropriate to the model. |
| `maxHealth` | Character health baseline; must remain positive. |
| `capsuleHeight`, `capsuleRadius`, `capsuleCenterX/Y/Z` | Main movement or physics capsule. This solid body shape is distinct from the combat [Hurtbox Profile](hurtbox.md). |
| `characterControlEnabled` | Whether the character control is enabled when assembled. |
| `movementProfile` | Optional `.j3move` reference. |
| `combatProfile` | Optional `.j3combat` reference. |
| `damageProfile` | Optional `.j3damage` reference. |
| `agentProfile` | Optional `.j3agent` reference for an AI-controlled character. |
| `skeletonMapping` | Stored by the character format; the current main inspector does not expose this field directly. |

The Character inspector saves many value changes automatically, but inspect its status after changes and use Save where available. A default asset can be created before every module exists; fill the references as you build the character.

## Capsule versus hurtbox

The capsule is the broad physical body used for movement and collision with the world. Hurtboxes are the body regions used to receive combat hits. A character can stand on the floor because its capsule works while still failing to receive a punch because its Damage Controller or Hurtbox Profile is missing.

## Preview checks

Check scale, feet position, capsule fit, model orientation, and module references. Then test the character in a runtime scene; an editor preview alone cannot prove that input, animation, or damage is wired correctly.
