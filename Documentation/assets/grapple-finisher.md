# Grapple and Finisher assets

The Create Asset menu includes **Grapple** (`.j3grapple`) and **Finisher** (`.j3finisher`). These are intended to describe paired close-range interactions and finishing moves. The current creation service makes a generic structured draft for each. The main project inspector does not currently route these extensions to dedicated editors, so creation is available before a complete authoring workflow.

## Create a draft

Choose **Assets → Create → Combat → Grapple** or **Finisher**, name the asset, and create the file. The draft contains the standard identity envelope and an empty `data` object. There is no verified field-level inspector for these types in the current UI. Keep such drafts under version control and wait for a defined schema and runtime consumer before using them as gameplay content.

## Intended relationship

The game design describes Grapple and Throw as a close-range interaction between an attacker and a valid target. It must check reach, facing, target state, and safe placement. A finisher would similarly require a clear eligibility rule and an authored animation or interaction. Those design requirements do not define the final `.j3grapple` or `.j3finisher` JSON fields yet.

![Grapple and Finisher future inspector](../images/grapple-finisher-inspector.png)

*Screenshot placeholder: once dedicated inspectors exist, capture their eligibility, animation, target alignment, and outcome fields. This screenshot cannot be produced from the current editor route.*

For playable melee attacks today, use [Melee Attack](melee-attack.md), [Attack Set](attack-set.md), and the existing combat assets.
