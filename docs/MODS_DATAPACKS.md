# Installed Mods, Datapacks, and Assets

This document catalogs every active modification, server datapack, and asset pack installed in Project Hajaribagh. Mod facts (sides, versions, licences) were checked against the Modrinth API on 2026-10-22. The jars themselves are not in this repo, so file names come from the earlier docs and were not re-read from the server.

---

## 1. Active Mods (`mods/` on the cloud VM)

| File Name | Source | Purpose | Client needs it? | Status on 2026-10-22 |
| :--- | :--- | :--- | :--- | :--- |
| `fabric-api-0.162.0+26.3.jar` | [Fabric API](https://modrinth.com/mod/fabric-api) | Base hooks and event bus for Fabric | No (optional) | Active |
| `lithium-fabric-0.26.2+mc26.3.jar` | [Lithium](https://modrinth.com/mod/lithium) | Game logic, chunk, and entity tick optimization | No (optional) | Active |
| `ferritecore-9.0.0-fabric.jar` | [FerriteCore](https://modrinth.com/mod/ferrite-core) | Lower memory use through data deduplication | No (optional) | Active |
| `krypton-0.3.2.jar` | [Krypton](https://modrinth.com/mod/krypton) | Networking stack optimization | No (optional) | Active |
| `polymer-bundled-0.18.4+26.3.jar` | [Polymer](https://modrinth.com/mod/polymer) | Protocol translation for server-side items and blocks | No (optional) | Active |
| `brewery-0.17.1+26.3.jar` | [Patbox's Brewery](https://modrinth.com/mod/brewery) | Cauldron brewing and barrel aging via Polymer | No (unsupported on client) | Active |
| `custompaintings-fabric-4.0.2+26.3.jar` | [Custom Paintings](https://modrinth.com/mod/custom-paintings-mod) | Painting packs and selection menu | Yes (required on client) | Active |
| `Chunky-Fabric-1.5.3.jar` | [Chunky](https://modrinth.com/mod/chunky) | Background chunk pregeneration for zero exploration lag | No (server only) | Active, 63,001 chunks generated |
| `spark-1.10.187-fabric.jar` | [spark](https://modrinth.com/mod/spark) | Performance profiler and tick health monitor | No (server only) | Active |
| `netherportalfix-fabric-26.3-26.3.0.1.jar` | [NetherPortalFix](https://modrinth.com/mod/netherportalfix) | Correct portal linking for multiplayer travel | No (server only) | Active |
| `balm-fabric-26.3-26.3.0.3.jar` | [Balm](https://modrinth.com/mod/balm) | Abstraction library required by NetherPortalFix | No (server only) | Active |
| `doubledoors-26.3.0-7.5.jar` | [Double Doors](https://modrinth.com/mod/double-doors) | Opens matching double doors, trapdoors, and gates together | No (server only) | Active |
| `collective-26.3.0-8.64.jar` | [Collective](https://modrinth.com/mod/collective) | Shared library required by Double Doors | No (server only) | Active |
| `rightclickharvest-fabric-4.6.2+26.3.x.jar` | [RightClickHarvest](https://modrinth.com/mod/rightclickharvest) | Harvest and replant crops with a right click | No (server only) | Active |
| `jamlib-fabric-2.3.1+26.3.x.jar` | [JamLib](https://modrinth.com/mod/jamlib) | Library required by RightClickHarvest | No (server only) | Active |
| `ledger-1.3.25.jar` | [Ledger](https://modrinth.com/mod/ledger) | Block and container transaction logger with rollback | No (server only) | Active |
| `fabric-language-kotlin-1.14.2+kotlin.2.4.21.jar` | [Fabric Kotlin](https://modrinth.com/mod/fabric-language-kotlin) | Kotlin language adapter required by Ledger | No (server only) | Active |
| `lootr-fabric-26.3-1.25.42.124.jar` | [Lootr](https://modrinth.com/mod/lootr) | Per-player instanced dungeon and structure loot | No (server only with Polymer) | Active |
| `LootrPolymer-1.3.jar` | [Lootr Polymer Patch](https://modrinth.com/mod/lootr-polymer-patch) | Virtualizes Lootr containers for vanilla clients | No (server only) | Active |

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
* **Seeds**: Crafted (1 Wheat Seed + 1 Dried Kelp = 2 Cannabis Seeds) or foraged by breaking wild ferns in forests (25% drop rate).
* **Cultivation**: Planted on hydrated farmland as a crop. Progresses through growth stages into tall stalks. Can be bonemealed to accelerate growth.
* **Harvesting**: Breaking or right-clicking mature crops drops 2 to 3 Raw Cannabis Buds and 1 to 2 Cannabis Seeds.
* **Curing**: Raw buds are dried on campfires (30s), in smokers (5s), or in furnaces (10s) to produce Cured Cannabis Buds.
* **Rolling**: 1 Paper + 1 Cured Bud (or Dried Kelp) crafts 3 Cannabis Joints (`warped_fungus_on_a_stick` with custom name and lore).
* **Right-click detection**: Using the joint item increments the `use_joint` scoreboard objective.
* **Effects per use**: Regeneration II for 15 seconds, Resistance II for 20 seconds, Slow Falling for 10 seconds, Saturation for 2 seconds, and Nausea for 6 seconds.
* **Presentation**: Campfire crackle audio plays for nearby players, drink sound plays for the smoker, an action bar alert appears, and smoke particles puff in front of the player's face for 3 seconds.
* **Trigger command**: `/trigger smoke` runs the same smoke animation and effects without needing a joint item in hand.

### `ore_xray`
* **Path**: `datapacks/ore_xray/`
* **What it does**: `/trigger xray` switches the player to spectator mode with infinite night vision, and switches back to survival and clears night vision on the next use.
* **Who can use it**: the trigger is enabled only for the player named `Kowsyke`. Everyone else's `xray` score is reset every tick.
* **Unused file**: `deny.mcfunction` (fake "Unknown or incomplete command" message) is not called by anything.

### `server_guide`
* **Path**: `datapacks/server_guide/`
* **What it does**: Equips every new player on first login with full leather armor, a stone toolset (sword, pickaxe, axe, hoe), 10 torches, 10 cooked beef steaks, an empty exploration map, and the written server guide book with base coordinates (X: 163, Z: -307).
* **On-demand access**: Any player can run `/trigger guide` at any time to receive a replacement copy of the book without duplicating starter armor or tools.
* **Files**: `pack.mcmeta`, `tags/function/load.json`, `tags/function/tick.json`, `function/load.mcfunction`, `function/tick.mcfunction`, `function/give_starter_kit.mcfunction`, `function/give_book.mcfunction`.

### `salman_f_rahman`
* **Path**: `datapacks/salman_f_rahman/`
* **What it does**: Tracks the total volume of stone and wood blocks mined by each player. The player with the highest total holds the title of Salman F Rahman.
* **Leaderboard**: Displays player scores on the sidebar scoreboard. Players can refresh the display with `/trigger leaderboard`.
* **Visual aura**: The active tycoon glows and cycles through rainbow colors on their team nameplate and player list entry.
* **Daily dividend**: Awards 1 random ore directly into the title holder's inventory every sunrise.
* **Full inventory reminder**: If the player's inventory is full at sunrise, an alert begins a 10 second countdown. If a slot opens within 10 seconds, the ore is granted. If the inventory stays full, the ore is forfeited.
* **Files**: `pack.mcmeta`, `data/minecraft/tags/function/load.json`, `data/minecraft/tags/function/tick.json`, `data/salman_f_rahman/loot_table/daily_ore.json`, `data/salman_f_rahman/function/*.mcfunction`.

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
