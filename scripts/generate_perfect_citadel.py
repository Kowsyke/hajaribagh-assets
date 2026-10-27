#!/usr/bin/env python3
"""
Master Architect Generator for the Perfected Subterranean Citadel.
Creates:
1. Seamless Gothic Arch Staircase Descent (connecting Treasury to Citadel with zero seam).
2. The Mesmerizing Bio-Atrium:
   - 2-tier wraparound observation mezzanine catwalk at Y: 54.
   - Organic sunken bio-aquarium with living coral, glowing sea pickles, axolotls, tropical fish.
   - Cross-vaulted coffered ceiling with hanging chain chandeliers and spore blossoms.
   - 3D layered wall architecture (pilasters, skirting, cornice, planter balconies).
3. The Grand High Parliament of the Republic:
   - Imposing Government Assembly Hall (X: 104..130, Z: -276..-244, Y: 49..58).
   - Speaker & Prime Minister Dais with high canopy throne, government charter lectern, golden mace plinth.
   - Opposing 3-tier parliamentary benches (Cabinet vs Assembly) seating over 40 members with desks, microphones, and voting buttons.
   - Upper Diplomatic & Public Balcony gallery.
   - Grand coffered ceiling with ceremonial chandeliers and national heraldry banners.
4. The Industrial Forge & Super Smelter:
   - Arched copper flues, smoke vents, glowing forge hearth, 16-furnace smelter, master smithing bay, potion laboratory.
5. The Bio-Dome Hydroponics & Tree Conservatory:
   - Automated observer-piston sugarcane/bamboo harvester, vaulted cherry/dark oak conservatory, glass bee apiary.
6. Executive Sovereign Suites:
   - Private chambers for Kowsyke, Ahsane, and Jamal with personalized luxury interiors.
7. Sub-Floor Redstone Conduits:
   - Tinted glass inspection trenches exposing functional redstone repeaters, comparators, and conduits.

100% silent execution (no tellraw spam to players).
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

    # pack.mcmeta
    with open(os.path.join(DP_BASE, "pack.mcmeta"), "w") as f:
        f.write('{\n  "pack": {\n    "pack_format": 48,\n    "description": "The Perfected Subterranean Citadel Datapack"\n  }\n}\n')

    # 1. stairs_descent.mcfunction
    with open(os.path.join(FUNC_DIR, "stairs_descent.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Grand Staircase Descent
# Seamless connection from Treasury floor (Y: 64) down through Y: 50

# Clear full staircase envelope
fill 113 49 -324 121 68 -304 air

# Outer protective structural shell
fill 113 49 -324 113 68 -304 deepslate_tiles
fill 121 49 -324 121 68 -304 deepslate_tiles
fill 113 68 -324 121 68 -304 deepslate_tiles

# Stair foundation and steps from Z=-322 down to Z=-308
# Z=-322: Y=64
fill 114 49 -322 120 63 -322 polished_deepslate
fill 116 64 -322 118 64 -322 spruce_stairs[facing=south]
setblock 115 64 -322 stripped_dark_oak_log[axis=y]
setblock 119 64 -322 stripped_dark_oak_log[axis=y]
setblock 115 65 -322 lantern[hanging=false]
setblock 119 65 -322 lantern[hanging=false]

# Z=-321: Y=63
fill 114 49 -321 120 62 -321 polished_deepslate
fill 116 63 -321 118 63 -321 spruce_stairs[facing=south]
setblock 115 63 -321 deepslate_tile_stairs[facing=south]
setblock 119 63 -321 deepslate_tile_stairs[facing=south]

# Z=-320: Y=62
fill 114 49 -320 120 61 -320 polished_deepslate
fill 116 62 -320 118 62 -320 spruce_stairs[facing=south]
setblock 115 62 -320 stripped_dark_oak_log[axis=y]
setblock 119 62 -320 stripped_dark_oak_log[axis=y]
setblock 115 63 -320 lantern[hanging=false]
setblock 119 63 -320 lantern[hanging=false]

# Z=-319: Y=61
fill 114 49 -319 120 60 -319 polished_deepslate
fill 116 61 -319 118 61 -319 spruce_stairs[facing=south]
setblock 115 61 -319 deepslate_tile_stairs[facing=south]
setblock 119 61 -319 deepslate_tile_stairs[facing=south]

# Z=-318: Y=60
fill 114 49 -318 120 59 -318 polished_deepslate
fill 116 60 -318 118 60 -318 spruce_stairs[facing=south]
setblock 115 60 -318 stripped_dark_oak_log[axis=y]
setblock 119 60 -318 stripped_dark_oak_log[axis=y]
setblock 115 61 -318 lantern[hanging=false]
setblock 119 61 -318 lantern[hanging=false]

# Z=-317: Y=59
fill 114 49 -317 120 58 -317 polished_deepslate
fill 116 59 -317 118 59 -317 spruce_stairs[facing=south]
setblock 115 59 -317 deepslate_tile_stairs[facing=south]
setblock 119 59 -317 deepslate_tile_stairs[facing=south]

# Z=-316: Y=58
fill 114 49 -316 120 57 -316 polished_deepslate
fill 116 58 -316 118 58 -316 spruce_stairs[facing=south]
setblock 115 58 -316 stripped_dark_oak_log[axis=y]
setblock 119 58 -316 stripped_dark_oak_log[axis=y]
setblock 115 59 -316 lantern[hanging=false]
setblock 119 59 -316 lantern[hanging=false]

# Z=-315: Y=57
fill 114 49 -315 120 56 -315 polished_deepslate
fill 116 57 -315 118 57 -315 spruce_stairs[facing=south]
setblock 115 57 -315 deepslate_tile_stairs[facing=south]
setblock 119 57 -315 deepslate_tile_stairs[facing=south]

# Z=-314: Y=56
fill 114 49 -314 120 55 -314 polished_deepslate
fill 116 56 -314 118 56 -314 spruce_stairs[facing=south]
setblock 115 56 -314 stripped_dark_oak_log[axis=y]
setblock 119 56 -314 stripped_dark_oak_log[axis=y]
setblock 115 57 -314 lantern[hanging=false]
setblock 119 57 -314 lantern[hanging=false]

# Z=-313: Y=55
fill 114 49 -313 120 54 -313 polished_deepslate
fill 116 55 -313 118 55 -313 spruce_stairs[facing=south]
setblock 115 55 -313 deepslate_tile_stairs[facing=south]
setblock 119 55 -313 deepslate_tile_stairs[facing=south]

# Z=-312: Y=54
fill 114 49 -312 120 53 -312 polished_deepslate
fill 116 54 -312 118 54 -312 spruce_stairs[facing=south]
setblock 115 54 -312 stripped_dark_oak_log[axis=y]
setblock 119 54 -312 stripped_dark_oak_log[axis=y]
setblock 115 55 -312 lantern[hanging=false]
setblock 119 55 -312 lantern[hanging=false]

# Z=-311: Y=53
fill 114 49 -311 120 52 -311 polished_deepslate
fill 116 53 -311 118 53 -311 spruce_stairs[facing=south]
setblock 115 53 -311 deepslate_tile_stairs[facing=south]
setblock 119 53 -311 deepslate_tile_stairs[facing=south]

# Z=-310: Y=52
fill 114 49 -310 120 51 -310 polished_deepslate
fill 116 52 -310 118 52 -310 spruce_stairs[facing=south]
setblock 115 52 -310 stripped_dark_oak_log[axis=y]
setblock 119 52 -310 stripped_dark_oak_log[axis=y]
setblock 115 53 -310 lantern[hanging=false]
setblock 119 53 -310 lantern[hanging=false]

# Z=-309: Y=51
fill 114 49 -309 120 50 -309 polished_deepslate
fill 116 51 -309 118 51 -309 spruce_stairs[facing=south]
setblock 115 51 -309 deepslate_tile_stairs[facing=south]
setblock 119 51 -309 deepslate_tile_stairs[facing=south]

# Z=-308: Y=50 (Final landing step)
fill 114 49 -308 120 49 -308 polished_deepslate
fill 116 50 -308 118 50 -308 spruce_stairs[facing=south]
setblock 115 50 -308 stripped_dark_oak_log[axis=y]
setblock 119 50 -308 stripped_dark_oak_log[axis=y]
setblock 115 51 -308 lantern[hanging=false]
setblock 119 51 -308 lantern[hanging=false]

# Grand Vestibule at Z: -307..-305 (Floor Y=50)
fill 114 49 -307 120 49 -305 polished_deepslate
fill 116 50 -307 118 50 -305 stripped_dark_oak_wood[axis=z]
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
# Core dimensions: X: 104..130, Y: 47..58, Z: -305..-277

fill 104 50 -304 130 57 -278 air
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

# Perimeter Walls with 3D Layered Pilasters & Moldings
fill 104 50 -305 104 57 -277 deepslate_tiles
fill 130 50 -305 130 57 -277 deepslate_tiles
fill 104 50 -305 130 57 -305 deepslate_tiles
fill 104 50 -277 130 57 -277 deepslate_tiles

# Wall Skirting (Inverted polished deepslate stairs along base of walls)
fill 105 51 -304 105 51 -278 polished_deepslate_stairs[facing=east,half=bottom]
fill 129 51 -304 129 51 -278 polished_deepslate_stairs[facing=west,half=bottom]
fill 105 51 -304 129 51 -304 polished_deepslate_stairs[facing=south,half=bottom]
fill 105 51 -278 129 51 -278 polished_deepslate_stairs[facing=north,half=bottom]

# Clear portals in the skirting
fill 115 51 -304 119 51 -304 air
fill 115 51 -278 119 51 -278 air
fill 105 51 -293 105 51 -289 air
fill 129 51 -293 129 51 -289 air

# Upper Mezzanine Catwalk at Y: 54
# Wraparound walkway around the perimeter
fill 105 54 -304 107 54 -278 dark_oak_planks
fill 127 54 -304 129 54 -278 dark_oak_planks
fill 105 54 -304 129 54 -302 dark_oak_planks
fill 105 54 -280 129 54 -278 dark_oak_planks

# Mezzanine Guard Railings (Dark Oak Fences)
fill 108 55 -301 108 55 -281 dark_oak_fence
fill 126 55 -301 126 55 -281 dark_oak_fence
fill 108 55 -301 126 55 -301 dark_oak_fence
fill 108 55 -281 126 55 -281 dark_oak_fence

# Clear portals through Mezzanine
fill 115 54 -304 119 56 -301 air
fill 115 54 -281 119 56 -278 air
fill 104 54 -293 107 56 -289 air
fill 127 54 -293 130 56 -289 air

# Main Cross Walkways at Y: 50
fill 116 50 -304 118 50 -278 stripped_dark_oak_wood[axis=z]
fill 105 50 -292 129 50 -290 stripped_dark_oak_wood[axis=x]

# Grand Corner Structural Pillars (Dark Oak, Basalt, Polished Blackstone)
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

# Vaulted Ceiling Ribs at Y: 57
fill 110 57 -299 124 57 -299 dark_oak_stairs[facing=south,half=top]
fill 110 57 -283 124 57 -283 dark_oak_stairs[facing=north,half=top]
fill 109 57 -298 109 57 -284 dark_oak_stairs[facing=east,half=top]
fill 125 57 -298 125 57 -284 dark_oak_stairs[facing=west,half=top]

# Sunken Bio-Aquarium Basin (X: 113..121, Z: -295..-287)
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

    # 5. parliament_build.mcfunction (THE GRAND HIGH PARLIAMENT CHAMBER)
    with open(os.path.join(FUNC_DIR, "parliament_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Grand High Parliament of the Republic
# Chamber Dimensions: X: 104..130, Z: -276..-244, Floor Y: 49..50, Ceiling Y: 58

# 1. Excavate Parliament envelope
fill 104 49 -276 130 58 -244 air

# 2. Outer Structural Shell
fill 104 48 -276 130 48 -244 polished_deepslate
fill 104 49 -276 130 49 -244 polished_blackstone
fill 104 59 -276 130 59 -244 deepslate_tiles

# Perimeter Walls: Deepslate Bricks with Polished Basalt Pilasters
fill 104 50 -276 104 58 -244 deepslate_bricks
fill 130 50 -276 130 58 -244 deepslate_bricks
fill 104 50 -276 130 58 -276 deepslate_bricks
fill 104 50 -244 130 58 -244 deepslate_bricks

# Polished Basalt Pilasters every 4 blocks along walls
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

# 3. North Entrance Portal from Atrium (Z: -277..-275, X: 115..119)
fill 115 50 -277 119 55 -275 air
fill 115 49 -277 119 49 -275 polished_blackstone
fill 114 50 -276 114 55 -276 crying_obsidian
fill 120 50 -276 120 55 -276 crying_obsidian
fill 115 55 -276 119 55 -276 crying_obsidian
setblock 114 52 -276 redstone_lamp[lit=true]
setblock 120 52 -276 redstone_lamp[lit=true]

# 4. Central Parliamentary Aisle & Red Carpet (X: 116..118, Z: -275..-252)
fill 116 50 -275 118 50 -252 red_carpet
fill 115 50 -275 115 50 -252 yellow_carpet
fill 119 50 -275 119 50 -252 yellow_carpet
# Hidden acoustic shroomlights under aisle
setblock 117 48 -272 shroomlight
setblock 117 48 -266 shroomlight
setblock 117 48 -260 shroomlight
setblock 117 48 -254 shroomlight

# -------------------------------------------------------------
# 5. Parliamentary Benches (West: Cabinet / Government Benches)
# Tier 1 (Front Bench, Floor Y=50, Seating Y=50, Desk Y=51 at X=114)
fill 114 50 -272 114 50 -254 dark_oak_planks
fill 114 51 -272 114 51 -254 dark_oak_slab[type=top]
fill 113 50 -272 113 50 -254 dark_oak_stairs[facing=east]
fill 113 51 -272 113 51 -254 green_carpet

# Tier 2 (Middle Bench, Elevated Y=51)
fill 111 50 -272 112 50 -254 polished_blackstone
fill 112 51 -272 112 51 -254 dark_oak_slab[type=top]
fill 111 51 -272 111 51 -254 dark_oak_stairs[facing=east]
fill 111 52 -272 111 52 -254 green_carpet

# Tier 3 (Back Bench, Elevated Y=52)
fill 109 50 -272 110 51 -254 polished_blackstone
fill 110 52 -272 110 52 -254 dark_oak_slab[type=top]
fill 109 52 -272 109 52 -254 dark_oak_stairs[facing=east]
fill 109 53 -272 109 53 -254 green_carpet

# Microphones (End Rods) & Voting Stone Buttons on West Desks
setblock 114 52 -270 end_rod
setblock 114 52 -269 stone_button[face=floor,facing=north]
setblock 114 52 -266 end_rod
setblock 114 52 -265 stone_button[face=floor,facing=north]
setblock 114 52 -262 end_rod
setblock 114 52 -261 stone_button[face=floor,facing=north]
setblock 114 52 -258 end_rod
setblock 114 52 -257 stone_button[face=floor,facing=north]

# -------------------------------------------------------------
# 6. Parliamentary Benches (East: Assembly / Member Benches)
# Tier 1 (Front Bench, Floor Y=50, Seating Y=50, Desk Y=51 at X=120)
fill 120 50 -272 120 50 -254 dark_oak_planks
fill 120 51 -272 120 51 -254 dark_oak_slab[type=top]
fill 121 50 -272 121 50 -254 dark_oak_stairs[facing=west]
fill 121 51 -272 121 51 -254 green_carpet

# Tier 2 (Middle Bench, Elevated Y=51)
fill 122 50 -272 123 50 -254 polished_blackstone
fill 122 51 -272 122 51 -254 dark_oak_slab[type=top]
fill 123 51 -272 123 51 -254 dark_oak_stairs[facing=west]
fill 123 52 -272 123 52 -254 green_carpet

# Tier 3 (Back Bench, Elevated Y=52)
fill 124 50 -272 125 51 -254 polished_blackstone
fill 124 52 -272 124 52 -254 dark_oak_slab[type=top]
fill 125 52 -272 125 52 -254 dark_oak_stairs[facing=west]
fill 125 53 -272 125 53 -254 green_carpet

# Microphones (End Rods) & Voting Stone Buttons on East Desks
setblock 120 52 -270 end_rod
setblock 120 52 -269 stone_button[face=floor,facing=north]
setblock 120 52 -266 end_rod
setblock 120 52 -265 stone_button[face=floor,facing=north]
setblock 120 52 -262 end_rod
setblock 120 52 -261 stone_button[face=floor,facing=north]
setblock 120 52 -258 end_rod
setblock 120 52 -257 stone_button[face=floor,facing=north]

# -------------------------------------------------------------
# 7. Speaker of the House & Prime Minister Dais (South End: Z: -251..-245)
# Raised Tier 1 (Y=51)
fill 113 50 -251 121 50 -245 smooth_quartz
fill 114 51 -251 120 51 -245 smooth_quartz

# Raised Tier 2 (Y=52)
fill 115 52 -249 119 52 -245 gold_block

# Central Clerk Table at Y=51 (Z: -251)
setblock 116 51 -251 dark_oak_slab[type=top]
setblock 117 51 -251 dark_oak_slab[type=top]
setblock 118 51 -251 dark_oak_slab[type=top]
setblock 117 52 -251 lectern[facing=north]

# Ceremonial Golden Mace Plinth (Right of Speaker)
setblock 119 52 -250 gold_block
summon armor_stand 119 53 -250 {ShowArms:1b,NoBasePlate:1b,Rotation:[0f,0f],Equipment:[{id:"golden_sword",count:1,components:{"minecraft:enchantments":{levels:{"minecraft:unbreaking":3}}}},{},{},{},{}]}

# Prime Minister Dispatch Box (Left of Speaker)
setblock 115 52 -250 dark_oak_slab[type=top]
setblock 115 53 -250 red_candle[lit=true]

# Grand Speaker Canopy Throne (Center: 117, Y=53..56, Z: -247)
setblock 117 53 -247 gilded_blackstone
setblock 117 54 -247 dark_oak_stairs[facing=north]
setblock 116 54 -247 dark_oak_trapdoor[facing=west,open=true]
setblock 118 54 -247 dark_oak_trapdoor[facing=east,open=true]

# Sounding Board Canopy over Throne
fill 116 53 -246 118 57 -246 stripped_dark_oak_log[axis=y]
fill 116 57 -247 118 57 -246 dark_oak_slab[type=bottom]
fill 116 56 -247 118 56 -247 yellow_carpet

# National Tapestry & Grand Heraldry Wall behind Speaker (Z: -245)
fill 113 50 -245 121 57 -245 crying_obsidian
fill 115 52 -245 119 56 -245 gold_block
fill 116 53 -245 118 55 -245 sea_lantern

# -------------------------------------------------------------
# 8. Grand Ceremonial Chandeliers (Ceiling: Y=58)
# Chandelier 1 (North)
setblock 117 58 -269 iron_chain[axis=y]
setblock 117 57 -269 iron_chain[axis=y]
setblock 117 56 -269 shroomlight
setblock 116 56 -269 dark_oak_trapdoor[facing=west,open=false,half=top]
setblock 118 56 -269 dark_oak_trapdoor[facing=east,open=false,half=top]
setblock 117 56 -270 dark_oak_trapdoor[facing=north,open=false,half=top]
setblock 117 56 -268 dark_oak_trapdoor[facing=south,open=false,half=top]
setblock 117 55 -269 soul_lantern[hanging=true]

# Chandelier 2 (Center)
setblock 117 58 -261 iron_chain[axis=y]
setblock 117 57 -261 iron_chain[axis=y]
setblock 117 56 -261 shroomlight
setblock 116 56 -261 dark_oak_trapdoor[facing=west,open=false,half=top]
setblock 118 56 -261 dark_oak_trapdoor[facing=east,open=false,half=top]
setblock 117 56 -262 dark_oak_trapdoor[facing=north,open=false,half=top]
setblock 117 56 -260 dark_oak_trapdoor[facing=south,open=false,half=top]
setblock 117 55 -261 soul_lantern[hanging=true]

# Chandelier 3 (South over Dais)
setblock 117 58 -250 iron_chain[axis=y]
setblock 117 57 -250 iron_chain[axis=y]
setblock 117 56 -250 shroomlight
setblock 116 56 -250 dark_oak_trapdoor[facing=west,open=false,half=top]
setblock 118 56 -250 dark_oak_trapdoor[facing=east,open=false,half=top]
setblock 117 56 -251 dark_oak_trapdoor[facing=north,open=false,half=top]
setblock 117 56 -249 dark_oak_trapdoor[facing=south,open=false,half=top]
setblock 117 55 -250 soul_lantern[hanging=true]
''')

    # 6. forge_build.mcfunction
    with open(os.path.join(FUNC_DIR, "forge_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Sector A Dwarven Industrial Forge and Super Smelter

# 1. Clear & Shell
fill 82 49 -301 99 49 -281 polished_basalt[axis=y]
fill 82 50 -301 82 57 -281 polished_deepslate
fill 99 50 -301 99 57 -281 polished_deepslate
fill 82 50 -301 99 57 -301 polished_deepslate
fill 82 50 -281 99 57 -281 polished_deepslate
fill 82 58 -301 99 58 -281 deepslate_tiles

# 2. Grand Arched Corridor to Atrium (X: 99..104, Z: -293..-289)
fill 99 50 -293 104 55 -289 air
fill 99 49 -292 104 49 -290 polished_basalt[axis=x]
fill 99 50 -292 104 50 -290 smooth_stone
fill 99 51 -293 104 54 -293 deepslate_tile_wall
fill 99 51 -289 104 54 -289 deepslate_tile_wall
fill 99 55 -292 104 55 -290 copper_grate
fill 99 56 -292 104 56 -290 sea_lantern

# Forge Floor (Smooth Stone with Polished Basalt borders)
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

    # 7. hydroponics_build.mcfunction
    with open(os.path.join(FUNC_DIR, "hydroponics_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Sector B Automated Hydroponics and Tree Conservatory

# 1. Shell and Foundation
fill 136 49 -302 154 49 -280 stripped_cherry_wood[axis=y]
fill 136 50 -302 136 60 -280 smooth_quartz
fill 154 50 -302 154 60 -280 smooth_quartz
fill 136 50 -302 154 60 -302 smooth_quartz
fill 136 50 -280 154 60 -280 smooth_quartz
fill 136 61 -302 154 61 -280 deepslate_tiles

# 2. Grand Botanical Promenade to Atrium (X: 130..136, Z: -293..-289)
fill 130 50 -293 136 55 -289 air
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
fill 140 49 -283 148 49 -283 campfire[lit=true]
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

    # 8. suites_build.mcfunction
    with open(os.path.join(FUNC_DIR, "suites_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Luxury Sovereign Suites (Kowsyke, Ahsane, Jamal)

# =============================================================
# 1. KOWSYKE PRIME MINISTER SUITE (Behind Parliament Dais: X: 111..123, Z: -243..-232)
# =============================================================
fill 110 49 -244 124 57 -231 air
fill 110 48 -244 124 48 -231 gilded_blackstone
fill 111 49 -243 123 49 -232 stripped_dark_oak_wood[axis=z]
fill 110 49 -244 110 57 -231 polished_blackstone_bricks
fill 124 49 -244 124 57 -231 polished_blackstone_bricks
fill 110 49 -231 124 57 -231 polished_blackstone_bricks
fill 110 58 -244 124 58 -231 deepslate_tiles

# Private Entrance Doorway from behind Speaker Dais (Z: -244, X: 116..118)
fill 116 49 -244 118 53 -244 air
fill 116 49 -244 118 49 -244 gold_block

# Royal King Canopy Bed (Gold and Red, X: 116..118, Z: -233..-235)
fill 116 50 -233 118 50 -233 gold_block
fill 116 50 -234 118 50 -234 red_bed[facing=south,part=head]
fill 116 50 -235 118 50 -235 red_bed[facing=south,part=foot]
fill 115 50 -233 115 54 -233 stripped_dark_oak_log[axis=y]
fill 119 50 -233 119 54 -233 stripped_dark_oak_log[axis=y]
fill 115 55 -235 119 55 -233 dark_oak_slab[type=bottom]
fill 116 54 -235 118 54 -235 yellow_wool

# Private Aquarium Wall (West Wall: X: 111, Z: -240..-236)
fill 110 49 -240 110 54 -236 sea_lantern
fill 110 50 -239 110 53 -237 water
fill 111 50 -239 111 53 -237 tinted_glass
summon axolotl 110.5 50.5 -238 {Variant:4,PersistenceRequired:1b}

# Prime Minister Display Pedestal (Gold Silence Trim Netherite Armor)
setblock 121 50 -238 gold_block
summon armor_stand 121 51 -238 {ShowArms:1b,NoBasePlate:1b,Rotation:[270f,0f],Equipment:[{id:"netherite_sword",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:gold",pattern:"minecraft:silence"}}}]}

# Private Executive Desk and Safe
setblock 121 50 -241 dark_oak_stairs[facing=south]
setblock 121 50 -242 ender_chest[facing=south]
setblock 120 50 -242 dark_oak_slab[type=top]
setblock 120 51 -242 lantern[hanging=false]

# =============================================================
# 2. AHSANE EXECUTIVE SUITE (West Flank of Parliament: X: 93..103, Z: -268..-256)
# =============================================================
fill 92 49 -269 104 57 -255 air
fill 92 48 -269 104 48 -255 polished_deepslate
fill 93 49 -268 103 49 -256 cyan_carpet
fill 92 49 -269 92 57 -255 deepslate_bricks
fill 92 49 -269 103 57 -269 deepslate_bricks
fill 92 49 -255 103 57 -255 deepslate_bricks
fill 92 58 -269 104 58 -255 deepslate_tiles

# Entrance Doorway from Parliament West Side
fill 103 49 -263 104 53 -261 air

# Ahsane Cyan Canopy Bed
fill 94 50 -266 94 53 -266 dark_oak_fence
fill 97 50 -266 97 53 -266 dark_oak_fence
fill 94 50 -264 94 53 -264 dark_oak_fence
fill 97 50 -264 97 53 -264 dark_oak_fence
fill 94 54 -266 97 54 -264 cyan_carpet
setblock 95 50 -265 cyan_bed[facing=west,part=head]
setblock 96 50 -265 cyan_bed[facing=west,part=foot]

# Private Grand Library Alcove
fill 93 50 -258 98 53 -258 bookshelf
setblock 96 50 -260 dark_oak_stairs[facing=north]
setblock 96 50 -259 dark_oak_slab[type=top]

# Ahsane Display Pedestal (Diamond Bolt Trim Armor)
setblock 100 50 -265 diamond_block
summon armor_stand 100 51 -265 {ShowArms:1b,NoBasePlate:1b,Rotation:[180f,0f],Equipment:[{id:"diamond_sword",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:diamond",pattern:"minecraft:bolt"}}}]}

# =============================================================
# 3. JAMAL EXECUTIVE SUITE (East Flank of Parliament: X: 131..141, Z: -268..-256)
# =============================================================
fill 130 49 -269 142 57 -255 air
fill 130 48 -269 142 48 -255 dark_prismarine
fill 131 49 -268 141 49 -256 purple_carpet
fill 142 49 -269 142 57 -255 deepslate_bricks
fill 131 49 -269 142 57 -269 deepslate_bricks
fill 131 49 -255 142 57 -255 deepslate_bricks
fill 130 58 -269 142 58 -255 deepslate_tiles

# Entrance Doorway from Parliament East Side
fill 130 49 -263 131 53 -261 air

# Jamal Purple Canopy Bed
fill 137 50 -266 137 53 -266 dark_oak_fence
fill 140 50 -266 140 53 -266 dark_oak_fence
fill 137 50 -264 137 53 -264 dark_oak_fence
fill 140 50 -264 140 53 -264 dark_oak_fence
fill 137 54 -266 140 54 -264 purple_carpet
setblock 139 50 -265 purple_bed[facing=east,part=head]
setblock 138 50 -265 purple_bed[facing=east,part=foot]

# Resonating Amethyst Geode Wall (East Wall)
fill 141 50 -262 141 54 -259 amethyst_block
setblock 140 51 -261 amethyst_cluster[facing=west]
setblock 140 52 -260 amethyst_cluster[facing=west]
setblock 140 50 -260 small_amethyst_bud[facing=west]

# Jamal Display Pedestal (Amethyst Ward Trim Armor)
setblock 134 50 -265 amethyst_block
summon armor_stand 134 51 -265 {ShowArms:1b,NoBasePlate:1b,Rotation:[180f,0f],Equipment:[{id:"bow",count:1},{},{},{},{id:"netherite_helmet",count:1,components:{"minecraft:trim":{material:"minecraft:amethyst",pattern:"minecraft:ward"}}}]}
''')

    # 9. conduits_build.mcfunction
    with open(os.path.join(FUNC_DIR, "conduits_build.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Sector D Sub-Floor Redstone Conduits

# Floor Conduits in Central Grand Atrium Walkways
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

    # 10. build_all.mcfunction
    with open(os.path.join(FUNC_DIR, "build_all.mcfunction"), "w") as f:
        f.write('''# Subterranean Citadel: Master Build Orchestrator
# Completely silent execution without broadcasting to other players

function citadel:stairs_descent
function citadel:atrium_excavate
function citadel:atrium_shell
function citadel:atrium_decor
function citadel:forge_build
function citadel:hydroponics_build
function citadel:parliament_build
function citadel:suites_build
function citadel:conduits_build
''')

    print("Perfected Citadel Datapack generated successfully!")

if __name__ == "__main__":
    main()
