# Game Level (`.j3level`)

A Game Level describes the scene, the default player and spawn point, and an ordered list of [Enemy Waves](wave.md). It is an encounter configuration asset; the `.j3o` scene holds the actual environment geometry.

## Create and edit

Choose **Assets → Create → Levels → Game Level** and open the file. Set the Name, Scene `.j3o`, and Default Player `.j3char`. Enter the player's feet position and yaw. Add Wave rows, choose `.j3wave` files, and use Up or Down to set their order. Save; the inspector checks that referenced files exist. **Preview Scene** opens the selected scene in the editor view.

![Game Level inspector](../images/game-level-inspector.png)

*Screenshot placeholder: show the Scene and Default Player pickers, player position, ordered wave list with Up/Down controls, and Preview Scene button. The image should show how a level connects a scene to encounters.*

## Fields

| Field | Meaning |
| --- | --- |
| `name` | Level label; cannot be blank. |
| `scene` | `.j3o` environment loaded for the level. |
| `player` | Default `.j3char` player, which a launch configuration may override. |
| `playerX/Y/Z` | World-space feet position at entry. |
| `playerYaw` | Facing angle in degrees. |
| `waves[]` | Ordered `.j3wave` references. Their order is part of the encounter sequence. |

The level validator requires the scene, player, and wave references it contains to have the expected extensions. The inspector additionally checks that nonempty referenced files exist before saving.
