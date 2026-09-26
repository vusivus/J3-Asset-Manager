# Characters and models

For step-by-step creation and every Character inspector field, read [Character (`.j3char`)](character-asset.md). For imported model materials and skeleton references, read [Imported Model (`.j3model`)](model-asset.md) and [Skeletal Mapping (`.j3skel`)](skeletal-mapping.md).

Character and model assets connect source geometry and skeleton data with game-facing configuration. A character definition can reference supporting assets such as model metadata, movement, animation, combat, and damage settings, depending on the schema version.

![Character setup concept](../images/character-test-and-animation-concept.png)

*Concept: show character setup beside an animation preview so model configuration and its result can be reviewed together.*

## Character asset

The `.j3char` format represents a character definition. Use it to bring together the character's model and the supported gameplay modules. Keep module references explicit so the character can be reviewed without hunting through code.

![Character inspector](../images/character-inspector.png)

*Screenshot placeholder: show a character asset selected in the editor, with its model and gameplay-module references visible. The image should explain how a character is assembled from reusable assets.*

## Model metadata and skeletons

The `.j3model` and `.j3skel` concepts support model metadata and skeleton mapping workflows. These are useful when a model's hierarchy or joint names need to be described for animation and character use. Verify mappings against the source model before relying on them in game.

![Model and skeleton inspector](../images/model-skeleton-inspector.png)

*Screenshot placeholder: show the model hierarchy or skeleton mapping controls and the resulting character preview. The image should make the relationship between source joints and mapped joints clear.*

## Character preview

Previewing a model helps catch missing references, unexpected scale, and skeleton issues early. A preview is an authoring aid; it does not guarantee identical results in every runtime scene.

## Related concepts

- [Animation and locomotion](animation.md)
- [Movement and input](movement-input.md)
- [Combat and weapons](combat.md)
