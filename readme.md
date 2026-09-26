# J3 Asset Manager documentation

J3 Asset Manager is a desktop editor for building jMonkeyEngine game assets. It lets you import and inspect models, configure characters, edit animation and movement, and assemble combat and encounter data from reusable J3 assets. The project also contains a J3 runtime library that loads supported assets in a game.

If you are new to game authoring, start with [how assets work](Documentation/getting-started/how-assets-work.md) and [creating an asset](Documentation/getting-started/create-and-edit.md). The guides explain ideas such as hitboxes and attack phases before introducing the editor fields.

![J3 Asset Manager character workflow concept](Documentation/images/J3%20Asset%20Manager%20Window.png)

*Concept illustration: character setup*

## Usage examples

[![Watch usage example 1](https://img.youtube.com/vi/TeCz-RBquhM/0.jpg)](https://www.youtube.com/watch?v=TeCz-RBquhM)

[![Watch usage example 2](https://img.youtube.com/vi/tHozf9721-c/0.jpg)](https://www.youtube.com/watch?v=tHozf9721-c)

## Use J3Runtime in your game

The editor's runtime library lets a jMonkeyEngine game load J3 assets, spawn configured characters, and run levels. Download [J3Runtime-1.0.jar](Distributions/J3Runtime/J3Runtime-1.0.jar) and [J3AssetManagerCore-1.0.jar](Distributions/J3Runtime/J3AssetManagerCore-1.0.jar), or copy them from the `libraries` folder in a J3 Asset Manager v1.0 distribution ZIP. Read [Use J3Runtime in a jMonkeyEngine game](Documentation/getting-started/use-j3runtime.md) for dependencies, asset placement, and Java code examples.

## What you build with it

Imagine a character that can throw a punch. You import a model and animation, describe the punch in a **Melee Attack**, and give the move a **Striker**: a small invisible shape that follows the fist while the punch can hit. The target has **Hurtboxes**, invisible receiving regions such as a torso and head. An **Attack Set** assigns the punch to a weapon action; a **Weapon Definition** and **Combat Controller** connect that action to the attacker. A **Damage Controller** connects the target to its hurtboxes and hit reactions. Finally, **Character** assets collect these settings for use by the game.

This is why the editor uses several small files instead of one large character file. You can reuse a move, weapon, or reaction setup, inspect each part separately, and see which reference is missing. Follow the [first melee character walkthrough](Documentation/getting-started/first-melee-character.md) to assemble the chain. The [hit detection guide](Documentation/assets/hit-detection.md) explains the collision terms with a diagram and a worked punch example.

## Start here

1. [What a J3 asset is](Documentation/getting-started/how-assets-work.md)
2. [Create, open, edit, and save an asset](Documentation/getting-started/create-and-edit.md)
3. [Choose and link other assets](Documentation/getting-started/references.md)
4. [Build a first melee character](Documentation/getting-started/first-melee-character.md)
5. [Find your way around the project and editor](Documentation/project-and-editor.md)

## Learn the systems

- [Characters and models](Documentation/assets/characters.md)
- [Animation and locomotion](Documentation/assets/animation.md)
- [Movement and input](Documentation/assets/movement-input.md)
- [Combat and weapons](Documentation/assets/combat.md)
- [Hit detection: hitboxes, strikers, and hurtboxes](Documentation/assets/hit-detection.md)
- [AI behaviour system](Documentation/assets/behaviours.md)
- [Levels, waves, and effects](Documentation/assets/world-ai-effects.md)

## Asset field guides

| Combat | Character and movement | World and AI |
| --- | --- | --- |
| [Melee Attack](Documentation/assets/melee-attack.md) | [Character](Documentation/assets/character-asset.md) | [Agent Profile](Documentation/assets/agent-profile.md) |
| [Attack Set](Documentation/assets/attack-set.md) | [Animation Clip](Documentation/assets/animation-clip.md) | [Game Level](Documentation/assets/level.md) |
| [Weapon Definition](Documentation/assets/weapon.md) | [Locomotion State](Documentation/assets/locomotion-state.md) | [Enemy Wave](Documentation/assets/wave.md) |
| [Striker](Documentation/assets/striker.md) | [Movement Controller](Documentation/assets/movement-controller.md) | [Particle Effect](Documentation/assets/particle-effect.md) |
| [Hurtbox Profile](Documentation/assets/hurtbox.md) | [Input Mapping](Documentation/assets/input-mapping.md) | |
| [Combat Controller](Documentation/assets/combat-controller.md) | [Skeletal Mapping](Documentation/assets/skeletal-mapping.md) | |
| [Damage Controller](Documentation/assets/damage-controller.md) | | |
| [Reaction Data](Documentation/assets/reaction.md) | | |
| [Firearm Attack](Documentation/assets/firearm-attack.md) | | |
| [Attack Charge](Documentation/assets/attack-charge.md) | | |
| [Attack Effects](Documentation/assets/attack-effects.md) | | |

For every file type, see the [asset catalogue](Documentation/reference/asset-catalogue.md). The [glossary](Documentation/reference/glossary.md) defines terms used across the guides.

Additional guides: [Imported Model](Documentation/assets/model-asset.md), [Material](Documentation/assets/material.md), [AI role configurations](Documentation/assets/ai-role-configurations.md), [Memory, inventory, and social assets](Documentation/assets/ai-supporting-assets.md), [Vehicle Definition](Documentation/assets/vehicle.md), and [Grapple and Finisher drafts](Documentation/assets/grapple-finisher.md).

## Features

- Project browser, asset creation menu, typed inspectors, project asset pickers, and validation feedback.
- Model import and preview; character setup; animation clip, skeleton mapping, and locomotion editing.
- Movement and input configuration; melee, firearm, weapon, damage, reaction, and encounter assets.
- Texture and material tools, particle effects, and editor previews where available.

These features develop at different rates. A type appearing in the Create Asset menu means the editor can create a file; it does not by itself establish complete runtime behavior. The field guides describe the current editor and mark design work separately.

## License

J3 Asset Manager is licensed under the **BSD 3-Clause License**, the same license used by jMonkeyEngine. See the [LICENSE](LICENSE) file for the full license text. Third-party dependencies and bundled assets may have separate licenses; see their respective notices.

## Open-source projects used

The following open source projects contributed to the development of J3 Asset Manager. Credit goes to their authors and contributors:

- [jMonkeyEngine](https://github.com/jMonkeyEngine/jmonkeyengine) — 3D engine and asset APIs used by the editor integration and runtime.
- [Wes](https://github.com/stephengold/Wes) by Stephen Gold and contributors — animation editing and retargeting library.
- [jme-effekseerNative](https://github.com/riccardobl/jme-effekseerNative) by riccardobl and contributors — Effekseer integration for jMonkeyEngine.
- [Effekseer](https://github.com/effekseer/Effekseer) and [EffekseerForMultiLanguages](https://github.com/effekseer/EffekseerForMultiLanguages) — effect tooling and native support used through the integration.
- [OpenJFX](https://github.com/openjdk/jfx) — desktop user interface toolkit.
- [Gson](https://github.com/google/gson) — JSON serialization for asset data.

The list describes dependencies verified in the project files. It is not a complete third-party license inventory; consult the modules and dependency manifests when preparing a release.

## Support development

As of today, the project has been under development for **two months and still going** and the cost of a **ChatGPT Pro subscription** has been the main development cost. Without an AI assistant, such a project would have taken years to develop, and even with AI, it takes a lot of time and testing to get it to work to the desired outcome. The exact period, total spending, and currency have not been confirmed yet.

More funding could support a complete authoring path from imported model to playable character: clearer inspectors and validation, broader runtime support for the authored assets, complete FBX (or even OBJ) support, complete EFFEkseer support, a sample project with working combat and AI examples, packaging for more machines, and screenshots and tutorials maintained alongside releases. Those are development goals, not promises tied to a donation amount.

In the long run, a website, with an asset store could be created, with the right amount of funding.

The immediate value of a donation would be more focused development time for the gaps users encounter now: connecting assets without broken references, previewing the result in the editor, and confirming that the same data behaves as expected in a running jMonkeyEngine game. Donations are voluntary.

Currently I accept Payoneer donations (from a business account or Paypal): [Payoneer donation link](https://link.payoneer.com/Token?t=554BA3D278DB4497A12C97970D236CE7&src=pl)
