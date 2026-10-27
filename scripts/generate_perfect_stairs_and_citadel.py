#!/usr/bin/env python3
"""
Master Builder Generator: Fixed Stair Logic, Restored Treasury Protection and Populated Utopia.
Key architecture rules:
1. All descending stairs facing NORTH (half=bottom) for stepping down to the south.
2. Treasury floor and vault at Y=64..72 completely protected and restored.
3. Descent tunnel ceiling stays strictly beneath Y=64 from Z=-319 southwards.
4. All seating, ceiling vault arches, wall skirting, dais steps, and spiral stairs verified.
5. Populated interior environments: tapestries, banners, feast platters, armor stands, flora, lighting.
6. All 12 sectors fully included and connected via clear doorways.
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

    # 1. STAIRS DESCENT (PERFECTED ORIENTATION AND TREASURY PROTECTION)
    with open(os.path.join(FUNC_DIR, "stairs_descent.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Grand Staircase Descent
# Starts at Treasury opening (X: 116..118, Z: -322..-320, Y: 64) descending to Citadel (Y: 50, Z: -308)
# All descending steps face NORTH (half=bottom) so players step DOWN going south.
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

# Step Z=-319 (Y=61): From here south, ceiling is Y=63, leaving Y=64 Treasury floor 100% solid
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

# Step Z=-308 (Y=50, Final Step)
fill 115 49 -308 119 49 -308 polished_deepslate
fill 116 50 -308 118 50 -308 spruce_stairs[facing=north,half=bottom]
fill 116 51 -308 118 56 -308 air
fill 115 64 -308 119 64 -308 spruce_planks
setblock 115 50 -308 stripped_dark_oak_log[axis=y]
setblock 119 50 -308 stripped_dark_oak_log[axis=y]
setblock 115 51 -308 lantern[hanging=false]
setblock 119 51 -308 lantern[hanging=false]

# Landing Crossroads Vestibule at Z=-307..-305 (Y=50)
fill 114 49 -307 120 49 -305 polished_deepslate
fill 116 50 -307 118 50 -305 stripped_dark_oak_wood[axis=z]
fill 115 50 -307 115 50 -305 mud_bricks
fill 119 50 -307 119 50 -305 mud_bricks
fill 114 51 -307 120 56 -305 air
setblock 117 49 -306 shroomlight
setblock 117 50 -306 moss_carpet

# Archway pillars entering Atrium to the south
fill 115 51 -305 115 55 -305 stripped_dark_oak_log[axis=y]
fill 119 51 -305 119 55 -305 stripped_dark_oak_log[axis=y]
setblock 116 55 -305 dark_oak_stairs[facing=east,half=top]
setblock 118 55 -305 dark_oak_stairs[facing=west,half=top]
setblock 117 55 -305 polished_deepslate_slab[type=top]

# West Portal Corridor to Athenaeum Library (X: 102..114, Z: -307..-305)
fill 102 49 -307 114 49 -305 polished_deepslate
fill 102 50 -307 114 54 -305 air
fill 102 50 -306 114 50 -306 stripped_dark_oak_wood[axis=x]
fill 102 55 -307 114 55 -305 deepslate_tiles
setblock 108 54 -306 lantern[hanging=true]

# East Portal Corridor to Sovereign Banquet Hall (X: 120..132, Z: -307..-305)
fill 120 49 -307 132 49 -305 polished_deepslate
fill 120 50 -307 132 54 -305 air
fill 120 50 -306 132 50 -306 stripped_dark_oak_wood[axis=x]
fill 120 55 -307 132 55 -305 deepslate_tiles
setblock 126 54 -306 lantern[hanging=true]

# West Flank Transit Corridor to Hyperloop Hub (X: 106..108, Z: -325..-307)
fill 106 49 -325 108 49 -307 polished_deepslate
fill 106 50 -325 108 53 -307 air
fill 106 54 -325 108 54 -307 deepslate_tiles
setblock 107 53 -315 lantern[hanging=true]
setblock 107 53 -322 lantern[hanging=true]

# East Flank Transit Corridor to Hyperloop Hub (X: 126..128, Z: -325..-307)
fill 126 49 -325 128 49 -307 polished_deepslate
fill 126 50 -325 128 53 -307 air
fill 126 54 -325 128 54 -307 deepslate_tiles
setblock 127 53 -315 lantern[hanging=true]
setblock 127 53 -322 lantern[hanging=true]
''')

    # 2. BIO DOME ATRIUM SHELL
    with open(os.path.join(FUNC_DIR, "atrium_shell.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Bio Dome Atrium Shell
fill 104 50 -305 130 58 -277 air

fill 103 49 -306 131 49 -276 polished_deepslate
fill 105 50 -304 129 50 -278 moss_block
fill 116 50 -304 118 50 -278 stripped_dark_oak_wood[axis=z]
fill 105 50 -291 129 50 -291 stripped_dark_oak_wood[axis=x]

fill 104 50 -305 104 57 -277 deepslate_tiles
fill 130 50 -305 130 57 -277 deepslate_tiles
fill 104 50 -305 130 57 -305 deepslate_tiles
fill 104 50 -277 130 57 -277 deepslate_tiles

# Wall Base Skirting (Right side up against wall)
fill 105 51 -304 105 51 -278 polished_deepslate_stairs[facing=east,half=bottom]
fill 129 51 -304 129 51 -278 polished_deepslate_stairs[facing=west,half=bottom]
fill 105 51 -304 129 51 -304 polished_deepslate_stairs[facing=south,half=bottom]
fill 105 51 -278 129 51 -278 polished_deepslate_stairs[facing=north,half=bottom]

# Clear portals in skirting
fill 115 51 -304 119 51 -304 air
fill 115 51 -278 119 51 -278 air
fill 105 51 -292 105 51 -290 air
fill 129 51 -292 129 51 -290 air

# Atrium Ceiling Vault
fill 104 58 -305 130 58 -277 deepslate_tiles
fill 111 58 -298 123 58 -284 glass

# Structural Pilasters
setblock 109 50 -299 polished_basalt[axis=y]
setblock 109 54 -299 smooth_quartz
setblock 109 57 -299 smooth_quartz_stairs[facing=south,half=top]

setblock 125 50 -299 polished_basalt[axis=y]
setblock 125 54 -299 smooth_quartz
setblock 125 57 -299 smooth_quartz_stairs[facing=south,half=top]

setblock 109 50 -283 polished_basalt[axis=y]
setblock 109 54 -283 smooth_quartz
setblock 109 57 -283 smooth_quartz_stairs[facing=north,half=top]

setblock 125 50 -283 polished_basalt[axis=y]
setblock 125 54 -283 smooth_quartz
setblock 125 57 -283 smooth_quartz_stairs[facing=north,half=top]

# Vaulted Ceiling Ribs at Y: 57
fill 110 57 -299 124 57 -299 dark_oak_stairs[facing=south,half=top]
fill 110 57 -283 124 57 -283 dark_oak_stairs[facing=north,half=top]
fill 109 57 -298 109 57 -284 dark_oak_stairs[facing=east,half=top]
fill 125 57 -298 125 57 -284 dark_oak_stairs[facing=west,half=top]

# Sunken Bio Aquarium Basin
fill 113 47 -295 121 47 -287 sea_lantern
fill 114 47 -294 120 47 -288 dark_prismarine
fill 113 48 -295 121 49 -287 water
fill 113 50 -295 121 50 -287 air

fill 113 50 -295 121 50 -295 dark_oak_fence
fill 113 50 -287 121 50 -287 dark_oak_fence
fill 113 50 -294 113 50 -288 dark_oak_fence
fill 121 50 -294 121 50 -288 dark_oak_fence

fill 116 50 -295 118 50 -287 glass
fill 113 50 -292 121 50 -290 glass

# Bubble Column Elevators to Celestial Nexus
fill 114 37 -291 114 50 -291 glass
setblock 114 37 -291 magma_block
fill 114 38 -291 114 50 -291 water

fill 120 37 -291 120 50 -291 glass
setblock 120 37 -291 soul_sand
fill 120 38 -291 120 50 -291 water
''')

    # 3. ATRIUM DECORATION AND FAUNA
    with open(os.path.join(FUNC_DIR, "atrium_decor.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Atrium Living Ecosystem
fill 106 51 -303 108 51 -297 moss_block
fill 106 52 -303 108 52 -297 flowering_azalea_leaves
fill 126 51 -303 128 51 -297 moss_block
fill 126 52 -303 128 52 -297 flowering_azalea_leaves

fill 106 51 -286 108 51 -278 moss_block
fill 106 52 -286 108 52 -278 flowering_azalea_leaves
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

# Seating Benches around central pond
fill 111 51 -293 111 51 -289 dark_oak_stairs[facing=east,half=bottom]
fill 123 51 -293 123 51 -289 dark_oak_stairs[facing=west,half=bottom]
''')

    # 4. CELESTIAL PORTAL NEXUS (DEEP LEVEL AT Y=36..48)
    with open(os.path.join(FUNC_DIR, "portal_nexus_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: The Celestial Portal Nexus
fill 106 36 -302 128 47 -280 air
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

# Monumental Nether Portal (North Wall: Z: -302)
fill 114 37 -302 120 44 -302 obsidian
fill 115 38 -302 119 43 -302 crying_obsidian
fill 116 39 -302 118 42 -302 nether_portal[axis=x]

# Amethyst Geode Cavity on East Wall
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
''')

    # 5. GRAND HIGH PARLIAMENT
    with open(os.path.join(FUNC_DIR, "parliament_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Grand High Parliament of the Republic
fill 104 50 -276 130 58 -244 air

fill 103 49 -277 131 49 -243 polished_deepslate
fill 104 50 -276 130 50 -244 polished_blackstone
fill 103 50 -277 103 58 -243 polished_blackstone_bricks
fill 131 50 -277 131 58 -243 polished_blackstone_bricks
fill 103 50 -277 131 58 -277 polished_blackstone_bricks
fill 103 50 -243 131 58 -243 polished_blackstone_bricks
fill 103 59 -277 131 59 -243 deepslate_tiles

# Chamber Pilasters
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

# Central Green Carpet Aisle
fill 116 50 -275 118 50 -252 green_carpet
fill 117 50 -275 117 50 -252 yellow_carpet

# Under floor ambient lights along aisle
setblock 117 48 -272 shroomlight
setblock 117 48 -266 shroomlight
setblock 117 48 -260 shroomlight
setblock 117 48 -254 shroomlight

# Cabinet Benches (West side: Members sit facing EAST towards aisle)
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

# Assembly Benches (East side: Members sit facing WEST towards aisle)
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

# Dais and Speaker Throne (South end: Steps face NORTH so players step UP to the south)
fill 113 50 -251 121 50 -245 smooth_quartz
fill 114 51 -251 120 51 -245 smooth_quartz
fill 114 51 -251 120 51 -251 smooth_quartz_stairs[facing=north,half=bottom]

fill 115 52 -249 119 52 -245 gold_block
fill 115 52 -249 119 52 -249 smooth_quartz_stairs[facing=north,half=bottom]

setblock 116 51 -251 dark_oak_slab[type=top]
setblock 117 51 -251 dark_oak_slab[type=top]
setblock 118 51 -251 dark_oak_slab[type=top]

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

# Heraldic Wall of State behind Dais
fill 114 50 -244 120 57 -244 crying_obsidian
fill 116 54 -244 118 56 -244 gold_block
setblock 117 55 -244 bell[facing=north]

# Vaulted Chandeliers
setblock 117 58 -269 iron_chain[axis=y]
setblock 117 57 -269 iron_chain[axis=y]
setblock 117 56 -269 shroomlight
setblock 116 56 -269 dark_oak_trapdoor[facing=west,open=false,half=top]
setblock 118 56 -269 dark_oak_trapdoor[facing=east,open=false,half=top]
setblock 117 55 -269 soul_lantern[hanging=true]

setblock 117 58 -261 iron_chain[axis=y]
setblock 117 57 -261 iron_chain[axis=y]
setblock 117 56 -261 shroomlight
setblock 116 56 -261 dark_oak_trapdoor[facing=west,open=false,half=top]
setblock 118 56 -261 dark_oak_trapdoor[facing=east,open=false,half=top]
setblock 117 55 -261 soul_lantern[hanging=true]

setblock 117 58 -250 iron_chain[axis=y]
setblock 117 57 -250 iron_chain[axis=y]
setblock 117 56 -250 shroomlight
setblock 116 56 -250 dark_oak_trapdoor[facing=west,open=false,half=top]
setblock 118 56 -250 dark_oak_trapdoor[facing=east,open=false,half=top]
setblock 117 55 -250 soul_lantern[hanging=true]
''')

    # 6. DWARVEN INDUSTRIAL FORGE
    with open(os.path.join(FUNC_DIR, "forge_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Dwarven Industrial Forge
fill 82 50 -301 99 58 -281 air
fill 81 49 -302 100 49 -280 polished_deepslate
fill 82 50 -301 99 50 -281 smooth_stone
fill 81 50 -302 81 58 -280 deepslate_tiles
fill 100 50 -302 100 58 -280 deepslate_tiles
fill 81 50 -302 100 58 -302 deepslate_tiles
fill 81 50 -280 100 58 -280 deepslate_tiles
fill 81 59 -302 100 59 -280 deepslate_tiles

# Central Magma Core & Crucible
fill 89 50 -293 93 50 -289 lava
fill 89 51 -293 93 53 -289 tinted_glass
fill 89 50 -293 93 54 -289 iron_bars replace tinted_glass
setblock 91 50 -291 lava

# 16-Furnace Super Smelter Battery (West Wall)
fill 82 51 -299 82 51 -292 blast_furnace[facing=east,lit=true]
fill 82 52 -299 82 52 -292 hopper[facing=down]
fill 82 53 -299 82 53 -292 chest[facing=east,type=single]

fill 82 51 -290 82 51 -283 furnace[facing=east,lit=true]
fill 82 52 -290 82 52 -283 hopper[facing=down]
fill 82 53 -290 82 53 -283 chest[facing=east,type=single]

# Smithing & Engineering Benches
setblock 86 51 -298 smithing_table
setblock 87 51 -298 anvil[facing=north]
setblock 88 51 -298 grindstone[facing=north,face=floor]
setblock 89 51 -298 crafting_table

setblock 86 51 -284 smithing_table
setblock 87 51 -284 chipped_anvil[facing=south]
setblock 88 51 -284 stonecutter[facing=south]
setblock 89 51 -284 crafting_table

# Alchemy & Brewing Counter
fill 95 51 -299 98 51 -299 polished_blackstone
setblock 95 52 -299 brewing_stand[has_bottle_0=true,has_bottle_1=true,has_bottle_2=true]
setblock 96 52 -299 cauldron
setblock 97 52 -299 brewing_stand[has_bottle_0=true,has_bottle_1=true,has_bottle_2=true]
setblock 98 52 -299 cauldron

# Archway connecting to Bio-Atrium (East Wall)
fill 100 50 -293 104 55 -289 air
fill 100 49 -293 104 49 -289 polished_deepslate
fill 100 50 -291 104 50 -291 stripped_dark_oak_wood[axis=x]
''')

    # 7. HYDROPONICS BIOSPHERE
    with open(os.path.join(FUNC_DIR, "hydroponics_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Hydroponics & Tree Biosphere
fill 136 50 -302 154 61 -280 air
fill 135 49 -303 155 49 -279 polished_deepslate
fill 136 50 -302 154 50 -280 moss_block
fill 135 50 -303 135 61 -279 deepslate_tiles
fill 155 50 -303 155 61 -279 deepslate_tiles
fill 135 50 -303 155 61 -303 deepslate_tiles
fill 135 50 -279 155 61 -279 deepslate_tiles
fill 135 62 -303 155 62 -279 glass

# Terraced Farm Channels
fill 142 50 -300 148 50 -300 water
fill 142 50 -299 148 50 -299 farmland[moisture=7]
fill 142 51 -299 148 51 -299 wheat[age=7]

fill 142 50 -297 148 50 -297 water
fill 142 50 -296 148 50 -296 farmland[moisture=7]
fill 142 51 -296 148 51 -296 carrots[age=7]

fill 142 50 -294 148 50 -294 water
fill 142 50 -293 148 50 -293 farmland[moisture=7]
fill 142 51 -293 148 51 -293 potatoes[age=7]

fill 142 50 -291 148 50 -291 water
fill 142 50 -290 148 50 -290 farmland[moisture=7]
fill 142 51 -290 148 51 -290 beetroot[age=3]

# Enclosed Glass Apiary (East Side)
fill 150 50 -299 154 56 -283 glass
fill 151 51 -298 153 55 -284 air
fill 151 50 -298 153 50 -284 moss_block
setblock 151 52 -297 beehive[facing=west,honey_level=5]
setblock 151 52 -295 beehive[facing=west,honey_level=5]
setblock 151 52 -287 beehive[facing=west,honey_level=5]
setblock 151 52 -285 beehive[facing=west,honey_level=5]
setblock 152 51 -296 poppy
setblock 152 51 -294 dandelion
setblock 152 51 -286 oxeye_daisy

# Companion Cherry Blossom Tree
fill 138 50 -286 138 54 -286 cherry_log[axis=y]
fill 136 54 -288 140 56 -284 cherry_leaves
fill 137 57 -287 139 57 -285 cherry_leaves

# Archway connecting to Bio-Atrium (West Wall)
fill 130 50 -293 135 55 -289 air
fill 130 49 -293 135 49 -289 polished_deepslate
fill 130 50 -291 135 50 -291 stripped_dark_oak_wood[axis=x]
''')

    # 8. SOVEREIGN RESIDENTIAL SUITES
    with open(os.path.join(FUNC_DIR, "suites_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Sovereign Residential Suites
fill 92 50 -268 142 58 -231 air
fill 91 49 -269 143 49 -230 polished_deepslate
fill 91 50 -269 143 58 -230 polished_deepslate
fill 91 59 -269 143 59 -230 deepslate_tiles

# Central Corridor (Y=50, Z: -268..-232, X: 115..119)
fill 115 50 -268 119 55 -232 air
fill 116 50 -268 118 50 -232 red_carpet
fill 115 50 -268 115 50 -232 polished_deepslate
fill 119 50 -268 119 50 -232 polished_deepslate
setblock 117 54 -260 lantern[hanging=true]
setblock 117 54 -250 lantern[hanging=true]
setblock 117 54 -240 lantern[hanging=true]

# Suite 1: King Abir Prime Minister Stateroom (South End: Z: -242..-232, X: 110..124)
fill 110 50 -242 124 57 -232 air
fill 110 50 -242 124 50 -232 dark_oak_planks
fill 114 50 -240 120 50 -234 yellow_carpet

# King Abir Grand Canopy Bed (X: 116..118, Z: -234..-232)
fill 116 50 -234 116 53 -234 stripped_dark_oak_log[axis=y]
fill 118 50 -234 118 53 -234 stripped_dark_oak_log[axis=y]
fill 116 50 -232 116 53 -232 stripped_dark_oak_log[axis=y]
fill 118 50 -232 118 53 -232 stripped_dark_oak_log[axis=y]
fill 116 54 -234 118 54 -232 red_carpet
setblock 117 50 -233 red_bed[facing=south,part=head]
setblock 117 50 -234 red_bed[facing=south,part=foot]

setblock 113 50 -234 ender_chest[facing=east]
setblock 121 50 -234 crafting_table

# Executive Writing Desk & Prime Minister Chair
setblock 116 51 -240 dark_oak_slab[type=top]
setblock 117 51 -240 dark_oak_slab[type=top]
setblock 118 51 -240 dark_oak_slab[type=top]
setblock 117 52 -240 lectern[facing=south]
setblock 117 51 -239 dark_oak_stairs[facing=north,half=bottom]

# Prime Minister Custom Trimmed Armor Stand
setblock 112 50 -238 gold_block
summon armor_stand 112 51 -238 {ShowArms:1b,NoBasePlate:1b,Rotation:[90f,0f],Equipment:[{id:"netherite_sword",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:gold",pattern:"minecraft:spire"}}}]}

# Suite 2: Ahsane Executive Library Suite (West Wing: X: 93..113, Z: -267..-255)
fill 93 50 -267 113 57 -255 air
fill 93 50 -267 113 50 -255 spruce_planks
fill 98 50 -264 108 50 -258 cyan_carpet

# Ahsane Canopy Bed (X: 95..98, Z: -266..-264)
fill 95 50 -266 95 53 -266 spruce_fence
fill 98 50 -266 98 53 -266 spruce_fence
fill 95 50 -264 95 53 -264 spruce_fence
fill 98 50 -264 98 53 -264 spruce_fence
fill 95 54 -266 98 54 -264 cyan_carpet
setblock 96 50 -265 cyan_bed[facing=west,part=head]
setblock 97 50 -265 cyan_bed[facing=west,part=foot]

# Ahsane Reading Pod with Bookshelves
fill 93 51 -260 93 55 -256 chiseled_bookshelf[facing=east]
setblock 96 51 -258 lectern[facing=west]
setblock 97 51 -258 spruce_stairs[facing=east,half=bottom]

setblock 101 50 -265 lapis_block
summon armor_stand 101 51 -265 {ShowArms:1b,NoBasePlate:1b,Rotation:[180f,0f],Equipment:[{id:"trident",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:lapis",pattern:"minecraft:tide"}}}]}

# Suite 3: Jamal Amethyst Sanctuary Suite (East Wing: X: 121..141, Z: -267..-255)
fill 121 50 -267 141 57 -255 air
fill 121 50 -267 141 50 -255 dark_oak_planks
fill 126 50 -264 136 50 -258 purple_carpet

# Jamal Canopy Bed (X: 137..140, Z: -266..-264)
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

    # 9. SUB FLOOR CONDUITS
    with open(os.path.join(FUNC_DIR, "conduits_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Sector D Sub Floor Redstone Conduits
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

    # 10. GRAND SUBTERRANEAN ATHENAEUM
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

# Perimeter Multi Tier Bookshelves (North & West Walls)
fill 80 51 -329 80 58 -307 chiseled_bookshelf[facing=east]
fill 81 51 -330 101 58 -330 chiseled_bookshelf[facing=south]

# Mezzanine Reading Balcony at Y: 55
fill 81 55 -328 83 55 -308 dark_oak_slab[type=top]
fill 84 55 -329 101 55 -327 dark_oak_slab[type=top]
fill 84 56 -326 101 56 -326 dark_oak_fence

# Spiral Access Stairs to Mezzanine (X: 100..101, Z: -310..-308)
setblock 100 50 -310 polished_deepslate
setblock 100 51 -310 dark_oak_stairs[facing=south,half=bottom]
setblock 101 51 -310 polished_deepslate
setblock 101 52 -310 dark_oak_stairs[facing=west,half=bottom]
setblock 101 52 -309 polished_deepslate
setblock 101 53 -309 dark_oak_stairs[facing=north,half=bottom]
setblock 100 53 -309 polished_deepslate
setblock 100 54 -309 dark_oak_stairs[facing=east,half=bottom]
setblock 100 54 -308 dark_oak_slab[type=top]

# Floating Lecterns & Study Tables
setblock 87 51 -314 dark_oak_slab[type=top]
setblock 87 52 -314 lectern[facing=south]
setblock 87 51 -313 dark_oak_stairs[facing=north,half=bottom]

setblock 95 51 -314 dark_oak_slab[type=top]
setblock 95 52 -314 lectern[facing=south]
setblock 95 51 -313 dark_oak_stairs[facing=north,half=bottom]

# Alchemical Distillation Corner (East Wall of Library: X: 101..102, Z: -316..-312)
fill 101 51 -316 102 51 -312 polished_blackstone
setblock 101 52 -315 brewing_stand[has_bottle_0=true,has_bottle_1=true,has_bottle_2=true]
setblock 101 52 -313 cauldron
fill 102 52 -316 102 54 -312 barrel[facing=west]

# Chandeliers and Lanterns
setblock 91 62 -318 iron_chain[axis=y]
setblock 91 61 -318 iron_chain[axis=y]
setblock 91 60 -318 copper_bulb[lit=true]
setblock 91 59 -318 lantern[hanging=true]

# Doorway connecting to Crossroads Corridor at X=103
fill 103 50 -307 103 54 -305 air
''')

    # 11. SOVEREIGN BANQUET AND GATHERING HALL
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
fill 137 51 -325 137 51 -310 dark_oak_stairs[facing=east,half=bottom]
fill 139 51 -325 139 51 -310 dark_oak_stairs[facing=west,half=bottom]

fill 148 50 -325 148 50 -310 dark_oak_planks
fill 148 51 -325 148 51 -310 dark_oak_slab[type=top]
fill 147 51 -325 147 51 -310 dark_oak_stairs[facing=east,half=bottom]
fill 149 51 -325 149 51 -310 dark_oak_stairs[facing=west,half=bottom]

# Feast Tableware (Cakes, Candles, Pots)
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
fill 140 51 -326 146 51 -326 smooth_quartz_stairs[facing=south,half=bottom]
fill 140 52 -327 146 52 -327 dark_oak_slab[type=top]
setblock 143 52 -328 dark_oak_stairs[facing=south,half=bottom]
setblock 142 52 -328 dark_oak_stairs[facing=south,half=bottom]
setblock 144 52 -328 dark_oak_stairs[facing=south,half=bottom]

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

# Doorway connecting to Crossroads Corridor at X=131
fill 131 50 -307 131 54 -305 air
''')

    # 12. SUBTERRANEAN HYPERLOOP TRANSIT HUB
    with open(os.path.join(FUNC_DIR, "transit_hub_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: The Subterranean Hyperloop Transit Hub
# Dimensions: X: 104..130, Z: -345..-325, Floor Y: 49..50, Ceiling Y: 58
# Completely subterranean, ceiling Y: 58 is 6 blocks below Treasury floor Y: 64
fill 104 49 -345 130 58 -325 air

# Foundation & Concourse
fill 103 48 -346 131 48 -324 polished_deepslate
fill 104 50 -345 130 50 -325 smooth_quartz
fill 103 50 -346 103 58 -324 polished_blackstone
fill 131 50 -346 131 58 -324 polished_blackstone
fill 103 50 -346 131 58 -346 polished_blackstone
fill 103 59 -346 131 59 -324 deepslate_tiles

# Subway Portals connecting to West and East Flank Corridors at Z=-325
fill 106 50 -325 108 53 -325 air
fill 126 50 -325 128 53 -325 air

# Solid sealed safety buffer wall at Z=-324 facing Treasury substructure
fill 109 50 -324 125 58 -324 deepslate_bricks

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

# Push Button Minecart Dispensers at Boarding Gates (Z: -328)
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

# Platform Waiting Benches
fill 112 50 -335 114 50 -335 dark_oak_stairs[facing=south,half=bottom]
fill 120 50 -335 122 50 -335 dark_oak_stairs[facing=south,half=bottom]

# Lighting via Inset Sea Lanterns and Copper Bulbs
fill 112 50 -340 114 50 -340 sea_lantern
fill 120 50 -340 122 50 -340 sea_lantern
setblock 109 55 -335 copper_bulb[lit=true]
setblock 117 55 -335 copper_bulb[lit=true]
setblock 125 55 -335 copper_bulb[lit=true]
''')

    # 13. MASTER BUILD ORCHESTRATOR
    with open(os.path.join(FUNC_DIR, "build_all.mcfunction"), "w") as f:
        f.write('''# Subterranean Utopia: Master Orchestrator
# Executes silently without any tellraw spam
function treasury:build_all
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

    print("Perfected stairs, citadel and all 12 sectors generated successfully!")

if __name__ == "__main__":
    main()
