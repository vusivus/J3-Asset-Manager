# Weapon Definition (`.j3weapon`)

A Weapon Definition describes the fighting equipment or unarmed style a character can use. It connects a category, optional visible model, attack sets, striker shapes, and presentation settings. **BareFists** is a weapon category too: it supplies the default unarmed setup without requiring a prop model.

## Create and connect it

1. Create any needed [Striker](striker.md) and [Attack Set](attack-set.md) assets first.
2. Choose **Assets → Create → Weapons → Weapon Definition** and open the new file.
3. Choose its category. Add one Attack Set row for each role you intend to use, then choose the corresponding `.j3attackset` file.
4. Add the striker assets that belong to the weapon. For bare fists these may be hand or foot shapes; for a bat they can represent its striking end.
5. If the weapon has a visible prop, assign the `.j3o` model and adjust its socket and local transform so it sits correctly in the character's hand.
6. Save and link the BareFists weapon in a [Combat Controller](combat-controller.md), or equip another weapon through the runtime.

![Weapon Definition inspector](../images/weapon-inspector.png)

*Screenshot placeholder: capture category, Attack Set roles, striker list, equipped model, socket, transform, and Save. The image should show the weapon as a collection of linked assets.*

## Identity and attack selection

| Field | Meaning |
| --- | --- |
| `category` | `BareFists`, `Bat`, `Chain`, `Knife`, `Blade`, `Pistol`, `Rifle`, `Shotgun`, or `Other`. The category describes the weapon family. |
| `attackSets[]` | One reference per role: Primary, Secondary, or Special. Each entry must point to a `.j3attackset`. Duplicate roles and blank entries are rejected. |
| `strikers[]` | The offensive collision shapes available on this weapon. The list cannot contain blank or duplicate references. The attack chooses which of those shapes it activates. |
| `locomotion` | Optional `.j3loco` override for this weapon's movement animation. |

A weapon can contain several striker assets because its attacks may use different contact regions. An unarmed weapon may include both hands and feet; an individual punch activates only the striker named by that attack.

## Presentation and attachment

| Field | Meaning |
| --- | --- |
| `equippedModel` | Optional visible `.j3o` model. BareFists may leave it empty. |
| `socket` | Canonical body bone where the model attaches, usually a hand. |
| `localPosition` | Model offset in metres relative to that socket. |
| `localEulerAngles` | Rotation in degrees relative to that socket. |
| `localScale` | Model scale on X, Y, and Z; all values must be positive. |
| `defaultTrailMaterial` | Optional `.j3m` used for weapon trails unless an attack effect overrides it. |

Adjust these while previewing the character and weapon together. The striker shape and visible model are separate: making the bat look aligned does not automatically align its hitbox.

## Durability and firearms

`indestructible` determines whether finite durability is intended to matter; `durability` must still be an integer of at least `1`. A firearm configuration can be enabled in the inspector. Its visible fields include magazine capacity, starting reserve ammunition, reload duration, and automatic reload when empty. The underlying firearm group also stores muzzle bone, position, direction, and animation references. Some of those fields are not currently exposed in this inspector, so check the runtime and schema before depending on them.

## Example: bare fists

Set Category to **BareFists** and leave Equipped Model empty. Add a Primary Attack Set with punches and a Secondary Attack Set with kicks, and add the matching hand and foot striker assets. Save. Then select this weapon as the Combat Controller's default bare-fists weapon.

## Common mistakes

- A Combat Controller refuses a default weapon whose category is not BareFists.
- An Attack Set row with no reference prevents the weapon from saving.
- A weapon striker and an attack's selected striker are different lists; the attack needs the correct active reference.
- A visible prop attached to the correct hand can still have an incorrectly positioned striker.
