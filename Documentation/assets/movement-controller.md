# Movement Controller (`.j3move`)

The Movement Controller holds input and physical movement configuration for a character. It links [Input Mappings](input-mapping.md) and a [Locomotion State](locomotion-state.md), then sets rotation, gravity, and target-selection values. The Character asset references the controller.

## Create and edit

Choose **Assets → Create → Movement → Movement Controller** and open the file. Add one or more Input Mapping references, choose a Locomotion State, set rotation and targeting values, then save. Assign the `.j3move` asset in the Character's Movement Profile field.

![Movement Controller inspector](../images/movement-controller-inspector.png)

*Screenshot placeholder: show the Inputs list, Locomotion reference, rotation and target-selection controls, and Save feedback. The image should explain where movement settings are authored.*

## Main fields

| Field | Meaning |
| --- | --- |
| `inputs[]` | `.j3input` schemes whose events this controller receives. |
| `locomotion` | `.j3loco` animation and movement profile. |
| `rotationSpeed` | How quickly the character turns in free movement. |
| `turn90Threshold`, `turn180Threshold` | Angle at which authored quarter or half turns may be chosen. |
| `targetingRotationSpeed` | Facing speed while focused on a target. |
| `gravity` | Downward acceleration; the default is negative. |
| `targetFocusEnabled` | Enables target-focused movement where supported. |
| `targetSearchRange` | Maximum distance to consider target candidates. |
| `targetVisibilityGracePeriod` | Brief period a recently occluded target may remain selected. |
| `directionalTargetSelection` | Allows movement direction to choose another target. |
| `directionalTargetDeadZone`, `directionalTargetMinimumAlignment` | Minimum input strength and alignment before a directional switch is accepted. |
| `directionalSwitchCooldown`, `manualTargetPriorityDuration` | Timing limits that reduce rapid target changes and preserve an explicit selection briefly. |

These fields tune movement and selection behavior, but the actual character still needs a valid model, physics setup, input events, and runtime controller. Test turning and target switching in a scene, especially if animations provide root motion.
