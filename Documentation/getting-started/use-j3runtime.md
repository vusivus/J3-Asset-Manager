# Use J3Runtime in a jMonkeyEngine game

J3 Asset Manager edits J3 asset files. `J3Runtime` loads those files in a jMonkeyEngine game and supplies character, combat, movement, input, effect, and level helpers. The editor application does not need to be on your game's classpath.

## Get the libraries

For version 1.0, download both [J3Runtime-1.0.jar](../../Distributions/J3Runtime/J3Runtime-1.0.jar) and [J3AssetManagerCore-1.0.jar](../../Distributions/J3Runtime/J3AssetManagerCore-1.0.jar) from this repository's `Distributions/J3Runtime` folder. Put them in your game's `libs` folder. `J3Runtime` uses the asset classes in `J3AssetManagerCore`; it is not a standalone JAR.

The same two files are bundled under `libraries/` in both the JAR and EXE J3 Asset Manager v1.0 distribution ZIPs. If you already downloaded either application ZIP, you can copy them from there. You do **not** need the desktop UI JAR, the EXE, or JavaFX in your game.

These libraries target Java 21 and jMonkeyEngine `3.9.0-stable`. Your game also needs `jme3-core`, `jme3-jbullet`, and Gson (`2.13.2`). Keep the rest of your game's normal jMonkeyEngine desktop and renderer dependencies.

### Gradle: use the downloaded JARs

Copy the two files into `libs/` beside your game's `build.gradle`, then add:

```groovy
repositories {
    mavenCentral()
}

dependencies {
    implementation files('libs/J3Runtime-1.0.jar', 'libs/J3AssetManagerCore-1.0.jar')
    implementation 'org.jmonkeyengine:jme3-core:3.9.0-stable'
    implementation 'org.jmonkeyengine:jme3-jbullet:3.9.0-stable'
    implementation 'com.google.code.gson:gson:2.13.2'
}
```

If your game already declares any of these jMonkeyEngine or Gson dependencies, keep one declaration of each. Local JAR file dependencies do not supply their Maven transitive dependencies, which is why the three external libraries are listed explicitly.

### Building from source instead

From the J3 Asset Manager Maven source project's root, run `mvn install`. This builds and installs `com.vts:J3Runtime:1.0` and `com.vts:J3AssetManagerCore:1.0` into your local Maven repository. A Gradle game can then use `mavenLocal()` and `implementation 'com.vts:J3Runtime:1.0'`. This is a **local source-build option**; version 1.0 is not being claimed as published on Maven Central.

## Make authored assets visible to jMonkeyEngine

Save your J3 files and every referenced model, material, texture, and animation inside the game's asset root. Use paths relative to that root as asset keys. For example, if the file is `assets/J3 Meta/Characters/Hero.j3char`, its key is `J3 Meta/Characters/Hero.j3char`.

During development, a game with an `assets/` directory can register it as a file locator:

```java
import com.jme3.asset.plugins.FileLocator;
import com.vts.j3.runtime.J3Runtime;

assetManager.registerLocator("assets", FileLocator.class);
J3Runtime.registerLoaders(assetManager);
```

Call `registerLoaders` before the first J3 asset load. It registers the supported `.j3char`, `.j3level`, `.j3wave`, `.j3model`, and other J3 extensions. When packaging the game, include the authored assets as game resources or register the location where you ship them. The editor's project folder itself is not automatically visible to a separate game.

## Example: read an asset definition

Inside a `SimpleApplication`, after registering the asset locator and J3 loaders:

```java
import com.vts.j3assetmanager.core.character.J3CharacterAsset;

J3CharacterAsset hero = (J3CharacterAsset) assetManager.loadAsset(
        "J3 Meta/Characters/Hero.j3char");
System.out.println("Loaded character: " + hero.displayName());
```

Replace the example key with a file you created. Loading the definition reads its data; it does not spawn a playable character.

## Example: spawn a configured character

Attach and initialize a `BulletAppState` before spawning. In a `SimpleApplication` method that runs after physics initialization:

```java
import com.jme3.bullet.BulletAppState;
import com.jme3.math.Vector3f;
import com.vts.j3.runtime.character.J3CharacterRuntime.CharacterInstance;
import com.vts.j3.runtime.character.JmeCharacters;

BulletAppState physics = stateManager.getState(BulletAppState.class);
if (physics == null || !physics.isInitialized()) {
    throw new IllegalStateException("Attach BulletAppState before spawning characters");
}

CharacterInstance hero = JmeCharacters.spawn(
        this, physics, "J3 Meta/Characters/Hero.j3char", new Vector3f(0, 1, 0));

// Access the spawned scene node and runtime controls:
hero.root().setName("Hero");
hero.combat().equipWeapon("J3 Meta/Weapons/HeroWeapon.j3weapon");
```

`JmeCharacters.spawn` registers the J3 loaders and creates the model, physics body, movement, combat, damage, and hurtbox controls. For a character configured as an enabled **Player**, it also wires input and the player camera. The character asset must contain valid references to its model, movement, locomotion, combat, and damage assets. Replace the example asset keys with your own files.

## Example: run a level with waves

`LevelSession` loads a `.j3level`, its scene, player character, and referenced waves. Use it after `BulletAppState` is initialized:

```java
import com.jme3.bullet.BulletAppState;
import com.vts.j3.runtime.level.LevelSession;

BulletAppState physics = stateManager.getState(BulletAppState.class);
LevelSession session = new LevelSession(this, physics);
session.load("J3 Meta/Game Play/Levels/MyLevel.j3level", null);
```

Pass `null` as the second argument to use the player named in the level asset, or pass another enabled Player `.j3char` asset key. Call `session.update(tpf)` from your application's update loop, and `session.close()` when leaving the level. A level needs a valid scene, Player character, and wave references; the runtime validates those when it loads them.

## If an asset does not load

- Check that the asset key is relative to the registered asset root and includes the correct `.j3...` extension.
- Check that all paths referenced inside the J3 asset point to files available to the game.
- Register loaders before directly calling `assetManager.loadAsset` for J3 files.
- If a Java class is missing at runtime, check both J3 JARs and the jMonkeyEngine, Bullet, and Gson dependencies above.

The editor can create more asset types than the current runtime fully implements. Confirm gameplay behavior in your own game build before relying on a type in a release.
