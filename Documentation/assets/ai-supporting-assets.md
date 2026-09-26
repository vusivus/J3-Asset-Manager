# Memory, inventory, and social assets

These AI assets hold reusable supporting data. They are created under **Assets → Create → AI** and open in the structured asset inspector. Unlike the dedicated Enemy/Police/Civilian/Traffic inspectors, the structured inspector presents fields from the saved document schema. Save after changing values or references.

![Structured AI asset inspector](../images/ai-supporting-assets-inspector.png)

*Screenshot placeholder: show a Memory Template, AI Inventory, or Social Performance selected in the project tree with its structured fields in the inspector. The image should demonstrate where these supporting assets are edited.*

## Memory Template (`.j3memory`)

Memory lets an agent retain observations and reports for a limited time instead of reacting only to what is visible in the current frame. The created document includes `capacity` (number of items), `confidenceDecay`, `forgetAfter`, `recognitionPersistence`, `sharePolicy`, and an `items` list. For example, a remembered last-seen location can make an agent search an area after losing sight of a target. The game runtime must implement how those records are created, updated, and shared.

## AI Inventory (`.j3inventory`)

The inventory asset describes which items or weapons an AI group may draw from. Its initial document contains `tags`, `allowedFactions`, `capacity`, `reservationDuration`, `restockPolicy`, and `entries`. Capacity limits concurrent stock or assignments according to the consuming system; reservation duration can prevent several agents claiming the same item at once. Fill entries with the format expected by the current runtime or project tools.

## Social Performance (`.j3social`)

A social performance describes an interaction or ambient performance. Its initial fields include `intent`, `speakerTags`, `recipientTags`, `audio`, `gestures`, `emotion`, `responses`, `duration`, `cooldown`, and `interruptible`. A greeting and a warning can be separate assets with different eligible participants and presentation. Save the file, then add its reference to an Enemy, Police, or Civilian Configuration that supports social performance lists.

## Before relying on them

These files are useful for authoring and inspection, but the current repository's complete AI behavior hierarchy and runtime decisions are still developing. Use [AI behaviour system](behaviours.md) for the goal/state/action design and [Agent Profile](agent-profile.md) for decision and perception settings.
