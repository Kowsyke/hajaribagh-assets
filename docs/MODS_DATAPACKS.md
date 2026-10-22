# Installed Mods, Datapacks, and Assets

This document catalogs every active modification, server datapack, and asset pack installed in Project Hajaribagh. Mod facts (sides, versions, licences) were checked against the Modrinth API on 2026-10-22. The jars themselves are not in this repo, so file names come from the earlier docs and were not re-read from the server.

---

## 1. Active Mods (`mods/` on the cloud VM)

| File Name | Source | Purpose | Client needs it? | Status on 2026-10-22 |
| :--- | :--- | :--- | :--- | :--- |
| `fabric-api-0.162.0+26.3.jar` | [Fabric API](https://modrinth.com/mod/fabric-api) | Base hooks and event bus for Fabric | No (optional) | Two newer builds exist for 26.3: 0.163.0 and 0.164.0 |
| `lithium-fabric-0.26.2+mc26.3.jar` | [Lithium](https://modrinth.com/mod/lithium) | Game logic, chunk, and entity tick optimization | No (optional) | Latest |
| `ferritecore-9.0.0-fabric.jar` | [FerriteCore](https://modrinth.com/mod/ferrite-core) | Lower memory use through data deduplication | No (optional) | Latest, supports 26.3 |
| `krypton-0.3.2.jar` | [Krypton](https://modrinth.com/mod/krypton) | Networking stack optimization | No (optional) | Latest |
| `polymer-bundled-0.18.4+26.3.jar` | [Polymer](https://modrinth.com/mod/polymer) | Library that shows server-side content to vanilla clients | No (optional) | Latest |
| `brewery-0.17.1+26.3.jar` | [Patbox's Brewery](https://modrinth.com/mod/brewery) | Cauldron brewing and barrel aging, built on Polymer | No (unsupported on client) | Latest |
| `custompaintings-fabric-4.0.2+26.3.jar` | [Custom Paintings](https://modrinth.com/mod/custom-paintings-mod) by Roundaround | Painting packs, custom sizes, painting picker menu | Yes (required on client and server) | Latest |

### Notes per mod

**Polymer.** Polymer is a library that other mods use to show server-side items and blocks as vanilla ones. Its configs are in `configs/polymer/`. Polymer's resource pack auto-hosting is switched off (`auto-host.json`, `enabled: false`), so any resource pack Polymer generates is not sent to players. The painting pack is sent separately through `server.properties`. If Brewery items ever look wrong in game, turning auto-hosting on is the first thing to try, and the painting zip can then be listed under `external_resource_packs` so both packs reach players.

**Brewery.** The mod's own page says it can work purely server-side. Basics from that page:
* Craft a Book of Brewery (1 Glass Bottle + 1 Book) to see every recipe in game.
* Cooking: drop ingredients into a cauldron of water placed above a fire or campfire, click it with a stick to start, then click it with an empty glass bottle to collect the mixture. The time spent cooking changes the result.
* Barrels are built in the world from a spigot, 4 fences, 16 wooden stairs, and 20 planks of the same wood type. Place the spigot last. Right-click the barrel to put items in to age. Barrel wood type affects quality.
* More drinks can be added with datapacks (see the Brewery page on Modrinth for examples).

**Custom Paintings.** Packs are zip files or folders placed in a `custompaintings` folder inside the world save, so on the VM that is `world/custompaintings/`. The mod adds a painting picker menu and gives each painting its own item icon. It supplies no paintings itself. `custompaintings/ServerPaintings/` in this repo is the source of Hajaribagh's pack. The Modrinth page marks the mod as required on both client and server, which conflicts with the Zero Client Mod Requirement. How it behaves for a vanilla client is untested (see `KNOWN_ISSUES.md`).

---

## 2. Server Datapacks (`datapacks/`)

### `cannabis_smoke`
* **Path**: `datapacks/cannabis_smoke/`
* **Recipe**: 1 Paper + 1 Dried Kelp (shapeless) yields 3 Cannabis Joints, which are `warped_fungus_on_a_stick` items with a custom name and lore.
* **Right-click detection**: using the item increments the `use_joint` scoreboard objective.
* **Effects per use**: Regeneration II for 15 seconds, Resistance II for 20 seconds, Slow Falling for 10 seconds, Saturation for 2 seconds, and Nausea for 6 seconds.
* **Presentation**: `block.campfire.crackle` is heard by nearby players, `entity.generic.drink` plays for the smoker, an action bar message appears, and smoke particles puff in front of the player's face for 3 seconds.
* **No joint needed**: `/trigger smoke` runs the same effects.
* **Items**: `give_joint.mcfunction` gives 3 joints to the player who runs it.

### `ore_xray`
* **Path**: `datapacks/ore_xray/`
* **What it does**: `/trigger xray` switches the player to spectator mode with infinite night vision, and switches back to survival and clears night vision on the next use.
* **Who can use it**: the trigger is enabled only for the player named `Kowsyke`. Everyone else's `xray` score is reset every tick.
* **Unused file**: `deny.mcfunction` (fake "Unknown or incomplete command" message) is not called by anything.

---

## 3. Custom Paintings Asset Pack

* **Package**: `Hajaribagh-Paintings.zip` (about 4.7 MB)
* **How it works**: the zip replaces all 46 vanilla painting textures in `assets/minecraft/textures/painting/` with six palette-reduced PNGs, so any painting a player places shows one of the six. Each vanilla texture got the image whose aspect ratio is closest.
* **Delivery**: the `resource-pack`, `resource-pack-sha1`, and `resource-pack-prompt` lines in `server.properties`. `require-resource-pack` is `false`, so players can decline.
* **Source images**: `custompaintings/ServerPaintings/images/`.

| Image | Pixels | Block size in manifest | Vanilla textures it replaces |
| :--- | :--- | :--- | :--- |
| Sarjis Alam | 635 x 358 | 3x2 | alban, bouquet, courbet, creebet, de_void, fighters, pond, pool, sea, sunset, void (11) |
| Sheikh Hasina | 503 x 609 | 2x3 | aztec, baroque, burning_skull, bust, endboss, finding, plant, sunflowers, wanderer (9) |
| President Chuppu | 180 x 240 | 1x2 | cavebird, fern, graham, humble, kebab, lowmist, skull_and_roses, wasteland (8) |
| Dhaka scene | 638 x 480 | 4x3 | cotan, donkey_kong, pigscene, prairie_ride, skeleton, unpacked, wither (7) |
| Bengal meme | 400 x 400 | 2x2 | aztec2, match, meditative, orb, pointer, tides (6) |
| Nahid Islam and Asif Mahmud | 300 x 450 | 2x3 | backyard, bomb, owlemons, passage, stage (5) |

Because a vanilla painting keeps its own block size, a 1x1 or 4x4 vanilla painting shows the nearest image stretched to fit. The "Block size in manifest" column is the size defined for the Custom Paintings mod, not for the texture override.
