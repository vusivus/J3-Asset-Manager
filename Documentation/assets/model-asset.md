# Imported Model (`.j3model`)

A `.j3model` is an imported, editable model container. It holds a scene spatial and material assignments, and can reference a Skeletal Mapping. A [Character](character-asset.md) points to the model container for its appearance. A raw `.j3o` scene or source model is a different resource.

## Import and edit

Use **Assets → Import → Model** to bring a source model into the project. Select the resulting `.j3model` in the project browser. Its inspector shows a skeleton reference and a table of geometry and embedded materials. Choose a geometry row to edit its material properties; save the model after changes. Older model containers may need reimporting before the current embedded-material inspector can edit them.

![Imported Model inspector](../images/model-asset-inspector.png)

*Screenshot placeholder: capture a `.j3model` with its Skeleton Mapping field, geometry/material table, selected material controls, and model preview. The image should show where the model's embedded materials are edited.*

## Important parts

| Part | Meaning |
| --- | --- |
| Spatial | The imported model hierarchy and geometry. |
| Skeleton reference | Optional `.j3skel` mapping for standardized bone roles. |
| Geometry/material bindings | Links each named geometry to an embedded material definition. |

After import, check orientation, scale, skeleton, and material appearance. A model can look correct in preview but still need a Character asset for movement, collision, and combat modules.
