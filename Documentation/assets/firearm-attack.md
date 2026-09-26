# Firearm Attack (`.j3firearm`)

A Firearm Attack describes one way a gun fires. It records trigger behavior, raycast reach and spread, damage, timing, animations, and effect references. A [Firearm Attack Set](attack-set.md) chooses the default firearm attack and optional targeting, crouching, or cover variants. The [Weapon Definition](weapon.md) stores the physical gun and ammunition configuration.

## Create and connect it

1. Prepare compatible firing [Animation Clips](animation-clip.md) and optional [Attack Effects](attack-effects.md).
2. Choose **Assets → Create → Combat → Firearm Attack** and open the `.j3firearm` file.
3. Set Trigger Mode, firing rate, range, spread, damage, and the normalized shot time. Add animation and effects references.
4. Save. Create an Attack Set in Firearm mode and choose this file as its **Default Firearm Attack**.
5. Add the set to a Weapon Definition with a firearm category such as Pistol, Rifle, or Shotgun.

![Firearm Attack inspector](../images/firearm-attack-inspector.png)

*Screenshot placeholder: capture Trigger Mode, RPM, cartridges per shot, raycast range and spread, damage, animation references, and shot time. The image should show how a gunshot is configured as an attack asset.*

## Trigger and raycast

| Field | Meaning |
| --- | --- |
| `trigger.mode` | `SemiAutomatic`, `Automatic`, or `Burst`. |
| `roundsPerMinute` | Intended firing cadence. Must be greater than zero. |
| `burstCount` | Shots in a burst. The schema stores it even though the current inspector does not expose it. |
| `cartridgesPerShot` | Ammunition consumed per shot; at least one. |
| `raycast.range` | Maximum shot distance; greater than zero. |
| `spreadXDegrees`, `spreadYDegrees` | Horizontal and vertical shot spread. |
| `raysPerShot` | Number of rays or pellets in one shot; at least one. |
| `pierces` | How many penetration steps are allowed; cannot be negative. |
| `maximumTargets` | Target limit stored by the schema; at least one. |

“Raycast” means the game checks along an imagined line from the gun to see what it intersects. Several rays per shot can represent pellets. Spread changes their direction; it does not make a bullet visibly larger.

## Damage, animation, and timing

| Field | Meaning |
| --- | --- |
| `damage.amount` | Base damage per resolved shot contact; nonnegative. |
| `poiseDamage`, `knockbackForce`, `power` | Stagger pressure, push force, and Weak/Heavy/Knockdown result class. |
| `timing.shotNormalizedTime` | Point in the firing animation when the shot is released, from `0` to `1`. |
| `animations.*` | Standing, crouching, and cover-side `.j3clip` variants. |
| `effects` | Optional `.j3attackfx` for sound and visual feedback. |

The schema also includes falloff, accuracy, recoil, and extra timing fields. The current Firearm Attack inspector does not expose all of them. Avoid treating an unshown field as an editable UI control; use the current schema and runtime implementation to judge whether it affects play.

## Common mistakes

- A Firearm Attack is not the same file as a firearm Weapon Definition: one defines a shot, the other groups attacks and equipment settings.
- Shot time at the wrong normalized position can make the shot occur before or after the visible muzzle flash.
- A Firearm Attack Set must reference a default `.j3firearm` asset before it can validate.
