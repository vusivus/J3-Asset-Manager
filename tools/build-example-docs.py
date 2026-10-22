"""Build asset example coverage from the local v1.1 Java sources."""
from pathlib import Path
import re
import sys

repo = Path(__file__).resolve().parents[1]
if len(sys.argv) != 2:
    raise SystemExit('Usage: python tools/build-example-docs.py PATH_TO_J3_ASSET_MANAGER_SOURCE')
src = Path(sys.argv[1]).resolve()
core = src / 'J3AssetManagerCore/src/main/java'
runtime = src / 'J3Runtime/src/main/java'
out = repo / 'Documentation/examples'
out.mkdir(parents=True, exist_ok=True)
catalog = (core / 'com/jme/j3asset/core/asset/InitialAssetCatalog.java').read_text()
entries = re.findall(r'(?:nativeType|type)\("[^"]+", "([^"]+)", "(j3[^"]+)"', catalog)
entries.append(('Character', 'j3char'))
entries += [('Imported model', 'j3model'), ('Animation library', 'j3anim'), ('Embedded material', 'j3mat'), ('Curve', 'j3curve'), ('Behaviour', 'j3behaviour'), ('State', 'j3state'), ('Action', 'j3action')]
entries += [('Legacy melee alias', 'j3attack'), ('Camera profile alias', 'j3camera')]
entries = list(dict((ext, name) for name, ext in entries).items())
registration = (runtime / 'com/jme/j3asset/runtime/J3Runtime.java').read_text()
loaders = {}
for loader, extensions in re.findall(r'registerLoader\((\w+)\.class, ([^;]+)\);', registration):
    path = runtime / f'com/jme/j3asset/runtime/asset/{loader}.java'
    if path.exists():
        text = path.read_text()
        match = re.search(r'extends JsonAssetLoader<(\w+)>', text)
        result = match.group(1) if match else {'J3ClipLoader':'J3AnimationClipAsset', 'J3AnimationLoader':'Spatial', 'J3ModelLoader':'Spatial', 'J3RigLoader':'Spatial', 'J3MaterialLoader':'Material', 'J3EffectLoader':'Node'}.get(loader, 'Object')
        for ext in re.findall(r'"(j3\w+)"', extensions):
            loaders[ext] = (loader, result, text)

consumers = {
'j3char':'Pass this key to `JmeCharacters.spawn`; see the character example.',
'j3level':'Pass this key to `LevelSession.load`; update and close the session as shown in the level example.',
'j3wave':'Reference the wave from a `.j3level`; `LevelSession` owns encounter spawning and progression.',
'j3weapon':'Pass the weapon key to the spawned character\'s `combat().equipWeapon`.',
'j3combat':'Reference from the character combat profile; character spawning constructs `CombatControl`.',
'j3damage':'Reference from the character damage profile; spawning constructs damage and hurtbox controls.',
'j3move':'Reference from the character movement profile; spawning wires movement to physics.',
'j3input':'Reference from movement settings. Player spawning configures input; avoid installing the same bindings twice.',
'j3loco':'Reference from movement settings; select compatible clip assets for movement states.',
'j3clip':'Pass the clip key to `J3AnimationPlayer.play`; see the playback example.',
'j3anim':'Use as an animation library with `J3AnimationPlayer.playLibraryClip`; loading alone does not start playback.',
'j3skel':'Supply the mapping to the `J3AnimationPlayer` constructor when explicit target mapping is needed.',
'j3rig':'Load the embedded rig as a model, or construct `J3AnimationPlayer` with its key.',
'j3melee':'Reference from an attack set; trigger through `CombatControl.onPrimaryAttack` or `onSecondaryAttack`.',
'j3firearm':'Reference from a weapon firearm configuration; use the combat controls rather than implementing a second firing loop.',
'j3attackset':'Reference from a weapon attack-set slot to make its moves available to combat.',
'j3attackfx':'Reference from the attack that should play its sounds and effects.',
'j3hurtbox':'Reference from a damage profile for receiving hit regions.',
'j3striker':'Reference from a weapon to define offensive collision shapes.',
'j3reaction':'Reference from a damage profile to select hit and knockdown reactions.',
'j3agent':'Reference from a character agent profile. Agent behaviours can reference behaviour/state/action definitions.',
'j3behaviour':'Reference from an agent profile; behaviour processing requires a resolver, action registry, context, and fallback AI.',
'j3state':'Reference from a behaviour; a loaded state definition does not run by itself.',
'j3action':'Reference from a state and provide matching action implementations in the runtime action registry.',
'j3car':'Use `J3VehicleFactory.create` with an initialized physics space; see the vehicle example.',
'j3cam':'Reference from a scene camera or character camera configuration. Reading a profile does not automatically replace the application camera.',
'j3model':'Attach the loaded Spatial to the scene graph. The loader reconstructs embedded materials.',
'j3mat':'Apply the loaded Material to a Geometry with `setMaterial`.',
'j3effect':'Attach the loaded particle Node to the scene graph so its controls can update.',
}
special = {
'j3scene': ('com.jme.j3asset.core.scene.J3SceneAsset', 'J3SceneAsset.load(file)', 'Read the scene document with Core; instantiate its linked content using `J3SceneLoader` from J3AssetManagerJme. See the scene example.'),
'j3curve': ('com.jme.j3asset.core.scene.J3CurveAsset', 'J3CurveAsset.load(file)', 'Read a curve for game path logic or reference it from a scene curve-array modifier.'),
}
header = '''# Java examples for every J3 asset

These examples were audited against the local v1.1 source and loader registration. They use `com.jme.j3asset` packages. Example asset paths are placeholders: create the assets in the editor and replace the keys with paths relative to your game's asset root.

Start with [runtime setup and complete application examples](runtime.md). The table below covers every Create Asset menu entry, imported containers, and registered behaviour types. A readable definition is not the same as a running gameplay system. Each section explains the consumer or the implementation gap.

The registration in `J3Runtime.registerLoaders` is authoritative for automatic loading. Structured binary assets contain an encoded JSON payload: use `BinaryAssetCodec`, not `Files.readString`. Native `.j3o` and `.j3m` use jMonkeyEngine loaders. `.j3anim` is a binary animation library, not a GLB renamed to another extension.

## Coverage index

| Asset | Extension | Example |
| --- | --- | --- |
'''
sections = []
imports = set()
methods = []
for ext, name in entries:
    header += f'| {name} | `.{ext}` | [{name}](#{ext}) |\n'
    section = f'\n## {ext}\n\n**{name} (`.{ext}`)**\n\n'
    if ext in loaders:
        loader, typ, text = loaders[ext]
        imported = re.search(r'import ([\w.]+\.' + re.escape(typ) + r');', text)
        fq = imported.group(1) if imported else {'Spatial':'com.jme3.scene.Spatial','Node':'com.jme3.scene.Node','Material':'com.jme3.material.Material','Object':'java.lang.Object'}.get(typ)
        if fq:
            imports.add(fq)
        code = f'{typ} definition = ({typ}) assets.loadAsset("Examples/Sample.{ext}");'
        section += f'Registered loader: `{loader}`. Returned value: `{typ}`.\n\n```java\n'
        if fq and typ != 'Object': section += f'import {fq};\n\n'
        section += code + '\n```\n\n' + consumers.get(ext, 'Read the definition and connect it to the consuming gameplay system.') + '\n'
        methods.append(f'    public static {typ} {ext}(AssetManager assets) {{ return ({typ}) assets.loadAsset("Examples/Sample.{ext}"); }}')
    elif ext in special:
        fq, expression, consumer = special[ext]
        section += f'```java\nimport {fq};\nimport java.nio.file.Path;\n\nPath file = Path.of("assets/Examples/Sample.{ext}");\nvar definition = {expression};\n```\n\n{consumer}\n'
    elif ext == 'j3m':
        section += '```java\nimport com.jme3.material.Material;\n\nMaterial material = assets.loadMaterial("Materials/Wall.j3m");\ngeometry.setMaterial(material);\n```\n\n`assets` is an AssetManager and `geometry` is the Geometry to receive the material. This uses the standard jME material loader.\n'
    else:
        section += f'''This editor asset has **no loader registered by `J3Runtime.registerLoaders`**. Read its encoded definition explicitly; do not assume `assets.loadAsset` supports the extension.

```java
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.jme.j3asset.core.asset.BinaryAssetCodec;
import java.nio.file.Path;

JsonObject definition = JsonParser.parseString(BinaryAssetCodec.readString(
        Path.of("assets/Examples/Sample.{ext}"))).getAsJsonObject();
```

This reads configuration only. Your game must interpret it and provide the corresponding behaviour; this example does not claim an automatic runtime executor for this asset. Keep the file in the editor's authored format when editing it.
'''
    sections.append(section)
(out/'assets.md').write_text(header + ''.join(sections), encoding='utf-8')
java = 'package examples;\n\nimport com.jme3.asset.AssetManager;\n' + ''.join(f'import {i};\n' for i in sorted(imports) if i != 'java.lang.Object')
java += '\n/** Loader examples only: replace sample keys with your authored assets. */\npublic final class AssetLoadingExamples {\n' + '\n'.join(methods) + '\n}\n'
(out/'AssetLoadingExamples.java').write_text(java, encoding='utf-8')
print(f'Generated coverage for {len(entries)} extensions; {len(loaders)} registered J3 extensions.')
guide_map = {
 'j3wave':'wave', 'j3level':'level', 'j3m':'material', 'j3effect':'particle-effect',
 'j3skel':'skeletal-mapping', 'j3clip':'animation-clip', 'j3loco':'locomotion-state',
 'j3combat':'combat-controller', 'j3damage':'damage-controller', 'j3melee':'melee-attack',
 'j3firearm':'firearm-attack', 'j3attackset':'attack-set', 'j3charge':'attack-charge',
 'j3attackfx':'attack-effects', 'j3hurtbox':'hurtbox', 'j3reaction':'reaction',
 'j3weapon':'weapon', 'j3striker':'striker', 'j3char':'character-asset', 'j3car':'vehicle',
 'j3agent':'agent-profile', 'j3move':'movement-controller', 'j3input':'input-mapping',
 'j3model':'model-asset', 'j3behaviour':'behaviours', 'j3grapple':'grapple-finisher',
 'j3memory':'ai-supporting-assets', 'j3enemy':'ai-role-configurations'
}
for ext, guide in guide_map.items():
    path = repo / f'Documentation/assets/{guide}.md'
    if path.exists():
        text = path.read_text(encoding='utf-8-sig')
        if '## Java example' not in text:
            text = text.rstrip() + f'\n\n## Java example\n\nSee [loading and using this asset](../examples/assets.md#{ext}) and the [runtime integration examples](../examples/runtime.md) for Java code, required setup, and runtime support limitations.\n'
            path.write_text(text, encoding='utf-8')
