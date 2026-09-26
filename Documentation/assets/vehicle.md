# Vehicle Definition (`.j3car`)

A Vehicle Definition is a reusable description of a car or other vehicle in the game world. It can record its category, model, audio, wheel and seat data, and lights. A traffic agent's configuration describes how it drives; the vehicle file describes the object it drives.

## Create and edit

Choose **Assets → Create → Vehicles → Vehicle Definition**. The editor creates a structured `.j3car` document and opens it through the structured asset inspector. The default document starts with category `civilian` and traffic role `parked`. Choose a model and fill only fields supported by the project's current vehicle loader before using it in a level.

![Vehicle Definition inspector](../images/vehicle-inspector.png)

*Screenshot placeholder: show a `.j3car` in the structured inspector with its category, traffic role, model reference, and wheel/seat/light groups. The image should show a vehicle as data distinct from driver behavior.*

## Initial fields

| Field | Meaning |
| --- | --- |
| `category` | Broad vehicle class, such as civilian or another project-specific type. |
| `trafficRole` | How the vehicle is presented in traffic, initially parked. |
| `model` | Visual model reference. |
| `audio.parkedAlarm` | Optional sound for a parked alarm. |
| `wheels[]` | Wheel configuration entries. |
| `seats[]` | Occupant attachment locations and related entries. |
| `lights[]` | Vehicle lighting entries. |

The current Create Asset template provides these fields but does not establish a complete driving or vehicle physics implementation. Test the model, seating, and traffic connection against the runtime used by the game.
