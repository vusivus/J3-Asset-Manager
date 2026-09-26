# Attack Charge (`.j3charge`)

An Attack Charge describes a held preparation period and optional approach dash for a [Melee Attack](melee-attack.md). It can change movement during charging and scale the attack's output between a minimum and maximum power. The move uses it only when the `.j3melee` asset references the charge.

## Create and connect it

Choose **Assets → Create → Combat → Attack Charge**, open the file, and set the hold, dash, animation, sound, and effect fields. Save it, then assign it in the Melee Attack's **Charge** reference.

![Attack Charge inspector](../images/attack-charge-inspector.png)

*Screenshot placeholder: show Enabled, animation, dash distance and speed, hold time, movement multiplier, power range, sound, and effect fields. The image should explain what can change while an attack is charging.*

## Fields

| Field | Meaning |
| --- | --- |
| `enabled` | Whether the charge configuration is active. |
| `animation`, `animationSpeed` | Optional `.j3clip` and playback speed while charging. Speed must be at least `0.05`. |
| `dashDistance`, `dashSpeed`, `stoppingDistance` | How far and how quickly an approach dash moves, and how close it should stop. Distances cannot be negative; dash speed must be positive. |
| `approachNearestTarget` | Directs the authored approach toward the nearest valid target where supported. |
| `minimumTime`, `maximumTime` | Allowed hold duration. Maximum must be at least minimum. |
| `movementMultiplier` | Portion of normal movement allowed while holding the charge; `0` means none, `1` full speed. |
| `minimumPower`, `maximumPower` | Power range for short to fully held charges; maximum cannot be below minimum. |
| `loopSound`, `effectPrefab` | Optional audio (`.ogg` or `.wav`) and visual `.j3o` references during charging. |

Test charged moves against nearby obstacles and moving targets. A configured approach dash should not carry the character through level geometry; actual collision and target behavior depend on the runtime.
