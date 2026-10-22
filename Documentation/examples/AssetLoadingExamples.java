package examples;

import com.jme3.asset.AssetManager;
import com.google.gson.JsonObject;
import com.jme.j3asset.core.ai.J3ActionAsset;
import com.jme.j3asset.core.ai.J3AgentAsset;
import com.jme.j3asset.core.ai.J3BehaviourAsset;
import com.jme.j3asset.core.ai.J3StateAsset;
import com.jme.j3asset.core.animation.J3AnimationClipAsset;
import com.jme.j3asset.core.combat.J3AttackAsset;
import com.jme.j3asset.core.combat.J3AttackSetAsset;
import com.jme.j3asset.core.combat.J3CombatAsset;
import com.jme.j3asset.core.combat.J3DamageAsset;
import com.jme.j3asset.core.combat.J3FirearmAsset;
import com.jme.j3asset.core.combat.J3HurtboxAsset;
import com.jme.j3asset.core.combat.J3ReactionAsset;
import com.jme.j3asset.core.combat.J3StrikerAsset;
import com.jme.j3asset.core.combat.J3WeaponAsset;
import com.jme.j3asset.core.input.J3InputAsset;
import com.jme.j3asset.core.level.J3LevelAsset;
import com.jme.j3asset.core.level.J3WaveAsset;
import com.jme.j3asset.core.locomotion.J3LocomotionAsset;
import com.jme.j3asset.core.movement.J3MovementAsset;
import com.jme.j3asset.core.skeleton.SkeletalMappingAsset;
import com.jme3.material.Material;
import com.jme3.scene.Node;
import com.jme3.scene.Spatial;

/** Loader examples only: replace sample keys with your authored assets. */
public final class AssetLoadingExamples {
    public static J3WaveAsset j3wave(AssetManager assets) {
        return (J3WaveAsset) assets.loadAsset("Examples/Sample.j3wave");
    }

    public static J3LevelAsset j3level(AssetManager assets) {
        return (J3LevelAsset) assets.loadAsset("Examples/Sample.j3level");
    }

    public static Node j3effect(AssetManager assets) {
        return (Node) assets.loadAsset("Examples/Sample.j3effect");
    }

    public static SkeletalMappingAsset j3skel(AssetManager assets) {
        return (SkeletalMappingAsset) assets.loadAsset("Examples/Sample.j3skel");
    }

    public static Spatial j3rig(AssetManager assets) {
        return (Spatial) assets.loadAsset("Examples/Sample.j3rig");
    }

    public static J3AnimationClipAsset j3clip(AssetManager assets) {
        return (J3AnimationClipAsset) assets.loadAsset("Examples/Sample.j3clip");
    }

    public static J3LocomotionAsset j3loco(AssetManager assets) {
        return (J3LocomotionAsset) assets.loadAsset("Examples/Sample.j3loco");
    }

    public static J3CombatAsset j3combat(AssetManager assets) {
        return (J3CombatAsset) assets.loadAsset("Examples/Sample.j3combat");
    }

    public static J3DamageAsset j3damage(AssetManager assets) {
        return (J3DamageAsset) assets.loadAsset("Examples/Sample.j3damage");
    }

    public static J3AttackAsset j3melee(AssetManager assets) {
        return (J3AttackAsset) assets.loadAsset("Examples/Sample.j3melee");
    }

    public static J3FirearmAsset j3firearm(AssetManager assets) {
        return (J3FirearmAsset) assets.loadAsset("Examples/Sample.j3firearm");
    }

    public static J3AttackSetAsset j3attackset(AssetManager assets) {
        return (J3AttackSetAsset) assets.loadAsset("Examples/Sample.j3attackset");
    }

    public static Object j3attackfx(AssetManager assets) {
        return (Object) assets.loadAsset("Examples/Sample.j3attackfx");
    }

    public static J3HurtboxAsset j3hurtbox(AssetManager assets) {
        return (J3HurtboxAsset) assets.loadAsset("Examples/Sample.j3hurtbox");
    }

    public static J3ReactionAsset j3reaction(AssetManager assets) {
        return (J3ReactionAsset) assets.loadAsset("Examples/Sample.j3reaction");
    }

    public static J3WeaponAsset j3weapon(AssetManager assets) {
        return (J3WeaponAsset) assets.loadAsset("Examples/Sample.j3weapon");
    }

    public static J3StrikerAsset j3striker(AssetManager assets) {
        return (J3StrikerAsset) assets.loadAsset("Examples/Sample.j3striker");
    }

    public static JsonObject j3cam(AssetManager assets) {
        return (JsonObject) assets.loadAsset("Examples/Sample.j3cam");
    }

    public static Object j3car(AssetManager assets) {
        return (Object) assets.loadAsset("Examples/Sample.j3car");
    }

    public static J3AgentAsset j3agent(AssetManager assets) {
        return (J3AgentAsset) assets.loadAsset("Examples/Sample.j3agent");
    }

    public static J3MovementAsset j3move(AssetManager assets) {
        return (J3MovementAsset) assets.loadAsset("Examples/Sample.j3move");
    }

    public static J3InputAsset j3input(AssetManager assets) {
        return (J3InputAsset) assets.loadAsset("Examples/Sample.j3input");
    }

    public static Object j3char(AssetManager assets) {
        return (Object) assets.loadAsset("Examples/Sample.j3char");
    }

    public static Spatial j3model(AssetManager assets) {
        return (Spatial) assets.loadAsset("Examples/Sample.j3model");
    }

    public static Spatial j3anim(AssetManager assets) {
        return (Spatial) assets.loadAsset("Examples/Sample.j3anim");
    }

    public static Material j3mat(AssetManager assets) {
        return (Material) assets.loadAsset("Examples/Sample.j3mat");
    }

    public static J3BehaviourAsset j3behaviour(AssetManager assets) {
        return (J3BehaviourAsset) assets.loadAsset("Examples/Sample.j3behaviour");
    }

    public static J3StateAsset j3state(AssetManager assets) {
        return (J3StateAsset) assets.loadAsset("Examples/Sample.j3state");
    }

    public static J3ActionAsset j3action(AssetManager assets) {
        return (J3ActionAsset) assets.loadAsset("Examples/Sample.j3action");
    }

    public static J3AttackAsset j3attack(AssetManager assets) {
        return (J3AttackAsset) assets.loadAsset("Examples/Sample.j3attack");
    }

    public static JsonObject j3camera(AssetManager assets) {
        return (JsonObject) assets.loadAsset("Examples/Sample.j3camera");
    }
}
