# Movement and input

For creation steps and field meanings, use [Input Mapping (`.j3input`)](input-mapping.md) and [Movement Controller (`.j3move`)](movement-controller.md).

Movement and input assets separate control bindings from movement tuning. This makes it possible to reuse a movement profile while adjusting a project's control scheme independently.

## Input schemes

The `.j3input` concept maps named game actions to device inputs. Use action names that describe intent, such as move, jump, or interact, so gameplay systems can use the same action regardless of the physical key or button.

![Input scheme inspector](../images/input-scheme-inspector.png)

*Screenshot placeholder: show an input asset with action names and their keyboard or controller bindings. The image should demonstrate how a developer reviews and edits a binding.*

## Movement profiles

The `.j3move` concept describes movement settings used by a character or runtime controller. Keep tuning values together and test the result with the intended model, input scheme, and runtime integration.

![Movement profile inspector](../images/movement-profile-inspector.png)

*Screenshot placeholder: show movement settings such as speeds and relevant movement options, alongside a character preview if available. The image should show where movement tuning is authored.*

## Related concepts

- [Characters and models](characters.md)
- [Animation and locomotion](animation.md)
