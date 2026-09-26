# Glossary

Use this page when a guide introduces an unfamiliar combat or editor term.

| Term | Meaning |
| --- | --- |
| Active strike window | The part of an attack animation during which its selected striker shapes can cause a hit. |
| Agent profile | Data describing an AI character's role, perception, thinking, and personality. |
| Animation clip | A reusable selection of animation data, including playback range, speed, looping, and blend settings. |
| Asset key | Project-relative path stored in a reference field, usually using forward slashes. |
| Attack Set | An asset that selects moves for a Primary, Secondary, or Special weapon/input slot. |
| Anticipation | The wind-up of an attack before the active strike. It gives the player time to read the move. |
| Behaviour | An AI goal such as patrol, investigate, combat, or flee. |
| Bone / joint | A point in a model's skeleton that moves during animation. A striker or hurtbox can follow one. |
| Capsule | A rounded cylinder-like collision shape, useful for limbs or a character's broad physical body. |
| Character capsule | Main physical body used for movement and world collision; separate from combat hurtboxes. |
| Damage Controller | Asset linking a character's hurtbox and reaction settings. |
| Emitter | Part of a particle effect that creates particles over time. |
| Hitbox | Common term for an invisible attacking collision shape. In J3 Asset Manager, a Striker asset describes one. |
| Hurtbox | Invisible receiving body region that an attack can touch. |
| Knockback | Movement imparted to the receiver after a hit. |
| Locomotion | Animation and tuning for ordinary movement states such as idle, walk, run, turn, and jump. |
| Normalized time | A position from `0` at the start to `1` at the end of a clip, independent of clip length in seconds. |
| Poise | Resistance to interruption or pressure toward stagger, depending on whether it is armor or damage. |
| Reaction | The receiver's response to a hit, including animation, stagger, knockdown, or recovery. |
| Recovery | End of a move after the active strike, before the attacker is fully ready again. |
| Skeleton mapping | Table connecting standard humanoid roles to a model's actual joint names. |
| Striker | J3 asset defining an offensive box, sphere, or capsule that can act as a hitbox during an attack. |
| Weapon Definition | Asset grouping weapon category, presentation, attack sets, and striker references. |

See [hit detection](../assets/hit-detection.md) for a step-by-step explanation of contact and [the first melee character](../getting-started/first-melee-character.md) for a full authoring sequence.
