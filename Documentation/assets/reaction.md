# Reaction Data (`.j3reaction`)

Reaction Data describes how a character responds after being hit: a light flinch, heavy stagger, knockdown, get-up, or other recovery. It does not decide whether an attack made contact. [Strikers and hurtboxes](hit-detection.md) establish that first; an attack's power and the receiver's reaction data help choose what happens next.

## Create and connect it

1. Prepare compatible [Animation Clips](animation-clip.md) for the reactions you want to show.
2. Choose **Assets → Create → Combat → Reaction Data**.
3. Open the asset and set the general knockback, stagger, downed, and recovery values.
4. Add Reaction rows by Height and Direction. Add Knockdown Recovery rows when a character can fall and get up. Assign their clip references.
5. Save and reference the Reaction Data from a [Damage Controller](damage-controller.md).

![Reaction Data inspector](../images/reaction-inspector.png)

*Screenshot placeholder: capture general reaction values and at least one Mid/Front Reaction row and one Knockdown Recovery row. The image should show how a hit's direction and height select animations.*

## Understanding the categories

`Height` is `High`, `Mid`, or `Low`: the approximate vertical area of the incoming hit. `Direction` is `Front`, `Back`, `Left`, or `Right`: where the force arrives relative to the receiver. A row pairs one height and direction with weak and heavy clips. Knockdown rows add weak and heavy fall clips plus a Get Up clip.

| Field group | Meaning |
| --- | --- |
| `reactions[]` | Weak and Heavy clips for one Height/Direction pair. Duplicate pairs are rejected. |
| `knockdownRecoveries[]` | Weak and Heavy knockdown clips plus a Get Up clip for one Height/Direction pair. Duplicate pairs are rejected. |
| `staggerAnimationClip` | Optional general stagger animation. |
| `staggerDuration`, `staggerThreshold`, `staggerRecoveryPerSecond` | Timing and accumulation settings for the stagger concept. |
| `grappleVulnerabilityDuration` | Period during which a staggered target can be easier to grapple. |
| `downedDuration`, `getUpAnimationSpeed` | Time spent down and playback speed for rising. |
| `knockbackDamageMultiplier`, `knockbackDuration` | Authored knockback scaling and duration. |

The asset validates nonnegative or minimum values for these numbers. The inspector reports invalid values when saving.

## How fallback works

You do not need to author every combination before starting. The reaction asset first tries the requested height and direction. If no suitable clip exists, it searches other directions, favoring Front, then other heights, favoring Mid. Knockdown and Get Up clips are resolved from the same recovery row so the fall and rise remain paired. A missing clip can still leave no playable reaction, so preview and test the important cases.

For a first pass, author Mid/Front weak and heavy clips, then expand to High/Low or side directions as the animation library grows.
