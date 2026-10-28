#!/usr/bin/env python3
"""Master Builder Generator: Fully Furnished and Restructured Subterranean Utopia Citadel.

Builds 12 complete, fully furnished, lamp-lit sectors with verified blockstate orientation:
1. Descent Staircase and Grand Crossroads Rotunda.
2. Bio Dome Atrium and Sunken Marine Aquarium.
3. Dwarven Metallurgy Forge and Super Smelter.
4. Hydroponics Biosphere and Apiary Sanctuary.
5. Celestial Portal Nexus and Amethyst Geode.
6. Grand Subterranean Athenaeum and Alchemical Stills.
7. Sovereign Banquet Hall and Dual Roaring Hearths.
8. Subterranean Hyperloop Transit Hub.
9. Grand High Parliament of the Republic.
10. Sovereign Residential Suites (King Abir, Ahsane, Jamal).
11. Vaulted Connecting Conduits.
12. The Great Treasury Vault (fully preserved and restored).
"""

import os
import shutil

DP_BASE = "/home/K/hajaribagh-repo/datapacks/underground_citadel"
FUNC_DIR = os.path.join(DP_BASE, "data/citadel/function")

def main():
    if os.path.exists(DP_BASE):
        shutil.rmtree(DP_BASE)
    os.makedirs(FUNC_DIR, exist_ok=True)

    with open(os.path.join(DP_BASE, "pack.mcmeta"), "w") as f:
        f.write('{\n  "pack": {\n    "pack_format": 48,\n    "description": "The Subterranean Utopia Mega Citadel Datapack"\n  }\n}\n')

    # 1. STAIRS DESCENT AND CROSSROADS ROTUNDA
    with open(os.path.join(FUNC_DIR, "stairs_descent.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Grand Staircase Descent and Crossroads
# Starts at Treasury opening (X: 116..118, Z: -322..-320, Y: 64) descending to Citadel (Y: 50, Z: -308)
# All descending steps face NORTH (half=bottom) so players step DOWN moving south.
# Ceiling stays beneath Y: 64 from Z=-319 onwards to protect the Treasury floor.

# Step Z=-322 (Y=64): Stair opening inside Treasury floor
fill 116 49 -322 118 63 -322 polished_deepslate
fill 116 64 -322 118 64 -322 spruce_stairs[facing=north,half=bottom]
setblock 115 64 -322 stripped_dark_oak_log[axis=y]
setblock 119 64 -322 stripped_dark_oak_log[axis=y]
setblock 115 65 -322 lantern[hanging=false]
setblock 119 65 -322 lantern[hanging=false]

# Step Z=-321 (Y=63)
fill 115 49 -321 119 62 -321 polished_deepslate
fill 116 63 -321 118 63 -321 spruce_stairs[facing=north,half=bottom]
fill 116 64 -321 118 66 -321 air
setblock 115 63 -321 stripped_dark_oak_log[axis=y]
setblock 119 63 -321 stripped_dark_oak_log[axis=y]

# Step Z=-320 (Y=62)
fill 115 49 -320 119 61 -320 polished_deepslate
fill 116 62 -320 118 62 -320 spruce_stairs[facing=north,half=bottom]
fill 116 63 -320 118 66 -320 air
setblock 115 62 -320 stripped_dark_oak_log[axis=y]
setblock 119 62 -320 stripped_dark_oak_log[axis=y]
setblock 115 63 -320 lantern[hanging=false]
setblock 119 63 -320 lantern[hanging=false]

# Step Z=-319 (Y=61): Ceiling is Y=63, leaving Y=64 Treasury floor 100% solid
fill 115 49 -319 119 60 -319 polished_deepslate
fill 116 61 -319 118 61 -319 spruce_stairs[facing=north,half=bottom]
fill 116 62 -319 118 63 -319 air
fill 115 64 -319 119 64 -319 spruce_planks
setblock 115 61 -319 stripped_dark_oak_log[axis=y]
setblock 119 61 -319 stripped_dark_oak_log[axis=y]

# Step Z=-318 (Y=60)
fill 115 49 -318 119 59 -318 polished_deepslate
fill 116 60 -318 118 60 -318 spruce_stairs[facing=north,half=bottom]
fill 116 61 -318 118 63 -318 air
fill 115 64 -318 119 64 -318 spruce_planks
setblock 115 60 -318 stripped_dark_oak_log[axis=y]
setblock 119 60 -318 stripped_dark_oak_log[axis=y]
setblock 115 61 -318 lantern[hanging=false]
setblock 119 61 -318 lantern[hanging=false]

# Step Z=-317 (Y=59)
fill 115 49 -317 119 58 -317 polished_deepslate
fill 116 59 -317 118 59 -317 spruce_stairs[facing=north,half=bottom]
fill 116 60 -317 118 63 -317 air
fill 115 64 -317 119 64 -317 spruce_planks
setblock 115 59 -317 stripped_dark_oak_log[axis=y]
setblock 119 59 -317 stripped_dark_oak_log[axis=y]

# Step Z=-316 (Y=58)
fill 115 49 -316 119 57 -316 polished_deepslate
fill 116 58 -316 118 58 -316 spruce_stairs[facing=north,half=bottom]
fill 116 59 -316 118 63 -316 air
fill 115 64 -316 119 64 -316 spruce_planks
setblock 115 58 -316 stripped_dark_oak_log[axis=y]
setblock 119 58 -316 stripped_dark_oak_log[axis=y]
setblock 115 59 -316 lantern[hanging=false]
setblock 119 59 -316 lantern[hanging=false]

# Step Z=-315 (Y=57)
fill 115 49 -315 119 56 -315 polished_deepslate
fill 116 57 -315 118 57 -315 spruce_stairs[facing=north,half=bottom]
fill 116 58 -315 118 62 -315 air
fill 115 64 -315 119 64 -315 spruce_planks
setblock 115 57 -315 stripped_dark_oak_log[axis=y]
setblock 119 57 -315 stripped_dark_oak_log[axis=y]

# Step Z=-314 (Y=56)
fill 115 49 -314 119 55 -314 polished_deepslate
fill 116 56 -314 118 56 -314 spruce_stairs[facing=north,half=bottom]
fill 116 57 -314 118 61 -314 air
fill 115 64 -314 119 64 -314 spruce_planks
setblock 115 56 -314 stripped_dark_oak_log[axis=y]
setblock 119 56 -314 stripped_dark_oak_log[axis=y]
setblock 115 57 -314 lantern[hanging=false]
setblock 119 57 -314 lantern[hanging=false]

# Step Z=-313 (Y=55)
fill 115 49 -313 119 54 -313 polished_deepslate
fill 116 55 -313 118 55 -313 spruce_stairs[facing=north,half=bottom]
fill 116 56 -313 118 60 -313 air
fill 115 64 -313 119 64 -313 spruce_planks
setblock 115 55 -313 stripped_dark_oak_log[axis=y]
setblock 119 55 -313 stripped_dark_oak_log[axis=y]

# Step Z=-312 (Y=54)
fill 115 49 -312 119 53 -312 polished_deepslate
fill 116 54 -312 118 54 -312 spruce_stairs[facing=north,half=bottom]
fill 116 55 -312 118 59 -312 air
fill 115 64 -312 119 64 -312 spruce_planks
setblock 115 54 -312 stripped_dark_oak_log[axis=y]
setblock 119 54 -312 stripped_dark_oak_log[axis=y]
setblock 115 55 -312 lantern[hanging=false]
setblock 119 55 -312 lantern[hanging=false]

# Step Z=-311 (Y=53)
fill 115 49 -311 119 52 -311 polished_deepslate
fill 116 53 -311 118 53 -311 spruce_stairs[facing=north,half=bottom]
fill 116 54 -311 118 58 -311 air
fill 115 64 -311 119 64 -311 spruce_planks
setblock 115 53 -311 stripped_dark_oak_log[axis=y]
setblock 119 53 -311 stripped_dark_oak_log[axis=y]

# Step Z=-310 (Y=52)
fill 115 49 -310 119 51 -310 polished_deepslate
fill 116 52 -310 118 52 -310 spruce_stairs[facing=north,half=bottom]
fill 116 53 -310 118 57 -310 air
fill 115 64 -310 119 64 -310 spruce_planks
setblock 115 52 -310 stripped_dark_oak_log[axis=y]
setblock 119 52 -310 stripped_dark_oak_log[axis=y]
setblock 115 53 -310 lantern[hanging=false]
setblock 119 53 -310 lantern[hanging=false]

# Step Z=-309 (Y=51)
fill 115 49 -309 119 50 -309 polished_deepslate
fill 116 51 -309 118 51 -309 spruce_stairs[facing=north,half=bottom]
fill 116 52 -309 118 56 -309 air
fill 115 64 -309 119 64 -309 spruce_planks
setblock 115 51 -309 stripped_dark_oak_log[axis=y]
setblock 119 51 -309 stripped_dark_oak_log[axis=y]

# Step Z=-308 (Y=50): Final landing step reaching Citadel ground floor
fill 115 49 -308 119 49 -308 polished_deepslate
fill 116 50 -308 118 50 -308 spruce_stairs[facing=north,half=bottom]
fill 116 51 -308 118 55 -308 air
fill 115 64 -308 119 64 -308 spruce_planks
setblock 115 50 -308 stripped_dark_oak_log[axis=y]
setblock 119 50 -308 stripped_dark_oak_log[axis=y]
setblock 115 51 -308 lantern[hanging=false]
setblock 119 51 -308 lantern[hanging=false]

# Grand Central Crossroads Rotunda (X: 114..120, Z: -307..-305, Y: 50..56)
fill 113 49 -307 121 49 -305 polished_deepslate
fill 114 50 -307 120 50 -305 polished_blackstone
fill 116 50 -306 118 50 -306 gilded_blackstone
setblock 117 50 -306 crying_obsidian
fill 114 51 -307 120 56 -305 air

# Arch Pilasters and Vault Ribs
setblock 114 51 -307 stripped_dark_oak_log[axis=y]
setblock 114 52 -307 stripped_dark_oak_log[axis=y]
setblock 114 53 -307 stripped_dark_oak_log[axis=y]
setblock 114 54 -307 dark_oak_stairs[facing=east,half=top]

setblock 120 51 -307 stripped_dark_oak_log[axis=y]
setblock 120 52 -307 stripped_dark_oak_log[axis=y]
setblock 120 53 -307 stripped_dark_oak_log[axis=y]
setblock 120 54 -307 dark_oak_stairs[facing=west,half=top]

setblock 114 51 -305 stripped_dark_oak_log[axis=y]
setblock 114 52 -305 stripped_dark_oak_log[axis=y]
setblock 114 53 -305 stripped_dark_oak_log[axis=y]
setblock 114 54 -305 dark_oak_stairs[facing=east,half=top]

setblock 120 51 -305 stripped_dark_oak_log[axis=y]
setblock 120 52 -305 stripped_dark_oak_log[axis=y]
setblock 120 53 -305 stripped_dark_oak_log[axis=y]
setblock 120 54 -305 dark_oak_stairs[facing=west,half=top]

# Central Rotunda Chandelier
setblock 117 56 -306 iron_chain[axis=y]
setblock 117 55 -306 copper_bulb[lit=true,powered=false]
setblock 117 54 -306 soul_lantern[hanging=true]

# Crossroads Portal Portals (West to Athenaeum, East to Banquet Hall)
fill 103 49 -307 113 49 -305 polished_deepslate
fill 103 50 -307 113 54 -305 air
fill 103 55 -307 113 55 -305 deepslate_tiles

fill 121 49 -307 131 49 -305 polished_deepslate
fill 121 50 -307 131 54 -305 air
fill 121 55 -307 131 55 -305 deepslate_tiles
''')

    # 2. BIO DOME ATRIUM AND SUNKEN MARINE AQUARIUM
    with open(os.path.join(FUNC_DIR, "atrium_shell.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Bio Dome Atrium Architecture
# Excavate bounding volume
fill 104 50 -305 130 58 -277 air

# Foundation and Primary Moss Carpet Floor
fill 103 49 -306 131 49 -276 polished_deepslate
fill 105 50 -304 129 50 -278 moss_block
fill 116 50 -304 118 50 -278 stripped_dark_oak_wood[axis=z]
fill 105 50 -291 129 50 -291 stripped_dark_oak_wood[axis=x]

# Perimeter Walls and Skirting
fill 104 50 -305 104 57 -277 deepslate_tiles
fill 130 50 -305 130 57 -277 deepslate_tiles
fill 104 50 -305 130 57 -305 deepslate_tiles
fill 104 50 -277 130 57 -277 deepslate_tiles

fill 105 51 -304 105 51 -278 polished_deepslate_stairs[facing=east,half=bottom]
fill 129 51 -304 129 51 -278 polished_deepslate_stairs[facing=west,half=bottom]
fill 105 51 -304 129 51 -304 polished_deepslate_stairs[facing=south,half=bottom]
fill 105 51 -278 129 51 -278 polished_deepslate_stairs[facing=north,half=bottom]

# Clear Doorway Openings in Skirting
fill 115 51 -304 119 51 -304 air
fill 115 51 -278 119 51 -278 air
fill 105 51 -292 105 51 -290 air
fill 129 51 -292 129 51 -290 air

# Coffered Ceiling and Glass Skylight Vault
fill 104 58 -305 130 58 -277 deepslate_tiles
fill 111 58 -298 123 58 -284 glass

# Structural Granite and Basalt Pilasters
fill 109 50 -299 109 57 -299 polished_basalt[axis=y]
setblock 109 54 -299 chiseled_tuff
setblock 109 57 -299 smooth_quartz_stairs[facing=south,half=top]

fill 125 50 -299 125 57 -299 polished_basalt[axis=y]
setblock 125 54 -299 chiseled_tuff
setblock 125 57 -299 smooth_quartz_stairs[facing=south,half=top]

fill 109 50 -283 109 57 -283 polished_basalt[axis=y]
setblock 109 54 -283 chiseled_tuff
setblock 109 57 -283 smooth_quartz_stairs[facing=north,half=top]

fill 125 50 -283 125 57 -283 polished_basalt[axis=y]
setblock 125 54 -283 chiseled_tuff
setblock 125 57 -283 smooth_quartz_stairs[facing=north,half=top]

# Arched Vault Ribs
fill 110 57 -299 124 57 -299 dark_oak_stairs[facing=south,half=top]
fill 110 57 -283 124 57 -283 dark_oak_stairs[facing=north,half=top]
fill 109 57 -298 109 57 -284 dark_oak_stairs[facing=east,half=top]
fill 125 57 -298 125 57 -284 dark_oak_stairs[facing=west,half=top]

# Sunken Marine Aquarium Basin (X: 113..121, Z: -295..-287, Y: 46..49)
fill 112 45 -296 122 45 -286 sea_lantern
fill 113 46 -295 121 46 -287 dark_prismarine
fill 113 47 -295 121 49 -287 water
fill 113 50 -295 121 50 -287 air

# Aquarium Perimeter Railing and Glass Viewing Panels
fill 113 50 -295 121 50 -295 dark_oak_fence
fill 113 50 -287 121 50 -287 dark_oak_fence
fill 113 50 -294 113 50 -288 dark_oak_fence
fill 121 50 -294 121 50 -288 dark_oak_fence

fill 116 50 -295 118 50 -287 tinted_glass
fill 113 50 -292 121 50 -290 tinted_glass

# Coral Reef Flora inside Aquarium
setblock 115 47 -293 fire_coral_block
setblock 115 48 -293 fire_coral_fan[waterlogged=true]
setblock 119 47 -293 tube_coral_block
setblock 119 48 -293 tube_coral_fan[waterlogged=true]
setblock 115 47 -289 horn_coral_block
setblock 115 48 -289 horn_coral_fan[waterlogged=true]
setblock 119 47 -289 brain_coral_block
setblock 119 48 -289 brain_coral_fan[waterlogged=true]
setblock 117 47 -291 sea_pickle[pickles=4,waterlogged=true]

# Bubble Column Shafts to Sector 3 (Celestial Nexus)
fill 114 37 -291 114 50 -291 tinted_glass
setblock 114 37 -291 magma_block
fill 114 38 -291 114 50 -291 water

fill 120 37 -291 120 50 -291 tinted_glass
setblock 120 37 -291 soul_sand
fill 120 38 -291 120 50 -291 water
''')

    with open(os.path.join(FUNC_DIR, "atrium_decor.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Atrium Living Ecosystem and Lighting
# Organic Flora Beds
fill 106 51 -303 108 51 -297 moss_carpet
fill 106 51 -303 108 51 -301 flowering_azalea
fill 126 51 -303 128 51 -297 moss_carpet
fill 126 51 -303 128 51 -301 flowering_azalea

fill 106 51 -286 108 51 -278 moss_carpet
fill 106 51 -280 108 51 -278 flowering_azalea
fill 127 51 -286 129 51 -278 moss_carpet
fill 127 51 -280 129 51 -278 flowering_azalea

# Custom Subterranean Azalea Trees
fill 107 51 -300 107 53 -300 stripped_dark_oak_log[axis=y]
fill 106 54 -301 108 54 -299 flowering_azalea_leaves
setblock 107 55 -300 flowering_azalea_leaves
setblock 107 53 -301 spore_blossom

fill 127 51 -300 127 53 -300 stripped_dark_oak_log[axis=y]
fill 126 54 -301 128 54 -299 flowering_azalea_leaves
setblock 127 55 -300 flowering_azalea_leaves
setblock 127 53 -301 spore_blossom

# Drifting Spore Dust and Cave Vines
setblock 111 57 -296 spore_blossom
setblock 123 57 -296 spore_blossom
setblock 111 57 -286 spore_blossom
setblock 123 57 -286 spore_blossom

fill 108 56 -301 108 57 -301 cave_vines[berries=true]
fill 126 56 -301 126 57 -301 cave_vines[berries=true]
fill 108 56 -281 108 57 -281 cave_vines[berries=true]
fill 126 56 -281 126 57 -281 cave_vines[berries=true]

# Central Monumental Lantern Chandelier
setblock 117 58 -291 iron_chain[axis=y]
setblock 117 57 -291 iron_chain[axis=y]
setblock 117 56 -291 copper_bulb[lit=true,powered=false]
setblock 116 56 -291 dark_oak_trapdoor[facing=west,open=false,half=top]
setblock 118 56 -291 dark_oak_trapdoor[facing=east,open=false,half=top]
setblock 117 56 -292 dark_oak_trapdoor[facing=north,open=false,half=top]
setblock 117 56 -290 dark_oak_trapdoor[facing=south,open=false,half=top]
setblock 117 55 -291 soul_lantern[hanging=true]

# Park Benches and Lamp Posts
fill 111 51 -293 111 51 -289 dark_oak_stairs[facing=east,half=bottom]
setblock 111 51 -294 dark_oak_trapdoor[facing=north,open=true]
setblock 111 51 -288 dark_oak_trapdoor[facing=south,open=true]

fill 123 51 -293 123 51 -289 dark_oak_stairs[facing=west,half=bottom]
setblock 123 51 -294 dark_oak_trapdoor[facing=north,open=true]
setblock 123 51 -288 dark_oak_trapdoor[facing=south,open=true]

# Streetlamp Posts
setblock 111 51 -302 dark_oak_fence
setblock 111 52 -302 dark_oak_fence
setblock 111 53 -302 dark_oak_stairs[facing=south,half=top]
setblock 111 52 -301 lantern[hanging=true]

setblock 123 51 -302 dark_oak_fence
setblock 123 52 -302 dark_oak_fence
setblock 123 53 -302 dark_oak_stairs[facing=south,half=top]
setblock 123 52 -301 lantern[hanging=true]

setblock 111 51 -280 dark_oak_fence
setblock 111 52 -280 dark_oak_fence
setblock 111 53 -280 dark_oak_stairs[facing=north,half=top]
setblock 111 52 -281 lantern[hanging=true]

setblock 123 51 -280 dark_oak_fence
setblock 123 52 -280 dark_oak_fence
setblock 123 53 -280 dark_oak_stairs[facing=north,half=top]
setblock 123 52 -281 lantern[hanging=true]
''')

    # 3. DWARVEN INDUSTRIAL FORGE
    with open(os.path.join(FUNC_DIR, "forge_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Dwarven Metallurgy Forge
# Dimensions: X: 82..99, Z: -301..-281, Floor Y: 50, Ceiling Y: 58
fill 82 50 -301 99 58 -281 air

# Shell and Heavy Masonry Foundation
fill 81 49 -302 100 49 -280 polished_deepslate
fill 82 50 -301 99 50 -281 polished_basalt[axis=y]
fill 81 50 -302 81 58 -280 deepslate_tiles
fill 100 50 -302 100 58 -280 deepslate_tiles
fill 81 50 -302 100 58 -302 deepslate_tiles
fill 81 50 -280 100 58 -280 deepslate_tiles
fill 81 59 -302 100 59 -280 smooth_stone

# 16 Furnace Super Smelter Battery (West Wall)
fill 82 51 -298 82 52 -284 blast_furnace[facing=east]
fill 82 53 -298 82 53 -284 hopper[facing=down]
fill 82 54 -298 82 54 -284 chest[facing=east,type=single]
fill 82 55 -298 82 57 -284 iron_bars

# Molten Lava Crucible (Center: X: 89..92, Z: -293..-289)
fill 88 50 -294 93 50 -288 polished_blackstone
fill 89 51 -293 92 51 -289 polished_blackstone_bricks
setblock 90 51 -291 lava
setblock 91 51 -291 lava
fill 89 52 -293 92 53 -289 iron_bars
fill 89 54 -293 92 55 -289 brick_stairs[facing=south,half=top]

# Master Smith Workstation (East side)
setblock 96 51 -295 polished_granite
setblock 96 52 -295 anvil[facing=north]

setblock 96 51 -293 smithing_table
setblock 96 51 -291 stonecutter[facing=west]

# Quenching Trough with Water
setblock 96 51 -289 cauldron
setblock 96 52 -289 tripwire_hook[facing=east]

# Hanging Grindstone
setblock 94 54 -291 iron_chain[axis=y]
setblock 94 53 -291 grindstone[facing=west,face=ceiling]

# Storage and Ingot Racks (North Wall)
fill 85 51 -301 88 53 -301 barrel[facing=south]
fill 93 51 -301 95 51 -301 raw_iron_block
fill 93 52 -301 95 52 -301 raw_copper_block
fill 93 53 -301 95 53 -301 coal_block

# Industrial Copper Bulb and Chain Lighting
setblock 86 58 -291 iron_chain[axis=y]
setblock 86 57 -291 copper_bulb[lit=true,powered=false]
setblock 86 56 -291 lantern[hanging=true]

setblock 96 58 -291 iron_chain[axis=y]
setblock 96 57 -291 copper_bulb[lit=true,powered=false]
setblock 96 56 -291 lantern[hanging=true]

# Doorway to Atrium at X=100
fill 100 50 -292 100 54 -290 air
''')

    # 4. HYDROPONICS BIOSPHERE AND APIARY
    with open(os.path.join(FUNC_DIR, "hydroponics_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Hydroponics Biosphere and Apiary
# Dimensions: X: 136..154, Z: -302..-280, Floor Y: 50, Ceiling Y: 61
fill 136 50 -302 154 61 -280 air

# Foundation & Outer Shell
fill 135 49 -303 155 49 -279 polished_deepslate
fill 135 50 -303 135 61 -279 stone_bricks
fill 155 50 -303 155 61 -279 stone_bricks
fill 135 50 -303 155 61 -303 stone_bricks
fill 135 50 -279 155 61 -279 stone_bricks
fill 135 62 -303 155 62 -279 deepslate_tiles

# Terraced Hydrated Farmland (South wing: Z: -290..-281)
fill 137 50 -290 144 50 -281 farmland[moisture=7]
fill 137 51 -290 144 51 -288 wheat[age=7]
fill 137 51 -287 144 51 -285 carrots[age=7]
fill 137 51 -284 144 51 -282 potatoes[age=7]
fill 137 51 -281 144 51 -281 beetroots[age=3]

# Stepped Irrigation Canal
fill 141 50 -291 141 50 -281 water
setblock 141 49 -286 sea_pickle[pickles=3,waterlogged=true]

# Enclosed Glass Apiary Sanctuary (North wing: Z: -301..-293)
fill 137 50 -301 144 50 -293 grass_block
fill 136 51 -302 145 56 -292 glass outline
fill 137 51 -301 144 55 -293 air

# 4 Active Beehives with Campfire Smoke Dampers
setblock 139 49 -298 campfire[lit=true]
setblock 139 50 -298 oak_trapdoor[half=top,open=false]
setblock 139 51 -298 beehive[facing=south,honey_level=5]

setblock 142 49 -298 campfire[lit=true]
setblock 142 50 -298 oak_trapdoor[half=top,open=false]
setblock 142 51 -298 beehive[facing=south,honey_level=5]

# Bee Flora
setblock 138 51 -295 rose_bush[half=lower]
setblock 138 52 -295 rose_bush[half=upper]
setblock 143 51 -295 sunflower[half=lower]
setblock 143 52 -295 sunflower[half=upper]
setblock 140 51 -295 dandelion
setblock 141 51 -295 poppy

# Subterranean Cherry Blossom Tree (East side: X: 149, Z: -291)
fill 149 50 -291 149 54 -291 stripped_cherry_log[axis=y]
fill 147 55 -293 151 56 -289 cherry_leaves
setblock 149 57 -291 cherry_leaves
setblock 149 54 -292 cave_vines[berries=true]

# Composter & Tool Storage
setblock 152 50 -283 composter[level=6]
setblock 153 50 -283 composter[level=7]
fill 152 50 -281 153 52 -281 barrel[facing=south]

# Warm Amber Lantern Lighting
setblock 145 58 -291 iron_chain[axis=y]
setblock 145 57 -291 copper_bulb[lit=true,powered=false]
setblock 145 56 -291 lantern[hanging=true]

# Doorway to Atrium at X=135
fill 135 50 -292 135 54 -290 air
''')

    # 5. CELESTIAL PORTAL NEXUS
    with open(os.path.join(FUNC_DIR, "portal_nexus_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Celestial Portal Nexus
# Dimensions: X: 106..128, Z: -302..-280, Floor Y: 36, Ceiling Y: 48
fill 106 36 -302 128 48 -280 air

# Foundation & Calcite Concentric Floor
fill 105 35 -303 129 35 -279 polished_deepslate
fill 106 36 -302 128 36 -280 polished_deepslate_bricks
fill 112 36 -296 122 36 -286 calcite
fill 115 36 -293 119 36 -289 crying_obsidian
fill 105 36 -303 105 48 -279 deepslate_tiles
fill 129 36 -303 129 48 -279 deepslate_tiles
fill 105 36 -303 129 48 -303 deepslate_tiles
fill 105 36 -279 129 48 -279 deepslate_tiles
fill 105 49 -303 129 49 -279 deepslate_tiles

# Active 5x7 Nether Portal Aperture (North Wall: Z: -302)
fill 115 37 -302 119 43 -302 obsidian
fill 116 38 -302 118 42 -302 nether_portal[axis=x]
fill 114 37 -302 114 43 -302 gilded_blackstone
fill 120 37 -302 120 43 -302 gilded_blackstone
setblock 113 37 -301 soul_fire
setblock 121 37 -301 soul_fire

# Sunken Authentic End Portal Well (South: Z: -284)
fill 115 35 -286 119 35 -282 end_stone_bricks
setblock 116 36 -286 end_portal_frame[facing=south,eye=true]
setblock 117 36 -286 end_portal_frame[facing=south,eye=true]
setblock 118 36 -286 end_portal_frame[facing=south,eye=true]
setblock 116 36 -282 end_portal_frame[facing=north,eye=true]
setblock 117 36 -282 end_portal_frame[facing=north,eye=true]
setblock 118 36 -282 end_portal_frame[facing=north,eye=true]
setblock 115 36 -285 end_portal_frame[facing=east,eye=true]
setblock 115 36 -284 end_portal_frame[facing=east,eye=true]
setblock 115 36 -283 end_portal_frame[facing=east,eye=true]
setblock 119 36 -285 end_portal_frame[facing=west,eye=true]
setblock 119 36 -284 end_portal_frame[facing=west,eye=true]
setblock 119 36 -283 end_portal_frame[facing=west,eye=true]
fill 116 36 -285 118 36 -283 end_portal

# Crystal Amethyst Geode Cavity (East Wall: X: 125..128)
fill 125 36 -293 128 42 -289 amethyst_block
fill 126 37 -292 127 41 -290 air
setblock 126 37 -291 budding_amethyst
setblock 127 37 -291 amethyst_cluster[facing=up]
setblock 126 41 -291 amethyst_cluster[facing=down]

# Celestial Chandelier
setblock 117 48 -291 iron_chain[axis=y]
setblock 117 47 -291 iron_chain[axis=y]
setblock 117 46 -291 copper_bulb[lit=true,powered=false]
setblock 117 45 -291 soul_lantern[hanging=true]
setblock 116 45 -291 end_rod
setblock 118 45 -291 end_rod
''')

    # 6. GRAND SUBTERRANEAN ATHENAEUM
    with open(os.path.join(FUNC_DIR, "athenaeum_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: The Grand Subterranean Athenaeum
# Dimensions: X: 80..102, Z: -330..-306, Floor Y: 50, Ceiling Y: 62
fill 80 50 -330 102 62 -306 air

# Shell & Foundation
fill 79 49 -331 103 49 -305 polished_deepslate
fill 80 50 -330 102 50 -306 dark_oak_planks
fill 79 50 -331 79 62 -305 tuff_bricks
fill 103 50 -331 103 62 -305 tuff_bricks
fill 79 50 -331 103 62 -331 tuff_bricks
fill 79 50 -305 103 62 -305 tuff_bricks
fill 79 63 -331 103 63 -305 deepslate_tiles

# Central Level 30 Enchanting Sanctum (X: 89..93, Z: -320..-316)
fill 89 50 -320 93 50 -316 smooth_quartz
setblock 91 51 -318 enchanting_table
fill 89 51 -320 93 52 -320 bookshelf
fill 89 51 -316 93 52 -316 bookshelf
fill 89 51 -319 89 52 -317 bookshelf
fill 93 51 -319 93 52 -317 chiseled_bookshelf[facing=west]
setblock 90 51 -317 amethyst_cluster[facing=up]
setblock 92 51 -317 amethyst_cluster[facing=up]

# Perimeter Multi Tier Bookshelves
fill 80 51 -329 80 58 -307 chiseled_bookshelf[facing=east]
fill 81 51 -330 101 58 -330 chiseled_bookshelf[facing=south]

# Mezzanine Reading Balcony at Y: 55
fill 81 55 -328 83 55 -308 dark_oak_slab[type=top]
fill 84 55 -329 101 55 -327 dark_oak_slab[type=top]
fill 84 56 -326 101 56 -326 dark_oak_fence

# Spiral Access Stairs to Mezzanine
setblock 100 50 -310 polished_deepslate
setblock 100 51 -310 dark_oak_stairs[facing=south,half=bottom]
setblock 101 51 -310 polished_deepslate
setblock 101 52 -310 dark_oak_stairs[facing=west,half=bottom]
setblock 101 52 -309 polished_deepslate
setblock 101 53 -309 dark_oak_stairs[facing=north,half=bottom]
setblock 100 53 -309 polished_deepslate
setblock 100 54 -309 dark_oak_stairs[facing=east,half=bottom]
setblock 100 54 -308 dark_oak_slab[type=top]

# Floating Lecterns & Scholar Study Tables
setblock 87 51 -314 dark_oak_slab[type=top]
setblock 87 52 -314 lectern[facing=south]
setblock 87 51 -313 dark_oak_stairs[facing=north,half=bottom]
setblock 86 52 -314 green_candle[lit=true,candles=2]

setblock 95 51 -314 dark_oak_slab[type=top]
setblock 95 52 -314 lectern[facing=south]
setblock 95 51 -313 dark_oak_stairs[facing=north,half=bottom]
setblock 96 52 -314 green_candle[lit=true,candles=2]

# Alchemical Distillation Corner
fill 101 51 -316 102 51 -312 polished_blackstone
setblock 101 52 -315 brewing_stand[has_bottle_0=true,has_bottle_1=true,has_bottle_2=true]
setblock 101 52 -313 cauldron
fill 102 52 -316 102 54 -312 barrel[facing=west]

# Library Chandeliers
setblock 91 62 -318 iron_chain[axis=y]
setblock 91 61 -318 iron_chain[axis=y]
setblock 91 60 -318 copper_bulb[lit=true,powered=false]
setblock 91 59 -318 lantern[hanging=true]

setblock 85 62 -325 iron_chain[axis=y]
setblock 85 61 -325 lantern[hanging=true]
setblock 97 62 -325 iron_chain[axis=y]
setblock 97 61 -325 lantern[hanging=true]

# Doorway to Crossroads Corridor at X=103
fill 103 50 -307 103 54 -305 air
''')

    # 7. SOVEREIGN BANQUET AND GATHERING HALL
    with open(os.path.join(FUNC_DIR, "banquet_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: The Sovereign Banquet and Gathering Hall
# Dimensions: X: 132..154, Z: -330..-306, Floor Y: 50, Ceiling Y: 62
fill 132 50 -330 154 62 -306 air

# Shell & Foundation
fill 131 49 -331 155 49 -305 polished_deepslate
fill 132 50 -330 154 50 -306 polished_blackstone_bricks
fill 131 50 -331 131 62 -305 polished_blackstone_bricks
fill 155 50 -331 155 62 -305 polished_blackstone_bricks
fill 131 50 -331 155 62 -331 polished_blackstone_bricks
fill 131 50 -305 155 62 -305 polished_blackstone_bricks
fill 131 63 -331 155 63 -305 deepslate_tiles

# Central Ceremonial Red & Gold Carpet Aisle
fill 142 50 -328 144 50 -308 red_carpet
fill 141 50 -328 141 50 -308 yellow_carpet
fill 145 50 -328 145 50 -308 yellow_carpet

# Long Banquet Feast Tables (West: X: 137..139, East: X: 147..149)
fill 138 50 -325 138 50 -310 dark_oak_planks
fill 138 51 -325 138 51 -310 dark_oak_slab[type=top]
fill 137 51 -325 137 51 -310 dark_oak_stairs[facing=east,half=bottom]
fill 139 51 -325 139 51 -310 dark_oak_stairs[facing=west,half=bottom]

fill 148 50 -325 148 50 -310 dark_oak_planks
fill 148 51 -325 148 51 -310 dark_oak_slab[type=top]
fill 147 51 -325 147 51 -310 dark_oak_stairs[facing=east,half=bottom]
fill 149 51 -325 149 51 -310 dark_oak_stairs[facing=west,half=bottom]

# Feast Tableware (Cakes, Candles, Steins, Decorated Pots)
setblock 138 52 -324 cake[bites=0]
setblock 138 52 -321 candle[lit=true,candles=3]
setblock 138 52 -318 decorated_pot[facing=north]
setblock 138 52 -315 candle[lit=true,candles=4]
setblock 138 52 -312 cake[bites=0]

setblock 148 52 -324 cake[bites=0]
setblock 148 52 -321 candle[lit=true,candles=3]
setblock 148 52 -318 decorated_pot[facing=north]
setblock 148 52 -315 candle[lit=true,candles=4]
setblock 148 52 -312 cake[bites=0]

# Sovereign High Table Dais (South End: Z: -308..-306)
fill 139 51 -308 147 51 -306 smooth_quartz
fill 140 52 -307 146 52 -306 dark_oak_slab[type=top]
setblock 143 52 -306 polished_deepslate_stairs[facing=north,half=bottom]
setblock 142 52 -306 dark_oak_stairs[facing=north,half=bottom]
setblock 144 52 -306 dark_oak_stairs[facing=north,half=bottom]

# Dual Roaring Hearths (East Wall: X: 154)
fill 153 50 -324 154 50 -322 netherrack
fill 153 51 -324 154 51 -322 fire
fill 153 52 -324 154 55 -322 bricks
setblock 152 51 -323 iron_bars

fill 153 50 -314 154 50 -312 netherrack
fill 153 51 -314 154 51 -312 fire
fill 153 52 -314 154 55 -312 bricks
setblock 152 51 -313 iron_bars

# Grand Triple Chandeliers
setblock 143 62 -324 iron_chain[axis=y]
setblock 143 61 -324 iron_chain[axis=y]
setblock 143 60 -324 copper_bulb[lit=true,powered=false]
setblock 143 59 -324 lantern[hanging=true]

setblock 143 62 -317 iron_chain[axis=y]
setblock 143 61 -317 iron_chain[axis=y]
setblock 143 60 -317 copper_bulb[lit=true,powered=false]
setblock 143 59 -317 lantern[hanging=true]

setblock 143 62 -310 iron_chain[axis=y]
setblock 143 61 -310 iron_chain[axis=y]
setblock 143 60 -310 copper_bulb[lit=true,powered=false]
setblock 143 59 -310 lantern[hanging=true]

# Doorway to Crossroads Corridor at X=131
fill 131 50 -307 131 54 -305 air
''')

    # 8. SUBTERRANEAN HYPERLOOP TRANSIT HUB
    with open(os.path.join(FUNC_DIR, "transit_hub_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Hyperloop Transit Hub
# Dimensions: X: 104..130, Z: -345..-325, Floor Y: 49, Ceiling Y: 58
fill 104 49 -345 130 58 -325 air

# Foundation & Concourse Quartz Floor
fill 103 48 -346 131 48 -324 polished_deepslate
fill 104 49 -345 130 49 -325 smooth_quartz
fill 103 49 -346 103 58 -324 polished_blackstone
fill 131 49 -346 131 58 -324 polished_blackstone
fill 103 49 -346 131 58 -346 polished_blackstone
fill 103 49 -324 131 58 -324 polished_blackstone
fill 103 59 -346 131 59 -324 deepslate_tiles

# Hazard Warning Stripes (Yellow and Black Concrete)
fill 109 49 -344 109 49 -328 yellow_concrete
fill 110 49 -344 110 49 -328 black_concrete
fill 124 49 -344 124 49 -328 yellow_concrete
fill 125 49 -344 125 49 -328 black_concrete

# Track Bays with Powered Rails
fill 107 49 -344 107 49 -328 polished_deepslate
fill 107 50 -344 107 50 -328 powered_rail[shape=north_south]
setblock 107 48 -336 redstone_block
setblock 107 48 -342 redstone_block

fill 127 49 -344 127 49 -328 polished_deepslate
fill 127 50 -344 127 50 -328 powered_rail[shape=north_south]
setblock 127 48 -336 redstone_block
setblock 127 48 -342 redstone_block

# Station Ticket Booth (Center: X: 115..119, Z: -340..-336)
fill 115 50 -340 119 53 -336 glass outline
setblock 117 50 -336 iron_door[facing=south,half=lower]
setblock 117 51 -336 iron_door[facing=south,half=upper]
setblock 116 50 -338 dark_oak_slab[type=top]
setblock 116 51 -338 daylight_detector

# Waiting Lounge Benches
fill 114 50 -332 114 50 -328 polished_deepslate_stairs[facing=east,half=bottom]
fill 120 50 -332 120 50 -328 polished_deepslate_stairs[facing=west,half=bottom]

# Station Illuminated Ceiling Grids
setblock 111 58 -336 sea_lantern
setblock 117 58 -336 sea_lantern
setblock 123 58 -336 sea_lantern

# Concourse Doorways to North Stairwell and Conduits
fill 116 50 -325 118 54 -325 air
''')

    # 9. GRAND HIGH PARLIAMENT OF THE REPUBLIC
    with open(os.path.join(FUNC_DIR, "parliament_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Grand High Parliament of the Republic
# Dimensions: X: 104..130, Z: -276..-244, Floor Y: 50, Ceiling Y: 58
fill 104 50 -276 130 58 -244 air

# Foundation & Polished Blackstone Floor
fill 103 49 -277 131 49 -243 polished_deepslate
fill 104 50 -276 130 50 -244 polished_blackstone
fill 103 50 -277 103 58 -243 polished_blackstone_bricks
fill 131 50 -277 131 58 -243 polished_blackstone_bricks
fill 103 50 -277 131 58 -277 polished_blackstone_bricks
fill 103 50 -243 131 58 -243 polished_blackstone_bricks
fill 103 59 -277 131 59 -243 deepslate_tiles

# Chamber Basalt Pilasters
fill 104 50 -272 104 58 -272 polished_basalt[axis=y]
fill 104 50 -266 104 58 -266 polished_basalt[axis=y]
fill 104 50 -260 104 58 -260 polished_basalt[axis=y]
fill 104 50 -254 104 58 -254 polished_basalt[axis=y]
fill 104 50 -248 104 58 -248 polished_basalt[axis=y]

fill 130 50 -272 130 58 -272 polished_basalt[axis=y]
fill 130 50 -266 130 58 -266 polished_basalt[axis=y]
fill 130 50 -260 130 58 -260 polished_basalt[axis=y]
fill 130 50 -254 130 58 -254 polished_basalt[axis=y]
fill 130 50 -248 130 58 -248 polished_basalt[axis=y]

# North Portal from Atrium
fill 115 50 -277 119 55 -275 air
fill 115 49 -277 119 49 -275 polished_blackstone
fill 114 50 -276 114 55 -276 crying_obsidian
fill 120 50 -276 120 55 -276 crying_obsidian
fill 115 56 -276 119 56 -276 crying_obsidian

# Central Green & Yellow Carpet Aisle
fill 116 50 -275 118 50 -252 green_carpet
fill 117 50 -275 117 50 -252 yellow_carpet

# Under floor ambient shroomlights along aisle
setblock 117 48 -272 shroomlight
setblock 117 48 -266 shroomlight
setblock 117 48 -260 shroomlight
setblock 117 48 -254 shroomlight

# Cabinet Benches (West side: Facing EAST)
fill 114 50 -272 114 50 -254 dark_oak_planks
fill 114 51 -272 114 51 -254 dark_oak_slab[type=top]
fill 113 50 -272 113 50 -254 dark_oak_stairs[facing=east,half=bottom]
fill 113 51 -272 113 51 -254 green_carpet

fill 111 50 -272 112 50 -254 polished_blackstone
fill 112 51 -272 112 51 -254 dark_oak_slab[type=top]
fill 111 51 -272 111 51 -254 dark_oak_stairs[facing=east,half=bottom]
fill 111 52 -272 111 52 -254 green_carpet

fill 109 50 -272 110 51 -254 polished_blackstone
fill 110 52 -272 110 52 -254 dark_oak_slab[type=top]
fill 109 52 -272 109 52 -254 dark_oak_stairs[facing=east,half=bottom]
fill 109 53 -272 109 53 -254 green_carpet

setblock 114 52 -270 end_rod
setblock 114 52 -269 stone_button[face=floor,facing=north]
setblock 114 52 -266 end_rod
setblock 114 52 -265 stone_button[face=floor,facing=north]
setblock 114 52 -262 end_rod
setblock 114 52 -261 stone_button[face=floor,facing=north]
setblock 114 52 -258 end_rod
setblock 114 52 -257 stone_button[face=floor,facing=north]

# Assembly Benches (East side: Facing WEST)
fill 120 50 -272 120 50 -254 dark_oak_planks
fill 120 51 -272 120 51 -254 dark_oak_slab[type=top]
fill 121 50 -272 121 50 -254 dark_oak_stairs[facing=west,half=bottom]
fill 121 51 -272 121 51 -254 green_carpet

fill 122 50 -272 123 50 -254 polished_blackstone
fill 122 51 -272 122 51 -254 dark_oak_slab[type=top]
fill 123 51 -272 123 51 -254 dark_oak_stairs[facing=west,half=bottom]
fill 123 52 -272 123 52 -254 green_carpet

fill 124 50 -272 125 51 -254 polished_blackstone
fill 124 52 -272 124 52 -254 dark_oak_slab[type=top]
fill 125 52 -272 125 52 -254 dark_oak_stairs[facing=west,half=bottom]
fill 125 53 -272 125 53 -254 green_carpet

setblock 120 52 -270 end_rod
setblock 120 52 -269 stone_button[face=floor,facing=north]
setblock 120 52 -266 end_rod
setblock 120 52 -265 stone_button[face=floor,facing=north]
setblock 120 52 -262 end_rod
setblock 120 52 -261 stone_button[face=floor,facing=north]
setblock 120 52 -258 end_rod
setblock 120 52 -257 stone_button[face=floor,facing=north]

# Speaker Dais & Prime Minister Sovereign Throne
fill 113 50 -251 121 50 -245 smooth_quartz
fill 114 51 -251 120 51 -245 smooth_quartz
fill 114 51 -251 120 51 -251 smooth_quartz_stairs[facing=north,half=bottom]

fill 115 52 -249 119 52 -245 gold_block
fill 115 52 -249 119 52 -249 smooth_quartz_stairs[facing=north,half=bottom]

# Ceremonial Mace on Blackstone Plinth
setblock 117 52 -251 polished_blackstone_brick_slab[type=bottom]
setblock 117 53 -251 lightning_rod[facing=up]

# Clerk Desks
setblock 119 52 -250 dark_oak_slab[type=top]
setblock 119 53 -250 green_candle[lit=true]
setblock 115 52 -250 dark_oak_slab[type=top]
setblock 115 53 -250 red_candle[lit=true]

setblock 117 53 -247 gilded_blackstone
setblock 117 54 -247 dark_oak_stairs[facing=north,half=bottom]
setblock 116 54 -247 dark_oak_trapdoor[facing=west,open=true]
setblock 118 54 -247 dark_oak_trapdoor[facing=east,open=true]

# Heraldic Wall of State
fill 114 50 -244 120 57 -244 crying_obsidian
fill 116 54 -244 118 56 -244 gold_block
setblock 117 55 -244 bell[facing=north]

# Triple Vaulted Chandeliers
setblock 117 58 -269 iron_chain[axis=y]
setblock 117 57 -269 copper_bulb[lit=true,powered=false]
setblock 117 56 -269 soul_lantern[hanging=true]

setblock 117 58 -261 iron_chain[axis=y]
setblock 117 57 -261 copper_bulb[lit=true,powered=false]
setblock 117 56 -261 soul_lantern[hanging=true]

setblock 117 58 -250 iron_chain[axis=y]
setblock 117 57 -250 copper_bulb[lit=true,powered=false]
setblock 117 56 -250 soul_lantern[hanging=true]
''')

    # 10. SOVEREIGN RESIDENTIAL SUITES
    with open(os.path.join(FUNC_DIR, "suites_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Sovereign Residential Suites
# Dimensions: X: 92..142, Z: -268..-231, Floor Y: 50, Ceiling Y: 58
fill 92 50 -268 142 58 -231 air

# Foundation & Shell
fill 91 49 -269 143 49 -230 polished_deepslate
fill 92 50 -268 142 50 -231 spruce_planks
fill 91 50 -269 91 58 -230 stone_bricks
fill 143 50 -269 143 58 -230 stone_bricks
fill 91 50 -269 143 58 -269 stone_bricks
fill 91 50 -230 143 58 -230 stone_bricks
fill 91 59 -269 143 59 -230 deepslate_tiles

# Corridor Spine linking suites (Z: -250, X: 92..142)
fill 92 50 -251 142 50 -249 stripped_dark_oak_wood[axis=x]
fill 92 50 -250 142 50 -250 red_carpet

# King Abir Sovereign Suite (Northwest: X: 93..105, Z: -268..-252)
# Royal Canopy Bed (Red)
fill 95 50 -266 96 50 -265 red_wool
setblock 95 51 -266 red_bed[facing=south,part=head]
setblock 95 51 -265 red_bed[facing=south,part=foot]
setblock 96 51 -266 red_bed[facing=south,part=head]
setblock 96 51 -265 red_bed[facing=south,part=foot]
# Canopy Posts
setblock 94 51 -266 stripped_spruce_log[axis=y]
setblock 94 52 -266 stripped_spruce_log[axis=y]
setblock 97 51 -266 stripped_spruce_log[axis=y]
setblock 97 52 -266 stripped_spruce_log[axis=y]
setblock 94 53 -266 spruce_trapdoor[half=top,open=false]
setblock 97 53 -266 spruce_trapdoor[half=top,open=false]

# Executive Writing Desk
setblock 102 51 -266 dark_oak_slab[type=top]
setblock 102 52 -266 lectern[facing=south]
setblock 102 51 -265 dark_oak_stairs[facing=north,half=bottom]
setblock 101 52 -266 lantern[hanging=false]

# Wardrobe Armor Stand
setblock 94 51 -255 armor_stand[facing=south]
setblock 93 51 -255 chiseled_bookshelf[facing=east]

# Ahsane Executive Library Suite (Northeast: X: 129..141, Z: -268..-252)
# Cyan Canopy Bed
setblock 135 51 -266 cyan_bed[facing=south,part=head]
setblock 135 51 -265 cyan_bed[facing=south,part=foot]
setblock 136 51 -266 cyan_bed[facing=south,part=head]
setblock 136 51 -265 cyan_bed[facing=south,part=foot]

# Library Study Pod
fill 139 51 -267 141 54 -267 bookshelf
setblock 140 51 -265 dark_oak_slab[type=top]
setblock 140 52 -265 lectern[facing=south]
setblock 140 51 -264 dark_oak_stairs[facing=north,half=bottom]
setblock 139 52 -265 sea_pickle[pickles=2]

# Jamal Tourism & Hunting Suite (South: X: 111..123, Z: -248..-232)
# Purple Canopy Bed
setblock 116 51 -234 purple_bed[facing=north,part=head]
setblock 116 51 -235 purple_bed[facing=north,part=foot]
setblock 117 51 -234 purple_bed[facing=north,part=head]
setblock 117 51 -235 purple_bed[facing=north,part=foot]

# Trophy Mount & Armory Chests
setblock 120 51 -234 armor_stand[facing=north]
setblock 121 51 -234 chest[facing=north,type=left]
setblock 122 51 -234 chest[facing=north,type=right]

# Suite Lighting Fixtures
setblock 99 58 -260 iron_chain[axis=y]
setblock 99 57 -260 copper_bulb[lit=true,powered=false]
setblock 99 56 -260 lantern[hanging=true]

setblock 135 58 -260 iron_chain[axis=y]
setblock 135 57 -260 copper_bulb[lit=true,powered=false]
setblock 135 56 -260 lantern[hanging=true]

setblock 117 58 -240 iron_chain[axis=y]
setblock 117 57 -240 copper_bulb[lit=true,powered=false]
setblock 117 56 -240 lantern[hanging=true]
''')

    # 11. CONNECTING CONDUITS
    with open(os.path.join(FUNC_DIR, "conduits_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Connecting Conduits
# West Wing Corridor (Crossing X: 100..104, Z: -292..-290, Y: 50..54)
fill 100 49 -292 104 49 -290 polished_deepslate
fill 100 50 -292 104 54 -290 air
fill 100 55 -292 104 55 -290 deepslate_tiles
setblock 102 54 -291 lantern[hanging=true]

# East Wing Corridor (Crossing X: 130..136, Z: -292..-290, Y: 50..54)
fill 130 49 -292 136 49 -290 polished_deepslate
fill 130 50 -292 136 54 -290 air
fill 130 55 -292 136 55 -290 deepslate_tiles
setblock 133 54 -291 lantern[hanging=true]

# South Parliament Corridor (Crossing X: 115..119, Z: -278..-276, Y: 50..55)
fill 115 49 -278 119 49 -276 polished_deepslate
fill 115 50 -278 119 55 -276 air
fill 115 56 -278 119 56 -276 deepslate_tiles
setblock 117 55 -277 copper_bulb[lit=true,powered=false]
''')

    # 12. MASTER BUILD ALL ORCHESTRATION
    with open(os.path.join(FUNC_DIR, "build_all.mcfunction"), "w") as f:
        f.write('''# Subterranean Utopia Mega Citadel Master Execution
# 1. Restore and protect The Great Treasury
function treasury:build_all

# 2. Build Grand Staircase Descent
function citadel:stairs_descent

# 3. Build Bio Dome Atrium Architecture & Marine Aquarium
function citadel:atrium_shell

# 4. Populate Atrium Living Ecosystem & Lighting
function citadel:atrium_decor

# 5. Build Dwarven Metallurgy Forge
function citadel:forge_build

# 6. Build Hydroponics Biosphere & Apiary
function citadel:hydroponics_build

# 7. Build Celestial Portal Nexus & Amethyst Geode
function citadel:portal_nexus_build

# 8. Build Grand Subterranean Athenaeum Library
function citadel:athenaeum_build

# 9. Build Sovereign Banquet and Gathering Hall
function citadel:banquet_build

# 10. Build Subterranean Hyperloop Transit Hub
function citadel:transit_hub_build

# 11. Build Grand High Parliament
function citadel:parliament_build

# 12. Build Sovereign Residential Suites
function citadel:suites_build

# 13. Build Connecting Vaulted Conduits
function citadel:conduits_build
''')

    print("Subterranean Utopia Citadel Generator successfully compiled all sectors.")

if __name__ == "__main__":
    main()
