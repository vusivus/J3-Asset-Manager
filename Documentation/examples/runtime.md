# Runtime integration examples

Use [the complete Java application](RuntimeExample.java) as a starting point. It demonstrates initialization, character spawning and weapon assignment, level lifecycle, animation playback, and vehicle creation in separate modes. [Asset loading examples](assets.md) cover every authored asset type and explain which definitions are consumed automatically.

## Dependencies and asset layout

Use Java 21 or newer. Copy `J3Runtime-1.1.jar` and `J3AssetManagerCore-1.1.jar` into your game's `libs/` directory. Use a consistent set of jMonkeyEngine libraries; the examples target `3.9.0-stable`.

```groovy
plugins {
    id 'application'
}
repositories { mavenCentral() }
dependencies {
    implementation files('libs/J3Runtime-1.1.jar', 'libs/J3AssetManagerCore-1.1.jar')
    implementation 'org.jmonkeyengine:jme3-core:3.9.0-stable'
    implementation 'org.jmonkeyengine:jme3-desktop:3.9.0-stable'
    implementation 'org.jmonkeyengine:jme3-lwjgl3:3.9.0-stable'
    implementation 'org.jmonkeyengine:jme3-plugins:3.9.0-stable'
    implementation 'org.jmonkeyengine:jme3-plugins-json:3.9.0-stable'
    implementation 'org.jmonkeyengine:jme3-jbullet:3.9.0-stable'
    implementation 'com.google.code.gson:gson:2.13.2'
}
application {
    mainClass = 'examples.RuntimeExample'
    applicationDefaultJvmArgs = ['--enable-native-access=ALL-UNNAMED']
}
```

Place `RuntimeExample.java` in `src/main/java/examples/`. Put authored assets and their referenced models, textures, sounds, and animations inside `assets/` at the project root. Run from that root. A key such as `J3Assets/Characters/Hero.j3char` is relative to `assets/`; it must not include the `assets/` prefix. Add further renderer, effect, audio, or model-loader dependencies when your actual assets require them.

```text
gradlew run --args="character J3Assets/Characters/Hero.j3char J3Assets/Weapons/Sword.j3weapon"
gradlew run --args="level J3Assets/Levels/Demo.j3level"
gradlew run --args="animation Models/Hero.glb J3Assets/Animation/Clips/Idle.j3clip"
gradlew run --args="vehicle J3Assets/Vehicles/Car.j3car"
```

These are integration examples using your own authored content, not a bundled playable demo. Character and vehicle modes require a ground collider in your game for physics actors to stand on. Level mode relies on the configured level scene and spawn definitions. Player camera and input settings come from the character's linked assets.

## Character, movement, combat, and damage

`JmeCharacters.spawn` creates the character's model and physics body and wires the configured movement, combat, damage, and hit-shape controls. The reference chain is:

1. `.j3char` → movement `.j3move`, combat `.j3combat`, damage `.j3damage`, and optional agent `.j3agent`.
2. Movement → input `.j3input` and locomotion `.j3loco`; locomotion → `.j3clip` assets.
3. Combat → `.j3weapon` → `.j3attackset`, melee `.j3melee`, firearm `.j3firearm`, and `.j3striker` references as configured.
4. Damage → `.j3hurtbox` and `.j3reaction`; attacks can reference `.j3attackfx` and particle `.j3effect` assets.

Loading an attack definition does not execute an attack. Route press/release events to the spawned character's combat control:

```java
hero.combat().onPrimaryAttack(true);
hero.combat().onPrimaryAttack(false);
hero.combat().onSecondaryAttack(true);
hero.combat().onSecondaryAttack(false);
hero.combat().reload();
```

Here `hero` is the `CharacterInstance` returned by `JmeCharacters.spawn`. Use input callbacks for these calls rather than firing all of them consecutively in gameplay. Do not manually update controls already attached to the scene graph. The complete example updates only its separately owned `J3AnimationPlayer` and `LevelSession`.

## Animation libraries and rigs

The animation example loads a target model and plays `.j3clip` metadata. For a named clip in a library instead:

```java
animation.playLibraryClip("Animations/Movement.j3anim", "Idle", true, 1f, .15f, true);
```

`animation` is the `J3AnimationPlayer` in the complete example. Call `update(tpf)` once per frame. A target can be a `.j3model`, `.j3rig`, or another supported rigged model such as J3O or GLB. The library must contain the named clip, and source and target skeletons must be compatible or mapped for retargeting. `.j3anim` is a binary animation library; do not rename a GLB to `.j3anim`. The editor can import GLB/J3O sources; the `.j3clip` picker currently accepts `.j3anim` and `.j3o`.

## Scenes and curves

Core can read scene/curve documents without the desktop editor. Instantiating an authored scene uses the **additional `J3AssetManagerJme-1.1.jar`** and its runtime dependencies, available in the Libraries/application distributions. It is not provided by the two runtime JARs alone.

```java
import com.jme.j3asset.core.scene.J3SceneAsset;
import com.jme.j3asset.core.scene.J3CurveAsset;
import com.jme.j3asset.scene.J3SceneLoader;
import java.nio.file.Path;

Path assetRoot = Path.of("assets").toAbsolutePath();
var document = J3SceneAsset.load(assetRoot.resolve("Scenes/Neighborhood.j3scene"));
var curve = J3CurveAsset.load(assetRoot.resolve("Curves/Patrol.j3curve"));
var scene = J3SceneLoader.load(assetRoot.resolve("Scenes/Neighborhood.j3scene"),
        assetRoot, assetManager, (spatial, item, control) -> {
            // Attach your game's implementation for each authored control name here.
        });
rootNode.attachChild(scene);
```

The last two variables are members of your `SimpleApplication`. The empty callback intentionally supplies no game-specific control implementation. Loading does not automatically bind arbitrary script names to Java classes or add all controls to Bullet; your game owns those bindings and physics registration. Scene camera profiles and curve-array paths must point to real files.

## AI and definitions without automatic execution

Agent `.j3agent`, behaviour `.j3behaviour`, state `.j3state`, and action `.j3action` definitions have runtime loaders. Authored behaviours require the runtime's resolver, action registry, context, and AI host; loading their definitions alone does not start a scheduler. Enemy waves and character setup provide the integrated entry points described above. Memory, inventory, role configurations, social data, grapple, finisher, and charge definitions do not have loaders registered by `J3Runtime.registerLoaders`; use the explicit decoding examples in the [asset reference](assets.md) and implement the required game-side consumer. This is a support boundary, not a complete AI executor example.

## Scripts and input callbacks

There is no general `.j3script` loader in the current `J3Runtime.registerLoaders`. Game scripts use the Java APIs in this guide; J3O/GLB model keys are accepted by model-loading workflows, rather than requiring a renamed file. For custom input consumers, implement the runtime's event interface:

```java
import com.jme.j3asset.runtime.input.J3Inputs;

public final class PlayerEvents implements J3Inputs {
    @Override public void onInteract(boolean pressed) {
        if (pressed) System.out.println("Interact");
    }
}
```

This class handles events only after your game connects it to an input source. Implementing the interface alone does not install key bindings or spawn a player.

## Library roles

| Library | Use |
| --- | --- |
| J3AssetManagerCore | Asset definitions, codecs, scene documents, metadata and authoring services. |
| J3Runtime | Runtime loaders, character/movement/combat controls, animation player, levels, vehicles and AI helpers. |
| J3AssetManagerJme | Model import and scene construction/editor integration; extra dependencies may be required. |
| J3AssetManagerControls | Editor controls; not needed for the basic runtime examples. |
| J3GUICore / J3GUIEditor / theme | GUI tooling and theme resources; separate from J3Runtime gameplay integration. |

See [runtime installation](../getting-started/use-j3runtime.md) for migration and installation details. All current Java packages use `com.jme.j3asset`; do not combine old `com.vts` imports with these examples.
