# Vehicle Definition (`.j3car`)

A Vehicle Definition assembles a jME model into a drivable four-wheel vehicle. It stores selected model parts, wheel physics, four animated doors, colored lamps, and audio references. The vehicle model must be a `.j3o` inside the open project's asset root.

## Build a vehicle

1. Import the chassis as a `.j3o`. Wheels and doors may be separate `.j3o` files or distinct parts inside the chassis model. Give embedded parts distinct names. Center a separate wheel model on its axle.
2. Choose **Assets → Create → Vehicles → Vehicle Definition** and select the `.j3o` in **Vehicle Model**. The model opens in the viewport, and the inspector lists its scene nodes and geometries.
3. For each wheel, choose an embedded geometry or a separate model, enter its suspension connection point and wheel radius, and mark driven wheels. The chassis uses a compound box collision shape configured by `collider.halfExtents` and `collider.offset`.
4. For each door, choose an embedded geometry or separate model, then enter its hinge pivot, open angle, and opening time. Separate door models also have a position offset relative to the hinge. The runtime rotates the selected part around its hinge; it does not require an imported skeletal animation.
5. Add lights. Each entry has a function (headlight, tail, brake, reverse, or left/right indicator), a spot or point light, a color, position, direction, range, intensity, and optional lens geometry. Spot lights are suited to beams; point lights suit rear lamps and indicators. A jME directional light has no position, so it cannot be placed at a headlamp.
6. Choose an optional horn audio asset, save, and select **Build and test vehicle**. The inspector provides door, lamp, indicator, steering, throttle, and brake controls for the viewport preview.

Coordinates are in model space. The vehicle's front is positive Z and up is positive Y. Negative X is the left side in the default template. Check your imported model orientation before entering wheel connections, door pivots, or lamp directions.

## Runtime use

Register the J3 loaders, then create the vehicle after adding a `BulletAppState`:

```java
J3Runtime.registerLoaders(assetManager);
J3Vehicle car = J3VehicleFactory.create(assetManager,
        bulletAppState.getPhysicsSpace(), "J3 Meta/Vehicles/Pickup.j3car");
rootNode.attachChild(car.spatial());

car.setThrottle(0.5f);          // -1 reverse to +1 forward
car.setSteering(0.2f);          // -1 left to +1 right
car.setBrake(0f);               // 0 to 1
car.openDoor("frontLeft");
car.setHeadlights(true);
car.setTailLights(true);
car.setIndicator(J3Vehicle.Indicator.LEFT);
car.soundHorn();
```

The runtime uses jME's ray-cast `VehicleControl`; wheel geometries are visible parts and the physical wheels are suspension rays. Door motion is a hinge animation. Indicators flash automatically. Headlights, tail, brake and reverse lamps can be switched separately. Assigning lamp geometry also changes its emissive color when its light is on, if its material supports `GlowColor` or `Emissive`.

## Current scope

The inspector can select embedded parts or reference separate wheel and door models. Wheel positions, door pivots, and lamp positions are entered numerically; viewport placement gizmos are still needed for easier tuning. The runtime has basic throttle, steering, brakes, suspension and indicators; transmission, advanced traction, damage, AI driving, and input bindings remain project-specific work. The editor's offscreen preview has audio disabled, so horn playback must be checked in a game with audio enabled.
