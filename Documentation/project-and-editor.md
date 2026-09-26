# Project and editor concepts

J3 Asset Manager is organized around a game project. The project browser provides access to files; selecting a supported asset opens its specialized inspector. The inspector edits the asset's structured properties and references, while preview tools help check visual or animation results where available.

## Typical workflow

1. Open a game project and locate or import source assets.
2. Create a J3 asset for the system you want to configure.
3. Set its values and references in the matching inspector.
4. Review validation feedback and use previews where supported.
5. Save the asset and load it through the appropriate runtime or jMonkeyEngine integration.

![Project browser and asset inspector](images/project-browser-inspector.png)

*Screenshot placeholder: show the project tree, a selected J3 asset, its inspector fields, and any validation or status feedback. The image should help readers identify where to find and edit project assets.*

## Editor areas

| Area | Purpose |
| --- | --- |
| Project browser | Browse project files and select assets. |
| Asset inspector | Edit the selected asset's properties and references. |
| Scene or model preview | Inspect supported models, animation, or effect previews. |
| Status and validation | Surface save, reference, and asset validation feedback. |
| Tools | Open focused utilities such as animation, texture, or material workflows. |

The exact layout and supported tools may change as development continues. Screenshots should be captured from the current build and labeled with the version or commit when practical.

## Saving and references

J3 assets are intended to hold reusable configuration and references to other project resources. Keep referenced files inside the project where possible, use descriptive names, and resolve validation messages before relying on an asset at runtime. The runtime integration and file support vary by asset type.

## Current maturity

The repository contains editor UI, core asset services, jMonkeyEngine integration, controls, and runtime modules. A file type existing in source does not guarantee a finished workflow. Treat the application and the individual concept pages as the authoritative guide to what is currently usable.
