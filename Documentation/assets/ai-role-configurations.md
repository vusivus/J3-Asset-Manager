# Enemy, police, civilian, and traffic configurations

These role assets supply data for different kinds of agents. An [Agent Profile](agent-profile.md) can identify broad perception and thinking settings; a role configuration adds details such as weapons, authority, civilian danger response, or driving style. The editor provides dedicated role inspectors for the four file types below.

## Create and edit

Use **Assets → Create → AI** and choose **Enemy Configuration**, **Police Configuration**, **Civilian Configuration**, or **Traffic Configuration**. Open the resulting file in the project browser. The inspector shows sections appropriate to its role. Fill the references and tuning values, save, and connect the file through an Agent Profile's role configuration where that path is supported.

![AI role inspector](../images/ai-role-inspector.png)

*Screenshot placeholder: show an Enemy Configuration with Classification, Starting Equipment, and Combat & Morale Tuning sections, plus its Save feedback. The image should show that role data is separate from general Agent Profile settings.*

## Enemy Configuration (`.j3enemy`)

This asset selects an enemy role such as Lookout, Grunt, Bruiser, Ranged, Support, Leader, or Boss and a rank such as Standard or Elite. Its inspector groups Default Locomotion, patrol/investigation/combat/flee speed multipliers, Unarmed/Starting/Sidearm weapon references, carry capacity, allowed and preferred weapon categories, weapon pickup rules, permitted grapples and finishers, social performances, role animations, and combat and morale tuning. For example, Preferred Combat Distance and Attack Aggression express how an enemy should pressure a target; the runtime behavior determines how those values are used.

Start by setting classification, locomotion, and an unarmed or starting weapon. Add weapon acquisition and special move lists only when the game has content for them. A field in the inspector describes configuration, not proof that every named AI behavior is already executed.

## Police Configuration (`.j3police`)

Police assets provide role, locomotion, default and additional weapons, social performances, and authority. Authority fields include weapon draw and lethal force thresholds, backup threshold, perimeter radius, and flags for restraint or hunter support. Choose values appropriate to the role; a tactical responder and a traffic officer need different starting equipment and response thresholds.

## Civilian Configuration (`.j3civilian`)

Civilian assets provide a role such as Pedestrian or Vendor, activity tags, default and panic locomotion, social performances, animation references, and danger response. The latter includes tendencies to comply, resist, flee, hide, report, or help others, plus a trust requirement for assisting the hunter. These values are intended to differentiate civilians in a living scene; actual decisions require matching runtime behavior.

## Traffic Configuration (`.j3traffic`)

Traffic assets describe route tags, permitted vehicle categories, driver locomotion and animation, driving temperament, obstacle response, danger response, and collision response. Examples include following distance, braking anticipation, pedestrian caution, reroute delay, and whether the driver can reverse. A vehicle definition supplies the vehicle itself; this configuration describes how an agent might drive it.

## Common rule

Choose reference files from the project asset root, save, and test the role in a representative scene. A preset with plausible values may still need navigation, perception, or behavior support before it acts as designed.
