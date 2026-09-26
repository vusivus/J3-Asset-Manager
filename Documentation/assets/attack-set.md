# Attack Set (`.j3attackset`)

An Attack Set decides which attack asset is used for one weapon action slot. It does not describe animation or damage itself; its references point to [Melee Attacks](melee-attack.md) or [Firearm Attacks](firearm-attack.md). A [Weapon Definition](weapon.md) then assigns the set to a Primary, Secondary, or Special role.

## Create and connect it

1. Create the attacks that this set will reference.
2. Choose **Assets → Create → Combat → Attack Set**.
3. Open the new asset and choose **Mode**: `Melee` or `Firearm`.
4. Choose the **Input Slot**: `Primary`, `Secondary`, or `Special`.
5. Fill the references shown for that mode and save. The inspector can save automatically when a reference or mode changes; review the status message.
6. Add the set to a Weapon Definition under the matching role.

![Attack Set inspector](../images/attack-set-inspector.png)

*Screenshot placeholder: capture one Attack Set in Melee mode and show Mode, Input Slot, Forward/Back/Knockdown references, and Knockdown Health Threshold. The image should demonstrate that the set selects existing moves.*

## Melee mode

| Field | Meaning |
| --- | --- |
| `forwardAttack` | The ordinary/default move for this set. It references `.j3melee` (older `.j3attack` files are accepted). |
| `backAttack` | Optional move for a backward or retreating attack selection. |
| `knockdownAttack` | Optional move for an eligible low-health target. |
| `knockdownHealthThreshold` | Normalized target-health threshold from `0–1`; the default is `0.25`, meaning 25% of maximum health. It only matters when a knockdown attack is assigned and the runtime supports that selection. |

The current asset validator allows the three melee references to be blank while a set is being authored. A useful set still needs at least one move connected to fulfill its purpose.

## Firearm mode

| Field | Meaning |
| --- | --- |
| `firearmAttack` | **Required** default `.j3firearm` attack. The asset cannot validate in Firearm mode without it. |
| `targetingFirearm` | Optional attack variant while targeting. |
| `crouchingFirearm` | Optional crouched variant. |
| `coverFirearm` | Optional cover variant. |

Choosing Firearm mode changes which group of fields is visible in the inspector. It does not convert a melee asset into a firearm asset; create a `.j3firearm` file for the default reference.

## Input Slot versus Weapon role

`input` is the slot recorded inside the Attack Set. The weapon stores separate Primary, Secondary, and Special entries that each point to an Attack Set. Use matching labels so the project remains understandable. The current schema validates that weapon roles are unique and that each role's reference is present.

## Example

For bare fists, a Primary set could use `Straight Punch.j3melee` for Forward Attack and `Back Elbow.j3melee` for Back Attack. A Secondary set could point to kick moves. The Attack Sets are then assigned to the BareFists weapon's Primary and Secondary roles.

## Common mistakes

- A Firearm set without `firearmAttack` fails validation.
- A set can be saved but remain unused until a weapon references it.
- Entering `25` for the knockdown threshold is invalid; `0.25` represents 25%.
- Mixing `.j3melee` and `.j3firearm` in the wrong mode fails type validation.
