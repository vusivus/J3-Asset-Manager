# Example coverage and verification

The older documentation provided a runtime introduction and asset field guides, but not code examples for every asset. This example set fills that gap using the local v1.1 source as the API reference.

- [Runtime setup and integration](runtime.md)
- [All 44 asset extensions and aliases](assets.md)
- [Application source](RuntimeExample.java)
- [Typed loading source](AssetLoadingExamples.java)
- [Scene construction source](SceneExample.java)

Coverage includes every entry in `InitialAssetCatalog`, imported model/animation/material containers, scenes, curves, registered behaviour/state/action assets, and legacy loader aliases. Unregistered types have explicit decoding examples and are marked as requiring game-side implementation. This does not claim automatic gameplay execution for every editor asset.

The application, typed loading examples, and scene helper were compiled with `javac --release 21` against the rebuilt v1.1 distribution libraries. They were not run with a sample content pack; provide your authored assets and their dependencies before launching. Examples do not bundle models, textures, animations or a physics test level.

Regenerate the per-asset reference from a local source checkout with:

```text
python tools/build-example-docs.py PATH_TO_J3_ASSET_MANAGER_SOURCE
```

The public GitHub page could not be retrieved during this audit. Verification used this local GitHub repository and the local source project; these documentation changes are ready for the repository owner to review and publish.
