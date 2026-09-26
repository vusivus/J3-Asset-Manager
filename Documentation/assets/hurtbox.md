# Hurtbox Profile (`.j3hurtbox`)

A hurtbox is a receiving collision shape on a character. It marks a region that an attack can hit. One Hurtbox Profile can contain several boxes: for example, a chest box and boxes for the head and limbs. This differs from a [Striker](striker.md), which is an attacking shape.

## Create and connect it

1. Choose **Assets → Create → Combat → Hurtbox Profile** and open the file.
2. Set the Global Damage Multiplier. Keep `1.0` for ordinary damage until you have a reason to change it.
3. Select **Add Hurtbox** for each receiving region. Choose a Hurt Location and Parent Bone, then set the box dimensions and offset so the box follows that body part.
4. Save the profile and select it in a [Damage Controller](damage-controller.md). Assign that controller to a [Character](character-asset.md).

![Hurtbox inspector](../images/hurtbox-inspector.png)

*Screenshot placeholder: capture the Hurtbox Profile inspector with at least a torso and head row, their bones and sizes, and a character preview. The image should show that one profile contains multiple receiving regions.*

## Profile and shape fields

| Field | Meaning |
| --- | --- |
| `globalDamageMultiplier` | Scales incoming damage for the whole profile. `1.0` means unchanged; `0.5` halves it; `2.0` doubles it. The value cannot be negative. |
| `shapes[]` | List of receiving boxes. The current asset permits an empty list as a draft, but a character with no receiving shape cannot be struck through this profile. |
| `location` | The body location reported for a hit, such as Body, Head, or a limb. Use the region that the box actually covers. |
| `parentBone` | Joint the receiving box follows as the character animates. |
| `localOffset` | Box center position in metres relative to the parent bone. |
| `localEulerAngles` | Box rotation in degrees relative to the parent bone. |
| `boxHalfExtents` | Half the box dimensions on X, Y, Z. All three values must be positive. |
| `wireframe` | Draw an outline instead of a filled box in preview. This changes the editor gizmo, not damage behavior. |

For example, a chest box with half extents `(0.25, 0.35, 0.15)` has full dimensions `(0.50, 0.70, 0.30)` metres. Adjust the numbers to fit the actual character instead of copying them between models of different sizes.

## Why location matters

When a striker overlaps a hurtbox, the receiving shape identifies an approximate body region. A reaction system can use that region to choose an animation or damage response. If every box is labeled Body, the system loses the distinction between head, torso, and limbs. The exact mapping from contact to reaction depends on the runtime.

## A starting layout

Begin with one chest or torso box and test a basic punch. Add head or limb boxes only when the gameplay needs their locations. Each box should follow the animated region and overlap neighboring boxes only as much as needed to avoid gaps. Oversized boxes make a near miss register as a hit; boxes that are too small cause visible contact to miss.

![Striker touching hurtbox](../images/striker-hurtbox-preview.png)

*Screenshot placeholder: show an attacker's active striker touching the target's torso hurtbox, with the boxes labeled. The image should explain which box deals contact and which box receives it.*

## Troubleshooting

If attacks pass through the visible torso, check the torso box's bone, offset, and size, then inspect the attack's active striker timing. If a target can never be hit, confirm that the Character references a Damage Controller and that Auto Generate Runtime Hurtboxes is enabled if your runtime depends on generated shapes.
