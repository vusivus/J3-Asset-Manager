# AI, levels, and effects

For field guides, read [Agent Profile](agent-profile.md), [AI role configurations](ai-role-configurations.md), [supporting AI assets](ai-supporting-assets.md), [Game Level](level.md), [Enemy Wave](wave.md), and [Particle Effect](particle-effect.md). The [AI behaviour system](behaviours.md) explains the planned goal → state → action model.

The project includes asset concepts for describing enemy roles, reusable AI data, encounter composition, and effects. These assets can help keep game-specific configuration outside of hard-coded systems.

## AI configuration

AI-related formats in the project include `.j3enemy`, `.j3social`, `.j3memory`, and `.j3inventory`. They represent different parts of an agent's configuration, such as role, social behavior, remembered data, or carried items. Their exact runtime behavior depends on the current integration.

![AI asset inspector](../images/ai-asset-inspector.png)

*Screenshot placeholder: show an AI or enemy asset with its role and references to related behavior or inventory assets. The image should show how an agent configuration is assembled.*

## Levels and waves

The `.j3level` and `.j3wave` concepts represent level and encounter setup. Use references to keep a level's composition understandable and to reuse wave definitions where practical.

![Level and wave inspector](../images/level-wave-inspector.png)

*Screenshot placeholder: show a level asset and its ordered wave or encounter references. The image should explain how encounter content is organized.*

## Effects

The `.j3effect` concept supports reusable effect configuration and preview workflows. Effect appearance depends on its referenced materials, textures, and runtime support.

![Effect preview editor](../images/effect-preview-editor.png)

*Screenshot placeholder: show an effect asset with its preview, editable properties, and any referenced material or texture. The image should show how an effect is inspected before runtime use.*

## Related concepts

- [Combat and weapons](combat.md)
- [Project and editor concepts](../project-and-editor.md)
