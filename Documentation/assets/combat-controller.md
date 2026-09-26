# Combat Controller (`.j3combat`)

The Combat Controller is the character's connection to combat configuration. Its current authored field is the default BareFists weapon. That weapon is the unarmed fallback when no external weapon is equipped.

## Create and connect it

1. Create a [Weapon Definition](weapon.md) and set its Category to **BareFists**. Give it an Attack Set and striker references for the moves you want.
2. Choose **Assets → Create → Combat → Combat Controller**.
3. Open the new `.j3combat` file and select the BareFists `.j3weapon` in **Default Bare Fists Weapon**.
4. Save. The inspector checks both that a weapon is assigned and that its category is BareFists.
5. Open the [Character](character-asset.md) and assign this Combat Controller in the Combat Profile field.

![Combat Controller inspector](../images/combat-controller-inspector.png)

*Screenshot placeholder: show the Combat Controller's Default Bare Fists Weapon reference and the saved status. The image should make the required fallback connection clear.*

## Field

| Field | Meaning |
| --- | --- |
| `defaultBareFistsWeapon` | Project-relative reference to a `.j3weapon` whose Category is BareFists. |

The underlying asset model allows an empty reference as an intermediate draft, but the current inspector requires a valid BareFists weapon before saving. An unrelated weapon category, missing file, or invalid weapon asset causes a save error.

## What it does not contain

Individual attacks live in [Melee Attack](melee-attack.md) files, their selection lives in [Attack Sets](attack-set.md), and striker shapes belong to the [Weapon Definition](weapon.md) and attacks. The Combat Controller does not duplicate these settings. The runtime's equip and unequip behavior is separate from this one authored field.
