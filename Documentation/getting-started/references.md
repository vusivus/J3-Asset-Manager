# Choose and link assets

A reference is a path from one asset to another file inside the same project. For example, a `.j3weapon` file can reference an attack set, and that attack set can reference a `.j3melee` file. The references are stored as project asset keys with forward slashes.

## Use the picker

In a reference field, choose a file of the expected type from the project. The field may also support clearing a reference. List fields let you add several files; certain inspectors accept a file dragged from the project tree. Check the expected extension shown in the field guide: selecting a `.j3firearm` where `.j3melee` is expected will fail validation or be rejected by the picker.

![Asset reference picker](../images/asset-reference-picker.png)

*Screenshot placeholder: show a reference field with its file picker open and a matching J3 asset selected. The image should illustrate a project-relative reference, not a Windows absolute path.*

## Order matters when authoring

Create the files that other assets will refer to first. For a melee character, a useful order is: animation clip and striker → melee attack → attack set → weapon → combat controller → character. For receiving hits: hurtbox and reaction → damage controller → character. You can create an empty parent asset earlier, then return to fill its references.

## Keep paths portable

Use asset files under the project's assets folder. A full machine path is not a portable project asset key. If you move an asset file, inspect every reference to it and save the referring assets again. Display names are for people and should not replace the stored path.

## Optional and required references

The exact rule varies by asset. A Melee Attack can leave its charge and effects references empty. A Firearm Attack Set requires its default firearm attack. The Combat Controller inspector requires a default weapon whose category is **BareFists**. The [field guides](../index.md#asset-field-guides) call out important requirements.

When a reference is missing, the inspector may report a save error, a status message, or a runtime loading failure. A file existing on disk does not prove that it has the right type or valid content.
