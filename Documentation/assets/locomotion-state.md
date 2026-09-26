# Locomotion State (`.j3loco`)

Locomotion means the animations used while a character stands, walks, runs, turns, jumps, targets another character, or uses cover. A Locomotion State collects those clip references and movement speeds in one asset. The current format has separate Standing and Crouching tabs with the same types of fields, plus shared jump fields.

## Create and edit

Create the relevant [Animation Clips](animation-clip.md) first. Choose **Assets → Create → Animation → Locomotion State** and open the file. Start with the Standing tab: set Idle 1, Walk Forward, and Run Forward. Add turning, targeting, cover, and crouching clips as they become available. The inspector saves edited fields; review its status after changes. Assign this asset in a [Movement Controller](movement-controller.md) or a Weapon Definition's locomotion override.

![Locomotion State inspector](../images/locomotion-state-inspector.png)

*Screenshot placeholder: show the Standing and Crouching tabs, Basic Movement section, Targeting section, and Shared Jump fields. The image should show that one asset groups many related animation states.*

## Standing and crouching fields

| Group | Fields and purpose |
| --- | --- |
| Basic Movement | `idle1–3` provide a primary idle and optional variations; `walkForward` and `runForward` are movement clips. Variation Min/Max delays control how often an idle variation may be chosen. Base Walk/Run speeds describe travel rates. |
| Turning | Left/Right 90° and 180° clips provide deliberate turns. Use Root Motion says whether authored animation movement should drive the turn. |
| Targeting | Idle plus Forward, Backward, Left, and Right clips for moving relative to a selected target. Base Move Speed sets the target-focused travel rate. |
| Cover | Enter, idle, move, peek, and exit clips for left and right sides, plus a cover movement speed. |
| Playback | Transition Duration, Animation Speed, and Match Animation to Movement Speed tune blends and foot speed. |

The Standing and Crouching tabs are separate; filling one does not automatically populate the other. An empty optional clip may use runtime fallback behavior or show no special animation, depending on the current implementation.

## Shared jump fields

`jumpStart`, `jumpLoop`, and `jumpLanding` cover takeoff, airborne travel, and landing. `baseJumpUpForce` controls upward launch, `heavyLandingMinImpactSpeed` chooses when a harder landing is warranted, and `landingLockDuration` describes a brief lock after landing.

Start with a small working set and preview it on the intended character. Missing or incompatible clips are more noticeable when a character changes state than while standing still.
