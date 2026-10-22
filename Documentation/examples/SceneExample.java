package examples;

import java.io.IOException;
import java.nio.file.Path;
import com.jme3.asset.AssetManager;
import com.jme3.scene.Node;
import com.jme.j3asset.scene.J3SceneLoader;

/** Requires J3AssetManagerJme in addition to Core and Runtime. */
public final class SceneExample {
    public static Node load(Path assetRoot, String sceneKey, AssetManager assets,
                            J3SceneLoader.ComponentFactory components) throws IOException {
        // Supply a factory that binds authored controls/assets to your game.
        return J3SceneLoader.load(assetRoot.resolve(sceneKey), assetRoot, assets, components);
    }
}
