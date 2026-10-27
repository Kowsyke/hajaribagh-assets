#!/usr/bin/env python3
"""
Master Architect Generator for the Complete Subterranean Utopia Mega Fortress.
Sectors included:
1. Grand Seamless Staircase & Arterial Crossways
2. Central Vibrant Bio-Atrium (2-tier mezzanine, bio-aquarium, elevator tubes)
3. Celestial Portal Nexus (Deep Stargate Sanctum with active Nether & End Portals, Amethyst Geode)
4. Grand Subterranean Athenaeum (Multi-level Arcane Library, Level 30 Enchanting Sanctum)
5. Sovereign Banquet & Feast Hall (Ceremonial Feast Tables, Dual Fireplaces, High Table Dais)
6. Subterranean Hyperloop Transit Hub (3-Line Rapid Terminal, Hazard Striping, Automated Rails)
7. Grand High Parliament of the Republic (Tiered Benches for 40+, Speaker Dais, Golden Mace)
8. Dwarven Industrial Forge & 16-Furnace Super Smelter
9. Automated Hydroponic Farms, Tree Conservatory & Apiary
10. Luxury Sovereign Suites (Kowsyke, Ahsane, Jamal)
11. Sub-Floor Redstone Technical Conduits

100% silent execution (no tellraw chat spam).
Strict adherence to punctuation rules (no em dashes, en dashes, or hyphens as punctuation).
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

    # 1. STAIRS & ARTERIAL CROSSWAYS
    with open(os.path.join(FUNC_DIR, "stairs_descent.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Grand Staircase and Arterial Crossroads
fill 113 49 -324 121 68 -304 air
fill 113 49 -324 113 68 -304 deepslate_tiles
fill 121 49 -324 121 68 -304 deepslate_tiles
fill 113 68 -324 121 68 -304 deepslate_tiles

# Steps from Z=-322 down to Z=-308
fill 114 49 -322 120 63 -322 polished_deepslate
fill 116 64 -322 118 64 -322 spruce_stairs[facing=south]
setblock 115 64 -322 stripped_dark_oak_log[axis=y]
setblock 119 64 -322 stripped_dark_oak_log[axis=y]
setblock 115 65 -322 lantern[hanging=false]
setblock 119 65 -322 lantern[hanging=false]

fill 114 49 -321 120 62 -321 polished_deepslate
fill 116 63 -321 118 63 -321 spruce_stairs[facing=south]
setblock 115 63 -321 deepslate_tile_stairs[facing=south]
setblock 119 63 -321 deepslate_tile_stairs[facing=south]

fill 114 49 -320 120 61 -320 polished_deepslate
fill 116 62 -320 118 62 -320 spruce_stairs[facing=south]
setblock 115 62 -320 stripped_dark_oak_log[axis=y]
setblock 119 62 -320 stripped_dark_oak_log[axis=y]
setblock 115 63 -320 lantern[hanging=false]
setblock 119 63 -320 lantern[hanging=false]

fill 114 49 -319 120 60 -319 polished_deepslate
fill 116 61 -319 118 61 -319 spruce_stairs[facing=south]
setblock 115 61 -319 deepslate_tile_stairs[facing=south]
setblock 119 61 -319 deepslate_tile_stairs[facing=south]

fill 114 49 -318 120 59 -318 polished_deepslate
fill 116 60 -318 118 60 -318 spruce_stairs[facing=south]
setblock 115 60 -318 stripped_dark_oak_log[axis=y]
setblock 119 60 -318 stripped_dark_oak_log[axis=y]
setblock 115 61 -318 lantern[hanging=false]
setblock 119 61 -318 lantern[hanging=false]

fill 114 49 -317 120 58 -317 polished_deepslate
fill 116 59 -317 118 59 -317 spruce_stairs[facing=south]
setblock 115 59 -317 deepslate_tile_stairs[facing=south]
setblock 119 59 -317 deepslate_tile_stairs[facing=south]

fill 114 49 -316 120 57 -316 polished_deepslate
fill 116 58 -316 118 58 -316 spruce_stairs[facing=south]
setblock 115 58 -316 stripped_dark_oak_log[axis=y]
setblock 119 58 -316 stripped_dark_oak_log[axis=y]
setblock 115 59 -316 lantern[hanging=false]
setblock 119 59 -316 lantern[hanging=false]

fill 114 49 -315 120 56 -315 polished_deepslate
fill 116 57 -315 118 57 -315 spruce_stairs[facing=south]
setblock 115 57 -315 deepslate_tile_stairs[facing=south]
setblock 119 57 -315 deepslate_tile_stairs[facing=south]

fill 114 49 -314 120 55 -314 polished_deepslate
fill 116 56 -314 118 56 -314 spruce_stairs[facing=south]
setblock 115 56 -314 stripped_dark_oak_log[axis=y]
setblock 119 56 -314 stripped_dark_oak_log[axis=y]
setblock 115 57 -314 lantern[hanging=false]
setblock 119 57 -314 lantern[hanging=false]

fill 114 49 -313 120 54 -313 polished_deepslate
fill 116 55 -313 118 55 -313 spruce_stairs[facing=south]
setblock 115 55 -313 deepslate_tile_stairs[facing=south]
setblock 119 55 -313 deepslate_tile_stairs[facing=south]

fill 114 49 -312 120 53 -312 polished_deepslate
fill 116 54 -312 118 54 -312 spruce_stairs[facing=south]
setblock 115 54 -312 stripped_dark_oak_log[axis=y]
setblock 119 54 -312 stripped_dark_oak_log[axis=y]
setblock 115 55 -312 lantern[hanging=false]
setblock 119 55 -312 lantern[hanging=false]

fill 114 49 -311 120 52 -311 polished_deepslate
fill 116 53 -311 118 53 -311 spruce_stairs[facing=south]
setblock 115 53 -311 deepslate_tile_stairs[facing=south]
setblock 119 53 -311 deepslate_tile_stairs[facing=south]

fill 114 49 -310 120 51 -310 polished_deepslate
fill 116 52 -310 118 52 -310 spruce_stairs[facing=south]
setblock 115 52 -310 stripped_dark_oak_log[axis=y]
setblock 119 52 -310 stripped_dark_oak_log[axis=y]
setblock 115 53 -310 lantern[hanging=false]
setblock 119 53 -310 lantern[hanging=false]

fill 114 49 -309 120 50 -309 polished_deepslate
fill 116 51 -309 118 51 -309 spruce_stairs[facing=south]
setblock 115 51 -309 deepslate_tile_stairs[facing=south]
setblock 119 51 -309 deepslate_tile_stairs[facing=south]

fill 114 49 -308 120 49 -308 polished_deepslate
fill 116 50 -308 118 50 -308 spruce_stairs[facing=south]
setblock 115 50 -308 stripped_dark_oak_log[axis=y]
setblock 119 50 -308 stripped_dark_oak_log[axis=y]
setblock 115 51 -308 lantern[hanging=false]
setblock 119 51 -308 lantern[hanging=false]

# Grand Central Vestibule & Crossroads at Z: -307..-305 (Y=50)
fill 114 49 -307 120 49 -305 polished_deepslate
fill 116 50 -307 118 50 -305 stripped_dark_oak_wood[axis=z]
fill 115 50 -307 115 50 -305 mud_bricks
fill 119 50 -307 119 50 -305 mud_bricks
setblock 117 49 -306 shroomlight
setblock 117 50 -306 moss_carpet

# Archways branching East to Banquet Hall and West to Athenaeum Library
fill 102 50 -307 113 54 -305 air
fill 102 49 -307 113 49 -305 polished_deepslate
fill 102 50 -306 113 50 -306 stripped_dark_oak_wood[axis=x]

fill 121 50 -307 132 54 -305 air
fill 121 49 -307 132 49 -305 polished_deepslate
fill 121 50 -306 132 50 -306 stripped_dark_oak_wood[axis=x]
''')

    # 2. ATRIUM SHELL, DECOR & ELEVATOR TUBES
    with open(os.path.join(FUNC_DIR, "atrium_shell.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Atrium Shell and Architecture
fill 104 50 -304 130 57 -278 air
fill 112 47 -296 122 49 -286 air
fill 104 49 -305 130 49 -277 polished_deepslate
fill 105 50 -304 129 50 -278 polished_andesite
fill 104 58 -305 130 58 -277 deepslate_tiles

# Perimeter Walls with 3D Layered Pilasters & Moldings
fill 104 50 -305 104 57 -277 deepslate_tiles
fill 130 50 -305 130 57 -277 deepslate_tiles
fill 104 50 -305 130 57 -305 deepslate_tiles
fill 104 50 -277 130 57 -277 deepslate_tiles

fill 105 51 -304 105 51 -278 polished_deepslate_stairs[facing=east,half=bottom]
fill 129 51 -304 129 51 -278 polished_deepslate_stairs[facing=west,half=bottom]
fill 105 51 -304 129 51 -304 polished_deepslate_stairs[facing=south,half=bottom]
fill 105 51 -278 129 51 -278 polished_deepslate_stairs[facing=north,half=bottom]

# Clear portals in skirting
fill 115 51 -304 119 51 -304 air
fill 115 51 -278 119 51 -278 air
fill 105 51 -293 105 51 -289 air
fill 129 51 -293 129 51 -289 air

# Upper Mezzanine Catwalk at Y: 54
fill 105 54 -304 107 54 -278 dark_oak_planks
fill 127 54 -304 129 54 -278 dark_oak_planks
fill 105 54 -304 129 54 -302 dark_oak_planks
fill 105 54 -280 129 54 -278 dark_oak_planks

fill 108 55 -301 108 55 -281 dark_oak_fence
fill 126 55 -301 126 55 -281 dark_oak_fence
fill 108 55 -301 126 55 -301 dark_oak_fence
fill 108 55 -281 126 55 -281 dark_oak_fence

fill 115 54 -304 119 56 -301 air
fill 115 54 -281 119 56 -278 air
fill 104 54 -293 107 56 -289 air
fill 127 54 -293 130 56 -289 air

fill 116 50 -304 118 50 -278 stripped_dark_oak_wood[axis=z]
fill 105 50 -292 129 50 -290 stripped_dark_oak_wood[axis=x]

# Grand Corner Pillars
fill 109 50 -299 109 57 -299 stripped_dark_oak_log[axis=y]
setblock 109 50 -299 polished_basalt[axis=y]
setblock 109 54 -299 smooth_quartz
setblock 109 57 -299 smooth_quartz_stairs[facing=south,half=top]

fill 125 50 -299 125 57 -299 stripped_dark_oak_log[axis=y]
setblock 125 50 -299 polished_basalt[axis=y]
setblock 125 54 -299 smooth_quartz
setblock 125 57 -299 smooth_quartz_stairs[facing=south,half=top]

fill 109 50 -283 109 57 -283 stripped_dark_oak_log[axis=y]
setblock 109 50 -283 polished_basalt[axis=y]
setblock 109 54 -283 smooth_quartz
setblock 109 57 -283 smooth_quartz_stairs[facing=north,half=top]

fill 125 50 -283 125 57 -283 stripped_dark_oak_log[axis=y]
setblock 125 50 -283 polished_basalt[axis=y]
setblock 125 54 -283 smooth_quartz
setblock 125 57 -283 smooth_quartz_stairs[facing=north,half=top]

# Sunken Bio-Aquarium Basin (X: 113..121, Z: -295..-287)
fill 113 47 -295 121 47 -287 sea_lantern
fill 114 47 -294 120 47 -288 dark_prismarine
setblock 117 47 -291 sea_lantern

fill 112 48 -296 122 49 -296 polished_deepslate
fill 112 48 -286 122 49 -286 polished_deepslate
fill 112 48 -296 112 49 -286 polished_deepslate
fill 122 48 -296 122 49 -286 polished_deepslate

fill 113 48 -295 121 49 -287 water
fill 113 50 -295 121 50 -287 cyan_stained_glass
fill 116 50 -295 118 50 -287 glass
fill 113 50 -292 121 50 -290 glass

# Downward & Upward Glass Bubble Column Elevators to Celestial Portal Nexus
# Downward Elevator (Magma Block at Y: 37)
fill 114 37 -291 114 50 -291 glass
setblock 114 37 -291 magma_block
fill 114 38 -291 114 50 -291 water

# Upward Elevator (Soul Sand at Y: 37)
fill 120 37 -291 120 50 -291 glass
setblock 120 37 -291 soul_sand
fill 120 38 -291 120 50 -291 water

summon tropical_fish 117 48.5 -291 {PersistenceRequired:1b}
summon tropical_fish 115 48.5 -293 {PersistenceRequired:1b}
summon axolotl 117 48.5 -289 {Variant:0,PersistenceRequired:1b}
''')

    with open(os.path.join(FUNC_DIR, "atrium_decor.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Atrium Foliage, Lighting & Detailing
fill 106 49 -303 108 49 -301 shroomlight
fill 106 50 -303 108 50 -301 moss_carpet
fill 126 49 -303 128 49 -301 shroomlight
fill 126 50 -303 128 50 -301 moss_carpet
fill 106 49 -281 108 49 -279 shroomlight
fill 106 50 -281 108 50 -279 moss_carpet
fill 126 49 -281 128 49 -279 shroomlight
fill 126 50 -281 128 50 -279 moss_carpet

fill 105 51 -304 107 51 -296 moss_block
fill 105 52 -304 107 52 -296 flowering_azalea_leaves
fill 127 51 -304 129 51 -296 moss_block
fill 127 52 -304 129 52 -296 flowering_azalea_leaves
fill 105 51 -286 107 51 -278 moss_block
fill 105 52 -286 107 52 -278 flowering_azalea_leaves
fill 127 51 -286 129 51 -278 moss_block
fill 127 52 -286 129 52 -278 flowering_azalea_leaves

setblock 111 57 -296 spore_blossom
setblock 123 57 -296 spore_blossom
setblock 111 57 -286 spore_blossom
setblock 123 57 -286 spore_blossom
setblock 117 57 -298 spore_blossom
setblock 117 57 -284 spore_blossom

fill 108 56 -301 108 57 -301 cave_vines[berries=true]
fill 126 56 -301 126 57 -301 cave_vines[berries=true]
fill 108 56 -281 108 57 -281 cave_vines[berries=true]
fill 126 56 -281 126 57 -281 cave_vines[berries=true]

setblock 117 57 -291 iron_chain[axis=y]
setblock 117 56 -291 iron_chain[axis=y]
setblock 117 55 -291 shroomlight
setblock 116 55 -291 dark_oak_trapdoor[facing=west,open=false,half=top]
setblock 118 55 -291 dark_oak_trapdoor[facing=east,open=false,half=top]
setblock 117 55 -292 dark_oak_trapdoor[facing=north,open=false,half=top]
setblock 117 55 -290 dark_oak_trapdoor[facing=south,open=false,half=top]
setblock 117 54 -291 soul_lantern[hanging=true]

setblock 112 51 -293 potted_flowering_azalea_bush
setblock 112 51 -289 potted_flowering_azalea_bush
setblock 122 51 -293 potted_flowering_azalea_bush
setblock 122 51 -289 potted_flowering_azalea_bush
''')

    # 3. CELESTIAL PORTAL NEXUS (DEEP STARGATE SANCTUM BENEATH ATRIUM)
    with open(os.path.join(FUNC_DIR, "portal_nexus_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: The Celestial Portal Nexus
# Dimensions: X: 106..128, Z: -302..-280, Y: 36..48
fill 106 36 -302 128 47 -280 air

# Foundation & Outer Obsidian / Basalt Shell
fill 105 35 -303 129 35 -279 polished_deepslate
fill 106 36 -302 128 36 -280 calcite
fill 105 36 -303 105 47 -279 deepslate_bricks
fill 129 36 -303 129 47 -279 deepslate_bricks
fill 105 36 -303 129 47 -303 deepslate_bricks
fill 105 36 -279 129 47 -279 deepslate_bricks
fill 105 48 -303 129 48 -279 crying_obsidian

# Central End Portal Well (Sunken at Y: 36)
fill 115 36 -293 119 36 -289 dark_prismarine
setblock 116 36 -293 end_portal_frame[facing=south,eye=true]
setblock 117 36 -293 end_portal_frame[facing=south,eye=true]
setblock 118 36 -293 end_portal_frame[facing=south,eye=true]

setblock 116 36 -289 end_portal_frame[facing=north,eye=true]
setblock 117 36 -289 end_portal_frame[facing=north,eye=true]
setblock 118 36 -289 end_portal_frame[facing=north,eye=true]

setblock 115 36 -292 end_portal_frame[facing=east,eye=true]
setblock 115 36 -291 end_portal_frame[facing=east,eye=true]
setblock 115 36 -290 end_portal_frame[facing=east,eye=true]

setblock 119 36 -292 end_portal_frame[facing=west,eye=true]
setblock 119 36 -291 end_portal_frame[facing=west,eye=true]
setblock 119 36 -290 end_portal_frame[facing=west,eye=true]

fill 116 36 -292 118 36 -290 end_portal

# Active Monumental Nether Portal (North Wall: Z: -302)
fill 114 37 -302 120 44 -302 obsidian
fill 115 38 -302 119 43 -302 crying_obsidian
fill 116 39 -302 118 42 -302 nether_portal[axis=x]

# Amethyst Geode Cavity on East Wall (X: 125..128, Z: -294..-288)
fill 125 36 -294 128 44 -288 amethyst_block
setblock 124 38 -292 budding_amethyst
setblock 124 39 -291 budding_amethyst
setblock 124 37 -290 budding_amethyst
setblock 123 38 -292 amethyst_cluster[facing=west]
setblock 123 39 -291 amethyst_cluster[facing=west]
setblock 123 37 -290 amethyst_cluster[facing=west]

# Ambient Lighting via Copper Bulbs and Soul Lanterns
setblock 107 41 -291 copper_bulb[lit=true]
setblock 127 41 -291 copper_bulb[lit=true]
setblock 117 41 -281 copper_bulb[lit=true]
setblock 117 46 -291 soul_lantern[hanging=true]
setblock 114 43 -301 soul_lantern[hanging=true]
setblock 120 43 -301 soul_lantern[hanging=true]
''')

    # 4. GRAND SUBTERRANEAN ATHENAEUM (NORTH-WEST WING)
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

# Perimeter Multi-Tier Bookshelves (North & West Walls)
fill 80 51 -329 80 58 -307 chiseled_bookshelf[facing=east]
fill 81 51 -330 101 58 -330 chiseled_bookshelf[facing=south]

# Mezzanine Reading Balcony at Y: 55
fill 81 55 -328 83 55 -308 dark_oak_slab[type=top]
fill 84 55 -329 101 55 -327 dark_oak_slab[type=top]
fill 84 56 -326 101 56 -326 dark_oak_fence

# Floating Lecterns & Study Tables
setblock 86 51 -313 lectern[facing=north]
setblock 87 51 -313 dark_oak_stairs[facing=south]
setblock 95 51 -313 lectern[facing=north]
setblock 96 51 -313 dark_oak_stairs[facing=south]

# Alchemical Distillation Corner (East Wall of Library: X: 101..102, Z: -312..-308)
fill 101 51 -312 102 51 -308 polished_blackstone
setblock 101 52 -311 brewing_stand[has_bottle_0=true,has_bottle_1=true,has_bottle_2=true]
setblock 101 52 -309 cauldron
fill 102 52 -312 102 54 -308 barrel[facing=west]

# Chandeliers and Lanterns
setblock 91 62 -318 iron_chain[axis=y]
setblock 91 61 -318 iron_chain[axis=y]
setblock 91 60 -318 copper_bulb[lit=true]
setblock 91 59 -318 lantern[hanging=true]
''')

    # 5. SOVEREIGN BANQUET & GATHERING HALL (NORTH-EAST WING)
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

# Central Ceremonial Red Carpet Aisle
fill 142 50 -328 144 50 -308 red_carpet
fill 141 50 -328 141 50 -308 yellow_carpet
fill 145 50 -328 145 50 -308 yellow_carpet

# Long Banquet Feast Tables (West: X: 137..139, East: X: 147..149)
fill 138 50 -325 138 50 -310 dark_oak_planks
fill 138 51 -325 138 51 -310 dark_oak_slab[type=top]
fill 137 51 -325 137 51 -310 dark_oak_stairs[facing=east]
fill 139 51 -325 139 51 -310 dark_oak_stairs[facing=west]

fill 148 50 -325 148 50 -310 dark_oak_planks
fill 148 51 -325 148 51 -310 dark_oak_slab[type=top]
fill 147 51 -325 147 51 -310 dark_oak_stairs[facing=east]
fill 149 51 -325 149 51 -310 dark_oak_stairs[facing=west]

# Feast Tableware (Cakes, Candles, Pots, Chalices)
setblock 138 52 -323 cake[bites=0]
setblock 138 52 -320 candle[lit=true,candles=3]
setblock 138 52 -317 decorated_pot[facing=north]
setblock 138 52 -314 candle[lit=true,candles=4]
setblock 138 52 -311 cake[bites=0]

setblock 148 52 -323 cake[bites=0]
setblock 148 52 -320 candle[lit=true,candles=3]
setblock 148 52 -317 decorated_pot[facing=north]
setblock 148 52 -314 candle[lit=true,candles=4]
setblock 148 52 -311 cake[bites=0]

# High Table Dais (North End: Z: -328..-326)
fill 136 51 -328 150 51 -326 smooth_quartz
fill 140 52 -327 146 52 -327 dark_oak_slab[type=top]
setblock 143 52 -328 dark_oak_stairs[facing=south]
setblock 142 52 -328 dark_oak_stairs[facing=south]
setblock 144 52 -328 dark_oak_stairs[facing=south]

# Dual Roaring Stone Fireplaces (East Wall X: 154, West Wall X: 132)
# West Fireplace
fill 132 50 -319 133 50 -317 netherrack
fill 132 51 -319 133 51 -317 campfire[lit=true]
fill 134 51 -319 134 53 -317 iron_bars
fill 132 52 -320 134 55 -316 polished_blackstone_bricks

# East Fireplace
fill 153 50 -319 154 50 -317 netherrack
fill 153 51 -319 154 51 -317 campfire[lit=true]
fill 152 51 -319 152 53 -317 iron_bars
fill 152 52 -320 154 55 -316 polished_blackstone_bricks

# Suspended Copper & Brass Chandeliers
setblock 143 62 -322 iron_chain[axis=y]
setblock 143 61 -322 iron_chain[axis=y]
setblock 143 60 -322 copper_bulb[lit=true]
setblock 143 59 -322 soul_lantern[hanging=true]

setblock 143 62 -314 iron_chain[axis=y]
setblock 143 61 -314 iron_chain[axis=y]
setblock 143 60 -314 copper_bulb[lit=true]
setblock 143 59 -314 soul_lantern[hanging=true]
''')

    # 6. SUBTERRANEAN HYPERLOOP TRANSIT HUB (NORTH TERMINAL)
    with open(os.path.join(FUNC_DIR, "transit_hub_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: The Subterranean Hyperloop Transit Hub
# Dimensions: X: 104..130, Z: -345..-325, Floor Y: 49..50, Ceiling Y: 58
fill 104 49 -345 130 58 -325 air

# Foundation & Concourse
fill 103 48 -346 131 48 -324 polished_deepslate
fill 104 50 -345 130 50 -325 smooth_quartz
fill 103 50 -346 103 58 -324 polished_blackstone
fill 131 50 -346 131 58 -324 polished_blackstone
fill 103 50 -346 131 58 -346 polished_blackstone
fill 103 59 -346 131 59 -324 deepslate_tiles

# Concourse Stairs connecting from Treasury area (Z: -325)
fill 115 50 -325 119 54 -325 air

# Track Trough 1 (West Line: Surface Express, X: 108..109, Y: 49)
fill 108 49 -345 109 49 -327 polished_blackstone
fill 108 50 -345 108 50 -327 yellow_concrete
fill 109 50 -345 109 50 -327 powered_rail[powered=true,shape=north_south]

# Track Trough 2 (Center Line: Bedrock Mining Express, X: 117..118, Y: 49)
fill 117 49 -345 118 49 -327 polished_blackstone
fill 116 50 -345 116 50 -327 yellow_concrete
fill 117 50 -345 117 50 -327 powered_rail[powered=true,shape=north_south]

# Track Trough 3 (East Line: City Base Express, X: 125..126, Y: 49)
fill 125 49 -345 126 49 -327 polished_blackstone
fill 124 50 -345 124 50 -327 yellow_concrete
fill 125 50 -345 125 50 -327 powered_rail[powered=true,shape=north_south]

# Push-Button Minecart Dispensers at Boarding Gates (Z: -328)
setblock 109 51 -328 dispenser[facing=north]
setblock 109 52 -328 stone_button[face=floor,facing=north]

setblock 117 51 -328 dispenser[facing=north]
setblock 117 52 -328 stone_button[face=floor,facing=north]

setblock 125 51 -328 dispenser[facing=north]
setblock 125 52 -328 stone_button[face=floor,facing=north]

# Hazard Warning Stripes along Platform Edges
fill 110 50 -345 110 50 -327 black_concrete
fill 115 50 -345 115 50 -327 black_concrete
fill 118 50 -345 118 50 -327 black_concrete
fill 123 50 -345 123 50 -327 black_concrete

# Lighting via Inset Sea Lanterns and Copper Bulbs
fill 112 50 -340 114 50 -340 sea_lantern
fill 120 50 -340 122 50 -340 sea_lantern
setblock 109 55 -335 copper_bulb[lit=true]
setblock 117 55 -335 copper_bulb[lit=true]
setblock 125 55 -335 copper_bulb[lit=true]
''')

    # 7. PARLIAMENT ASSEMBLY (REMAINS PERFECTED)
    with open(os.path.join(FUNC_DIR, "parliament_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Grand High Parliament of the Republic
fill 104 49 -276 130 58 -244 air
fill 104 48 -276 130 48 -244 polished_deepslate
fill 104 49 -276 130 49 -244 polished_blackstone
fill 104 59 -276 130 59 -244 deepslate_tiles

fill 104 50 -276 104 58 -244 deepslate_bricks
fill 130 50 -276 130 58 -244 deepslate_bricks
fill 104 50 -276 130 58 -276 deepslate_bricks
fill 104 50 -244 130 58 -244 deepslate_bricks

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

# Portal from Atrium
fill 115 50 -277 119 55 -275 air
fill 115 49 -277 119 49 -275 polished_blackstone
fill 114 50 -276 114 55 -276 crying_obsidian
fill 120 50 -276 120 55 -276 crying_obsidian
fill 115 55 -276 119 55 -276 crying_obsidian
setblock 114 52 -276 redstone_lamp[lit=true]
setblock 120 52 -276 redstone_lamp[lit=true]

# Central Aisle
fill 116 50 -275 118 50 -252 red_carpet
fill 115 50 -275 115 50 -252 yellow_carpet
fill 119 50 -275 119 50 -252 yellow_carpet
setblock 117 48 -272 shroomlight
setblock 117 48 -266 shroomlight
setblock 117 48 -260 shroomlight
setblock 117 48 -254 shroomlight

# Cabinet Benches (West)
fill 114 50 -272 114 50 -254 dark_oak_planks
fill 114 51 -272 114 51 -254 dark_oak_slab[type=top]
fill 113 50 -272 113 50 -254 dark_oak_stairs[facing=east]
fill 113 51 -272 113 51 -254 green_carpet

fill 111 50 -272 112 50 -254 polished_blackstone
fill 112 51 -272 112 51 -254 dark_oak_slab[type=top]
fill 111 51 -272 111 51 -254 dark_oak_stairs[facing=east]
fill 111 52 -272 111 52 -254 green_carpet

fill 109 50 -272 110 51 -254 polished_blackstone
fill 110 52 -272 110 52 -254 dark_oak_slab[type=top]
fill 109 52 -272 109 52 -254 dark_oak_stairs[facing=east]
fill 109 53 -272 109 53 -254 green_carpet

setblock 114 52 -270 end_rod
setblock 114 52 -269 stone_button[face=floor,facing=north]
setblock 114 52 -266 end_rod
setblock 114 52 -265 stone_button[face=floor,facing=north]
setblock 114 52 -262 end_rod
setblock 114 52 -261 stone_button[face=floor,facing=north]
setblock 114 52 -258 end_rod
setblock 114 52 -257 stone_button[face=floor,facing=north]

# Assembly Benches (East)
fill 120 50 -272 120 50 -254 dark_oak_planks
fill 120 51 -272 120 51 -254 dark_oak_slab[type=top]
fill 121 50 -272 121 50 -254 dark_oak_stairs[facing=west]
fill 121 51 -272 121 51 -254 green_carpet

fill 122 50 -272 123 50 -254 polished_blackstone
fill 122 51 -272 122 51 -254 dark_oak_slab[type=top]
fill 123 51 -272 123 51 -254 dark_oak_stairs[facing=west]
fill 123 52 -272 123 52 -254 green_carpet

fill 124 50 -272 125 51 -254 polished_blackstone
fill 124 52 -272 124 52 -254 dark_oak_slab[type=top]
fill 125 52 -272 125 52 -254 dark_oak_stairs[facing=west]
fill 125 53 -272 125 53 -254 green_carpet

setblock 120 52 -270 end_rod
setblock 120 52 -269 stone_button[face=floor,facing=north]
setblock 120 52 -266 end_rod
setblock 120 52 -265 stone_button[face=floor,facing=north]
setblock 120 52 -262 end_rod
setblock 120 52 -261 stone_button[face=floor,facing=north]
setblock 120 52 -258 end_rod
setblock 120 52 -257 stone_button[face=floor,facing=north]

# Dais & Speaker Throne
fill 113 50 -251 121 50 -245 smooth_quartz
fill 114 51 -251 120 51 -245 smooth_quartz
fill 115 52 -249 119 52 -245 gold_block

setblock 116 51 -251 dark_oak_slab[type=top]
setblock 117 51 -251 dark_oak_slab[type=top]
setblock 118 51 -251 dark_oak_slab[type=top]
setblock 117 52 -251 lectern[facing=north]

setblock 119 52 -250 gold_block
summon armor_stand 119 53 -250 {ShowArms:1b,NoBasePlate:1b,Rotation:[0f,0f],Equipment:[{id:"golden_sword",count:1,components:{"minecraft:enchantments":{levels:{"minecraft:unbreaking":3}}}},{},{},{},{}]}

setblock 115 52 -250 dark_oak_slab[type=top]
setblock 115 53 -250 red_candle[lit=true]

setblock 117 53 -247 gilded_blackstone
setblock 117 54 -247 dark_oak_stairs[facing=north]
setblock 116 54 -247 dark_oak_trapdoor[facing=west,open=true]
setblock 118 54 -247 dark_oak_trapdoor[facing=east,open=true]

fill 116 53 -246 118 57 -246 stripped_dark_oak_log[axis=y]
fill 116 57 -247 118 57 -246 dark_oak_slab[type=bottom]
fill 116 56 -247 118 56 -247 yellow_carpet

fill 113 50 -245 121 57 -245 crying_obsidian
fill 115 52 -245 119 56 -245 gold_block
fill 116 53 -245 118 55 -245 sea_lantern

# Chandeliers
setblock 117 58 -269 iron_chain[axis=y]
setblock 117 57 -269 iron_chain[axis=y]
setblock 117 56 -269 shroomlight
setblock 116 56 -269 dark_oak_trapdoor[facing=west,open=false,half=top]
setblock 118 56 -269 dark_oak_trapdoor[facing=east,open=false,half=top]
setblock 117 56 -270 dark_oak_trapdoor[facing=north,open=false,half=top]
setblock 117 56 -268 dark_oak_trapdoor[facing=south,open=false,half=top]
setblock 117 55 -269 soul_lantern[hanging=true]

setblock 117 58 -261 iron_chain[axis=y]
setblock 117 57 -261 iron_chain[axis=y]
setblock 117 56 -261 shroomlight
setblock 116 56 -261 dark_oak_trapdoor[facing=west,open=false,half=top]
setblock 118 56 -261 dark_oak_trapdoor[facing=east,open=false,half=top]
setblock 117 56 -262 dark_oak_trapdoor[facing=north,open=false,half=top]
setblock 117 56 -260 dark_oak_trapdoor[facing=south,open=false,half=top]
setblock 117 55 -261 soul_lantern[hanging=true]

setblock 117 58 -250 iron_chain[axis=y]
setblock 117 57 -250 iron_chain[axis=y]
setblock 117 56 -250 shroomlight
setblock 116 56 -250 dark_oak_trapdoor[facing=west,open=false,half=top]
setblock 118 56 -250 dark_oak_trapdoor[facing=east,open=false,half=top]
setblock 117 56 -251 dark_oak_trapdoor[facing=north,open=false,half=top]
setblock 117 56 -249 dark_oak_trapdoor[facing=south,open=false,half=top]
setblock 117 55 -250 soul_lantern[hanging=true]
''')

    # 8. FORGE & SUPER SMELTER
    with open(os.path.join(FUNC_DIR, "forge_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Sector A Dwarven Industrial Forge and Super Smelter
fill 82 49 -301 99 49 -281 polished_basalt[axis=y]
fill 82 50 -301 82 57 -281 polished_deepslate
fill 99 50 -301 99 57 -281 polished_deepslate
fill 82 50 -301 99 57 -301 polished_deepslate
fill 82 50 -281 99 57 -281 polished_deepslate
fill 82 58 -301 99 58 -281 deepslate_tiles

fill 99 50 -293 104 55 -289 air
fill 99 49 -292 104 49 -290 polished_basalt[axis=x]
fill 99 50 -292 104 50 -290 smooth_stone
fill 99 51 -293 104 54 -293 deepslate_tile_wall
fill 99 51 -289 104 54 -289 deepslate_tile_wall
fill 99 55 -292 104 55 -290 copper_grate
fill 99 56 -292 104 56 -290 sea_lantern

fill 83 50 -300 98 50 -282 smooth_stone
fill 85 50 -298 96 50 -284 polished_basalt[axis=y]

# 16 Furnace Super Smelter Array
setblock 89 50 -299 chest[facing=south,type=left]
setblock 90 50 -299 chest[facing=south,type=right]

fill 84 51 -300 91 51 -300 blast_furnace[facing=south,lit=true]
fill 92 51 -300 97 51 -300 furnace[facing=south,lit=true]

fill 84 50 -300 97 50 -300 hopper[facing=south]
fill 84 52 -300 97 52 -300 hopper[facing=down]
fill 84 53 -300 97 53 -300 chest[facing=south]

fill 84 54 -300 97 54 -300 redstone_lamp[lit=true]
fill 84 55 -300 97 55 -300 redstone_block

# Master Smithing & Anvil Station
fill 89 50 -293 92 50 -291 iron_block
setblock 89 51 -293 anvil[facing=south]
setblock 90 51 -293 smithing_table
setblock 91 51 -293 grindstone[facing=south,face=floor]
setblock 92 51 -293 chipped_anvil[facing=south]

summon armor_stand 88 51 -293 {ShowArms:1b,NoBasePlate:1b,Rotation:[0f,0f],Equipment:[{id:"netherite_pickaxe",count:1},{},{},{},{id:"netherite_helmet",count:1}]}
summon armor_stand 93 51 -293 {ShowArms:1b,NoBasePlate:1b,Rotation:[0f,0f],Equipment:[{id:"netherite_sword",count:1},{},{},{},{id:"netherite_chestplate",count:1}]}

fill 83 50 -293 83 55 -291 lava
fill 84 50 -293 84 55 -291 tinted_glass
fill 84 50 -294 84 55 -294 copper_grate
fill 84 50 -290 84 55 -290 copper_grate

# Alchemy Lab
fill 84 50 -283 87 50 -283 soul_sand
fill 84 51 -283 87 51 -283 nether_wart[age=3]

fill 89 50 -283 93 50 -283 polished_blackstone
setblock 89 51 -283 brewing_stand[has_bottle_0=true,has_bottle_1=true,has_bottle_2=true]
setblock 90 51 -283 water_cauldron[level=3]
setblock 91 51 -283 brewing_stand[has_bottle_0=true,has_bottle_1=true]
setblock 92 51 -283 barrel[facing=up]
setblock 93 51 -283 water_cauldron[level=3]

fill 94 51 -283 97 51 -283 chiseled_bookshelf[facing=north]
fill 94 52 -283 97 52 -283 barrel[facing=south]
''')

    # 9. HYDROPONICS & TREE CONSERVATORY
    with open(os.path.join(FUNC_DIR, "hydroponics_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Sector B Automated Hydroponics and Tree Conservatory
fill 136 49 -302 154 49 -280 stripped_cherry_wood[axis=y]
fill 136 50 -302 136 60 -280 smooth_quartz
fill 154 50 -302 154 60 -280 smooth_quartz
fill 136 50 -302 154 60 -302 smooth_quartz
fill 136 50 -280 154 60 -280 smooth_quartz
fill 136 61 -302 154 61 -280 deepslate_tiles

fill 130 50 -293 136 55 -289 air
fill 130 49 -292 136 49 -290 stripped_cherry_wood[axis=x]
fill 130 50 -292 136 50 -290 bamboo_mosaic
fill 130 51 -293 136 54 -293 smooth_quartz_stairs[facing=south]
fill 130 51 -289 136 54 -289 smooth_quartz_stairs[facing=north]
fill 130 55 -292 136 55 -290 sea_lantern

fill 137 50 -301 153 50 -281 bamboo_mosaic
fill 142 50 -297 148 50 -285 mud

# 1. Automated Sugarcane & Bamboo Harvester
fill 138 49 -300 151 49 -300 water
setblock 137 49 -300 hopper[facing=west]
setblock 136 49 -300 barrel[facing=up]

fill 138 50 -301 144 50 -301 sand
fill 145 50 -301 151 50 -301 mud

fill 138 51 -301 144 51 -301 sugar_cane
fill 145 51 -301 151 51 -301 bamboo[age=1,leaves=large,stage=0]

fill 138 52 -301 151 52 -301 piston[facing=south]
fill 138 53 -301 151 53 -301 observer[facing=south]

fill 138 52 -302 151 52 -302 smooth_stone
fill 138 53 -302 151 53 -302 redstone_wire

fill 138 51 -299 151 54 -299 glass
fill 138 55 -301 151 55 -299 sea_lantern

# 2. Indoor Tree Conservatory
fill 143 50 -295 147 50 -287 rooted_dirt
fill 144 50 -294 146 50 -288 mud

fill 145 51 -293 145 56 -293 stripped_cherry_log[axis=y]
fill 143 56 -295 147 58 -291 cherry_leaves
fill 144 59 -294 146 59 -292 cherry_leaves

fill 145 51 -288 145 55 -288 stripped_dark_oak_log[axis=y]
fill 143 55 -290 147 57 -286 dark_oak_leaves

setblock 142 51 -291 dispenser[facing=east]
setblock 142 52 -291 stone_button[facing=east]

# 3. Apiary Bee Sanctuary
fill 138 50 -284 151 50 -284 packed_mud
fill 140 49 -283 148 49 -283 campfire[lit=true]
fill 140 50 -283 148 50 -283 moss_carpet

setblock 141 51 -283 beehive[facing=north,honey_level=5]
setblock 143 51 -283 bee_nest[facing=north,honey_level=5]
setblock 145 51 -283 beehive[facing=north,honey_level=5]
setblock 147 51 -283 bee_nest[facing=north,honey_level=5]

setblock 141 51 -284 flowering_azalea
setblock 143 51 -284 rose_bush[half=lower]
setblock 143 52 -284 rose_bush[half=upper]
setblock 145 51 -284 flowering_azalea
setblock 147 51 -284 peony[half=lower]
setblock 147 52 -284 peony[half=upper]

fill 139 51 -285 149 54 -285 tinted_glass
fill 139 55 -285 149 55 -283 sea_lantern

summon bee 144 52 -284 {CannotEnterHiveTicks:0,TicksInHive:0}
summon bee 146 52 -284 {CannotEnterHiveTicks:0,TicksInHive:0}
''')

    # 10. SOVEREIGN SUITES
    with open(os.path.join(FUNC_DIR, "suites_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Luxury Sovereign Suites (Kowsyke, Ahsane, Jamal)

# 1. KOWSYKE PRIME MINISTER SUITE (Behind Parliament: X: 111..123, Z: -243..-232)
fill 110 49 -244 124 57 -231 air
fill 110 48 -244 124 48 -231 gilded_blackstone
fill 111 49 -243 123 49 -232 stripped_dark_oak_wood[axis=z]
fill 110 49 -244 110 57 -231 polished_blackstone_bricks
fill 124 49 -244 124 57 -231 polished_blackstone_bricks
fill 110 49 -231 124 57 -231 polished_blackstone_bricks
fill 110 58 -244 124 58 -231 deepslate_tiles

fill 116 49 -244 118 53 -244 air
fill 116 49 -244 118 49 -244 gold_block

fill 116 50 -233 118 50 -233 gold_block
fill 116 50 -234 118 50 -234 red_bed[facing=south,part=head]
fill 116 50 -235 118 50 -235 red_bed[facing=south,part=foot]
fill 115 50 -233 115 54 -233 stripped_dark_oak_log[axis=y]
fill 119 50 -233 119 54 -233 stripped_dark_oak_log[axis=y]
fill 115 55 -235 119 55 -233 dark_oak_slab[type=bottom]
fill 116 54 -235 118 54 -235 yellow_wool

fill 110 49 -240 110 54 -236 sea_lantern
fill 110 50 -239 110 53 -237 water
fill 111 50 -239 111 53 -237 tinted_glass
summon axolotl 110.5 50.5 -238 {Variant:4,PersistenceRequired:1b}

setblock 121 50 -238 gold_block
summon armor_stand 121 51 -238 {ShowArms:1b,NoBasePlate:1b,Rotation:[270f,0f],Equipment:[{id:"netherite_sword",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:gold",pattern:"minecraft:silence"}}}]}

setblock 121 50 -241 dark_oak_stairs[facing=south]
setblock 121 50 -242 ender_chest[facing=south]
setblock 120 50 -242 dark_oak_slab[type=top]
setblock 120 51 -242 lantern[hanging=false]

# 2. AHSANE EXECUTIVE SUITE (West Flank of Parliament: X: 93..103, Z: -268..-256)
fill 92 49 -269 104 57 -255 air
fill 92 48 -269 104 48 -255 polished_deepslate
fill 93 49 -268 103 49 -256 cyan_carpet
fill 92 49 -269 92 57 -255 deepslate_bricks
fill 92 49 -269 103 57 -269 deepslate_bricks
fill 92 49 -255 103 57 -255 deepslate_bricks
fill 92 58 -269 104 58 -255 deepslate_tiles

fill 103 49 -263 104 53 -261 air

fill 94 50 -266 94 53 -266 dark_oak_fence
fill 97 50 -266 97 53 -266 dark_oak_fence
fill 94 50 -264 94 53 -264 dark_oak_fence
fill 97 50 -264 97 53 -264 dark_oak_fence
fill 94 54 -266 97 54 -264 cyan_carpet
setblock 95 50 -265 cyan_bed[facing=west,part=head]
setblock 96 50 -265 cyan_bed[facing=west,part=foot]

fill 93 50 -258 98 53 -258 bookshelf
setblock 96 50 -260 dark_oak_stairs[facing=north]
setblock 96 50 -259 dark_oak_slab[type=top]

setblock 100 50 -265 diamond_block
summon armor_stand 100 51 -265 {ShowArms:1b,NoBasePlate:1b,Rotation:[180f,0f],Equipment:[{id:"diamond_sword",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:diamond",pattern:"minecraft:bolt"}}}]}

# 3. JAMAL EXECUTIVE SUITE (East Flank of Parliament: X: 131..141, Z: -268..-256)
fill 130 49 -269 142 57 -255 air
fill 130 48 -269 142 48 -255 dark_prismarine
fill 131 49 -268 141 49 -256 purple_carpet
fill 142 49 -269 142 57 -255 deepslate_bricks
fill 131 49 -269 142 57 -269 deepslate_bricks
fill 131 49 -255 142 57 -255 deepslate_bricks
fill 130 58 -269 142 58 -255 deepslate_tiles

fill 130 49 -263 131 53 -261 air

fill 137 50 -266 137 53 -266 dark_oak_fence
fill 140 50 -266 140 53 -266 dark_oak_fence
fill 137 50 -264 137 53 -264 dark_oak_fence
fill 140 50 -264 140 53 -264 dark_oak_fence
fill 137 54 -266 140 54 -264 purple_carpet
setblock 139 50 -265 purple_bed[facing=east,part=head]
setblock 138 50 -265 purple_bed[facing=east,part=foot]

fill 141 50 -262 141 54 -259 amethyst_block
setblock 140 51 -261 amethyst_cluster[facing=west]
setblock 140 52 -260 amethyst_cluster[facing=west]
setblock 140 50 -260 small_amethyst_bud[facing=west]

setblock 134 50 -265 amethyst_block
summon armor_stand 134 51 -265 {ShowArms:1b,NoBasePlate:1b,Rotation:[180f,0f],Equipment:[{id:"bow",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:amethyst",pattern:"minecraft:ward"}}}]}
''')

    # 11. SUB-FLOOR CONDUITS
    with open(os.path.join(FUNC_DIR, "conduits_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Sector D Sub-Floor Redstone Conduits
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

setblock 117 50 -302 tinted_glass
setblock 117 49 -302 repeater[facing=south]
setblock 117 50 -300 tinted_glass
setblock 117 49 -300 redstone_wire
setblock 117 50 -282 tinted_glass
setblock 117 49 -282 comparator[facing=south]
setblock 117 50 -280 tinted_glass
setblock 117 49 -280 redstone_wire
''')

    # 12. MASTER BUILD ALL ORCHESTRATOR
    with open(os.path.join(FUNC_DIR, "build_all.mcfunction"), "w") as f:
        f.write('''# Subterranean Utopia: Master Orchestrator
function citadel:stairs_descent
function citadel:atrium_shell
function citadel:atrium_decor
function citadel:portal_nexus_build
function citadel:athenaeum_build
function citadel:banquet_build
function citadel:transit_hub_build
function citadel:parliament_build
function citadel:forge_build
function citadel:hydroponics_build
function citadel:suites_build
function citadel:conduits_build
''')

    print("Complete Subterranean Utopia Datapack successfully generated!")

if __name__ == "__main__":
    main()
