# Material (`.j3m`)

A material describes how a model surface is rendered: base color, metallic response, roughness, and texture inputs. It affects appearance rather than movement or combat rules. J3 Asset Manager can create a jMonkeyEngine PBR material, inspect materials, and edit materials embedded in an imported `.j3model`.

## Create and edit

Choose **Assets → Create → Materials → Material**. The new `.j3m` starts with a PBR lighting definition, white base color, metallic `0`, and roughness `1`. Open the file to inspect and adjust its properties. For a model with embedded material bindings, open the [Imported Model](model-asset.md), select a geometry row, and edit that surface's material in the embedded material inspector.

![Material inspector](../images/material-inspector.png)

*Screenshot placeholder: show a selected surface, Base Color, Metallic, Roughness, and relevant texture inputs beside the model preview. The image should show how a material changes appearance.*

## PBR basics

- **Base Color** is the visible color before lighting effects.
- **Metallic** controls whether the surface behaves more like a metal or a nonmetal.
- **Roughness** controls how broad or sharp highlights appear. Higher roughness looks less polished.
- **Texture maps** can vary these properties across the surface. Their channels and color spaces must match the material definition.

The editor includes tools for PBR map generation and channel packing. Use them to prepare textures, then verify the result under representative lighting in the model preview.
