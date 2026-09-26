# Combat, attacks, and weapons

Use the individual guides to author a [Melee Attack](melee-attack.md), [Attack Set](attack-set.md), [Weapon Definition](weapon.md), [Striker](striker.md), [Hurtbox Profile](hurtbox.md), [Combat Controller](combat-controller.md), and [Damage Controller](damage-controller.md). This page explains how the parts work together.

This page explains the combat concepts behind the J3 assets. It is written for readers who have not built a combat system before. The separate [hit detection guide](hit-detection.md) explains strikers, hitboxes, and hurtboxes in more detail.

## How a move becomes a hit

A move is more than an animation. It has a wind-up, a moment when it can connect, and a recovery period. For example, a punch animation may begin while the fist is still moving toward the target. During that wind-up the punch should not deal damage. The strike becomes active only during the frames when the fist is meant to hit. Afterward, the attacker finishes the move and is briefly committed to recovery.

```text
Choose move → Wind-up → Active strike → Resolve contact → Recovery → Ready again
```

The attack asset describes the move: its animation, timing, damage, reach, effects, and which striker shapes are active. An attack set groups moves for a weapon or input slot. A combat controller selects or equips the appropriate weapon configuration. A weapon provides its attacks and the physical striking shapes it can use.

![Combat setup overview](../images/combat-setup-overview.png)

*Screenshot placeholder: show a character's combat configuration, selected weapon and attack set, and a striker preview. The image should show how the author connects the move to the weapon and the character.*

## What are a hitbox and a hurtbox?

Games need a simple way to decide whether an attack touched somebody. They use invisible shapes for this, separate from the detailed visible mesh.

- A **hitbox** is the invisible shape used to check whether an attack connects. It represents the dangerous part of the move, such as a fist, boot, sword edge, or bat head.
- A **hurtbox** is the invisible shape used to represent the part of a character that can be hit. It may cover the torso, head, arms, or legs.

Think of the hitbox as the moving hand reaching out, and the hurtbox as the target area on another character. If the two overlap while the attack is active, the game can register a hit. If they never overlap, the animation may look close but the game treats it as a miss.

These are not usually visible during ordinary play. In an editor or debug view they can be drawn as simple boxes, spheres, or capsules to help an author line them up with the animated body or weapon.

## Strikers and hurtboxes in J3 assets

In this project, a **striker** is the authored attacking shape that supplies a hitbox to an attack. A `.j3striker` asset describes one such shape and where it attaches, such as a hand bone or a section of a weapon. The term *hitbox* describes the general game concept; *striker* is the project's asset name for an offensive shape.

A `.j3hurtbox` asset describes the receiving shapes on a character. These shapes can be associated with body locations, such as head or torso. A hit can then identify not only that the character was hit, but approximately which region was contacted. The damage or reaction system can use that location to choose a response.

| Term | Plain meaning | J3 asset or use |
| --- | --- | --- |
| Hitbox | An invisible attack shape used to check contact. | Supplied by a striker while a move is active. |
| Striker | An authored offensive shape attached to a body part or weapon. | `.j3striker` |
| Hurtbox | An invisible receiving shape on a character. | `.j3hurtbox` |
| Attack | The move, including when to activate shapes and what a confirmed hit does. | Current `.j3melee` file; older `.j3attack` references are also accepted. |
| Reaction | The receiver's response to a hit, such as stagger or knockdown. | `.j3reaction`, referenced through damage configuration. |

For example, a right-hand punch can activate only the right-hand striker during its strike window. If it overlaps the opponent's torso hurtbox, the system resolves one hit and can use the torso location when selecting damage feedback or a reaction. The punch should not keep damaging the same opponent every frame merely because the shapes remain overlapped; repeated hits need to be an explicit move rule.

![Striker and hurtbox preview](../images/striker-hurtbox-preview.png)

*Screenshot placeholder: show a posed character with a colored striker on the attacking hand and separate hurtbox shapes on the target body. Label which shape attacks and which receives damage. The image should make the overlap relationship obvious.*

## What happens when shapes touch?

At a high level, hit resolution follows these steps:

1. The attack enters its active strike window.
2. Its assigned striker shapes follow the animated bones or weapon parts.
3. The runtime checks for overlap with valid character hurtboxes.
4. It ignores invalid contacts, such as the attacker hitting themself or a disallowed teammate.
5. It resolves the target and body location, then applies the attack's damage and reaction rules.
6. It plays the appropriate hit, block, parry, or miss feedback.

This is a conceptual explanation of the intended system. Exact runtime behavior and asset support can vary by implementation stage. A preview shape helps tune placement, but testing in the game is still needed because animation, timing, collision filters, and runtime transforms all affect the final result.

## Weapon assets

A `.j3weapon` asset describes an item or fighting style used by a character. It can connect the visible model and attachment point to attack sets, strikers, movement style, and other weapon-specific properties. Bare fists can use a weapon definition too, giving the character a consistent fallback configuration when no physical weapon is equipped.

Weapons should change how a fight is played, not only increase a damage number. The following are design roles from the game design document; treat them as direction for the game, not a claim that all six complete systems are implemented in the editor or runtime.

| Weapon system | Intended feel and use | Trade-off |
| --- | --- | --- |
| Bare fists | Fast punches and kicks at close range, with mobile movement and access to grapples and throws. | Short reach and limited crowd control. |
| Guns | Aim and apply pressure from range, subject to line of sight, ammunition, recoil, and reloads. | Risky when surrounded or interrupted at close range. |
| Bats | Strong blunt strikes with medium reach and useful stagger or knockback. | Slower, committed swings leave recovery if they miss. |
| Chains | Sweeping attacks that threaten a broad area and control space. | Need room to swing and readable wind-up or recovery. |
| Shinobi swords | Precise, dangerous blade attacks that reward spacing and timing. | Commitment and recovery create punish opportunities. |
| Grenades | Limited-use area denial that disrupts groups and forces movement. | Finite supply, visible danger, and risk to nearby allies or civilians. |

## Asset roles

| Asset | What it describes |
| --- | --- |
| `.j3combat` | Character-level combat controller settings, including the default bare-fists weapon. |
| `.j3weapon` | A weapon's category, model, attachment, attack-set references, and striker references. |
| `.j3attackset` | A group of attacks organized for a weapon or action slot. |
| `.j3melee` | One current melee move: animation, timing, active strike, damage, movement, and feedback. |
| `.j3striker` | One offensive collision shape, such as a fist, foot, or weapon section. |
| `.j3hurtbox` | Receiving body shapes and their associated body locations or damage settings. |
| `.j3damage` | Character damage configuration, including hurtbox and reaction references. |
| `.j3reaction` | Response data such as hit, stagger, knockdown, or death animation. |
| `.j3attackfx` | Reusable audiovisual feedback associated with attacks and their outcomes. |

## Preview and validation

Where supported, preview overlays make shapes visible so authors can check their position as the model moves. Validation can identify missing references or bones. A shape attached to the wrong bone, an overly large shape, or a badly timed strike can make combat feel unfair even if the asset saves successfully.

![Attack timeline inspector](../images/attack-timeline-inspector.png)

*Screenshot placeholder: show an attack timeline with its wind-up, active strike, and recovery phases, plus the selected attack properties. The image should show when the striker becomes active.*

## Related concepts

- [Hit detection: strikers and hurtboxes](hit-detection.md)
- [Characters and models](characters.md)
- [AI behaviour system](behaviours.md)
- [J3 asset catalogue](index.md)

## Design source

The explanations and weapon roles here follow the project's *Ultimate Bounty Hunter* GDD, Revision 2, especially *Combat Style* and *J3 Asset Manager Software*. The editor and runtime remain under active development, so design intent and shipped behavior should be kept distinct.
