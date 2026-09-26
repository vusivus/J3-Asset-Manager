# Striker (`.j3striker`)

A striker is an offensive collision shape. During an active attack, it represents the part of a fist, foot, or weapon that can hit someone. “Hitbox” is the common game-development word for that offensive shape. The [hit detection guide](hit-detection.md) explains how it interacts with a receiving hurtbox.

## Create and connect it

1. Choose **Assets → Create → Combat → Striker** and name the body part or weapon region, for example `Right Hand Punch`.
2. Open the asset, choose a Location label and Parent Bone, then choose a shape: Box, Sphere, or Capsule.
3. Position and size the shape relative to its parent bone. Use the editor preview when available; the default shape is only a starting point.
4. Set filtering and gizmo options, then save.
5. Add the striker to the [Weapon Definition](weapon.md) and select it in each [Melee Attack](melee-attack.md) that should use it.

![Striker inspector](../images/striker-inspector.png)

*Screenshot placeholder: capture the Striker inspector with Location, Parent Bone, Shape, dimensions, collision filters, and preview visible. The image should show the authored box on the correct hand or weapon section.*

## Placement fields

| Field | Meaning |
| --- | --- |
| `title`, `description` | Human-readable explanation for authors. The title falls back to the asset name if blank. |
| `location` | Semantic label such as RightHand, LeftFoot, or WeaponPrimary. This identifies what the shape represents. |
| `parentBone` | Canonical joint the shape follows during animation. Choose the joint that actually moves with the striking limb. |
| `shape` | `Box`, `Sphere`, or `Capsule`. Choose a simple shape that follows the intended contact region. |
| `localOffset` | X, Y, Z position in metres relative to the bone. |
| `localEulerAngles` | X, Y, Z rotation in degrees relative to the bone. |
| `boxHalfExtents` | Box half-size in metres on each axis. A half-extent of `0.1` gives a total width of `0.2` on that axis. |
| `radius` | Sphere or capsule radius in metres. |
| `capsuleHeight` | Total capsule height in metres. It is clamped to at least twice the radius. |
| `capsuleDirection` | Capsule's principal local axis: `0` X, `1` Y, `2` Z. The value is clamped to `0–2`. |

The inspector shows only the dimension fields relevant to the chosen shape. The service clamps extremely small box extents or radius to `0.001`, so inspect the saved result if you entered near-zero values.

## Collision and preview fields

| Field | Meaning |
| --- | --- |
| `targetLayers` | Integer bit mask of collision layers eligible for overlap checks; the default `-1` represents all bits set. It does not by itself establish which objects have those layers. |
| `includeTriggers` | Whether trigger collision volumes are included by the overlap query. |
| `ignoreSameTeam` | Intended to reject friendly characters during ordinary damage resolution. |
| `showGizmo` | Shows the shape in a preview or debug view where gizmo rendering is available. It is not a gameplay visibility setting. |

## Shape selection

Use a small sphere near a fist for a compact punch, a capsule along a forearm or bat for an elongated region, and a box for a broad striking face. The best shape is the smallest one that reliably represents the contact you want. Oversized shapes make attacks hit before the visible object reaches the opponent.

![Striker shape comparison](../images/striker-shapes.png)

*Screenshot placeholder: show the same model with Box, Sphere, and Capsule striker previews, each labeled. The image should help readers choose a shape and understand half extents versus radius.*

## Troubleshooting

If a striker stays behind as the hand moves, check Parent Bone and the model's skeleton mapping. If it appears offset, adjust Local Offset or Rotation. If it hits too early, first inspect the Melee Attack's active window, then the striker's size. A correctly placed striker remains harmless while its attack is outside the active window.
