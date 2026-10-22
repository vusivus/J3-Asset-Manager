package examples;

import com.jme.j3asset.runtime.J3Runtime;
import com.jme.j3asset.runtime.animation.J3AnimationPlayer;
import com.jme.j3asset.runtime.character.JmeCharacters;
import com.jme.j3asset.runtime.character.J3CharacterRuntime.CharacterInstance;
import com.jme.j3asset.runtime.level.LevelSession;
import com.jme.j3asset.runtime.vehicle.J3Vehicle;
import com.jme.j3asset.runtime.vehicle.J3VehicleFactory;
import com.jme3.app.SimpleApplication;
import com.jme3.asset.plugins.FileLocator;
import com.jme3.bullet.BulletAppState;
import com.jme3.light.AmbientLight;
import com.jme3.light.DirectionalLight;
import com.jme3.math.ColorRGBA;
import com.jme3.math.Vector3f;

/** Run one mode at a time; supply real authored asset keys as arguments. */
public final class RuntimeExample extends SimpleApplication {
    private final String[] arguments;
    private BulletAppState physics;
    private boolean ready;
    private LevelSession level;
    private J3AnimationPlayer animation;
    private J3Vehicle vehicle;

    public RuntimeExample(String[] arguments) { this.arguments = arguments; }

    public static void main(String[] args) {
        if (args.length < 2) {
            System.err.println("Usage: RuntimeExample character|level|animation|vehicle assetKey [weaponKey|clipKey]");
            return;
        }
        new RuntimeExample(args).start();
    }

    @Override public void simpleInitApp() {
        assetManager.registerLocator("assets", FileLocator.class);
        J3Runtime.registerLoaders(assetManager);
        physics = new BulletAppState();
        stateManager.attach(physics);
        rootNode.addLight(new AmbientLight(ColorRGBA.White.mult(.4f)));
        DirectionalLight sun = new DirectionalLight();
        sun.setDirection(new Vector3f(-1, -2, -1).normalizeLocal());
        rootNode.addLight(sun);
        cam.setLocation(new Vector3f(0, 3, 8));
        cam.lookAt(new Vector3f(0, 1, 0), Vector3f.UNIT_Y);
    }

    @Override public void simpleUpdate(float tpf) {
        // Bullet's app state initializes after simpleInitApp; wait before spawning.
        if (!ready && physics.isInitialized()) {
            ready = true;
            switch (arguments[0]) {
                case "character" -> {
                    CharacterInstance hero = JmeCharacters.spawn(this, physics,
                            arguments[1], new Vector3f(0, 1, 0));
                    if (arguments.length > 2) hero.combat().equipWeapon(arguments[2]);
                    // In your input handler: hero.combat().onPrimaryAttack(pressed);
                    // Release with false. Secondary attack and reload use the same combat control.
                }
                case "level" -> {
                    level = new LevelSession(this, physics);
                    level.load(arguments[1], null); // null uses the level's configured player.
                }
                case "animation" -> {
                    if (arguments.length < 3) throw new IllegalArgumentException("Supply target model and .j3clip key");
                    animation = new J3AnimationPlayer(assetManager, arguments[1]);
                    rootNode.attachChild(animation.model());
                    animation.play(arguments[2]);
                }
                case "vehicle" -> {
                    vehicle = J3VehicleFactory.create(assetManager, physics.getPhysicsSpace(), arguments[1]);
                    rootNode.attachChild(vehicle.spatial());
                    // In your input handler: vehicle.setThrottle(value), setSteering(value), setBrake(value).
                }
                default -> throw new IllegalArgumentException("Unknown example mode: " + arguments[0]);
            }
        }
        if (level != null) level.update(tpf);
        if (animation != null) animation.update(tpf);
    }

    @Override public void destroy() {
        if (level != null) level.close();
        super.destroy();
    }
}
