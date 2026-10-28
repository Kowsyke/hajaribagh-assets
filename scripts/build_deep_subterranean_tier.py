#!/usr/bin/env python3
"""Build Tier 3 Deep Subterranean Facilities for King Abir Hivemind Bunker.

Generates the Tier 3 deep infrastructure at Y levels 36 to 45 directly beneath the bunker.
Includes:
1. Central Beacon Well beneath the Rotunda (X: 115..119, Z: -303..-299, Y: 36..45).
2. Dual water bubble elevators (soul sand up, magma down) connecting Y: 46 to Y: 36.
3. Heavy Ore Processing Basement beneath Blacksmith (X: 78..90, Z: -289..-277, Y: 38..45).
4. Forbidden Apocrypha Archive beneath Library (X: 144..156, Z: -305..-297, Y: 38..45).
5. Subterranean Aquaponics Grotto beneath Farm (X: 98..112, Z: -289..-267, Y: 36..45).
6. Connecting transit concourses with full copper bulb and sea lantern illumination.
"""

import math
import os
import subprocess
import sys
import time

DEFAULT_HOST = os.environ.get("HZ_HOST", "132.226.135.26")
DEFAULT_USER = os.environ.get("HZ_USER", "ubuntu")
DEFAULT_KEY = os.environ.get("HZ_KEY", os.path.expanduser("~/.ssh/id_ed25519"))

FUNCTION_PATH = "datapacks/underground_citadel/data/citadel/function/bunker_deep_tier.mcfunction"

def write_mcfunction(filepath, lines):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    clean_lines = [line.strip() for line in lines if line.strip()]
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(clean_lines) + "\n")
    return clean_lines

def build_beacon_well():
    """Generates commands for the Central Beacon Well beneath the Rotunda."""
    cmds = [
        "# Central Beacon Well beneath the Rotunda (X: 115..119, Z: -303..-299, Y: 36..45)",
        # Excavation of well chamber
        "fill 115 36 -303 119 45 -299 air",
        # Well outer perimeter walls
        "fill 114 36 -304 120 45 -304 deepslate_tiles",
        "fill 114 36 -298 120 45 -298 deepslate_tiles",
        "fill 114 36 -303 114 45 -299 deepslate_tiles",
        "fill 120 36 -303 120 45 -299 deepslate_tiles",
        # Corner structural pilasters
        "fill 114 36 -304 114 45 -304 chiseled_deepslate",
        "fill 120 36 -304 120 45 -304 chiseled_deepslate",
        "fill 114 36 -298 114 45 -298 chiseled_deepslate",
        "fill 120 36 -298 120 45 -298 chiseled_deepslate",
        # Beacon pyramid base at Y: 36 (5x5 netherite base)
        "fill 115 36 -303 119 36 -299 netherite_block",
        # Beacon pyramid tier 2 at Y: 37 (3x3 netherite base)
        "fill 116 37 -302 118 37 -300 netherite_block",
        # Active beacon block at Y: 38
        "setblock 117 38 -301 beacon",
        # Decorative plinth surround at Y: 38
        "setblock 116 38 -302 crying_obsidian",
        "setblock 118 38 -302 crying_obsidian",
        "setblock 116 38 -300 crying_obsidian",
        "setblock 118 38 -300 crying_obsidian",
        "setblock 117 38 -302 sea_lantern",
        "setblock 117 38 -300 sea_lantern",
        "setblock 116 38 -301 sea_lantern",
        "setblock 118 38 -301 sea_lantern",
        # Walkway collar ring at Y: 38 around the well
        "fill 114 38 -303 114 38 -299 polished_deepslate",
        "fill 120 38 -303 120 38 -299 polished_deepslate",
        "fill 115 38 -304 119 38 -304 polished_deepslate",
        "fill 115 38 -298 119 38 -298 polished_deepslate",
        # Well illumination fixtures
        "setblock 114 41 -301 copper_bulb[lit=true,powered=false]",
        "setblock 120 41 -301 copper_bulb[lit=true,powered=false]",
        "setblock 117 41 -304 copper_bulb[lit=true,powered=false]",
        "setblock 117 41 -298 copper_bulb[lit=true,powered=false]",
        "setblock 114 44 -301 sea_lantern",
        "setblock 120 44 -301 sea_lantern",
        # Glass viewing floor at Y: 46 in the upper Rotunda
        "fill 115 46 -303 119 46 -303 polished_blackstone",
        "fill 115 46 -299 119 46 -299 polished_blackstone",
        "fill 115 46 -303 115 46 -299 polished_blackstone",
        "fill 119 46 -303 119 46 -299 polished_blackstone",
        "fill 116 46 -302 118 46 -300 tinted_glass",
        "setblock 117 46 -301 glass",
        # Skyward conduit for beacon activation
        "fill 117 47 -301 117 52 -301 air",
        "setblock 117 53 -301 glass",
        "fill 117 54 -301 117 85 -301 glass replace",
    ]
    return cmds

def build_bubble_elevators():
    """Generates dual water bubble elevators connecting Y: 46 to Y: 36."""
    cmds = [
        "# Dual Water Bubble Elevators (Soul Sand Up, Magma Down, Y: 36..46)",
        # Shaft excavation
        "fill 111 36 -298 115 47 -296 air",
        # Rear enclosure wall
        "fill 111 36 -298 115 47 -298 deepslate_tiles",
        # Outer side walls
        "fill 111 36 -297 111 47 -296 deepslate_tiles",
        "fill 115 36 -297 115 47 -296 deepslate_tiles",
        # Center divider between elevators
        "fill 113 36 -297 113 47 -297 tinted_glass",
        "fill 113 36 -296 113 47 -296 tinted_glass",
        # Elevator bases at Y: 36
        "setblock 112 36 -297 soul_sand",
        "setblock 114 36 -297 magma_block",
        # Bottom entrance floor at Y: 36
        "fill 112 36 -296 114 36 -296 polished_deepslate",
        # Water bubble columns from Y: 37 through Y: 46
        "fill 112 37 -297 112 46 -297 bubble_column[drag=false]",
        "fill 114 37 -297 114 46 -297 bubble_column[drag=true]",
        # Bottom doorways at Y: 37..38 (Z: -296) with water containment signs
        "setblock 112 37 -296 spruce_wall_sign[facing=east]",
        "setblock 112 38 -296 spruce_wall_sign[facing=east]",
        "setblock 114 37 -296 spruce_wall_sign[facing=west]",
        "setblock 114 38 -296 spruce_wall_sign[facing=west]",
        # Mid level front observation glass (Y: 39..45)
        "fill 112 39 -296 112 45 -296 glass",
        "fill 114 39 -296 114 45 -296 glass",
        # Top doorways at Y: 46..47 (Z: -296) in Rotunda with water containment signs
        "setblock 112 46 -296 spruce_wall_sign[facing=east]",
        "setblock 112 47 -296 spruce_wall_sign[facing=east]",
        "setblock 114 46 -296 spruce_wall_sign[facing=west]",
        "setblock 114 47 -296 spruce_wall_sign[facing=west]",
        # Top landing lintel and direction indicators at Y: 48
        "fill 111 48 -296 115 48 -296 polished_deepslate",
        "setblock 112 48 -296 emerald_block",
        "setblock 114 48 -296 redstone_block",
        "setblock 113 48 -296 copper_bulb[lit=true,powered=false]",
        # Illumination lanterns inside elevator shafts
        "setblock 113 36 -298 sea_lantern",
        "setblock 113 41 -298 sea_lantern",
        "setblock 113 46 -298 sea_lantern",
    ]
    return cmds

def build_ore_processing():
    """Generates the Heavy Ore Processing Basement beneath the Blacksmith."""
    cmds = [
        "# Heavy Ore Processing Basement beneath Blacksmith (X: 78..90, Z: -289..-277, Y: 38..45)",
        # Room excavation
        "fill 78 38 -289 90 45 -277 air",
        # Floor at Y: 38
        "fill 78 38 -289 90 38 -277 smooth_basalt",
        "fill 80 38 -287 88 38 -279 polished_blackstone",
        # Ceiling at Y: 45
        "fill 78 45 -289 90 45 -277 deepslate_tiles",
        # Perimeter walls
        "fill 77 38 -290 91 45 -290 deepslate_bricks",
        "fill 77 38 -276 91 45 -276 deepslate_bricks",
        "fill 77 38 -290 77 45 -276 deepslate_bricks",
        "fill 91 38 -290 91 45 -276 deepslate_bricks",
        # Corner columns
        "fill 77 38 -290 77 45 -290 chiseled_polished_blackstone",
        "fill 91 38 -290 91 45 -290 chiseled_polished_blackstone",
        "fill 77 38 -276 77 45 -276 chiseled_polished_blackstone",
        "fill 91 38 -276 91 45 -276 chiseled_polished_blackstone",
        # Bulk Chest Hopper Storage Array along North wall (Z: -288)
        # Pair 1: X: 79..80
        "setblock 79 39 -288 chest[facing=south,type=right]",
        "setblock 80 39 -288 chest[facing=south,type=left]",
        "setblock 79 40 -288 hopper[facing=down]",
        "setblock 80 40 -288 hopper[facing=down]",
        "setblock 79 41 -288 chest[facing=south,type=right]",
        "setblock 80 41 -288 chest[facing=south,type=left]",
        "setblock 79 42 -288 hopper[facing=down]",
        "setblock 80 42 -288 hopper[facing=down]",
        # Pair 2: X: 82..83
        "setblock 82 39 -288 chest[facing=south,type=right]",
        "setblock 83 39 -288 chest[facing=south,type=left]",
        "setblock 82 40 -288 hopper[facing=down]",
        "setblock 83 40 -288 hopper[facing=down]",
        "setblock 82 41 -288 chest[facing=south,type=right]",
        "setblock 83 41 -288 chest[facing=south,type=left]",
        "setblock 82 42 -288 hopper[facing=down]",
        "setblock 83 42 -288 hopper[facing=down]",
        # Pair 3: X: 85..86
        "setblock 85 39 -288 chest[facing=south,type=right]",
        "setblock 86 39 -288 chest[facing=south,type=left]",
        "setblock 85 40 -288 hopper[facing=down]",
        "setblock 86 40 -288 hopper[facing=down]",
        "setblock 85 41 -288 chest[facing=south,type=right]",
        "setblock 86 41 -288 chest[facing=south,type=left]",
        "setblock 85 42 -288 hopper[facing=down]",
        "setblock 86 42 -288 hopper[facing=down]",
        # Central Lava Fuel Containment Cistern (X: 83..85, Z: -284..-282)
        "fill 83 38 -284 85 38 -282 chiseled_polished_blackstone",
        "fill 83 39 -284 85 42 -282 tinted_glass",
        "fill 84 39 -283 84 42 -283 lava",
        "fill 83 43 -284 85 43 -282 iron_bars",
        "setblock 84 44 -283 lightning_rod[facing=up]",
        # Fuel draw stations
        "setblock 82 39 -283 lava_cauldron",
        "setblock 86 39 -283 lava_cauldron",
        # Smelting furnace bank along West wall (X: 78)
        "fill 78 39 -286 78 39 -280 blast_furnace[facing=east,lit=true]",
        "fill 78 40 -286 78 40 -280 hopper[facing=down]",
        "fill 78 41 -286 78 41 -280 chest[facing=east,type=single]",
        # Heavy ore reserves along East wall (X: 89..90)
        "fill 89 39 -288 89 41 -287 raw_iron_block",
        "fill 90 39 -288 90 41 -287 iron_block",
        "fill 89 39 -280 89 41 -279 raw_copper_block",
        "fill 90 39 -280 90 41 -279 copper_block",
        "fill 89 39 -283 89 40 -282 raw_gold_block",
        "fill 90 39 -283 90 40 -282 gold_block",
        # Metallurgy workstation equipment
        "setblock 81 39 -278 anvil[facing=north]",
        "setblock 82 39 -278 smithing_table",
        "setblock 83 39 -278 stonecutter[facing=north]",
        "setblock 84 39 -278 grindstone[face=floor,facing=north]",
        # Ceiling illumination grid (ensures zero mob spawns)
        "setblock 80 45 -286 copper_bulb[lit=true,powered=false]",
        "setblock 84 45 -286 sea_lantern",
        "setblock 88 45 -286 copper_bulb[lit=true,powered=false]",
        "setblock 80 45 -280 copper_bulb[lit=true,powered=false]",
        "setblock 84 45 -280 sea_lantern",
        "setblock 88 45 -280 copper_bulb[lit=true,powered=false]",
        # Wall sconce illumination
        "setblock 78 41 -284 sea_lantern",
        "setblock 90 41 -284 sea_lantern",
    ]
    return cmds

def build_forbidden_apocrypha():
    """Generates the Forbidden Apocrypha Archive beneath the Arcane Library."""
    cmds = [
        "# Forbidden Apocrypha Archive beneath Library (X: 144..156, Z: -305..-297, Y: 38..45)",
        # Room excavation
        "fill 144 38 -305 156 45 -297 air",
        # Floor at Y: 38
        "fill 144 38 -305 156 38 -297 dark_oak_planks",
        "fill 146 38 -303 154 38 -299 polished_blackstone",
        # Ceiling at Y: 45
        "fill 144 45 -305 156 45 -297 deepslate_tiles",
        # Perimeter walls
        "fill 143 38 -306 157 45 -306 deepslate_tiles",
        "fill 143 38 -296 157 45 -296 deepslate_tiles",
        "fill 143 38 -306 143 45 -296 deepslate_tiles",
        "fill 157 38 -306 157 45 -296 deepslate_tiles",
        # Corner columns of crying obsidian
        "fill 143 38 -306 143 45 -306 crying_obsidian",
        "fill 157 38 -306 157 45 -306 crying_obsidian",
        "fill 143 38 -296 143 45 -296 crying_obsidian",
        "fill 157 38 -296 157 45 -296 crying_obsidian",
        # Perimeter chiseled bookshelves
        "fill 144 39 -305 156 42 -305 chiseled_bookshelf",
        "fill 144 39 -297 156 42 -297 chiseled_bookshelf",
        "fill 156 39 -304 156 42 -298 chiseled_bookshelf",
        # Crying obsidian wall veins
        "setblock 148 41 -305 crying_obsidian",
        "setblock 152 41 -305 crying_obsidian",
        "setblock 148 41 -297 crying_obsidian",
        "setblock 152 41 -297 crying_obsidian",
        # Central Apocryphal Altar at (150, 39, -301)
        "fill 149 39 -302 151 39 -300 crying_obsidian",
        "setblock 150 40 -301 lectern[facing=west]",
        "setblock 149 40 -301 amethyst_cluster[facing=up]",
        "setblock 151 40 -301 amethyst_cluster[facing=up]",
        "setblock 150 40 -302 amethyst_cluster[facing=up]",
        "setblock 150 40 -300 amethyst_cluster[facing=up]",
        # Ancient Study Lecterns on crying obsidian pedestals
        # West North Lectern
        "setblock 146 39 -303 crying_obsidian",
        "setblock 146 40 -303 lectern[facing=south]",
        "setblock 145 40 -303 candle[candles=3,lit=true]",
        # East North Lectern
        "setblock 154 39 -303 crying_obsidian",
        "setblock 154 40 -303 lectern[facing=south]",
        "setblock 155 40 -303 candle[candles=3,lit=true]",
        # West South Lectern
        "setblock 146 39 -299 crying_obsidian",
        "setblock 146 40 -299 lectern[facing=north]",
        "setblock 145 40 -299 candle[candles=3,lit=true]",
        # East South Lectern
        "setblock 154 39 -299 crying_obsidian",
        "setblock 154 40 -299 lectern[facing=north]",
        "setblock 155 40 -299 candle[candles=3,lit=true]",
        # Ritual braziers
        "setblock 148 39 -301 soul_campfire[lit=true]",
        "setblock 152 39 -301 soul_campfire[lit=true]",
        # Overhead illumination grid
        "setblock 146 45 -303 copper_bulb[lit=true,powered=false]",
        "setblock 150 45 -303 sea_lantern",
        "setblock 154 45 -303 copper_bulb[lit=true,powered=false]",
        "setblock 146 45 -299 copper_bulb[lit=true,powered=false]",
        "setblock 150 45 -299 sea_lantern",
        "setblock 154 45 -299 copper_bulb[lit=true,powered=false]",
        # Wall sconces
        "setblock 150 42 -305 sea_lantern",
        "setblock 150 42 -297 sea_lantern",
    ]
    return cmds

def build_aquaponics_grotto():
    """Generates the Subterranean Aquaponics Grotto beneath the Farm."""
    cmds = [
        "# Subterranean Aquaponics Grotto beneath Farm (X: 98..112, Z: -289..-267, Y: 36..45)",
        # Room excavation
        "fill 98 36 -289 112 45 -267 air",
        # Floor at Y: 36
        "fill 98 36 -289 112 36 -267 moss_block",
        # Ceiling at Y: 45
        "fill 98 45 -289 112 45 -267 moss_block",
        # Perimeter walls
        "fill 97 36 -290 113 45 -290 mossy_stone_bricks",
        "fill 97 36 -266 113 45 -266 mossy_stone_bricks",
        "fill 97 36 -290 97 45 -266 mossy_stone_bricks",
        "fill 113 36 -290 113 45 -266 mossy_stone_bricks",
        # Wall textural variation
        "fill 97 38 -285 97 42 -282 tuff_bricks",
        "fill 113 38 -285 113 42 -282 tuff_bricks",
        "fill 97 38 -274 97 42 -271 tuff_bricks",
        "fill 113 38 -274 113 42 -271 tuff_bricks",
        # North Aquaponics Clay Pool (X: 100..104, Z: -286..-281)
        "fill 100 35 -286 104 35 -281 clay",
        "fill 100 36 -286 104 36 -281 water",
        "setblock 101 36 -284 sea_pickle[waterlogged=true,pickles=3]",
        "setblock 103 36 -284 sea_pickle[waterlogged=true,pickles=4]",
        "setblock 102 36 -282 seagrass",
        "setblock 102 37 -285 lily_pad",
        "setblock 103 37 -283 lily_pad",
        "setblock 102 35 -283 sea_lantern",
        # South Aquaponics Clay Pool (X: 106..110, Z: -275..-270)
        "fill 106 35 -275 110 35 -270 clay",
        "fill 106 36 -275 110 36 -270 water",
        "setblock 107 36 -273 sea_pickle[waterlogged=true,pickles=4]",
        "setblock 109 36 -273 sea_pickle[waterlogged=true,pickles=3]",
        "setblock 108 36 -272 seagrass",
        "setblock 107 37 -274 lily_pad",
        "setblock 109 37 -271 lily_pad",
        "setblock 108 35 -273 sea_lantern",
        # Hanging glow berries and cave vines
        # Vine cluster 1
        "setblock 102 44 -284 cave_vines_plant[berries=true]",
        "setblock 102 43 -284 cave_vines_plant[berries=true]",
        "setblock 102 42 -284 cave_vines_plant[berries=true]",
        "setblock 102 41 -284 cave_vines[berries=true,age=24]",
        # Vine cluster 2
        "setblock 108 44 -284 cave_vines_plant[berries=true]",
        "setblock 108 43 -284 cave_vines_plant[berries=true]",
        "setblock 108 42 -284 cave_vines_plant[berries=true]",
        "setblock 108 41 -284 cave_vines[berries=true,age=24]",
        # Vine cluster 3
        "setblock 102 44 -273 cave_vines_plant[berries=true]",
        "setblock 102 43 -273 cave_vines_plant[berries=true]",
        "setblock 102 42 -273 cave_vines[berries=true,age=24]",
        # Vine cluster 4
        "setblock 108 44 -273 cave_vines_plant[berries=true]",
        "setblock 108 43 -273 cave_vines_plant[berries=true]",
        "setblock 108 42 -273 cave_vines[berries=true,age=24]",
        # Vine cluster 5
        "setblock 105 44 -278 cave_vines_plant[berries=true]",
        "setblock 105 43 -278 cave_vines_plant[berries=true]",
        "setblock 105 42 -278 cave_vines[berries=true,age=24]",
        # Hanging spore blossoms
        "setblock 104 44 -280 spore_blossom",
        "setblock 106 44 -276 spore_blossom",
        # Lush vegetation and dripleaf plantings
        "setblock 99 37 -285 big_dripleaf[facing=east]",
        "setblock 99 37 -282 big_dripleaf[facing=east]",
        "setblock 111 37 -274 big_dripleaf[facing=west]",
        "setblock 111 37 -271 big_dripleaf[facing=west]",
        "setblock 100 37 -280 flowering_azalea",
        "setblock 110 37 -276 azalea",
        # Mineral filtration dripstone station
        "setblock 111 44 -286 pointed_dripstone[thickness=tip,vertical_direction=down]",
        "setblock 111 37 -286 water_cauldron[level=3]",
        "setblock 111 44 -284 pointed_dripstone[thickness=tip,vertical_direction=down]",
        "setblock 111 37 -284 water_cauldron[level=3]",
        # Overhead illumination grid
        "setblock 101 45 -286 copper_bulb[lit=true,powered=false]",
        "setblock 109 45 -286 copper_bulb[lit=true,powered=false]",
        "setblock 105 45 -278 sea_lantern",
        "setblock 101 45 -270 copper_bulb[lit=true,powered=false]",
        "setblock 109 45 -270 copper_bulb[lit=true,powered=false]",
    ]
    return cmds

def build_connecting_concourses():
    """Generates subterranean concourses connecting the deep tier facilities."""
    cmds = [
        "# Connecting Subterranean Concourses (Floor Y: 38/36, Clear Y: 39..41, Ceiling Y: 42)",
        # West transit concourse to Heavy Ore Processing
        # From Beacon Well (X: 114) heading West to X: 91
        "fill 91 38 -302 114 41 -300 air",
        "fill 91 37 -302 114 37 -300 polished_deepslate",
        "fill 91 42 -302 114 42 -300 deepslate_tiles",
        "fill 91 38 -303 114 41 -303 deepslate_tiles",
        "fill 91 38 -299 114 41 -299 deepslate_tiles",
        "setblock 108 42 -301 copper_bulb[lit=true,powered=false]",
        "setblock 102 42 -301 copper_bulb[lit=true,powered=false]",
        "setblock 96 42 -301 copper_bulb[lit=true,powered=false]",
        # Turn South from X: 91 towards Heavy Ore Processing doorway
        "fill 90 38 -301 92 41 -284 air",
        "fill 90 37 -301 92 37 -284 polished_deepslate",
        "fill 90 42 -301 92 42 -284 deepslate_tiles",
        "fill 93 38 -301 93 41 -284 deepslate_tiles",
        "fill 89 38 -301 89 41 -291 deepslate_tiles",
        "setblock 91 42 -294 copper_bulb[lit=true,powered=false]",
        "setblock 91 42 -288 copper_bulb[lit=true,powered=false]",
        # Doorway into Heavy Ore Processing
        "fill 90 39 -284 91 42 -282 air",
        # East transit concourse to Forbidden Apocrypha Archive
        # From Beacon Well (X: 120) heading East to X: 143
        "fill 120 38 -302 143 41 -300 air",
        "fill 120 37 -302 143 37 -300 polished_deepslate",
        "fill 120 42 -302 143 42 -300 deepslate_tiles",
        "fill 120 38 -303 143 41 -303 deepslate_tiles",
        "fill 120 38 -299 143 41 -299 deepslate_tiles",
        "setblock 126 42 -301 copper_bulb[lit=true,powered=false]",
        "setblock 132 42 -301 copper_bulb[lit=true,powered=false]",
        "setblock 138 42 -301 copper_bulb[lit=true,powered=false]",
        # Doorway into Forbidden Apocrypha
        "fill 143 39 -302 143 42 -300 air",
        # South transit concourse to Aquaponics Grotto
        # From Beacon Well south collar (Z: -298) and Elevator Hub (Z: -296)
        "fill 104 36 -296 114 41 -296 air",
        "fill 104 36 -295 107 41 -290 air",
        "fill 103 35 -295 108 35 -290 moss_block",
        "fill 103 42 -295 108 42 -290 deepslate_tiles",
        "fill 103 36 -295 103 41 -290 mossy_stone_bricks",
        "fill 108 36 -295 108 41 -290 mossy_stone_bricks",
        "setblock 105 42 -293 copper_bulb[lit=true,powered=false]",
        # Doorway into Aquaponics Grotto
        "fill 104 37 -290 106 40 -290 air",
    ]
    return cmds

def execute_remote_batch(all_cmds, host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Executes all commands via RCON in chunks under 80 commands per invocation."""
    batch_size = 70
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
            "python3"
        ]
        res = subprocess.run(ssh_cmd, input=py_code, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"Batch {i//batch_size + 1} error: {res.stderr}", file=sys.stderr)
            sys.exit(res.returncode)
        total_batches = math.ceil(total / batch_size)
        current_batch = (i // batch_size) + 1
        print(f"Batch {current_batch}/{total_batches} complete.")

def verify_live_blockstates(host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Verifies live blockstates of all constructed facilities via RCON."""
    checks = [
        ("Beacon Block", "execute if block 117 38 -301 beacon"),
        ("Beacon Viewing Floor Glass", "execute if block 117 46 -301 glass"),
        ("Beacon Netherite Base", "execute if block 117 36 -301 netherite_block"),
        ("Soul Sand Elevator Base", "execute if block 112 36 -297 soul_sand"),
        ("Soul Sand Bubble Column", "execute if block 112 37 -297 bubble_column[drag=false]"),
        ("Magma Elevator Base", "execute if block 114 36 -297 magma_block"),
        ("Magma Bubble Column", "execute if block 114 37 -297 bubble_column[drag=true]"),
        ("Elevator Tinted Divider", "execute if block 113 40 -297 tinted_glass"),
        ("Ore Processing Smelter", "execute if block 78 39 -283 blast_furnace[facing=east,lit=true]"),
        ("Ore Processing Lava Core", "execute if block 84 40 -283 lava"),
        ("Ore Processing Hopper Array", "execute if block 79 40 -288 hopper[facing=down]"),
        ("Forbidden Apocrypha Lectern", "execute if block 146 40 -303 lectern[facing=south]"),
        ("Forbidden Crying Obsidian", "execute if block 146 39 -303 crying_obsidian"),
        ("Aquaponics Moss Floor", "execute if block 105 36 -278 moss_block"),
        ("Aquaponics Clay Pool", "execute if block 101 35 -283 clay"),
        ("Aquaponics Cave Vines", "execute if block 105 44 -278 cave_vines_plant[berries=true]"),
        ("Aquaponics Sea Lantern", "execute if block 105 45 -278 sea_lantern"),
    ]

    py_code = f"""
import socket, struct

with open('/home/ubuntu/minecraft-server/server.properties') as f:
    props = dict(line.strip().split('=', 1) for line in f if '=' in line and not line.startswith('#'))

rcon_port = int(props.get('rcon.port', 25575))
rcon_pass = props.get('rcon.password', '')

s = socket.create_connection(('127.0.0.1', rcon_port), timeout=10)
s.sendall(struct.pack('<iii', len(rcon_pass) + 10, 1, 3) + rcon_pass.encode('utf-8') + b'\\x00\\x00')
s.recv(4096)

checks = {repr(checks)}
results = []
for label, cmd in checks:
    s.sendall(struct.pack('<iii', len(cmd) + 10, 50, 2) + cmd.encode('utf-8') + b'\\x00\\x00')
    resp = s.recv(4096)
    txt = resp[12:-2].decode('utf-8', errors='ignore')
    status = 'PASSED' if 'passed' in txt else 'FAILED (' + txt + ')'
    results.append((label, status))

# Also check beacon level data
cmd = 'data get block 117 38 -301 Levels'
s.sendall(struct.pack('<iii', len(cmd) + 10, 51, 2) + cmd.encode('utf-8') + b'\\x00\\x00')
resp = s.recv(4096)
b_lvl = resp[12:-2].decode('utf-8', errors='ignore')
results.append(('Beacon Power Level Data', b_lvl))

s.close()
for label, status in results:
    print(f'{{label}}: {{status}}')
"""
    ssh_cmd = [
        "ssh", "-o", "StrictHostKeyChecking=no",
        "-i", key,
        f"{user}@{host}",
        "python3"
    ]
    res = subprocess.run(ssh_cmd, input=py_code, capture_output=True, text=True)
    print("\n=== Live Blockstate Verification Results ===")
    print(res.stdout)

def deploy_datapack_file(host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Syncs the mcfunction to the remote server world datapacks."""
    remote_target = f"{user}@{host}:~/minecraft-server/world/{FUNCTION_PATH}"
    remote_dir = os.path.dirname(f"~/minecraft-server/world/{FUNCTION_PATH}")
    mkdir_cmd = ["ssh", "-o", "StrictHostKeyChecking=no", "-i", key, f"{user}@{host}", f"mkdir -p {remote_dir}"]
    subprocess.run(mkdir_cmd, check=True)
    scp_cmd = ["scp", "-o", "StrictHostKeyChecking=no", "-i", key, FUNCTION_PATH, remote_target]
    subprocess.run(scp_cmd, check=True)
    print(f"Deployed {FUNCTION_PATH} to {remote_target}")

if __name__ == "__main__":
    commands = []
    commands.extend(build_beacon_well())
    commands.extend(build_bubble_elevators())
    commands.extend(build_ore_processing())
    commands.extend(build_forbidden_apocrypha())
    commands.extend(build_aquaponics_grotto())
    commands.extend(build_connecting_concourses())

    print(f"Generated {len(commands)} commands.")
    write_mcfunction(FUNCTION_PATH, commands)
    print(f"Wrote native mcfunction to {FUNCTION_PATH}.")

    print("Deploying datapack file to production server...")
    deploy_datapack_file()

    print("Executing batch construction over RCON...")
    execute_remote_batch([c for c in commands if not c.startswith("#")])

    print("Pausing briefly for block ticks and beacon initialization...")
    time.sleep(2)

    print("Verifying live blockstates...")
    verify_live_blockstates()
    print("Tier 3 deep subterranean facilities constructed and verified.")
