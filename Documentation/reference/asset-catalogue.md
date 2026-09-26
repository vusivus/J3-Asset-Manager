# Asset catalogue

This table follows the **current Create Asset menu** in `InitialAssetCatalog`. “Create” means the editor creates a file and may open an inspector. It does not guarantee complete runtime support. The [field guides](../index.md#asset-field-guides) explain the most developed authoring paths.

| Menu item | Extension | Purpose | Guide |
| --- | --- | --- | --- |
| Enemy Wave | `.j3wave` | Enemy spawns and encounter pacing | [Wave](../assets/wave.md) |
| Game Level | `.j3level` | Scene, player entry, ordered waves | [Level](../assets/level.md) |
| Material | `.j3m` | jMonkeyEngine material | [Material](../assets/material.md) |
| Particle Effect | `.j3effect` | Particle emitters and preview | [Effect](../assets/particle-effect.md) |
| Skeletal Mapping | `.j3skel` | Humanoid role to model joint mapping | [Skeleton](../assets/skeletal-mapping.md) |
| Animation Clip | `.j3clip` | Reusable animation range and playback | [Clip](../assets/animation-clip.md) |
| Locomotion State | `.j3loco` | Standing, crouching, targeting, cover, jump | [Locomotion](../assets/locomotion-state.md) |
| Combat Controller | `.j3combat` | Default BareFists weapon | [Combat Controller](../assets/combat-controller.md) |
| Damage Controller | `.j3damage` | Hurtbox and reaction links | [Damage Controller](../assets/damage-controller.md) |
| Melee Attack | `.j3melee` | One melee move and its timing | [Melee Attack](../assets/melee-attack.md) |
| Firearm Attack | `.j3firearm` | One firearm shot configuration | [Firearm Attack](../assets/firearm-attack.md) |
| Attack Set | `.j3attackset` | Move selection for one role | [Attack Set](../assets/attack-set.md) |
| Attack Charge | `.j3charge` | Hold and approach-dash tuning | [Charge](../assets/attack-charge.md) |
| Attack Effects | `.j3attackfx` | Sounds, effects, trails, hit pause | [Effects](../assets/attack-effects.md) |
| Hurtbox Profile | `.j3hurtbox` | Receiving body regions | [Hurtbox](../assets/hurtbox.md) |
| Reaction Data | `.j3reaction` | Hit and knockdown responses | [Reaction](../assets/reaction.md) |
| Grapple | `.j3grapple` | Grapple configuration draft | [Grapple and Finisher](../assets/grapple-finisher.md) |
| Finisher | `.j3finisher` | Finisher configuration draft | [Grapple and Finisher](../assets/grapple-finisher.md) |
| Weapon Definition | `.j3weapon` | Equipment, attack sets, strikers | [Weapon](../assets/weapon.md) |
| Striker | `.j3striker` | Offensive collision shape | [Striker](../assets/striker.md) |
| Character | `.j3char` | Model and gameplay modules | [Character](../assets/character-asset.md) |
| Vehicle Definition | `.j3car` | Vehicle configuration draft | [Vehicle](../assets/vehicle.md) |
| Agent Profile | `.j3agent` | AI thinking and perception profile | [Agent](../assets/agent-profile.md) |
| Memory Template | `.j3memory` | AI memory configuration | [Supporting AI assets](../assets/ai-supporting-assets.md) |
| AI Inventory | `.j3inventory` | Inventory or stash configuration | [Supporting AI assets](../assets/ai-supporting-assets.md) |
| Enemy Configuration | `.j3enemy` | Enemy role and weapon preferences | [AI role configurations](../assets/ai-role-configurations.md) |
| Police Configuration | `.j3police` | Police role and authority settings | [AI role configurations](../assets/ai-role-configurations.md) |
| Civilian Configuration | `.j3civilian` | Civilian activity and danger response | [AI role configurations](../assets/ai-role-configurations.md) |
| Traffic Configuration | `.j3traffic` | Driver and route tuning | [AI role configurations](../assets/ai-role-configurations.md) |
| Social Performance | `.j3social` | Social audio, gestures, and responses | [Supporting AI assets](../assets/ai-supporting-assets.md) |
| Movement Controller | `.j3move` | Input, locomotion, rotation, targeting | [Movement](../assets/movement-controller.md) |
| Input Mapping | `.j3input` | Device bindings to gameplay events | [Input](../assets/input-mapping.md) |

The editor also imports model and animation resources. An imported `.j3model` is described in the [model guide](../assets/model-asset.md). `.j3behaviour`, `.j3state`, and `.j3action` have core design models but are **not** entries in the current Create Asset menu. They are discussed as design direction in the [AI behaviour guide](../assets/behaviours.md).
