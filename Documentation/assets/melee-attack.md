# Melee Attack (`.j3melee`)

A Melee Attack is one authored move: a punch, kick, bat swing, or similar close combat action. It combines animation, the time at which the move can hit, damage, movement, and audiovisual cues. The current Create Asset menu calls it **Melee Attack** and saves `.j3melee`. Older `.j3attack` references are still accepted by the Attack Set inspector.

Before editing these fields, read [hit detection](hit-detection.md): a move's striker is an invisible offensive shape, and it should be active only when the visible attack ought to connect.

## Create and connect it

1. Prepare the [Animation Clip](animation-clip.md) and any [Striker](striker.md) assets for the move.
2. Choose **Assets → Create → Combat → Melee Attack**, name the move, and create it.
3. Select the new `.j3melee` file to open the Melee Attack inspector.
4. Fill the Ground Animation Clip, Strike, and Sequencer sections. Add striker references to the list by dragging `.j3striker` files from the project tree.
5. Preview the move, adjust its active window, then select **Save Attack**.
6. Assign the move to a [Melee Attack Set](attack-set.md).

![Melee Attack inspector](../images/melee-attack-inspector.png)

*Screenshot placeholder: capture a selected `.j3melee` asset with animation references, Strike fields, striker list, Sequencer fields, timeline, and Save Attack button visible. The image should show where move timing is edited.*

## Animation and linked assets

| Field | Meaning |
| --- | --- |
| `groundAnimationClip` | The normal grounded `.j3clip` animation for this move. The preview requires the chosen clip. |
| `airAttackStartAnimationClip`, `airAttackLoopAnimationClip`, `airAttackEndAnimationClip` | Optional airborne phases. Use these only for a move designed to begin, continue, and finish in the air. |
| `charge` | Optional `.j3charge` asset for a held charge or approach dash. |
| `effects` | Optional `.j3attackfx` asset for sounds, effects, trails, and result feedback. |

References must be project-relative keys of the expected type. An empty optional field is allowed by the asset validator.

## Strike fields

| Field | Meaning and authoring advice |
| --- | --- |
| `strike.enabled` | Turns the damaging strike window on or off. Disable it for a movement or presentation move that should never hit. |
| `strike.damage` | Base damage before the receiving character's damage rules. It must be zero or greater. |
| `strike.power` | `Weak`, `Heavy`, or `Knockdown`: the move's result class, used by reaction logic. This is not the numeric damage amount. |
| `strike.direction` | `Forward`, `Backward`, `Up`, `Down`, or `Radial`: how the move is classified spatially. |
| `strike.useStrikers` | The specific `.j3striker` shapes used by this move. A right-hand punch should list its right-hand striker, not every limb. Empty and duplicate entries are rejected. |
| `strike.maximumTargets` | Maximum victims for the move; at least one. Use one for a focused punch and a larger value only for an intended sweep. |
| `strike.allowRepeatedHits` | Allows the same victim to be hit again during one move. Leave off for an ordinary punch or swing. |
| `strike.knockbackForce` | Base push force after a confirmed hit; cannot be negative. |

## Sequencer and timing

The timeline uses normalized positions: `0` is the start of the played clip and `1` is its end. An **Anticipation End** of `0.25` means the first quarter is wind-up. A **Strike End** of `0.55` means the active window runs from 25% to 55%. The remainder is recovery.

| Field | Meaning |
| --- | --- |
| `sequencer.startFrame`, `endFrame` | Optional source frame override for this attack. Leave the inspector fields blank to inherit the clip asset's range. The end must follow the start; an end of `0` can represent the full source in the underlying range logic. |
| `transitionIn`, `transitionOut` | Blend times when entering and leaving the move; each is limited to `0–0.5`. |
| `anticipationEnd` | When wind-up ends and the striker becomes active; valid range `0.01–0.95`. |
| `strikeEnd` | When the striker becomes inactive; it must be at least `0.01` later than Anticipation End and no later than `0.99`. |
| `anticipationSpeed`, `strikeSpeed`, `recoverySpeed` | Playback speed for each phase. Each must be at least `0.05`. |
| `gravityMultiplier` | Gravity adjustment during the move, valid from `0–2`. |
| `forwardDistance` | Authored forward travel; zero means no scripted advance. |
| `motion` | `None`, `Scripted`, `RootMotion`, or `MotionWarping` selects how motion is intended to be handled. Verify the chosen mode in the runtime. |

The inspector's timeline can play, pause, scrub, step frames, and set the two strike markers from the current frame. If you change the frame range or timing while previewing, restart the preview to see the changed sequence. A displayed “Striker ACTIVE” phase is a timing aid; test actual contact with a target in runtime.

![Melee attack timing](../images/melee-attack-timing.png)

*Screenshot placeholder: capture the timeline while the fist is near the target. Show the Anticipation End and Strike End markers and the status reading “Striker ACTIVE.” The image should teach that the active window is shorter than the animation.*

## Timeline events and poise

Each event has a normalized time (`0–1`), a type, and a cue asset. Types include `Audio`, `Effect`, `TrailOn`, `TrailOff`, `ComboWindowOpen`, and `ComboWindowClose`. Place events where the visible action supports them; a whoosh near the swing and an impact effect on contact are different events.

`poiseArmor` describes resistance to interruption during the move, while `poiseDamage` describes stagger pressure on the receiver. Both must be nonnegative. Their effect depends on the current combat runtime.

## Example: straight punch

Assign a compatible punch clip and a right-hand striker. Keep repeated hits off and Maximum Targets at `1`. Preview the fist's path and set the active window around the point where the hand extends into the target. Save, add the move to an Attack Set, and test against a character with a torso hurtbox.

## Common mistakes

- A striker that activates during wind-up makes the punch hit early.
- A wide active window may let the same move hit at visually unrelated poses.
- A missing or wrong bone on the striker makes the shape follow the wrong body part.
- The move can save without being used until an Attack Set references it.
