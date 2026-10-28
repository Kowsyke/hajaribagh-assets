#!/usr/bin/env python3
"""Build Full Veteran Hivemind Bunker for King Abir.

Generates the complete 8-room veteran subterranean bunker.
Floor is at Y: 46, clear air is Y: 47..52 (6 blocks tall clear interior height),
ceiling is at Y: 53. Strictly obeys Y <= 53 ceiling cap.
Installs complete lighting grids to prevent mob spawning.
Writes native mcfunction files and executes them via RCON.
"""

import os
import subprocess
import sys

DEFAULT_HOST = os.environ.get("HZ_HOST", "132.226.135.26")
DEFAULT_USER = os.environ.get("HZ_USER", "ubuntu")
DEFAULT_KEY = os.environ.get("HZ_KEY", os.path.expanduser("~/.ssh/id_ed25519"))

FUNCTION_DIR = "datapacks/underground_citadel/data/citadel/function"

def write_mcfunction(name, lines):
    os.makedirs(FUNCTION_DIR, exist_ok=True)
    filepath = os.path.join(FUNCTION_DIR, name)
    clean_lines = [line.strip() for line in lines if line.strip()]
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(clean_lines) + "\n")
    return clean_lines

def build_rotunda():
    cmds = [
        "# Sector 0: Central Command Rotunda (X: 111..123, Z: -307..-295, Y: 46..53)",
        # Excavation
        "fill 111 46 -307 123 52 -295 air",
        # Ceiling
        "fill 111 53 -307 123 53 -295 deepslate_tiles",
        # Floor
        "fill 111 46 -307 123 46 -295 polished_deepslate",
        # Outer walls
        "fill 111 46 -307 123 52 -307 deepslate_tiles",
        "fill 111 46 -295 123 52 -295 deepslate_tiles",
        "fill 111 46 -307 111 52 -295 deepslate_tiles",
        "fill 123 46 -307 123 52 -295 deepslate_tiles",
        # Pilasters in corners
        "fill 111 46 -307 111 52 -307 chiseled_deepslate",
        "fill 123 46 -307 123 52 -307 chiseled_deepslate",
        "fill 111 46 -295 111 52 -295 chiseled_deepslate",
        "fill 123 46 -295 123 52 -295 chiseled_deepslate",
        # Central Compass Rose & Beacon Well
        "setblock 117 45 -301 sea_lantern",
        "setblock 117 46 -301 gold_block",
        "setblock 116 46 -301 polished_blackstone",
        "setblock 118 46 -301 polished_blackstone",
        "setblock 117 46 -300 polished_blackstone",
        "setblock 117 46 -302 polished_blackstone",
        # Grand Stair Transition from landing (Y: 50 down to 46)
        "fill 115 46 -307 119 50 -304 polished_deepslate",
        "fill 116 50 -307 118 50 -307 spruce_stairs[facing=north,half=bottom]",
        "fill 116 49 -306 118 49 -306 spruce_stairs[facing=north,half=bottom]",
        "fill 116 48 -305 118 48 -305 spruce_stairs[facing=north,half=bottom]",
        "fill 116 47 -304 118 47 -304 spruce_stairs[facing=north,half=bottom]",
        "fill 116 48 -307 118 52 -304 air",
        # Rotunda Chandelier Array
        "setblock 117 53 -301 copper_bulb[lit=true,powered=false]",
        "setblock 114 53 -301 copper_bulb[lit=true,powered=false]",
        "setblock 120 53 -301 copper_bulb[lit=true,powered=false]",
        "setblock 117 53 -298 copper_bulb[lit=true,powered=false]",
        "setblock 117 53 -304 copper_bulb[lit=true,powered=false]",
        "setblock 114 53 -298 copper_bulb[lit=true,powered=false]",
        "setblock 120 53 -298 copper_bulb[lit=true,powered=false]",
        "setblock 114 53 -304 copper_bulb[lit=true,powered=false]",
        "setblock 120 53 -304 copper_bulb[lit=true,powered=false]",
        # Hanging lanterns
        "setblock 117 52 -301 chain[axis=y]",
        "setblock 117 51 -301 soul_lantern[hanging=true]",
    ]
    return write_mcfunction("bunker_rotunda.mcfunction", cmds)

def build_corridors():
    cmds = [
        "# Arterial Corridors & Boulevard (Floor Y: 46, Clear Y: 47..52, Ceiling Y: 53)",
        # West Arterial Corridor to Tool Armory
        "fill 95 46 -302 110 52 -300 air",
        "fill 95 46 -302 110 46 -300 polished_deepslate",
        "fill 95 53 -302 110 53 -300 deepslate_tiles",
        "fill 95 46 -303 110 52 -303 deepslate_tiles",
        "fill 95 46 -299 110 52 -299 deepslate_tiles",
        "setblock 100 53 -301 copper_bulb[lit=true,powered=false]",
        "setblock 106 53 -301 copper_bulb[lit=true,powered=false]",

        # East Arterial Corridor to Arcane Library
        "fill 124 46 -302 139 52 -300 air",
        "fill 124 46 -302 139 46 -300 polished_deepslate",
        "fill 124 53 -302 139 53 -300 deepslate_tiles",
        "fill 124 46 -303 139 52 -303 deepslate_tiles",
        "fill 124 46 -299 139 52 -299 deepslate_tiles",
        "setblock 128 53 -301 copper_bulb[lit=true,powered=false]",
        "setblock 134 53 -301 copper_bulb[lit=true,powered=false]",

        # South Sovereign Boulevard
        "fill 116 46 -294 118 52 -262 air",
        "fill 116 46 -294 118 46 -262 polished_deepslate",
        "fill 116 53 -294 118 53 -262 deepslate_tiles",
        "fill 115 46 -294 115 52 -262 deepslate_tiles",
        "fill 119 46 -294 119 52 -262 deepslate_tiles",
        "fill 117 47 -294 117 47 -262 red_carpet",
        # Lighting along boulevard
        "setblock 117 53 -290 copper_bulb[lit=true,powered=false]",
        "setblock 117 53 -284 copper_bulb[lit=true,powered=false]",
        "setblock 117 53 -278 copper_bulb[lit=true,powered=false]",
        "setblock 117 53 -272 copper_bulb[lit=true,powered=false]",
        "setblock 117 53 -266 copper_bulb[lit=true,powered=false]",

        # Inter-room Cross Connectors
        # Armory to Blacksmith
        "fill 83 46 -294 85 52 -292 air",
        "fill 83 46 -294 85 46 -292 polished_deepslate",
        "fill 83 53 -294 85 53 -292 deepslate_tiles",
        "setblock 84 53 -293 copper_bulb[lit=true,powered=false]",

        # Library to Brewing
        "fill 149 46 -294 151 52 -292 air",
        "fill 149 46 -294 151 46 -292 polished_deepslate",
        "fill 149 53 -294 151 53 -292 deepslate_tiles",
        "setblock 150 53 -293 copper_bulb[lit=true,powered=false]",

        # Farm to Boulevard
        "fill 114 46 -279 116 52 -277 air",
        "fill 114 46 -279 116 46 -277 polished_deepslate",

        # Housing to Boulevard
        "fill 118 46 -279 120 52 -277 air",
        "fill 118 46 -279 120 46 -277 polished_deepslate",

        # Farm to Blacksmith
        "fill 94 46 -284 96 52 -282 air",
        "fill 94 46 -284 96 46 -282 polished_deepslate",
        "fill 94 53 -284 96 53 -282 deepslate_tiles",

        # Housing to Brewing
        "fill 138 46 -284 140 52 -282 air",
        "fill 138 46 -284 140 46 -282 polished_deepslate",
        "fill 138 53 -284 140 53 -282 deepslate_tiles",
    ]
    return write_mcfunction("bunker_corridors.mcfunction", cmds)

def build_armory():
    cmds = [
        "# Sector 1: Tool & Equipment Armory (X: 74..94, Z: -307..-295, Y: 46..53)",
        # Excavation
        "fill 74 46 -307 94 52 -295 air",
        # Ceiling
        "fill 74 53 -307 94 53 -295 deepslate_tiles",
        # Floor
        "fill 74 46 -307 94 46 -295 polished_andesite",
        "fill 75 46 -306 93 46 -296 deepslate_tiles",
        # Outer walls
        "fill 74 46 -307 94 52 -307 deepslate_bricks",
        "fill 74 46 -295 94 52 -295 deepslate_bricks",
        "fill 74 46 -307 74 52 -295 deepslate_bricks",
        "fill 94 46 -307 94 52 -295 deepslate_bricks",
        # Doorway to West Corridor
        "fill 94 47 -302 94 51 -300 air",
        # Wall Skirting
        "fill 75 47 -306 93 47 -306 polished_andesite_stairs[facing=south,half=bottom]",
        "fill 75 47 -296 93 47 -296 polished_andesite_stairs[facing=north,half=bottom]",
        # Armor Display Alcoves (6 Pods along West Wall)
        "setblock 75 47 -304 smooth_stone_slab",
        "setblock 75 47 -302 smooth_stone_slab",
        "setblock 75 47 -300 smooth_stone_slab",
        "setblock 75 47 -298 smooth_stone_slab",
        "setblock 75 48 -304 iron_trapdoor[half=top]",
        "setblock 75 48 -302 iron_trapdoor[half=top]",
        "setblock 75 48 -300 iron_trapdoor[half=top]",
        "setblock 75 48 -298 iron_trapdoor[half=top]",
        # Tool Smithing Cluster
        "setblock 80 47 -305 anvil[facing=north]",
        "setblock 81 47 -305 smithing_table",
        "setblock 82 47 -305 grindstone[face=floor,facing=north]",
        "setblock 83 47 -305 crafting_table",
        "setblock 84 47 -305 ender_chest[facing=south]",
        # Shulker Box Sorting Bay
        "setblock 80 47 -297 hopper[facing=down]",
        "setblock 80 46 -297 barrel[facing=up]",
        "setblock 81 47 -297 barrel[facing=up]",
        "setblock 82 47 -297 barrel[facing=up]",
        # Equipment Double Chest Wall
        "fill 86 47 -306 91 48 -306 chest[facing=south,type=left]",
        "fill 87 47 -306 92 48 -306 chest[facing=south,type=right]",
        # Overhead Lighting Grid
        "setblock 78 53 -302 copper_bulb[lit=true,powered=false]",
        "setblock 84 53 -302 copper_bulb[lit=true,powered=false]",
        "setblock 90 53 -302 copper_bulb[lit=true,powered=false]",
        "setblock 78 53 -298 copper_bulb[lit=true,powered=false]",
        "setblock 84 53 -298 copper_bulb[lit=true,powered=false]",
        "setblock 90 53 -298 copper_bulb[lit=true,powered=false]",
    ]
    return write_mcfunction("bunker_armory.mcfunction", cmds)

def build_blacksmith():
    cmds = [
        "# Sector 2: Blacksmith & Smelting Workshop (X: 74..94, Z: -291..-275, Y: 46..53)",
        # Excavation
        "fill 74 46 -291 94 52 -275 air",
        # Ceiling
        "fill 74 53 -291 94 53 -275 deepslate_tiles",
        # Floor
        "fill 74 46 -291 94 46 -275 smooth_basalt",
        "fill 75 46 -290 93 46 -276 polished_blackstone",
        # Walls
        "fill 74 46 -291 94 52 -291 deepslate_bricks",
        "fill 74 46 -275 94 52 -275 deepslate_bricks",
        "fill 74 46 -291 74 52 -275 deepslate_bricks",
        "fill 94 46 -291 94 52 -275 deepslate_bricks",
        # Doorways
        "fill 94 47 -284 94 51 -282 air",
        "fill 83 47 -291 85 51 -291 air",
        # Super Smelter Battery (16 Furnaces along West Wall)
        "fill 75 47 -290 75 47 -283 blast_furnace[facing=east,lit=false]",
        "fill 75 47 -282 75 47 -276 furnace[facing=east,lit=false]",
        "fill 75 48 -290 75 48 -276 hopper[facing=down]",
        "fill 75 49 -290 75 49 -276 chest[facing=east,type=left]",
        # Central Molten Lava Crucible
        "fill 83 46 -284 85 46 -282 chiseled_polished_blackstone",
        "setblock 84 46 -283 lava",
        "fill 83 47 -284 85 48 -282 tinted_glass",
        "setblock 84 47 -283 lava",
        "setblock 84 48 -283 lava",
        "fill 83 49 -284 85 49 -282 iron_bars",
        # Heavy Metallurgy Bench
        "setblock 89 47 -289 anvil[facing=east]",
        "setblock 89 47 -287 stonecutter[facing=east]",
        "setblock 89 47 -285 grindstone[face=floor,facing=east]",
        "setblock 89 47 -283 cauldron[level=3]",
        "setblock 89 47 -281 cauldron[level=3]",
        # Ingot Storage Racks
        "setblock 92 47 -288 raw_iron_block",
        "setblock 92 48 -288 raw_iron_block",
        "setblock 92 47 -287 iron_block",
        "setblock 92 47 -286 raw_gold_block",
        "setblock 92 47 -285 gold_block",
        "setblock 92 47 -284 raw_copper_block",
        # Overhead Lighting Grid
        "setblock 78 53 -287 copper_bulb[lit=true,powered=false]",
        "setblock 84 53 -287 copper_bulb[lit=true,powered=false]",
        "setblock 90 53 -287 copper_bulb[lit=true,powered=false]",
        "setblock 78 53 -279 copper_bulb[lit=true,powered=false]",
        "setblock 84 53 -279 copper_bulb[lit=true,powered=false]",
        "setblock 90 53 -279 copper_bulb[lit=true,powered=false]",
    ]
    return write_mcfunction("bunker_blacksmith.mcfunction", cmds)

def build_library():
    cmds = [
        "# Sector 3: Grand Arcane Library (X: 140..160, Z: -307..-295, Y: 46..53)",
        # Excavation
        "fill 140 46 -307 160 52 -295 air",
        # Ceiling
        "fill 140 53 -307 160 53 -295 deepslate_tiles",
        # Floor
        "fill 140 46 -307 160 46 -295 dark_oak_planks",
        "fill 142 46 -305 158 46 -297 spruce_planks",
        # Walls
        "fill 140 46 -307 160 52 -307 chiseled_bookshelf",
        "fill 140 46 -295 160 52 -295 chiseled_bookshelf",
        "fill 140 46 -307 140 52 -295 stripped_dark_oak_log",
        "fill 160 46 -307 160 52 -295 chiseled_bookshelf",
        # Doorways
        "fill 140 47 -302 140 51 -300 air",
        "fill 149 47 -295 151 51 -295 air",
        # Level 30 Enchanting Sanctum (Center X: 150, Z: -301)
        "fill 148 46 -303 152 46 -299 smooth_quartz",
        "setblock 150 47 -301 enchanting_table",
        # 15+ Bookshelves surrounding altar with 1 block air gap
        "fill 148 47 -303 152 47 -303 bookshelf",
        "fill 148 48 -303 152 48 -303 bookshelf",
        "fill 148 47 -299 152 47 -299 bookshelf",
        "fill 148 48 -299 152 48 -299 bookshelf",
        "setblock 148 47 -302 bookshelf",
        "setblock 148 48 -302 bookshelf",
        "setblock 148 47 -300 bookshelf",
        "setblock 148 48 -300 bookshelf",
        "setblock 152 47 -302 bookshelf",
        "setblock 152 48 -302 bookshelf",
        "setblock 152 47 -300 bookshelf",
        "setblock 152 48 -300 bookshelf",
        # Floating Study Lecterns
        "setblock 144 47 -304 lectern[facing=east]",
        "setblock 144 47 -298 lectern[facing=east]",
        "setblock 156 47 -304 lectern[facing=west]",
        "setblock 156 47 -298 lectern[facing=west]",
        # Reading Desks with Chairs
        "setblock 144 47 -301 dark_oak_stairs[facing=east,half=bottom]",
        "setblock 145 47 -301 dark_oak_slab[type=bottom]",
        "setblock 156 47 -301 dark_oak_stairs[facing=west,half=bottom]",
        "setblock 155 47 -301 dark_oak_slab[type=bottom]",
        # Overhead Lighting Grid
        "setblock 144 53 -304 copper_bulb[lit=true,powered=false]",
        "setblock 150 53 -304 copper_bulb[lit=true,powered=false]",
        "setblock 156 53 -304 copper_bulb[lit=true,powered=false]",
        "setblock 144 53 -298 copper_bulb[lit=true,powered=false]",
        "setblock 150 53 -298 copper_bulb[lit=true,powered=false]",
        "setblock 156 53 -298 copper_bulb[lit=true,powered=false]",
        # Soul Lanterns on Lecterns
        "setblock 144 48 -304 candle[candles=3,lit=true]",
        "setblock 144 48 -298 candle[candles=3,lit=true]",
        "setblock 156 48 -304 candle[candles=3,lit=true]",
        "setblock 156 48 -298 candle[candles=3,lit=true]",
    ]
    return write_mcfunction("bunker_library.mcfunction", cmds)

def build_brewing():
    cmds = [
        "# Sector 4: Brewing & Alchemy Laboratory (X: 140..160, Z: -291..-275, Y: 46..53)",
        # Excavation
        "fill 140 46 -291 160 52 -275 air",
        # Ceiling
        "fill 140 53 -291 160 53 -275 deepslate_tiles",
        # Floor
        "fill 140 46 -291 160 46 -275 tuff_bricks",
        "fill 141 46 -290 159 46 -276 polished_andesite",
        # Walls
        "fill 140 46 -291 160 52 -291 tuff_bricks",
        "fill 140 46 -275 160 52 -275 tuff_bricks",
        "fill 140 46 -291 140 52 -275 tuff_bricks",
        "fill 160 46 -291 160 52 -275 tuff_bricks",
        # Doorways
        "fill 140 47 -284 140 51 -282 air",
        "fill 149 47 -291 151 51 -291 air",
        # U-Shaped Brewing Bench (East Wall)
        "fill 157 47 -286 159 47 -286 smooth_stone_slab[type=bottom]",
        "fill 157 47 -280 159 47 -280 smooth_stone_slab[type=bottom]",
        "fill 159 47 -285 159 47 -281 smooth_stone_slab[type=bottom]",
        "setblock 159 48 -285 brewing_stand",
        "setblock 159 48 -284 brewing_stand",
        "setblock 159 48 -282 brewing_stand",
        "setblock 159 48 -281 brewing_stand",
        "setblock 159 47 -283 cauldron[level=3]",
        "setblock 158 47 -283 water",
        # Nether Wart Farm Bed (North Wall)
        "fill 153 47 -290 158 47 -290 soul_sand",
        "fill 153 48 -290 158 48 -290 nether_wart[age=3]",
        "fill 153 47 -289 158 47 -289 polished_andesite_stairs[facing=south,half=bottom]",
        # Alchemical Distillation Apparatus
        "setblock 143 47 -288 barrel[facing=up]",
        "setblock 143 48 -288 hopper[facing=down]",
        "setblock 143 49 -288 lightning_rod[facing=up]",
        "setblock 143 47 -284 barrel[facing=up]",
        "setblock 143 48 -284 hopper[facing=down]",
        "setblock 143 49 -284 lightning_rod[facing=up]",
        # Overhead Lighting Grid
        "setblock 144 53 -287 copper_bulb[lit=true,powered=false]",
        "setblock 150 53 -287 copper_bulb[lit=true,powered=false]",
        "setblock 156 53 -287 copper_bulb[lit=true,powered=false]",
        "setblock 144 53 -279 copper_bulb[lit=true,powered=false]",
        "setblock 150 53 -279 copper_bulb[lit=true,powered=false]",
        "setblock 156 53 -279 copper_bulb[lit=true,powered=false]",
    ]
    return write_mcfunction("bunker_brewing.mcfunction", cmds)

def build_farm():
    cmds = [
        "# Sector 5: Underground Farm & Botany Pod (X: 96..114, Z: -291..-265, Y: 46..53)",
        # Excavation
        "fill 96 46 -291 114 52 -265 air",
        # Ceiling
        "fill 96 53 -291 114 53 -265 deepslate_tiles",
        # Floor
        "fill 96 46 -291 114 46 -265 moss_block",
        # Walls
        "fill 96 46 -291 114 52 -291 mossy_stone_bricks",
        "fill 96 46 -265 114 52 -265 mossy_stone_bricks",
        "fill 96 46 -291 96 52 -265 mossy_stone_bricks",
        "fill 114 46 -291 114 52 -265 mossy_stone_bricks",
        # Doorways
        "fill 114 47 -279 114 51 -277 air",
        "fill 96 47 -284 96 51 -282 air",
        # Terraced Irrigated Crop Plots
        # Wheat Plot
        "fill 98 46 -289 104 46 -285 farmland[moisture=7]",
        "fill 98 47 -289 104 47 -285 wheat[age=7]",
        "setblock 101 46 -287 water",
        "setblock 101 47 -287 lily_pad",
        # Carrot Plot
        "fill 106 46 -289 112 46 -285 farmland[moisture=7]",
        "fill 106 47 -289 112 47 -285 carrots[age=7]",
        "setblock 109 46 -287 water",
        "setblock 109 47 -287 lily_pad",
        # Potato Plot
        "fill 98 46 -283 104 46 -279 farmland[moisture=7]",
        "fill 98 47 -283 104 47 -279 potatoes[age=7]",
        "setblock 101 46 -281 water",
        "setblock 101 47 -281 lily_pad",
        # Beetroot Plot
        "fill 106 46 -283 112 46 -279 farmland[moisture=7]",
        "fill 106 47 -283 112 47 -279 beetroots[age=3]",
        "setblock 109 46 -281 water",
        "setblock 109 47 -281 lily_pad",
        # Automated Sugarcane & Bamboo Row (South Wall)
        "fill 98 46 -267 106 46 -267 sand",
        "fill 98 46 -268 106 46 -268 water",
        "fill 98 47 -267 106 48 -267 sugar_cane",
        "fill 98 48 -266 106 48 -266 piston[facing=north]",
        "fill 98 49 -266 106 49 -266 observer[facing=south]",
        # Enclosed Glass Apiary (West End)
        "fill 98 46 -275 104 46 -271 grass_block",
        "fill 98 47 -275 104 51 -271 glass",
        "fill 99 47 -274 103 50 -272 air",
        "setblock 99 47 -273 campfire[lit=true]",
        "setblock 99 48 -273 bee_nest[facing=east,honey_level=5]",
        "setblock 103 47 -273 campfire[lit=true]",
        "setblock 103 48 -273 bee_nest[facing=west,honey_level=5]",
        "setblock 101 47 -273 poppy",
        "setblock 101 47 -274 dandelion",
        # Composter & Tool Shed
        "setblock 111 47 -267 composter[level=5]",
        "setblock 111 47 -268 barrel[facing=up]",
        "setblock 112 47 -268 chest[facing=west]",
        # Spore Blossoms & Foliage
        "setblock 105 52 -287 spore_blossom",
        "setblock 105 52 -273 spore_blossom",
        # Overhead Lighting Grid
        "setblock 100 53 -287 copper_bulb[lit=true,powered=false]",
        "setblock 110 53 -287 copper_bulb[lit=true,powered=false]",
        "setblock 100 53 -279 copper_bulb[lit=true,powered=false]",
        "setblock 110 53 -279 copper_bulb[lit=true,powered=false]",
        "setblock 105 53 -269 copper_bulb[lit=true,powered=false]",
    ]
    return write_mcfunction("bunker_farm.mcfunction", cmds)

def build_housing():
    cmds = [
        "# Sector 6: Modern Subterranean Housing (X: 120..138, Z: -291..-265, Y: 46..53)",
        # Excavation
        "fill 120 46 -291 138 52 -265 air",
        # Ceiling
        "fill 120 53 -291 138 53 -265 smooth_quartz",
        # Floor
        "fill 120 46 -291 138 46 -265 smooth_quartz",
        "fill 122 46 -289 136 46 -267 gray_carpet",
        # Walls
        "fill 120 46 -291 138 52 -291 white_concrete",
        "fill 120 46 -265 138 52 -265 white_concrete",
        "fill 120 46 -291 120 52 -265 white_concrete",
        "fill 138 46 -291 138 52 -265 white_concrete",
        # Doorways
        "fill 120 47 -279 120 51 -277 air",
        "fill 138 47 -284 138 51 -282 air",
        # King Abir Master Suite (North Section Z: -290..-283)
        "fill 130 46 -290 137 46 -283 light_blue_carpet",
        "setblock 136 47 -289 red_bed[facing=north,part=head]",
        "setblock 136 47 -288 red_bed[facing=north,part=foot]",
        "setblock 135 47 -289 red_bed[facing=north,part=head]",
        "setblock 135 47 -288 red_bed[facing=north,part=foot]",
        "setblock 137 47 -289 stripped_spruce_log",
        "setblock 134 47 -289 stripped_spruce_log",
        "setblock 137 48 -289 lantern[hanging=false]",
        "setblock 134 48 -289 lantern[hanging=false]",
        # Wardrobe
        "fill 131 47 -290 133 48 -290 barrel[facing=south]",
        # Partition wall
        "fill 121 47 -282 137 51 -282 white_concrete",
        "fill 128 47 -282 130 50 -282 air",
        # Modern Lounge & Fireplace (South Section Z: -281..-266)
        # Brick Fireplace
        "fill 135 47 -274 137 49 -274 bricks",
        "setblock 136 47 -274 netherrack",
        "setblock 136 48 -274 fire",
        "setblock 136 48 -273 iron_bars",
        # Modern Sofa
        "fill 131 47 -275 131 47 -271 smooth_quartz_stairs[facing=west,half=bottom]",
        "setblock 131 47 -276 smooth_quartz_stairs[facing=south,half=bottom]",
        "setblock 131 47 -270 smooth_quartz_stairs[facing=north,half=bottom]",
        # Coffee Table
        "setblock 133 47 -273 smooth_stone_slab[type=bottom]",
        "setblock 133 47 -272 smooth_stone_slab[type=bottom]",
        # Kitchen & Bar
        "fill 122 47 -276 122 47 -269 smooth_quartz_stairs[facing=east,half=bottom]",
        "setblock 121 47 -275 smoker[facing=east]",
        "setblock 121 47 -274 cauldron[level=3]",
        "setblock 121 48 -274 tripwire_hook[facing=east]",
        "setblock 121 47 -273 barrel[facing=east]",
        "setblock 121 47 -272 barrel[facing=east]",
        "setblock 121 47 -271 brewing_stand",
        # Overhead Lighting Grid
        "setblock 125 53 -287 copper_bulb[lit=true,powered=false]",
        "setblock 133 53 -287 copper_bulb[lit=true,powered=false]",
        "setblock 125 53 -273 copper_bulb[lit=true,powered=false]",
        "setblock 133 53 -273 copper_bulb[lit=true,powered=false]",
        "setblock 125 53 -267 copper_bulb[lit=true,powered=false]",
        "setblock 133 53 -267 copper_bulb[lit=true,powered=false]",
    ]
    return write_mcfunction("bunker_housing.mcfunction", cmds)

def build_parliament():
    cmds = [
        "# Sector 7: King's Council & High Parliament (X: 105..129, Z: -261..-235, Y: 46..53)",
        # Excavation
        "fill 105 46 -261 129 52 -235 air",
        # Ceiling
        "fill 105 53 -261 129 53 -235 polished_blackstone",
        # Floor
        "fill 105 46 -261 129 46 -235 polished_blackstone",
        # Walls
        "fill 105 46 -261 129 52 -261 polished_blackstone_bricks",
        "fill 105 46 -235 129 52 -235 polished_blackstone_bricks",
        "fill 105 46 -261 105 52 -235 polished_blackstone_bricks",
        "fill 129 46 -261 129 52 -235 polished_blackstone_bricks",
        # Pilasters & Gold Accents
        "fill 105 46 -261 105 52 -261 crying_obsidian",
        "fill 129 46 -261 129 52 -261 crying_obsidian",
        "fill 105 46 -235 105 52 -235 crying_obsidian",
        "fill 129 46 -235 129 52 -235 crying_obsidian",
        "setblock 117 48 -236 gold_block",
        "setblock 117 49 -236 gold_block",
        "setblock 117 50 -236 gold_block",
        # Entrance from South Boulevard
        "fill 116 47 -261 118 51 -261 air",
        # Central Aisle with Red Carpet
        "fill 116 47 -260 118 47 -240 red_carpet",
        "fill 115 47 -260 115 47 -240 yellow_carpet",
        "fill 119 47 -260 119 47 -240 yellow_carpet",
        # Sovereign Prime Minister Throne Dais (South Wall)
        "fill 115 47 -239 119 47 -237 gilded_blackstone",
        "fill 116 48 -238 118 48 -237 gilded_blackstone",
        "setblock 117 49 -237 polished_blackstone_stairs[facing=south,half=bottom]",
        "setblock 117 50 -237 red_banner[rotation=0]",
        "setblock 116 49 -237 red_banner[rotation=0]",
        "setblock 118 49 -237 red_banner[rotation=0]",
        # Ceremonial Golden Mace Plinth
        "setblock 117 47 -244 chiseled_polished_blackstone",
        "setblock 117 48 -244 gold_block",
        "setblock 117 49 -244 lightning_rod[facing=up]",
        # 3-Tier Opposing Parliament Benches (West & East Benches)
        # West Benches (facing East towards central aisle)
        "fill 111 47 -256 113 47 -256 dark_oak_stairs[facing=east,half=bottom]",
        "fill 111 47 -254 113 47 -254 dark_oak_stairs[facing=east,half=bottom]",
        "fill 111 47 -252 113 47 -252 dark_oak_stairs[facing=east,half=bottom]",
        "fill 111 47 -250 113 47 -250 dark_oak_stairs[facing=east,half=bottom]",
        "fill 111 47 -248 113 47 -248 dark_oak_stairs[facing=east,half=bottom]",
        "fill 111 47 -246 113 47 -246 dark_oak_stairs[facing=east,half=bottom]",
        # East Benches (facing West towards central aisle)
        "fill 121 47 -256 123 47 -256 dark_oak_stairs[facing=west,half=bottom]",
        "fill 121 47 -254 123 47 -254 dark_oak_stairs[facing=west,half=bottom]",
        "fill 121 47 -252 123 47 -252 dark_oak_stairs[facing=west,half=bottom]",
        "fill 121 47 -250 123 47 -250 dark_oak_stairs[facing=west,half=bottom]",
        "fill 121 47 -248 123 47 -248 dark_oak_stairs[facing=west,half=bottom]",
        "fill 121 47 -246 123 47 -246 dark_oak_stairs[facing=west,half=bottom]",
        # Desk slabs in front of benches
        "fill 113 47 -256 113 47 -246 dark_oak_slab[type=bottom]",
        "fill 121 47 -256 121 47 -246 dark_oak_slab[type=bottom]",
        # Overhead Grand Chandeliers
        "setblock 117 53 -256 copper_bulb[lit=true,powered=false]",
        "setblock 117 53 -248 copper_bulb[lit=true,powered=false]",
        "setblock 117 53 -240 copper_bulb[lit=true,powered=false]",
        "setblock 111 53 -256 copper_bulb[lit=true,powered=false]",
        "setblock 123 53 -256 copper_bulb[lit=true,powered=false]",
        "setblock 111 53 -248 copper_bulb[lit=true,powered=false]",
        "setblock 123 53 -248 copper_bulb[lit=true,powered=false]",
        "setblock 111 53 -240 copper_bulb[lit=true,powered=false]",
        "setblock 123 53 -240 copper_bulb[lit=true,powered=false]",
    ]
    return write_mcfunction("bunker_parliament.mcfunction", cmds)

def build_master():
    cmds = [
        "# Master Dispatcher for King Abir's Hivemind Bunker",
        "function citadel:bunker_rotunda",
        "function citadel:bunker_corridors",
        "function citadel:bunker_armory",
        "function citadel:bunker_blacksmith",
        "function citadel:bunker_library",
        "function citadel:bunker_brewing",
        "function citadel:bunker_farm",
        "function citadel:bunker_housing",
        "function citadel:bunker_parliament",
    ]
    return write_mcfunction("build_all.mcfunction", cmds)

def execute_remote_batch(all_cmds, host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Executes all commands via RCON in chunks under 100 commands per socket invocation."""
    batch_size = 80
    total = len(all_cmds)
    print(f"Total commands to execute: {total}")
    for i in range(0, total, batch_size):
        chunk = all_cmds[i:i + batch_size]
        py_code = f"""
import socket, struct

with open('/home/ubuntu/minecraft-server/server.properties') as f:
    props = dict(line.strip().split('=', 1) for line in f if '=' in line and not line.startswith('#'))

rcon_port = int(props.get('rcon.port', 25575))
rcon_pass = props.get('rcon.password', '')

s = socket.create_connection(('127.0.0.1', rcon_port), timeout=10)
s.sendall(struct.pack('<iii', len(rcon_pass) + 10, 1, 3) + rcon_pass.encode('utf-8') + b'\\x00\\x00')
auth_resp = s.recv(4096)

cmds = {repr(chunk)}
for idx, cmd in enumerate(cmds, 1):
    s.sendall(struct.pack('<iii', len(cmd) + 10, idx + 10, 2) + cmd.encode('utf-8') + b'\\x00\\x00')
    resp = s.recv(4096)

s.close()
"""
        ssh_cmd = [
            "ssh", "-o", "StrictHostKeyChecking=no",
            "-i", key,
            f"{user}@{host}",
            f"python3 -c {subprocess.list2cmdline([py_code])}"
        ]
        res = subprocess.run(ssh_cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"Batch {i//batch_size + 1} error: {res.stderr}", file=sys.stderr)
            sys.exit(res.returncode)
        print(f"Batch {i//batch_size + 1}/{(total + batch_size - 1)//batch_size} ({min(i + batch_size, total)}/{total}) complete.")

if __name__ == "__main__":
    all_commands = []
    all_commands.extend([c for c in build_rotunda() if not c.startswith("#")])
    all_commands.extend([c for c in build_corridors() if not c.startswith("#")])
    all_commands.extend([c for c in build_armory() if not c.startswith("#")])
    all_commands.extend([c for c in build_blacksmith() if not c.startswith("#")])
    all_commands.extend([c for c in build_library() if not c.startswith("#")])
    all_commands.extend([c for c in build_brewing() if not c.startswith("#")])
    all_commands.extend([c for c in build_farm() if not c.startswith("#")])
    all_commands.extend([c for c in build_housing() if not c.startswith("#")])
    all_commands.extend([c for c in build_parliament() if not c.startswith("#")])
    build_master()
    print("Generated all mcfunction files.")
    execute_remote_batch(all_commands)
    print("Full veteran bunker construction complete.")
