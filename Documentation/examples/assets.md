# Java examples for every J3 asset

These examples were audited against the local v1.1 source and loader registration. They use `com.jme.j3asset` packages. Example asset paths are placeholders: create the assets in the editor and replace the keys with paths relative to your game's asset root.

Start with [runtime setup and complete application examples](runtime.md). The table below covers every Create Asset menu entry, imported containers, and registered behaviour types. A readable definition is not the same as a running gameplay system. Each section explains the consumer or the implementation gap.

The registration in `J3Runtime.registerLoaders` is authoritative for automatic loading. Structured binary assets contain an encoded JSON payload: use `BinaryAssetCodec`, not `Files.readString`. Native `.j3o` and `.j3m` use jMonkeyEngine loaders. `.j3anim` is a binary animation library, not a GLB renamed to another extension.

## Coverage index

| Asset | Extension | Example |
| --- | --- | --- |
| Enemy Wave | `.j3wave` | [Enemy Wave](#j3wave) |
| Game Level | `.j3level` | [Game Level](#j3level) |
| Scene | `.j3scene` | [Scene](#j3scene) |
| Material | `.j3m` | [Material](#j3m) |
| Particle Effect | `.j3effect` | [Particle Effect](#j3effect) |
| Skeletal Mapping | `.j3skel` | [Skeletal Mapping](#j3skel) |
| Humanoid Rig | `.j3rig` | [Humanoid Rig](#j3rig) |
| Animation Clip | `.j3clip` | [Animation Clip](#j3clip) |
| Locomotion State | `.j3loco` | [Locomotion State](#j3loco) |
| Combat Controller | `.j3combat` | [Combat Controller](#j3combat) |
| Damage Controller | `.j3damage` | [Damage Controller](#j3damage) |
| Melee Attack | `.j3melee` | [Melee Attack](#j3melee) |
| Firearm Attack | `.j3firearm` | [Firearm Attack](#j3firearm) |
| Attack Set | `.j3attackset` | [Attack Set](#j3attackset) |
| Attack Charge | `.j3charge` | [Attack Charge](#j3charge) |
| Attack Effects | `.j3attackfx` | [Attack Effects](#j3attackfx) |
| Hurtbox Profile | `.j3hurtbox` | [Hurtbox Profile](#j3hurtbox) |
| Reaction Data | `.j3reaction` | [Reaction Data](#j3reaction) |
| Grapple | `.j3grapple` | [Grapple](#j3grapple) |
| Finisher | `.j3finisher` | [Finisher](#j3finisher) |
| Weapon Definition | `.j3weapon` | [Weapon Definition](#j3weapon) |
| Striker | `.j3striker` | [Striker](#j3striker) |
| Camera Profile | `.j3cam` | [Camera Profile](#j3cam) |
| Vehicle Definition | `.j3car` | [Vehicle Definition](#j3car) |
| Agent Profile | `.j3agent` | [Agent Profile](#j3agent) |
| Memory Template | `.j3memory` | [Memory Template](#j3memory) |
| AI Inventory | `.j3inventory` | [AI Inventory](#j3inventory) |
| Enemy Configuration | `.j3enemy` | [Enemy Configuration](#j3enemy) |
| Police Configuration | `.j3police` | [Police Configuration](#j3police) |
| Civilian Configuration | `.j3civilian` | [Civilian Configuration](#j3civilian) |
| Traffic Configuration | `.j3traffic` | [Traffic Configuration](#j3traffic) |
| Social Performance | `.j3social` | [Social Performance](#j3social) |
| Movement Controller | `.j3move` | [Movement Controller](#j3move) |
| Input Mapping | `.j3input` | [Input Mapping](#j3input) |
| Character | `.j3char` | [Character](#j3char) |
| Imported model | `.j3model` | [Imported model](#j3model) |
| Animation library | `.j3anim` | [Animation library](#j3anim) |
| Embedded material | `.j3mat` | [Embedded material](#j3mat) |
| Curve | `.j3curve` | [Curve](#j3curve) |
| Behaviour | `.j3behaviour` | [Behaviour](#j3behaviour) |
| State | `.j3state` | [State](#j3state) |
| Action | `.j3action` | [Action](#j3action) |
| Legacy melee alias | `.j3attack` | [Legacy melee alias](#j3attack) |
| Camera profile alias | `.j3camera` | [Camera profile alias](#j3camera) |

## j3wave

**Enemy Wave (`.j3wave`)**

Registered loader: `J3WaveLoader`. Returned value: `J3WaveAsset`.

```java
import com.jme.j3asset.core.level.J3WaveAsset;

J3WaveAsset definition = (J3WaveAsset) assets.loadAsset("Examples/Sample.j3wave");
```

Reference the wave from a `.j3level`; `LevelSession` owns encounter spawning and progression.

## j3level

**Game Level (`.j3level`)**

Registered loader: `J3LevelLoader`. Returned value: `J3LevelAsset`.

```java
import com.jme.j3asset.core.level.J3LevelAsset;

J3LevelAsset definition = (J3LevelAsset) assets.loadAsset("Examples/Sample.j3level");
```

Pass this key to `LevelSession.load`; update and close the session as shown in the level example.

## j3scene

**Scene (`.j3scene`)**

```java
import com.jme.j3asset.core.scene.J3SceneAsset;
import java.nio.file.Path;

Path file = Path.of("assets/Examples/Sample.j3scene");
var definition = J3SceneAsset.load(file);
```

Read the scene document with Core; instantiate its linked content using `J3SceneLoader` from J3AssetManagerJme. See the scene example.

## j3m

**Material (`.j3m`)**

```java
import com.jme3.material.Material;

Material material = assets.loadMaterial("Materials/Wall.j3m");
geometry.setMaterial(material);
```

`assets` is an AssetManager and `geometry` is the Geometry to receive the material. This uses the standard jME material loader.

## j3effect

**Particle Effect (`.j3effect`)**

Registered loader: `J3EffectLoader`. Returned value: `Node`.

```java
import com.jme3.scene.Node;

Node definition = (Node) assets.loadAsset("Examples/Sample.j3effect");
```

Attach the loaded particle Node to the scene graph so its controls can update.

## j3skel

**Skeletal Mapping (`.j3skel`)**

Registered loader: `J3SkeletonLoader`. Returned value: `SkeletalMappingAsset`.

```java
import com.jme.j3asset.core.skeleton.SkeletalMappingAsset;

SkeletalMappingAsset definition = (SkeletalMappingAsset) assets.loadAsset("Examples/Sample.j3skel");
```

Supply the mapping to the `J3AnimationPlayer` constructor when explicit target mapping is needed.

## j3rig

**Humanoid Rig (`.j3rig`)**

Registered loader: `J3RigLoader`. Returned value: `Spatial`.

```java
import com.jme3.scene.Spatial;

Spatial definition = (Spatial) assets.loadAsset("Examples/Sample.j3rig");
```

Load the embedded rig as a model, or construct `J3AnimationPlayer` with its key.

## j3clip

**Animation Clip (`.j3clip`)**

Registered loader: `J3ClipLoader`. Returned value: `J3AnimationClipAsset`.

```java
import com.jme.j3asset.core.animation.J3AnimationClipAsset;

J3AnimationClipAsset definition = (J3AnimationClipAsset) assets.loadAsset("Examples/Sample.j3clip");
```

Pass the clip key to `J3AnimationPlayer.play`; see the playback example.

## j3loco

**Locomotion State (`.j3loco`)**

Registered loader: `J3LocomotionLoader`. Returned value: `J3LocomotionAsset`.

```java
import com.jme.j3asset.core.locomotion.J3LocomotionAsset;

J3LocomotionAsset definition = (J3LocomotionAsset) assets.loadAsset("Examples/Sample.j3loco");
```

Reference from movement settings; select compatible clip assets for movement states.

## j3combat

**Combat Controller (`.j3combat`)**

Registered loader: `J3CombatLoader`. Returned value: `J3CombatAsset`.

```java
import com.jme.j3asset.core.combat.J3CombatAsset;

J3CombatAsset definition = (J3CombatAsset) assets.loadAsset("Examples/Sample.j3combat");
```

Reference from the character combat profile; character spawning constructs `CombatControl`.

## j3damage

**Damage Controller (`.j3damage`)**

Registered loader: `J3DamageLoader`. Returned value: `J3DamageAsset`.

```java
import com.jme.j3asset.core.combat.J3DamageAsset;

J3DamageAsset definition = (J3DamageAsset) assets.loadAsset("Examples/Sample.j3damage");
```

Reference from the character damage profile; spawning constructs damage and hurtbox controls.

## j3melee

**Melee Attack (`.j3melee`)**

Registered loader: `J3AttackLoader`. Returned value: `J3AttackAsset`.

```java
import com.jme.j3asset.core.combat.J3AttackAsset;

J3AttackAsset definition = (J3AttackAsset) assets.loadAsset("Examples/Sample.j3melee");
```

Reference from an attack set; trigger through `CombatControl.onPrimaryAttack` or `onSecondaryAttack`.

## j3firearm

**Firearm Attack (`.j3firearm`)**

Registered loader: `J3FirearmLoader`. Returned value: `J3FirearmAsset`.

```java
import com.jme.j3asset.core.combat.J3FirearmAsset;

J3FirearmAsset definition = (J3FirearmAsset) assets.loadAsset("Examples/Sample.j3firearm");
```

Reference from a weapon firearm configuration; use the combat controls rather than implementing a second firing loop.

## j3attackset

**Attack Set (`.j3attackset`)**

Registered loader: `J3AttackSetLoader`. Returned value: `J3AttackSetAsset`.

```java
import com.jme.j3asset.core.combat.J3AttackSetAsset;

J3AttackSetAsset definition = (J3AttackSetAsset) assets.loadAsset("Examples/Sample.j3attackset");
```

Reference from a weapon attack-set slot to make its moves available to combat.

## j3charge

**Attack Charge (`.j3charge`)**

This editor asset has **no loader registered by `J3Runtime.registerLoaders`**. Read its encoded definition explicitly; do not assume `assets.loadAsset` supports the extension.

```java
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.jme.j3asset.core.asset.BinaryAssetCodec;
import java.nio.file.Path;

JsonObject definition = JsonParser.parseString(BinaryAssetCodec.readString(
        Path.of("assets/Examples/Sample.j3charge"))).getAsJsonObject();
```

This reads configuration only. Your game must interpret it and provide the corresponding behaviour; this example does not claim an automatic runtime executor for this asset. Keep the file in the editor's authored format when editing it.

## j3attackfx

**Attack Effects (`.j3attackfx`)**

Registered loader: `J3AttackEffectsLoader`. Returned value: `Object`.

```java
Object definition = (Object) assets.loadAsset("Examples/Sample.j3attackfx");
```

Reference from the attack that should play its sounds and effects.

## j3hurtbox

**Hurtbox Profile (`.j3hurtbox`)**

Registered loader: `J3HurtboxLoader`. Returned value: `J3HurtboxAsset`.

```java
import com.jme.j3asset.core.combat.J3HurtboxAsset;

J3HurtboxAsset definition = (J3HurtboxAsset) assets.loadAsset("Examples/Sample.j3hurtbox");
```

Reference from a damage profile for receiving hit regions.

## j3reaction

**Reaction Data (`.j3reaction`)**

Registered loader: `J3ReactionLoader`. Returned value: `J3ReactionAsset`.

```java
import com.jme.j3asset.core.combat.J3ReactionAsset;

J3ReactionAsset definition = (J3ReactionAsset) assets.loadAsset("Examples/Sample.j3reaction");
```

Reference from a damage profile to select hit and knockdown reactions.

## j3grapple

**Grapple (`.j3grapple`)**

This editor asset has **no loader registered by `J3Runtime.registerLoaders`**. Read its encoded definition explicitly; do not assume `assets.loadAsset` supports the extension.

```java
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.jme.j3asset.core.asset.BinaryAssetCodec;
import java.nio.file.Path;

JsonObject definition = JsonParser.parseString(BinaryAssetCodec.readString(
        Path.of("assets/Examples/Sample.j3grapple"))).getAsJsonObject();
```

This reads configuration only. Your game must interpret it and provide the corresponding behaviour; this example does not claim an automatic runtime executor for this asset. Keep the file in the editor's authored format when editing it.

## j3finisher

**Finisher (`.j3finisher`)**

This editor asset has **no loader registered by `J3Runtime.registerLoaders`**. Read its encoded definition explicitly; do not assume `assets.loadAsset` supports the extension.

```java
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.jme.j3asset.core.asset.BinaryAssetCodec;
import java.nio.file.Path;

JsonObject definition = JsonParser.parseString(BinaryAssetCodec.readString(
        Path.of("assets/Examples/Sample.j3finisher"))).getAsJsonObject();
```

This reads configuration only. Your game must interpret it and provide the corresponding behaviour; this example does not claim an automatic runtime executor for this asset. Keep the file in the editor's authored format when editing it.

## j3weapon

**Weapon Definition (`.j3weapon`)**

Registered loader: `J3WeaponLoader`. Returned value: `J3WeaponAsset`.

```java
import com.jme.j3asset.core.combat.J3WeaponAsset;

J3WeaponAsset definition = (J3WeaponAsset) assets.loadAsset("Examples/Sample.j3weapon");
```

Pass the weapon key to the spawned character's `combat().equipWeapon`.

## j3striker

**Striker (`.j3striker`)**

Registered loader: `J3StrikerLoader`. Returned value: `J3StrikerAsset`.

```java
import com.jme.j3asset.core.combat.J3StrikerAsset;

J3StrikerAsset definition = (J3StrikerAsset) assets.loadAsset("Examples/Sample.j3striker");
```

Reference from a weapon to define offensive collision shapes.

## j3cam

**Camera Profile (`.j3cam`)**

Registered loader: `J3CameraLoader`. Returned value: `JsonObject`.

```java
import com.google.gson.JsonObject;

JsonObject definition = (JsonObject) assets.loadAsset("Examples/Sample.j3cam");
```

Reference from a scene camera or character camera configuration. Reading a profile does not automatically replace the application camera.

## j3car

**Vehicle Definition (`.j3car`)**

Registered loader: `J3VehicleLoader`. Returned value: `Object`.

```java
Object definition = (Object) assets.loadAsset("Examples/Sample.j3car");
```

Use `J3VehicleFactory.create` with an initialized physics space; see the vehicle example.

## j3agent

**Agent Profile (`.j3agent`)**

Registered loader: `J3AgentLoader`. Returned value: `J3AgentAsset`.

```java
import com.jme.j3asset.core.ai.J3AgentAsset;

J3AgentAsset definition = (J3AgentAsset) assets.loadAsset("Examples/Sample.j3agent");
```

Reference from a character agent profile. Agent behaviours can reference behaviour/state/action definitions.

## j3memory

**Memory Template (`.j3memory`)**

This editor asset has **no loader registered by `J3Runtime.registerLoaders`**. Read its encoded definition explicitly; do not assume `assets.loadAsset` supports the extension.

```java
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.jme.j3asset.core.asset.BinaryAssetCodec;
import java.nio.file.Path;

JsonObject definition = JsonParser.parseString(BinaryAssetCodec.readString(
        Path.of("assets/Examples/Sample.j3memory"))).getAsJsonObject();
```

This reads configuration only. Your game must interpret it and provide the corresponding behaviour; this example does not claim an automatic runtime executor for this asset. Keep the file in the editor's authored format when editing it.

## j3inventory

**AI Inventory (`.j3inventory`)**

This editor asset has **no loader registered by `J3Runtime.registerLoaders`**. Read its encoded definition explicitly; do not assume `assets.loadAsset` supports the extension.

```java
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.jme.j3asset.core.asset.BinaryAssetCodec;
import java.nio.file.Path;

JsonObject definition = JsonParser.parseString(BinaryAssetCodec.readString(
        Path.of("assets/Examples/Sample.j3inventory"))).getAsJsonObject();
```

This reads configuration only. Your game must interpret it and provide the corresponding behaviour; this example does not claim an automatic runtime executor for this asset. Keep the file in the editor's authored format when editing it.

## j3enemy

**Enemy Configuration (`.j3enemy`)**

This editor asset has **no loader registered by `J3Runtime.registerLoaders`**. Read its encoded definition explicitly; do not assume `assets.loadAsset` supports the extension.

```java
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.jme.j3asset.core.asset.BinaryAssetCodec;
import java.nio.file.Path;

JsonObject definition = JsonParser.parseString(BinaryAssetCodec.readString(
        Path.of("assets/Examples/Sample.j3enemy"))).getAsJsonObject();
```

This reads configuration only. Your game must interpret it and provide the corresponding behaviour; this example does not claim an automatic runtime executor for this asset. Keep the file in the editor's authored format when editing it.

## j3police

**Police Configuration (`.j3police`)**

This editor asset has **no loader registered by `J3Runtime.registerLoaders`**. Read its encoded definition explicitly; do not assume `assets.loadAsset` supports the extension.

```java
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.jme.j3asset.core.asset.BinaryAssetCodec;
import java.nio.file.Path;

JsonObject definition = JsonParser.parseString(BinaryAssetCodec.readString(
        Path.of("assets/Examples/Sample.j3police"))).getAsJsonObject();
```

This reads configuration only. Your game must interpret it and provide the corresponding behaviour; this example does not claim an automatic runtime executor for this asset. Keep the file in the editor's authored format when editing it.

## j3civilian

**Civilian Configuration (`.j3civilian`)**

This editor asset has **no loader registered by `J3Runtime.registerLoaders`**. Read its encoded definition explicitly; do not assume `assets.loadAsset` supports the extension.

```java
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.jme.j3asset.core.asset.BinaryAssetCodec;
import java.nio.file.Path;

JsonObject definition = JsonParser.parseString(BinaryAssetCodec.readString(
        Path.of("assets/Examples/Sample.j3civilian"))).getAsJsonObject();
```

This reads configuration only. Your game must interpret it and provide the corresponding behaviour; this example does not claim an automatic runtime executor for this asset. Keep the file in the editor's authored format when editing it.

## j3traffic

**Traffic Configuration (`.j3traffic`)**

This editor asset has **no loader registered by `J3Runtime.registerLoaders`**. Read its encoded definition explicitly; do not assume `assets.loadAsset` supports the extension.

```java
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.jme.j3asset.core.asset.BinaryAssetCodec;
import java.nio.file.Path;

JsonObject definition = JsonParser.parseString(BinaryAssetCodec.readString(
        Path.of("assets/Examples/Sample.j3traffic"))).getAsJsonObject();
```

This reads configuration only. Your game must interpret it and provide the corresponding behaviour; this example does not claim an automatic runtime executor for this asset. Keep the file in the editor's authored format when editing it.

## j3social

**Social Performance (`.j3social`)**

This editor asset has **no loader registered by `J3Runtime.registerLoaders`**. Read its encoded definition explicitly; do not assume `assets.loadAsset` supports the extension.

```java
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.jme.j3asset.core.asset.BinaryAssetCodec;
import java.nio.file.Path;

JsonObject definition = JsonParser.parseString(BinaryAssetCodec.readString(
        Path.of("assets/Examples/Sample.j3social"))).getAsJsonObject();
```

This reads configuration only. Your game must interpret it and provide the corresponding behaviour; this example does not claim an automatic runtime executor for this asset. Keep the file in the editor's authored format when editing it.

## j3move

**Movement Controller (`.j3move`)**

Registered loader: `J3MovementLoader`. Returned value: `J3MovementAsset`.

```java
import com.jme.j3asset.core.movement.J3MovementAsset;

J3MovementAsset definition = (J3MovementAsset) assets.loadAsset("Examples/Sample.j3move");
```

Reference from the character movement profile; spawning wires movement to physics.

## j3input

**Input Mapping (`.j3input`)**

Registered loader: `J3InputLoader`. Returned value: `J3InputAsset`.

```java
import com.jme.j3asset.core.input.J3InputAsset;

J3InputAsset definition = (J3InputAsset) assets.loadAsset("Examples/Sample.j3input");
```

Reference from movement settings. Player spawning configures input; avoid installing the same bindings twice.

## j3char

**Character (`.j3char`)**

Registered loader: `J3CharacterLoader`. Returned value: `Object`.

```java
Object definition = (Object) assets.loadAsset("Examples/Sample.j3char");
```

Pass this key to `JmeCharacters.spawn`; see the character example.

## j3model

**Imported model (`.j3model`)**

Registered loader: `J3ModelLoader`. Returned value: `Spatial`.

```java
import com.jme3.scene.Spatial;

Spatial definition = (Spatial) assets.loadAsset("Examples/Sample.j3model");
```

Attach the loaded Spatial to the scene graph. The loader reconstructs embedded materials.

## j3anim

**Animation library (`.j3anim`)**

Registered loader: `J3AnimationLoader`. Returned value: `Spatial`.

```java
import com.jme3.scene.Spatial;

Spatial definition = (Spatial) assets.loadAsset("Examples/Sample.j3anim");
```

Use as an animation library with `J3AnimationPlayer.playLibraryClip`; loading alone does not start playback.

## j3mat

**Embedded material (`.j3mat`)**

Registered loader: `J3MaterialLoader`. Returned value: `Material`.

```java
import com.jme3.material.Material;

Material definition = (Material) assets.loadAsset("Examples/Sample.j3mat");
```

Apply the loaded Material to a Geometry with `setMaterial`.

## j3curve

**Curve (`.j3curve`)**

```java
import com.jme.j3asset.core.scene.J3CurveAsset;
import java.nio.file.Path;

Path file = Path.of("assets/Examples/Sample.j3curve");
var definition = J3CurveAsset.load(file);
```

Read a curve for game path logic or reference it from a scene curve-array modifier.

## j3behaviour

**Behaviour (`.j3behaviour`)**

Registered loader: `J3BehaviourLoader`. Returned value: `J3BehaviourAsset`.

```java
import com.jme.j3asset.core.ai.J3BehaviourAsset;

J3BehaviourAsset definition = (J3BehaviourAsset) assets.loadAsset("Examples/Sample.j3behaviour");
```

Reference from an agent profile; behaviour processing requires a resolver, action registry, context, and fallback AI.

## j3state

**State (`.j3state`)**

Registered loader: `J3StateLoader`. Returned value: `J3StateAsset`.

```java
import com.jme.j3asset.core.ai.J3StateAsset;

J3StateAsset definition = (J3StateAsset) assets.loadAsset("Examples/Sample.j3state");
```

Reference from a behaviour; a loaded state definition does not run by itself.

## j3action

**Action (`.j3action`)**

Registered loader: `J3ActionLoader`. Returned value: `J3ActionAsset`.

```java
import com.jme.j3asset.core.ai.J3ActionAsset;

J3ActionAsset definition = (J3ActionAsset) assets.loadAsset("Examples/Sample.j3action");
```

Reference from a state and provide matching action implementations in the runtime action registry.

## j3attack

**Legacy melee alias (`.j3attack`)**

Registered loader: `J3AttackLoader`. Returned value: `J3AttackAsset`.

```java
import com.jme.j3asset.core.combat.J3AttackAsset;

J3AttackAsset definition = (J3AttackAsset) assets.loadAsset("Examples/Sample.j3attack");
```

Read the definition and connect it to the consuming gameplay system.

## j3camera

**Camera profile alias (`.j3camera`)**

Registered loader: `J3CameraLoader`. Returned value: `JsonObject`.

```java
import com.google.gson.JsonObject;

JsonObject definition = (JsonObject) assets.loadAsset("Examples/Sample.j3camera");
```

Read the definition and connect it to the consuming gameplay system.
