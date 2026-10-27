#!/usr/bin/env python3
"""
Generator for the Subterranean Citadel Datapack.
Constructs a pro-tier underground mega fortress with:
- Grand descent stairs from Treasury
- Central Grand Bio-Atrium (Lush Cave fusion, sunken illuminated bio-aquarium, gothic vault ribs)
- Sector A: Dwarven Industrial Super Smelter, Smithing Forge and Alchemy Lab
- Sector B: Automated Hydroponic Sugarcane/Bamboo Observer Farm and Tree Conservatory
- Sector C: Heavy Blast Door, Sovereign War Room, and Luxury Suites (Kowsyke, Ahsane, Jamal)
- Sector D: Sub-floor redstone conduits and inspection channels
"""
import os
import shutil

DP_BASE = "/home/K/hajaribagh-repo/datapacks/underground_citadel"
FUNC_DIR = os.path.join(DP_BASE, "data/citadel/function")

def main():
    if os.path.exists(DP_BASE):
        shutil.rmtree(DP_BASE)
    os.makedirs(FUNC_DIR, exist_ok=True)

    # pack.mcmeta
    with open(os.path.join(DP_BASE, "pack.mcmeta"), "w") as f:
        f.write('{\n  "pack": {\n    "pack_format": 48,\n    "description": "The Subterranean Citadel Mega Fortress Datapack"\n  }\n}\n')

    # 1. stairs_descent.mcfunction
    with open(os.path.join(FUNC_DIR, "stairs_descent.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Grand Staircase Descent
# Extends from Treasury stairs at X: 116..118, Z: -318, Y: 60 down to Atrium landing at Y: 50, Z: -305

# Clear stair corridor
fill 114 49 -318 120 65 -305 air

# Enclosure walls and vaulting
fill 114 49 -318 114 65 -305 deepslate_tiles
fill 120 49 -318 120 65 -305 deepslate_tiles

# Stair steps descending south facing south
# Z=-317: Y=59
fill 114 49 -317 120 58 -317 polished_deepslate
fill 116 59 -317 118 59 -317 spruce_stairs[facing=south]
setblock 115 59 -317 stripped_dark_oak_log[axis=y]
setblock 119 59 -317 stripped_dark_oak_log[axis=y]
fill 115 60 -317 115 64 -317 deepslate_tile_wall
fill 119 60 -317 119 64 -317 deepslate_tile_wall

# Z=-316: Y=58
fill 114 49 -316 120 57 -316 polished_deepslate
fill 116 58 -316 118 58 -316 spruce_stairs[facing=south]

# Z=-315: Y=57
fill 114 49 -315 120 56 -315 polished_deepslate
fill 116 57 -315 118 57 -315 spruce_stairs[facing=south]
setblock 115 58 -315 stripped_dark_oak_log[axis=y]
setblock 119 58 -315 stripped_dark_oak_log[axis=y]
setblock 115 59 -315 lantern[hanging=false]
setblock 119 59 -315 lantern[hanging=false]

# Z=-314: Y=56
fill 114 49 -314 120 55 -314 polished_deepslate
fill 116 56 -314 118 56 -314 spruce_stairs[facing=south]

# Z=-313: Y=55
fill 114 49 -313 120 54 -313 polished_deepslate
fill 116 55 -313 118 55 -313 spruce_stairs[facing=south]

# Z=-312: Y=54
fill 114 49 -312 120 53 -312 polished_deepslate
fill 116 54 -312 118 54 -312 spruce_stairs[facing=south]
setblock 115 55 -312 stripped_dark_oak_log[axis=y]
setblock 119 55 -312 stripped_dark_oak_log[axis=y]
setblock 115 56 -312 lantern[hanging=false]
setblock 119 56 -312 lantern[hanging=false]

# Z=-311: Y=53
fill 114 49 -311 120 52 -311 polished_deepslate
fill 116 53 -311 118 53 -311 spruce_stairs[facing=south]

# Z=-310: Y=52
fill 114 49 -310 120 51 -310 polished_deepslate
fill 116 52 -310 118 52 -310 spruce_stairs[facing=south]

# Z=-309: Y=51
fill 114 49 -309 120 50 -309 polished_deepslate
fill 116 51 -309 118 51 -309 spruce_stairs[facing=south]
setblock 115 52 -309 stripped_dark_oak_log[axis=y]
setblock 119 52 -309 stripped_dark_oak_log[axis=y]
setblock 115 53 -309 lantern[hanging=false]
setblock 119 53 -309 lantern[hanging=false]

# Z=-308: Y=50 (Final landing step)
fill 114 49 -308 120 49 -308 polished_deepslate
fill 116 50 -308 118 50 -308 spruce_stairs[facing=south]

# Transition Vestibule at Z: -307..-305 with floor Y=50
fill 114 49 -307 120 49 -305 polished_deepslate
fill 116 50 -307 118 50 -305 stripped_spruce_wood[axis=z]
fill 115 50 -307 115 50 -305 mud_bricks
fill 119 50 -307 119 50 -305 mud_bricks

# Under-floor ambient lights in vestibule
setblock 117 49 -306 shroomlight
setblock 117 50 -306 moss_carpet
setblock 116 50 -306 moss_block
setblock 118 50 -306 moss_block

# Archway pillars entering Atrium
fill 115 51 -305 115 54 -305 stripped_dark_oak_log[axis=y]
fill 119 51 -305 119 54 -305 stripped_dark_oak_log[axis=y]
setblock 116 55 -305 dark_oak_stairs[facing=east,half=top]
setblock 118 55 -305 dark_oak_stairs[facing=west,half=top]
setblock 117 55 -305 polished_deepslate_slab[type=top]
''')

    # 2. atrium_excavate.mcfunction
    with open(os.path.join(FUNC_DIR, "atrium_excavate.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Atrium Excavation
# Core dimensions: X: 104..130, Y: 48..58, Z: -305..-277

# Clear central volume to air
fill 105 50 -304 129 57 -278 air

# Clear sunken pool basin
fill 112 47 -296 122 49 -286 air
''')

    # 3. atrium_shell.mcfunction
    with open(os.path.join(FUNC_DIR, "atrium_shell.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Atrium Shell and Architecture
# Main Floor at Y: 50
fill 104 49 -305 130 49 -277 polished_deepslate
fill 105 50 -304 129 50 -278 polished_andesite

# Ceiling Vault Shell at Y: 58
fill 104 58 -305 130 58 -277 deepslate_tiles

# Perimeter Structural Walls
fill 104 50 -305 104 58 -277 deepslate_tiles
fill 130 50 -305 130 58 -277 deepslate_tiles
fill 104 50 -305 130 58 -305 deepslate_tiles
fill 104 50 -277 130 58 -277 deepslate_tiles

# Walkway Ribbons with Dark Oak and Smooth Quartz Borders
fill 116 50 -304 118 50 -278 stripped_dark_oak_wood[axis=z]
fill 105 50 -292 129 50 -290 stripped_dark_oak_wood[axis=x]

# Grand Corner Structural Pillars (Dark Oak, Basalt, Polished Blackstone)
# Pillar 1 (NW: 109, -299)
fill 109 50 -299 109 57 -299 stripped_dark_oak_log[axis=y]
setblock 109 50 -299 polished_basalt[axis=y]
setblock 109 56 -299 smooth_quartz
setblock 109 57 -299 smooth_quartz_stairs[facing=south,half=top]

# Pillar 2 (NE: 125, -299)
fill 125 50 -299 125 57 -299 stripped_dark_oak_log[axis=y]
setblock 125 50 -299 polished_basalt[axis=y]
setblock 125 56 -299 smooth_quartz
setblock 125 57 -299 smooth_quartz_stairs[facing=south,half=top]

# Pillar 3 (SW: 109, -283)
fill 109 50 -283 109 57 -283 stripped_dark_oak_log[axis=y]
setblock 109 50 -283 polished_basalt[axis=y]
setblock 109 56 -283 smooth_quartz
setblock 109 57 -283 smooth_quartz_stairs[facing=north,half=top]

# Pillar 4 (SE: 125, -283)
fill 125 50 -283 125 57 -283 stripped_dark_oak_log[axis=y]
setblock 125 50 -283 polished_basalt[axis=y]
setblock 125 56 -283 smooth_quartz
setblock 125 57 -283 smooth_quartz_stairs[facing=north,half=top]

# Sunken Bio-Aquarium Basin at X: 113..121, Z: -295..-287
# Foundation at Y: 47
fill 113 47 -295 121 47 -287 sea_lantern
fill 114 47 -294 120 47 -288 dark_prismarine
setblock 117 47 -291 sea_lantern

# Basin Walls at Y: 48..49
fill 112 48 -296 122 49 -296 polished_deepslate
fill 112 48 -286 122 49 -286 polished_deepslate
fill 112 48 -296 112 49 -286 polished_deepslate
fill 122 48 -296 122 49 -286 polished_deepslate

# Water Layer at Y: 48..49
fill 113 48 -295 121 49 -287 water

# Top Glass Walkway Layer at Y: 50
fill 113 50 -295 121 50 -287 cyan_stained_glass
# Central Crosswalk in Clear Glass
fill 116 50 -295 118 50 -287 glass
fill 113 50 -292 121 50 -290 glass

# Spawn tropical aquatic wildlife into the bio-basin
summon tropical_fish 117 48.5 -291 {PersistenceRequired:1b}
summon tropical_fish 115 48.5 -293 {PersistenceRequired:1b}
summon tropical_fish 119 48.5 -289 {PersistenceRequired:1b}
summon axolotl 117 48.5 -289 {Variant:0,PersistenceRequired:1b}
summon axolotl 115 48.5 -290 {Variant:1,PersistenceRequired:1b}
''')

    # 4. atrium_decor.mcfunction
    with open(os.path.join(FUNC_DIR, "atrium_decor.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Atrium Foliage, Lighting and Detailing

# Under-Floor Hidden Lighting under Moss
fill 106 49 -303 108 49 -301 shroomlight
fill 106 50 -303 108 50 -301 moss_carpet
fill 126 49 -303 128 49 -301 shroomlight
fill 126 50 -303 128 50 -301 moss_carpet
fill 106 49 -281 108 49 -279 shroomlight
fill 106 50 -281 108 50 -279 moss_carpet
fill 126 49 -281 128 49 -279 shroomlight
fill 126 50 -281 128 50 -279 moss_carpet

# Perimeter Raised Moss Planters and Terraces
fill 105 51 -304 107 51 -296 moss_block
fill 105 52 -304 107 52 -296 flowering_azalea_leaves
fill 127 51 -304 129 51 -296 moss_block
fill 127 52 -304 129 52 -296 flowering_azalea_leaves
fill 105 51 -286 107 51 -278 moss_block
fill 105 52 -286 107 52 -278 flowering_azalea_leaves
fill 127 51 -286 129 51 -278 moss_block
fill 127 52 -286 129 52 -278 flowering_azalea_leaves

# Ceiling Hanging Spore Blossoms and Cave Vines
setblock 111 57 -296 spore_blossom
setblock 123 57 -296 spore_blossom
setblock 111 57 -286 spore_blossom
setblock 123 57 -286 spore_blossom
setblock 117 57 -298 spore_blossom
setblock 117 57 -284 spore_blossom

# Cave Vines with Glowing Berries
fill 108 56 -301 108 57 -301 cave_vines[berries=true]
fill 126 56 -301 126 57 -301 cave_vines[berries=true]
fill 108 56 -281 108 57 -281 cave_vines[berries=true]
fill 126 56 -281 126 57 -281 cave_vines[berries=true]

# Central Hanging Chandelier over the Bio-Aquarium
setblock 117 57 -291 iron_chain[axis=y]
setblock 117 56 -291 iron_chain[axis=y]
setblock 117 55 -291 shroomlight
setblock 116 55 -291 dark_oak_trapdoor[facing=west,open=false,half=top]
setblock 118 55 -291 dark_oak_trapdoor[facing=east,open=false,half=top]
setblock 117 55 -292 dark_oak_trapdoor[facing=north,open=false,half=top]
setblock 117 55 -290 dark_oak_trapdoor[facing=south,open=false,half=top]
setblock 117 54 -291 soul_lantern[hanging=true]

# Potted Flora along the Crossways
setblock 112 51 -293 potted_flowering_azalea_bush
setblock 112 51 -289 potted_flowering_azalea_bush
setblock 122 51 -293 potted_flowering_azalea_bush
setblock 122 51 -289 potted_flowering_azalea_bush
''')

    # 5. forge_excavate.mcfunction
    with open(os.path.join(FUNC_DIR, "forge_excavate.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Sector A (Forge and Super Smelter) Excavation
# Connecting corridor from Atrium: X: 99..104, Z: -292..-290, Y: 50..55
fill 99 50 -292 104 55 -290 air

# Main Forge Hall: X: 83..98, Z: -300..-282, Y: 49..57
fill 83 49 -300 98 57 -282 air
''')

    # 6. forge_build.mcfunction
    with open(os.path.join(FUNC_DIR, "forge_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Sector A Dwarven Industrial Forge and Super Smelter

# Enclosure Shell
fill 82 49 -301 99 49 -281 polished_basalt[axis=y]
fill 82 50 -301 82 57 -281 polished_deepslate
fill 99 50 -301 99 57 -281 polished_deepslate
fill 82 50 -301 99 57 -301 polished_deepslate
fill 82 50 -281 99 57 -281 polished_deepslate
fill 82 58 -301 99 58 -281 deepslate_tiles

# Corridor to Atrium
fill 99 49 -292 104 49 -290 polished_basalt[axis=x]
fill 99 50 -292 104 50 -290 smooth_stone
fill 99 51 -293 104 54 -293 deepslate_tile_wall
fill 99 51 -289 104 54 -289 deepslate_tile_wall
fill 99 55 -292 104 55 -290 polished_deepslate_stairs[facing=south,half=top]

# Forge Floor (Industrial Grate Pattern: Smooth Stone and Basalt)
fill 83 50 -300 98 50 -282 smooth_stone
fill 85 50 -298 96 50 -284 polished_basalt[axis=y]

# -------------------------------------------------------------
# 16-Furnace Super Smelter Battery (North Wall, Z: -300)
# Output Double Chest at (89, 50, -299) and (90, 50, -299)
setblock 89 50 -299 chest[facing=south,type=left]
setblock 90 50 -299 chest[facing=south,type=right]

# Smelter Line: 8 Blast Furnaces (X: 84..91) and 8 Furnaces (X: 92..97)
fill 84 51 -300 91 51 -300 blast_furnace[facing=south,lit=true]
fill 92 51 -300 97 51 -300 furnace[facing=south,lit=true]

# Bottom collection hoppers below furnaces feeding output
fill 84 50 -300 97 50 -300 hopper[facing=south]

# Top Item-Input Hoppers at Y: 52 feeding down into furnaces
fill 84 52 -300 97 52 -300 hopper[facing=down]

# Top Input Chests at Y: 53
fill 84 53 -300 97 53 -300 chest[facing=south]

# Smelter Status Lighting (Redstone Lamps above)
fill 84 54 -300 97 54 -300 redstone_lamp[lit=true]
fill 84 55 -300 97 55 -300 redstone_block

# -------------------------------------------------------------
# Heavy Anvil and Master Smithing Bay (Center: X: 89..92, Z: -291..-293)
fill 89 50 -293 92 50 -291 iron_block
setblock 89 51 -293 anvil[facing=south]
setblock 90 51 -293 smithing_table
setblock 91 51 -293 grindstone[facing=south,face=floor]
setblock 92 51 -293 chipped_anvil[facing=south]

# Tool and Armor Displays
summon armor_stand 88 51 -293 {ShowArms:1b,NoBasePlate:1b,Rotation:[0f,0f],Equipment:[{id:"netherite_pickaxe",count:1},{},{},{},{id:"netherite_helmet",count:1}]}
summon armor_stand 93 51 -293 {ShowArms:1b,NoBasePlate:1b,Rotation:[0f,0f],Equipment:[{id:"netherite_sword",count:1},{},{},{},{id:"netherite_chestplate",count:1}]}

# Lava Observation Core in Tinted Glass (West Wall: X: 83, Z: -291..-293)
fill 83 50 -293 83 55 -291 lava
fill 84 50 -293 84 55 -291 tinted_glass
fill 84 50 -294 84 55 -294 copper_grate
fill 84 50 -290 84 55 -290 copper_grate

# -------------------------------------------------------------
# Potion Alchemy Laboratory (South Wall, Z: -282)
# Soul Sand Nether Wart Nursery
fill 84 50 -283 87 50 -283 soul_sand
fill 84 51 -283 87 51 -283 nether_wart[age=3]

# Brewing Station Counter
fill 89 50 -283 93 50 -283 polished_blackstone
setblock 89 51 -283 brewing_stand[has_bottle_0=true,has_bottle_1=true,has_bottle_2=true]
setblock 90 51 -283 water_cauldron[level=3]
setblock 91 51 -283 brewing_stand[has_bottle_0=true,has_bottle_1=true]
setblock 92 51 -283 barrel[facing=up]
setblock 93 51 -283 water_cauldron[level=3]

# Alchemy Supply Chests and Shelving
fill 94 51 -283 97 51 -283 chiseled_bookshelf[facing=north]
fill 94 52 -283 97 52 -283 barrel[facing=south]
''')

    # 7. hydroponics_excavate.mcfunction
    with open(os.path.join(FUNC_DIR, "hydroponics_excavate.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Sector B (Hydroponics and Tree Conservatory) Excavation
# Connecting corridor from Atrium: X: 130..136, Z: -292..-290, Y: 50..55
fill 130 50 -292 136 55 -290 air

# Main Agricultural Wing: X: 137..153, Z: -301..-281, Y: 49..60
fill 137 49 -301 153 60 -281 air
''')

    # 8. hydroponics_build.mcfunction
    with open(os.path.join(FUNC_DIR, "hydroponics_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Sector B Automated Hydroponics and Tree Conservatory

# Shell and Foundation
fill 136 49 -302 154 49 -280 stripped_cherry_wood[axis=y]
fill 136 50 -302 136 60 -280 smooth_quartz
fill 154 50 -302 154 60 -280 smooth_quartz
fill 136 50 -302 154 60 -302 smooth_quartz
fill 136 50 -280 154 60 -280 smooth_quartz
fill 136 61 -302 154 61 -280 deepslate_tiles

# Corridor to Atrium
fill 130 49 -292 136 49 -290 stripped_cherry_wood[axis=x]
fill 130 50 -292 136 50 -290 bamboo_mosaic
fill 130 51 -293 136 54 -293 smooth_quartz_stairs[facing=south]
fill 130 51 -289 136 54 -289 smooth_quartz_stairs[facing=north]
fill 130 55 -292 136 55 -290 sea_lantern

# Wing Floor: Bamboo Mosaic, Moss, and Mud Soil
fill 137 50 -301 153 50 -281 bamboo_mosaic
fill 142 50 -297 148 50 -285 mud

# -------------------------------------------------------------
# 1. Automated Sugarcane and Bamboo Observer Farm (North Wall, Z: -301..-298)
# Water canal at Y: 49 feeding collection hopper
fill 138 49 -300 151 49 -300 water
setblock 137 49 -300 hopper[facing=west]
setblock 136 49 -300 barrel[facing=up]

# Planting Bed at Y: 50 (Sand and Mud)
fill 138 50 -301 144 50 -301 sand
fill 145 50 -301 151 50 -301 mud

# Stalks at Y: 51
fill 138 51 -301 144 51 -301 sugar_cane
fill 145 51 -301 151 51 -301 bamboo[age=1,leaves=large,stage=0]

# Sticky Pistons at Y: 52 facing South
fill 138 52 -301 151 52 -301 piston[facing=south]

# Observers at Y: 53 facing South (detecting growth at height 3)
fill 138 53 -301 151 53 -301 observer[facing=south]

# Redstone Transmission Line behind Pistons at Y: 52
fill 138 52 -302 151 52 -302 smooth_stone
fill 138 53 -302 151 53 -302 redstone_wire

# Clear Glass Enclosure so crops drop straight down
fill 138 51 -299 151 54 -299 glass
fill 138 55 -301 151 55 -299 sea_lantern

# -------------------------------------------------------------
# 2. Indoor Tree Conservatory and Wood Farm (Center: X: 142..148, Z: -296..-286)
# Rich Rooted Dirt and Mud Soil
fill 143 50 -295 147 50 -287 rooted_dirt
fill 144 50 -294 146 50 -288 mud

# Cherry Blossom and Dark Oak Canopy
fill 145 51 -293 145 56 -293 stripped_cherry_log[axis=y]
fill 143 56 -295 147 58 -291 cherry_leaves
fill 144 59 -294 146 59 -292 cherry_leaves

# Dark Oak Companion Tree
fill 145 51 -288 145 55 -288 stripped_dark_oak_log[axis=y]
fill 143 55 -290 147 57 -286 dark_oak_leaves

# Bonemeal Dispenser Station for Manual Rapid Sapling Growth
setblock 142 51 -291 dispenser[facing=east]
setblock 142 52 -291 stone_button[facing=east]

# -------------------------------------------------------------
# 3. Apiary Bee Sanctuary (South Wall, Z: -282..-284)
# Enclosed in Tinted Glass
fill 138 50 -284 151 50 -284 packed_mud
# Submerged Campfires to keep bees calm
fill 140 49 -283 148 49 -283 campfire[lit=true]
# Carpet over campfires
fill 140 50 -283 148 50 -283 moss_carpet

# Beehives and Bee Nests full of honey
setblock 141 51 -283 beehive[facing=north,honey_level=5]
setblock 143 51 -283 bee_nest[facing=north,honey_level=5]
setblock 145 51 -283 beehive[facing=north,honey_level=5]
setblock 147 51 -283 bee_nest[facing=north,honey_level=5]

# Flowers for pollination
setblock 141 51 -284 flowering_azalea
setblock 143 51 -284 rose_bush[half=lower]
setblock 143 52 -284 rose_bush[half=upper]
setblock 145 51 -284 flowering_azalea
setblock 147 51 -284 peony[half=lower]
setblock 147 52 -284 peony[half=upper]

# Tinted Glass Barrier
fill 139 51 -285 149 54 -285 tinted_glass
fill 139 55 -285 149 55 -283 sea_lantern

# Spawn friendly bees
summon bee 144 52 -284 {CannotEnterHiveTicks:0,TicksInHive:0}
summon bee 146 52 -284 {CannotEnterHiveTicks:0,TicksInHive:0}
''')

    # 9. bunker_excavate.mcfunction
    with open(os.path.join(FUNC_DIR, "bunker_excavate.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Sector C (Bunker, War Room and Suites) Excavation
# Connecting airlock corridor: X: 115..119, Z: -277..-272, Y: 50..55
fill 115 50 -277 119 55 -272 air

# War Room Chamber: X: 108..126, Z: -271..-259, Y: 49..57
fill 108 49 -271 126 57 -259 air

# Sovereign Suites:
# Kowsyke Suite (South): X: 111..123, Z: -258..-246, Y: 49..57
fill 111 49 -258 123 57 -246 air

# Ahsane Suite (West Wing): X: 98..107, Z: -271..-259, Y: 49..56
fill 98 49 -271 107 56 -259 air

# Jamal Suite (East Wing): X: 127..136, Z: -271..-259, Y: 49..56
fill 127 49 -271 136 56 -259 air
''')

    # 10. bunker_build.mcfunction
    with open(os.path.join(FUNC_DIR, "bunker_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Sector C Heavy Blast Door and War Room

# -------------------------------------------------------------
# Heavy Blast Door Airlock at Z: -275..-273
# Frame in Crying Obsidian and Polished Deepslate
fill 114 49 -275 120 49 -273 crying_obsidian
fill 114 55 -275 120 55 -273 crying_obsidian
fill 114 50 -275 114 54 -275 crying_obsidian
fill 120 50 -275 120 54 -275 crying_obsidian

# Blast Door Opening: 3x3 at X: 116..118, Y: 51..53
# Heavy Iron Bars and Polished Basalt Piston Seal
fill 115 50 -274 119 50 -274 polished_deepslate
fill 116 51 -274 118 53 -274 iron_bars
setblock 115 52 -275 redstone_lamp[lit=true]
setblock 119 52 -275 redstone_lamp[lit=true]
setblock 115 51 -275 lever[facing=north]
setblock 119 51 -275 lever[facing=north]

# -------------------------------------------------------------
# Sovereign Council War Room (X: 108..126, Z: -271..-259)
# Shell and Foundation
fill 107 49 -272 127 49 -258 polished_deepslate
fill 108 50 -271 126 50 -259 polished_blackstone
fill 107 58 -272 127 58 -258 deepslate_tiles

# Perimeter Walls: Deepslate Bricks and Chiseled Deepslate
fill 107 50 -272 107 57 -258 deepslate_bricks
fill 127 50 -272 127 57 -258 deepslate_bricks
fill 107 50 -272 127 57 -272 deepslate_bricks
fill 107 50 -258 127 57 -258 deepslate_bricks

# Red Carpet Runner
fill 116 50 -271 118 50 -259 red_carpet
setblock 117 49 -268 shroomlight
setblock 117 49 -265 shroomlight
setblock 117 49 -262 shroomlight

# Grand Council Conference Table (Center: X: 115..119, Z: -267..-263)
fill 115 51 -267 119 51 -263 dark_oak_slab[type=top]
fill 116 51 -266 118 51 -264 polished_blackstone_slab[type=top]
summon end_crystal 117.5 52.0 -264.5 {ShowBottom:0b}

# Sovereign Council Armchairs
# Prime Minister Chair (South end facing north)
setblock 117 51 -262 dark_oak_stairs[facing=north]
setblock 116 51 -262 dark_oak_trapdoor[facing=west,open=true]
setblock 118 51 -262 dark_oak_trapdoor[facing=east,open=true]

# Executive Chairs (East and West)
setblock 114 51 -266 dark_oak_stairs[facing=east]
setblock 114 51 -264 dark_oak_stairs[facing=east]
setblock 120 51 -266 dark_oak_stairs[facing=west]
setblock 120 51 -264 dark_oak_stairs[facing=west]

# Sovereign Strategic Map Wall (East Wall: X: 126, Z: -266..-264)
fill 126 51 -266 126 53 -264 stripped_dark_oak_wood[axis=y]
fill 126 52 -266 126 52 -264 cartography_table

# Server Constitution Lectern (West Wall: X: 108, Z: -265)
setblock 108 51 -265 lectern[facing=east]
setblock 108 52 -265 lantern[hanging=false]
fill 108 51 -267 108 53 -267 bookshelf
fill 108 51 -263 108 53 -263 bookshelf
''')

    # 11. suites_build.mcfunction
    with open(os.path.join(FUNC_DIR, "suites_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Luxury Sovereign Suites (Kowsyke, Ahsane, Jamal)

# =============================================================
# 1. KOWSYKE PRIME MINISTER SUITE (South: X: 111..123, Z: -258..-246)
# =============================================================
fill 110 49 -258 124 49 -245 gilded_blackstone
fill 111 50 -257 123 50 -246 stripped_dark_oak_wood[axis=z]
fill 110 50 -258 110 57 -245 polished_blackstone_bricks
fill 124 50 -258 124 57 -245 polished_blackstone_bricks
fill 110 50 -245 124 57 -245 polished_blackstone_bricks
fill 110 58 -258 124 58 -245 deepslate_tiles

# Royal King Canopy Bed (Gold and Red, X: 116..118, Z: -247..-249)
fill 116 51 -247 118 51 -247 gold_block
fill 116 51 -248 118 51 -248 red_bed[facing=south,part=head]
fill 116 51 -249 118 51 -249 red_bed[facing=south,part=foot]
fill 115 51 -247 115 54 -247 stripped_dark_oak_log[axis=y]
fill 119 51 -247 119 54 -247 stripped_dark_oak_log[axis=y]
fill 115 55 -249 119 55 -247 dark_oak_slab[type=bottom]
fill 116 54 -249 118 54 -249 yellow_wool

# Private Aquarium Wall (West Wall: X: 111, Z: -254..-250)
fill 110 50 -254 110 54 -250 sea_lantern
fill 110 51 -253 110 53 -251 water
fill 111 51 -253 111 53 -251 tinted_glass
summon axolotl 110.5 51.5 -252 {Variant:4,PersistenceRequired:1b}

# Prime Minister Display Pedestal (Gold Silence Trim Netherite Armor)
setblock 121 51 -252 gold_block
summon armor_stand 121 52 -252 {ShowArms:1b,NoBasePlate:1b,Rotation:[270f,0f],Equipment:[{id:"netherite_sword",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:gold",pattern:"minecraft:silence"}}}]}

# Private Executive Desk and Safe
setblock 121 51 -255 dark_oak_stairs[facing=south]
setblock 121 51 -256 ender_chest[facing=south]
setblock 120 51 -256 dark_oak_slab[type=top]
setblock 120 52 -256 lantern[hanging=false]

# =============================================================
# 2. AHSANE EXECUTIVE SUITE (West: X: 98..107, Z: -271..-259)
# =============================================================
fill 97 49 -272 108 49 -258 polished_deepslate
fill 98 50 -271 107 50 -259 cyan_carpet
fill 97 50 -272 97 56 -258 deepslate_bricks
fill 97 50 -272 107 56 -272 deepslate_bricks
fill 97 50 -258 107 56 -258 deepslate_bricks
fill 97 57 -272 108 57 -258 deepslate_tiles

# Ahsane Cyan Canopy Bed
fill 98 51 -269 98 54 -269 dark_oak_fence
fill 101 51 -269 101 54 -269 dark_oak_fence
fill 98 51 -267 98 54 -267 dark_oak_fence
fill 101 51 -267 101 54 -267 dark_oak_fence
fill 98 55 -269 101 55 -267 cyan_carpet
setblock 99 51 -268 cyan_bed[facing=west,part=head]
setblock 100 51 -268 cyan_bed[facing=west,part=foot]

# Private Grand Library Alcove
fill 98 51 -261 103 53 -261 bookshelf
setblock 101 51 -263 dark_oak_stairs[facing=north]
setblock 101 51 -262 dark_oak_slab[type=top]

# Ahsane Display Pedestal (Diamond Bolt Trim Armor)
setblock 105 51 -268 diamond_block
summon armor_stand 105 52 -268 {ShowArms:1b,NoBasePlate:1b,Rotation:[180f,0f],Equipment:[{id:"diamond_sword",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:diamond",pattern:"minecraft:bolt"}}}]}

# =============================================================
# 3. JAMAL EXECUTIVE SUITE (East: X: 127..136, Z: -271..-259)
# =============================================================
fill 126 49 -272 137 49 -258 dark_prismarine
fill 127 50 -271 136 50 -259 purple_carpet
fill 137 50 -272 137 56 -258 deepslate_bricks
fill 127 50 -272 137 56 -272 deepslate_bricks
fill 127 50 -258 137 56 -258 deepslate_bricks
fill 126 57 -272 137 57 -258 deepslate_tiles

# Jamal Purple Canopy Bed
fill 133 51 -269 133 54 -269 dark_oak_fence
fill 136 51 -269 136 54 -269 dark_oak_fence
fill 133 51 -267 133 54 -267 dark_oak_fence
fill 136 51 -267 136 54 -267 dark_oak_fence
fill 133 55 -269 136 55 -267 purple_carpet
setblock 135 51 -268 purple_bed[facing=east,part=head]
setblock 134 51 -268 purple_bed[facing=east,part=foot]

# Resonating Amethyst Geode Wall (East Wall)
fill 136 51 -265 136 54 -262 amethyst_block
setblock 135 52 -264 amethyst_cluster[facing=west]
setblock 135 53 -263 amethyst_cluster[facing=west]
setblock 135 51 -263 small_amethyst_bud[facing=west]

# Jamal Display Pedestal (Amethyst Ward Trim Armor)
setblock 129 51 -268 amethyst_block
summon armor_stand 129 52 -268 {ShowArms:1b,NoBasePlate:1b,Rotation:[180f,0f],Equipment:[{id:"bow",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:amethyst",pattern:"minecraft:ward"}}}]}
''')

    # 12. conduits_build.mcfunction
    with open(os.path.join(FUNC_DIR, "conduits_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Sector D Sub-Floor Redstone Conduits & Inspection Traces

# Floor Conduits in Central Grand Atrium Walkways (Glass inserts showing engineering below)
# East-West Conduits at Y: 49 under tinted glass at Y: 50
setblock 110 50 -291 tinted_glass
setblock 110 49 -291 comparator[facing=west]
setblock 111 50 -291 tinted_glass
setblock 111 49 -291 redstone_wire
setblock 112 50 -291 tinted_glass
setblock 112 49 -291 repeater[facing=west]

setblock 122 50 -291 tinted_glass
setblock 122 49 -291 repeater[facing=east]
setblock 123 50 -291 tinted_glass
setblock 123 49 -291 redstone_wire
setblock 124 50 -291 tinted_glass
setblock 124 49 -291 comparator[facing=east]

# North-South Conduits at Y: 49 under tinted glass at Y: 50
setblock 117 50 -302 tinted_glass
setblock 117 49 -302 repeater[facing=south]
setblock 117 50 -300 tinted_glass
setblock 117 49 -300 redstone_wire
setblock 117 50 -282 tinted_glass
setblock 117 49 -282 comparator[facing=south]
setblock 117 50 -280 tinted_glass
setblock 117 49 -280 redstone_wire
''')

    # 13. build_all.mcfunction
    with open(os.path.join(FUNC_DIR, "build_all.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Master Build Orchestrator
# Executes all sectors sequentially to construct the underground fortress

function citadel:stairs_descent
function citadel:atrium_excavate
function citadel:atrium_shell
function citadel:atrium_decor
function citadel:forge_excavate
function citadel:forge_build
function citadel:hydroponics_excavate
function citadel:hydroponics_build
function citadel:bunker_excavate
function citadel:bunker_build
function citadel:suites_build
function citadel:conduits_build

tellraw @a [{"text":"[Architect] ","color":"gold","bold":true},{"text":"The Subterranean Citadel Mega Fortress has been completed! All sectors operational.","color":"green"}]
''')

    print("Updated Subterranean Citadel Datapack generated successfully!")

if __name__ == "__main__":
    main()
