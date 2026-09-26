# Animation and locomotion

Use [Animation Clip (`.j3clip`)](animation-clip.md) for clip creation and field meanings, and [Locomotion State (`.j3loco`)](locomotion-state.md) for standing, crouching, targeting, cover, and jump authoring.

Animation assets describe reusable clips and how motion can be selected or blended. A typical workflow starts with a source model and animation, defines a clip range, then uses that clip in a locomotion setup or character configuration.

## Animation clips

The `.j3clip` concept describes a named animation range from a source animation. Clip boundaries, names, and playback settings should be checked against the source asset; incorrect ranges can produce foot sliding, abrupt transitions, or empty playback.

![Animation clip editor](../images/animation-clip-editor.png)

*Screenshot placeholder: show the source animation, clip range markers, clip properties, and playback controls. The image should explain how a reusable clip is selected and previewed.*

## Locomotion

The `.j3loco` concept groups animation choices for movement states or directions. It lets character movement refer to animation configuration without embedding every clip choice in gameplay code.

![Locomotion inspector](../images/locomotion-inspector.png)

*Screenshot placeholder: show locomotion states or directional slots with their assigned animation clips, plus the preview state. The image should show how movement animation references are organized.*

## Skeleton compatibility

Animation playback depends on compatible skeleton hierarchies and joint transforms. Mapping tools can help identify relationships between skeletons, but retargeted output should always be previewed on the intended model and checked in the target runtime.

## Related concepts

- [Characters and models](characters.md)
- [Movement and input](movement-input.md)
