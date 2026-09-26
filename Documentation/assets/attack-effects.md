# Attack Effects (`.j3attackfx`)

Attack Effects collect the sound and visual feedback for using an attack and for its different outcomes. A move can sound different when it misses, hits, is blocked, or is parried. Keeping those references in one asset lets multiple attacks reuse a consistent effect style.

## Create and connect it

Choose **Assets → Create → Combat → Attack Effects** and open the file. Fill the sound and effect references you need, adjust trail and hit-pause values, then save. Reference this file from a [Melee Attack](melee-attack.md) or [Firearm Attack](firearm-attack.md).

![Attack Effects inspector](../images/attack-effects-inspector.png)

*Screenshot placeholder: capture the Attack Effects inspector with Use, Hit, Blocked, and Parried sound and effect fields and trail settings. The image should show that outcomes can have separate feedback.*

## Fields

| Field | Meaning |
| --- | --- |
| `useSound`, `useEffect` | Played when the attack is initiated or released, depending on runtime timing. |
| `hitSound`, `hitEffect` | Feedback for a confirmed hit. |
| `blockedSound`, `blockedEffect` | Feedback for an attack stopped by a block. |
| `parriedSound`, `parriedEffect` | Feedback for a parry result. |
| `overrideWeaponTrail` | Uses this asset's trail settings instead of the weapon default. |
| `trailMaterial`, `trailWidth`, `trailLifetime` | Optional material and the width and lifetime of a trail. Width and lifetime cannot be negative. |
| `hitPauseDuration`, `hitPauseScale` | Brief timing effect on impact. Both values must be nonnegative in the inspector. |

Sound pickers accept `.ogg` and `.wav`; effect pickers accept `.j3effect`; trail material accepts `.j3m`. The current inspector writes these fields into the asset's `data` section. Effects supplement hit logic; they do not decide whether a striker touched a hurtbox.
