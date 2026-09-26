# Build a first melee character

This walkthrough connects the main files used by an unarmed character. It explains the authoring order; it does not assume a completed game scene. Use a model and animation that are compatible with each other.

## 1. Prepare the model and animation

Use **Assets → Import → Model** for a source model, then create or import an [Animation Clip](../assets/animation-clip.md) for the punch. Preview the clip on the intended character and check that the arm and hand move as expected. If the source skeleton uses different joint names, review [Skeletal Mapping](../assets/skeletal-mapping.md).

## 2. Create the offensive shape

Create a [Striker](../assets/striker.md) named `Right Hand Punch`. Choose the right hand as its parent bone and a small Box, Sphere, or Capsule. Position it near the fist using the local offset. The striker is the attack's invisible contact region, commonly called a hitbox.

## 3. Create the move

Create a [Melee Attack](../assets/melee-attack.md), such as `Straight Punch`. Assign the punch Animation Clip. Enable Strike, add the right-hand striker, and set damage and maximum targets. Set the anticipation end and strike end so the striker is active only while the fist should connect. Use the timeline preview to inspect those frames, then save.

## 4. Give the weapon an attack

Create an [Attack Set](../assets/attack-set.md) in Melee mode and assign the Straight Punch to **Forward Attack**. Create a [Weapon Definition](../assets/weapon.md) with category **BareFists**. Add the Attack Set in its Primary role and add the right-hand striker to the weapon's striker list. Bare fists need no equipped model.

## 5. Configure the attacker

Create a [Combat Controller](../assets/combat-controller.md) and assign the BareFists weapon as its default. The inspector checks that this weapon really has category BareFists.

## 6. Configure the receiver

Create a [Hurtbox Profile](../assets/hurtbox.md), add a torso receiving box, and position it around the model's chest. Create [Reaction Data](../assets/reaction.md) with at least one useful hit reaction clip if available. Create a [Damage Controller](../assets/damage-controller.md) and reference the Hurtbox Profile and Reaction Data.

## 7. Assemble the character

Create a [Character](../assets/character-asset.md). Assign its model, Combat Controller, and Damage Controller. Add movement and input configuration if you want to control it in a runtime scene. Save and inspect the preview, then test the hit in the game using the matching J3 runtime.

![Connected melee assets in project](../images/first-melee-character.png)

*Screenshot placeholder: show the created files in the project browser and the character inspector referencing its combat and damage controllers. Include a preview where the fist striker and torso hurtbox can be seen.*

## When a punch looks right but misses

Check four things in order: the active strike window, the striker's parent bone and size, the target's hurtbox placement, and the validity of the combat references. The [hit detection guide](../assets/hit-detection.md) explains why each one matters.
