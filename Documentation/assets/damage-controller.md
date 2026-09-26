# Damage Controller (`.j3damage`)

The Damage Controller gathers the assets that describe how a character receives hits. It links a [Hurtbox Profile](hurtbox.md), which provides receiving body shapes, and [Reaction Data](reaction.md), which provides animation and recovery responses. It can request runtime generation of hurtbox collision volumes.

## Create and connect it

1. Create and position a Hurtbox Profile on the intended character model.
2. Create Reaction Data with suitable hit or knockdown clips where available.
3. Choose **Assets → Create → Combat → Damage Controller** and open the file.
4. Choose the Hurtbox Profile and Reaction Data in their reference fields. Keep **Auto Generate Runtime Hurtboxes** enabled if you want the runtime to construct the receiving collision shapes from the profile.
5. Save, then assign the `.j3damage` file to the character's Damage Profile.

![Damage Controller inspector](../images/damage-controller-inspector.png)

*Screenshot placeholder: show both asset reference fields, the Auto Generate Runtime Hurtboxes option, and a character preview with receiving shapes. The image should show where the defensive side of collision is configured.*

## Fields

| Field | Meaning |
| --- | --- |
| `hurtboxProfile` | `.j3hurtbox` file containing receiving body shapes and global damage multiplier. |
| `reactionData` | `.j3reaction` file containing hit, stagger, knockdown, and get-up responses. |
| `autoGenerateRuntimeHurtboxes` | Requests collision volumes from the saved profile at runtime; default is enabled. |

The model-level validator accepts empty references as a draft. For a working receiving character, fill the relevant links and test in the runtime. The inspector can clear either reference deliberately.

## How this differs from a weapon

The weapon and its striker shapes describe the attacker. The Damage Controller and Hurtbox Profile describe the receiver. When an active striker reaches a valid hurtbox, the runtime can resolve damage and select a reaction. Keeping the two sides separate means a character can change weapons without changing its receiving body layout.
