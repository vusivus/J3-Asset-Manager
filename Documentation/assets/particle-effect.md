# Particle Effect (`.j3effect`)

A Particle Effect produces many small visual elements over time: sparks, smoke, dust, blood spray, or a short impact burst. An **emitter** is one source of particles. A single effect can contain several emitters, such as bright sparks and slower smoke, each with its own material, texture, lifetime, and motion.

## Create and edit

Choose **Assets → Create → Effects → Particle Effect** and open the file. Set the effect's Name and Loop option. Add an emitter, assign a material or texture, and tune its particle rate, lifetime, size, speed, and color. The inspector can save and prepare a preview as fields change. Use Play/Pause, frame stepping, and the timeline to inspect the effect over its lifetime, then select Save.

![Particle Effect inspector](../images/particle-effect-inspector.png)

*Screenshot placeholder: capture one emitter's Material, Texture, Max Particles, Particles/Second, Life, Size, Velocity, Gravity, and Color fields beside the animated preview. The image should explain what an emitter controls.*

## Emitter fields

| Field group | Meaning |
| --- | --- |
| `material`, `texture` | `.j3m` and `.png`/`.dds` resources used to render particles. |
| `mesh`, `billboard` | Shape and orientation of each particle. Camera billboards face the camera; velocity options orient them with motion. |
| `maxParticles`, `particlesPerSecond` | Capacity and emission rate. Larger values can increase visual density and cost. |
| `imagesX`, `imagesY` | Sprite sheet columns and rows when a texture atlas is used. |
| `lowLife`, `highLife` | Minimum and maximum particle lifetime. |
| `startSize`, `endSize` | Size change over each particle's life. |
| `startSpeed`, `endSpeed` | Speed change over life. |
| `minVelocity`, `maxVelocity` | Range of initial X/Y/Z motion; enter comma-separated triples in the inspector. |
| `gravity` | X/Y/Z acceleration applied to particles. |
| `startColor`, `endColor`, `startAlpha`, `endAlpha` | Color and opacity change over life. |

Loop controls whether the effect repeats. For a brief impact, turn Loop off and give particles a short lifetime. For continuous smoke, Loop may be appropriate. Reference the effect in [Attack Effects](attack-effects.md) where a combat outcome needs it.
