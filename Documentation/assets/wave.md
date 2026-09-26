# Enemy Wave (`.j3wave`)

An Enemy Wave describes one group of enemies to introduce during a level. It records when the wave starts, where each enemy appears, which character and optional weapon each spawn uses, and several combat pacing values. A Game Level can reuse and order wave assets.

## Create and edit

Choose **Assets → Create → Waves → Enemy Wave** and open the file. Set the delay and combat pacing fields. Use **Add Enemy** for each spawn, choose its `.j3char` Character and optional `.j3weapon` override, then set X, Y, Z feet position and yaw. Save and reference the Wave from a [Game Level](level.md).

![Enemy Wave inspector](../images/enemy-wave-inspector.png)

*Screenshot placeholder: show wave delays, simultaneous attacker count, combat radius, attack distance, cooldown, and one enemy spawn row. The image should explain a wave as a reusable encounter group.*

## Fields

| Field | Meaning |
| --- | --- |
| `startDelay` | Seconds before this wave begins. Cannot be negative. |
| `nextWaveDelay` | Delay associated with progression to the following wave. Cannot be negative. |
| `simultaneousAttackers` | Desired cap from `1–6` for attackers committing at once. |
| `combatRadius` | Radius for combat positioning. Must be positive and at least the attack distance. |
| `attackDistance` | Distance used for attack positioning; must be positive. |
| `attackCooldown` | Minimum authored pause between attack opportunities; must be positive. |
| `enemies[]` | Up to 100 spawn entries. Each needs a `.j3char`; the weapon override is optional. |
| Spawn `x/y/z`, `yaw` | World-space feet position and facing angle for that enemy. |

The values describe encounter pressure and placement. Actual enemy decision making depends on the runtime AI and combat coordinator. A wave can validate but still feel crowded if spawn points are too close; preview and test it in the scene.
