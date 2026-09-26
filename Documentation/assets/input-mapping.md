# Input Mapping (`.j3input`)

An Input Mapping translates a physical key, button, or axis into a named gameplay event. Game code or a movement controller can respond to the event without hard-coding the device control into every system. A binding can be digital (press/release) or analog (continuous value).

## Create and edit

Choose **Assets → Create → Input → Input Mapping** and open the file. The inspector shows an input schema or device choice, native event groups, and custom events. Add a binding to the desired event, choose its physical trigger, and set Scale where the event is analog. The inspector saves changes as you edit. Link the file in a [Movement Controller](movement-controller.md).

![Input Mapping inspector](../images/input-mapping-inspector.png)

*Screenshot placeholder: show a named native event with a key or button binding, an analog event with Scale, and the Event Class field. The image should teach the distinction between gameplay event and physical trigger.*

## Fields

| Field | Meaning |
| --- | --- |
| `name` | Human-readable scheme name. |
| `eventClass` | Qualified Java interface name generated for strongly named input events. Review it before relying on generated code. |
| `device` | Input family or schema, such as Keyboard. |
| `bindings[].event` | Logical game event produced by the binding. |
| `bindings[].trigger` | Physical key, button, or axis that invokes the event. |
| `bindings[].scale` | Multiplier for an analog value; a negative scale can invert a direction. |
| `bindings[].analog` | Whether the binding carries a continuous value. |
| `bindings[].custom` | Marks a user-authored event rather than a predefined native one. |

For example, two keyboard keys can map to the same “Move Forward” event, or a gamepad axis can supply a scaled analog movement value. If movement behaves in the wrong direction, inspect the trigger and scale before changing the movement controller's speed.
