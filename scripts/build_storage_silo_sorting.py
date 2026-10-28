#!/usr/bin/env python3
"""Build Sector 14 Automated Subterranean Storage Silo and Central Sorting System.

Generates Tier 3 Logistics Bay infrastructure at Y levels 36 to 45 directly beneath the Tool Armory.
Coordinates: X: 74..94, Z: -307..-295, Y: 36..45.
Includes:
1. Four tier vertical double chest storage columns along North and South walls.
2. Vertical hopper feeding lines, item sorting filters, redstone comparators, and repeaters.
3. Dual water bubble elevator (soul sand up, magma down) connecting Y: 36 to Tool Armory floor at Y: 46.
4. Central bulk inspection console with barrels, crafting stations, smooth quartz platforms, and hazard striping.
5. Transit terminal integration with Hyperloop Line 1 arrival and departure bays.
6. Illumination grid using lit copper bulbs and recessed sea lanterns.
"""

import math
import os
import subprocess
import sys
import time

DEFAULT_HOST = os.environ.get("HZ_HOST", "132.226.135.26")
DEFAULT_USER = os.environ.get("HZ_USER", "ubuntu")
DEFAULT_KEY = os.environ.get("HZ_KEY", os.path.expanduser("~/.ssh/id_ed25519"))

FUNCTION_PATH = "datapacks/underground_citadel/data/citadel/function/bunker_storage_silo.mcfunction"

def write_mcfunction(filepath, lines):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    clean_lines = [line.strip() for line in lines if line.strip()]
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(clean_lines) + "\n")
    return clean_lines

def build_perimeter_and_structure():
    """Generates structural excavation, walls, subfloor, main floor, and ceiling cap."""
    cmds = [
        "# Sector 14 Perimeter and Foundation (X: 74..94, Z: -307..-295, Y: 36..45)",
        # Clear interior volume from Y: 36 to Y: 45
        "fill 74 36 -307 94 45 -295 air",
        # Subfloor foundation layer at Y: 36
        "fill 74 36 -307 94 36 -295 polished_blackstone",
        # Main floor at Y: 37
        "fill 74 37 -307 94 37 -295 deepslate_tiles",
        # Walkway aisles at Y: 37
        "fill 75 37 -305 93 37 -304 smooth_stone",
        "fill 75 37 -298 93 37 -297 smooth_stone",
        # Ceiling cap at Y: 45 directly beneath Armory floor
        "fill 74 45 -307 94 45 -295 deepslate_tiles",
        # North wall at Z: -307
        "fill 74 36 -307 94 45 -307 deepslate_bricks",
        # South wall at Z: -295
        "fill 74 36 -295 94 45 -295 deepslate_bricks",
        # West wall at X: 74
        "fill 74 36 -307 74 45 -295 deepslate_bricks",
        # East wall at X: 94
        "fill 94 36 -307 94 45 -295 deepslate_bricks",
        # East entrance archway connecting Hyperloop Line 1 and pedestrian concourse
        "fill 94 38 -302 94 42 -300 air",
        "fill 94 38 -303 94 43 -303 chiseled_deepslate",
        "fill 94 38 -299 94 43 -299 chiseled_deepslate",
        "fill 94 43 -302 94 43 -300 polished_deepslate",
        # West wall architectural pilasters and decorative alcove
        "fill 74 37 -303 74 44 -303 chiseled_deepslate",
        "fill 74 37 -299 74 44 -299 chiseled_deepslate",
        "setblock 74 41 -301 sea_lantern",
        "setblock 74 40 -301 crying_obsidian",
        "setblock 74 39 -301 crying_obsidian",
    ]
    return cmds

def build_north_storage_columns():
    """Generates 4 tier vertical double chest columns along North wall (Z: -306)."""
    cmds = [
        "# North Wall Storage Columns (Z: -306, X: 75..93, Y: 38..44)",
    ]

    # Pilasters along North wall
    pilaster_xs = [75, 80, 85, 90, 93]
    for x in pilaster_xs:
        cmds.append(f"fill {x} 37 -306 {x} 44 -306 chiseled_deepslate")
        cmds.append(f"setblock {x} 41 -306 copper_bulb[lit=true,powered=false]")
        cmds.append(f"setblock {x} 37 -306 polished_blackstone")

    # Double chest columns (7 pairs)
    column_pairs = [
        (76, 77),
        (78, 79),
        (81, 82),
        (83, 84),
        (86, 87),
        (88, 89),
        (91, 92),
    ]

    for x1, x2 in column_pairs:
        # Floor base beneath chests
        cmds.append(f"setblock {x1} 37 -306 polished_blackstone_bricks")
        cmds.append(f"setblock {x2} 37 -306 polished_blackstone_bricks")

        # Tier 1 Double Chest at Y: 38
        cmds.append(f"setblock {x1} 38 -306 chest[facing=south,type=right]")
        cmds.append(f"setblock {x2} 38 -306 chest[facing=south,type=left]")

        # Hopper layer 1 at Y: 39 feeding into Tier 1 chest
        cmds.append(f"setblock {x1} 39 -306 hopper[facing=down]")
        cmds.append(f"setblock {x2} 39 -306 hopper[facing=down]")

        # Tier 2 Double Chest at Y: 40
        cmds.append(f"setblock {x1} 40 -306 chest[facing=south,type=right]")
        cmds.append(f"setblock {x2} 40 -306 chest[facing=south,type=left]")

        # Hopper layer 2 at Y: 41 feeding into Tier 2 chest
        cmds.append(f"setblock {x1} 41 -306 hopper[facing=down]")
        cmds.append(f"setblock {x2} 41 -306 hopper[facing=down]")

        # Tier 3 Double Chest at Y: 42
        cmds.append(f"setblock {x1} 42 -306 chest[facing=south,type=right]")
        cmds.append(f"setblock {x2} 42 -306 chest[facing=south,type=left]")

        # Hopper layer 3 at Y: 43 feeding into Tier 3 chest
        cmds.append(f"setblock {x1} 43 -306 hopper[facing=down]")
        cmds.append(f"setblock {x2} 43 -306 hopper[facing=down]")

        # Tier 4 Double Chest at Y: 44
        cmds.append(f"setblock {x1} 44 -306 chest[facing=south,type=right]")
        cmds.append(f"setblock {x2} 44 -306 chest[facing=south,type=left]")

        # Ceiling top slab at Y: 45 allowing Tier 4 double chest to open freely
        cmds.append(f"setblock {x1} 45 -306 deepslate_tile_slab[type=top]")
        cmds.append(f"setblock {x2} 45 -306 deepslate_tile_slab[type=top]")

    # Overhead horizontal sorting feed line at Z: -305, Y: 45
    # Running west from X: 92 to X: 76
    cmds.append("# North Sorting Feed Hopper Line (Z: -305, Y: 45)")
    for x in range(76, 93):
        cmds.append(f"setblock {x} 45 -305 hopper[facing=west]")

    # Sorting filters and redstone comparators along North gantry (Z: -305, Y: 44)
    cmds.append("# North Sorting Filters and Redstone Comparators")
    for px in [75, 80, 85, 90]:
        # Support block
        cmds.append(f"setblock {px} 43 -305 polished_deepslate")
        # Redstone comparator reading filter hoppers
        cmds.append(f"setblock {px} 44 -305 comparator[facing=south,mode=compare]")
        # Redstone repeater outputting to column latch
        cmds.append(f"setblock {px} 44 -304 repeater[facing=south,delay=1]")
        cmds.append(f"setblock {px} 43 -304 polished_deepslate")
        # Column sorting status indicator lamp
        cmds.append(f"setblock {px} 44 -303 copper_bulb[lit=true,powered=false]")

    return cmds

def build_south_storage_columns():
    """Generates 4 tier vertical double chest columns along South wall (Z: -296)."""
    cmds = [
        "# South Wall Storage Columns (Z: -296, X: 75..93, Y: 38..44)",
    ]

    # Pilasters along South wall (X: 83..85 reserved for dual bubble elevator)
    pilaster_xs = [75, 80, 86, 91]
    for x in pilaster_xs:
        cmds.append(f"fill {x} 37 -296 {x} 44 -296 chiseled_deepslate")
        cmds.append(f"setblock {x} 41 -296 copper_bulb[lit=true,powered=false]")
        cmds.append(f"setblock {x} 37 -296 polished_blackstone")

    # Double chest columns (6 pairs)
    column_pairs = [
        (76, 77),
        (78, 79),
        (81, 82),
        (87, 88),
        (89, 90),
        (92, 93),
    ]

    for x1, x2 in column_pairs:
        # Floor base beneath chests
        cmds.append(f"setblock {x1} 37 -296 polished_blackstone_bricks")
        cmds.append(f"setblock {x2} 37 -296 polished_blackstone_bricks")

        # Tier 1 Double Chest at Y: 38 (facing north)
        cmds.append(f"setblock {x1} 38 -296 chest[facing=north,type=left]")
        cmds.append(f"setblock {x2} 38 -296 chest[facing=north,type=right]")

        # Hopper layer 1 at Y: 39 feeding into Tier 1 chest
        cmds.append(f"setblock {x1} 39 -296 hopper[facing=down]")
        cmds.append(f"setblock {x2} 39 -296 hopper[facing=down]")

        # Tier 2 Double Chest at Y: 40
        cmds.append(f"setblock {x1} 40 -296 chest[facing=north,type=left]")
        cmds.append(f"setblock {x2} 40 -296 chest[facing=north,type=right]")

        # Hopper layer 2 at Y: 41 feeding into Tier 2 chest
        cmds.append(f"setblock {x1} 41 -296 hopper[facing=down]")
        cmds.append(f"setblock {x2} 41 -296 hopper[facing=down]")

        # Tier 3 Double Chest at Y: 42
        cmds.append(f"setblock {x1} 42 -296 chest[facing=north,type=left]")
        cmds.append(f"setblock {x2} 42 -296 chest[facing=north,type=right]")

        # Hopper layer 3 at Y: 43 feeding into Tier 3 chest
        cmds.append(f"setblock {x1} 43 -296 hopper[facing=down]")
        cmds.append(f"setblock {x2} 43 -296 hopper[facing=down]")

        # Tier 4 Double Chest at Y: 44
        cmds.append(f"setblock {x1} 44 -296 chest[facing=north,type=left]")
        cmds.append(f"setblock {x2} 44 -296 chest[facing=north,type=right]")

        # Ceiling top slab at Y: 45 allowing Tier 4 double chest to open freely
        cmds.append(f"setblock {x1} 45 -296 deepslate_tile_slab[type=top]")
        cmds.append(f"setblock {x2} 45 -296 deepslate_tile_slab[type=top]")

    # Overhead horizontal sorting feed line at Z: -297, Y: 45
    # Running east across columns (skipping elevator shaft at 83..85)
    cmds.append("# South Sorting Feed Hopper Line (Z: -297, Y: 45)")
    for x in range(76, 83):
        cmds.append(f"setblock {x} 45 -297 hopper[facing=east]")
    for x in range(86, 94):
        cmds.append(f"setblock {x} 45 -297 hopper[facing=east]")

    # Sorting filters and redstone comparators along South gantry (Z: -297, Y: 44)
    cmds.append("# South Sorting Filters and Redstone Comparators")
    for px in [75, 80, 86, 91]:
        cmds.append(f"setblock {px} 43 -297 polished_deepslate")
        cmds.append(f"setblock {px} 44 -297 comparator[facing=north,mode=compare]")
        cmds.append(f"setblock {px} 44 -298 repeater[facing=north,delay=1]")
        cmds.append(f"setblock {px} 43 -298 polished_deepslate")
        cmds.append(f"setblock {px} 44 -299 copper_bulb[lit=true,powered=false]")

    return cmds

def build_bubble_elevator():
    """Generates dual water bubble elevator connecting Tier 3 to Tool Armory floor at Y: 46."""
    cmds = [
        "# Dual Water Bubble Elevator (X: 83..85, Z: -296, Y: 36..47)",
        # Clear elevator shaft column from Y: 36 to Y: 47
        "fill 82 36 -296 86 47 -296 air",
        # Rear enclosure wall at Z: -295
        "fill 82 36 -295 86 47 -295 deepslate_bricks",
        # Internal shaft illumination fixtures
        "setblock 84 36 -295 sea_lantern",
        "setblock 84 41 -295 sea_lantern",
        "setblock 84 46 -295 sea_lantern",
        # Lateral enclosure walls at X: 82 and X: 86
        "fill 82 36 -296 82 47 -296 deepslate_tiles",
        "fill 86 36 -296 86 47 -296 deepslate_tiles",
        # Center divider between ascending and descending shafts
        "fill 84 36 -296 84 47 -296 tinted_glass",
        # Bases at Y: 36
        "setblock 83 36 -296 soul_sand",
        "setblock 85 36 -296 magma_block",
        # Bubble columns from Y: 37 up through Y: 46
        "fill 83 37 -296 83 46 -296 bubble_column[drag=false]",
        "fill 85 37 -296 85 46 -296 bubble_column[drag=true]",
        # Lower elevator entrance at Tier 3 Storage (Z: -297, Y: 37..38)
        "fill 83 37 -297 85 37 -297 polished_blackstone",
        "setblock 82 37 -297 polished_deepslate",
        "setblock 82 38 -297 polished_deepslate",
        "setblock 86 37 -297 polished_deepslate",
        "setblock 86 38 -297 polished_deepslate",
        "fill 84 37 -297 84 38 -297 tinted_glass",
        "setblock 83 38 -297 spruce_wall_sign[facing=east]",
        "setblock 85 38 -297 spruce_wall_sign[facing=west]",
        # Observation window into elevator shafts (Z: -297, Y: 39..45)
        "fill 83 39 -297 85 45 -297 tinted_glass",
        # Upper elevator entrance in Tool Armory (Z: -297, Y: 46..47)
        "fill 83 46 -297 85 46 -297 polished_andesite",
        "setblock 82 46 -297 polished_andesite",
        "setblock 82 47 -297 polished_andesite",
        "setblock 86 46 -297 polished_andesite",
        "setblock 86 47 -297 polished_andesite",
        "fill 84 46 -297 84 47 -297 tinted_glass",
        "setblock 83 47 -297 spruce_wall_sign[facing=east]",
        "setblock 85 47 -297 spruce_wall_sign[facing=west]",
        # Upper direction indicator lintel at Y: 48 in Tool Armory
        "setblock 83 48 -296 emerald_block",
        "setblock 84 48 -296 copper_bulb[lit=true,powered=false]",
        "setblock 85 48 -296 redstone_block",
        "setblock 82 48 -296 polished_deepslate",
        "setblock 86 48 -296 polished_deepslate",
        "fill 83 48 -297 85 48 -297 polished_andesite_stairs[facing=north,half=bottom]",
    ]
    return cmds

def build_inspection_console_and_hazard_striping():
    """Generates central bulk inspection console, quartz platforms, and safety hazard striping."""
    cmds = [
        "# Central Bulk Inspection Console and Hazard Safety Striping",
        # Hazard concrete perimeter border around West Console Island (X: 76..82, Z: -303..-298 at Y: 37)
        "setblock 76 37 -303 yellow_concrete",
        "setblock 77 37 -303 black_concrete",
        "setblock 78 37 -303 yellow_concrete",
        "setblock 79 37 -303 black_concrete",
        "setblock 80 37 -303 yellow_concrete",
        "setblock 81 37 -303 black_concrete",
        "setblock 82 37 -303 yellow_concrete",

        "setblock 76 37 -298 black_concrete",
        "setblock 77 37 -298 yellow_concrete",
        "setblock 78 37 -298 black_concrete",
        "setblock 79 37 -298 yellow_concrete",
        "setblock 80 37 -298 black_concrete",
        "setblock 81 37 -298 yellow_concrete",
        "setblock 82 37 -298 black_concrete",

        "setblock 76 37 -302 black_concrete",
        "setblock 76 37 -301 yellow_concrete",
        "setblock 76 37 -300 black_concrete",
        "setblock 76 37 -299 yellow_concrete",

        "setblock 82 37 -302 black_concrete",
        "setblock 82 37 -301 yellow_concrete",
        "setblock 82 37 -300 black_concrete",
        "setblock 82 37 -299 yellow_concrete",

        # Smooth quartz platform foundation inside console island (X: 77..81, Z: -302..-299 at Y: 37)
        "fill 77 37 -302 81 37 -299 smooth_quartz",

        # Elevated quartz counter bases at Y: 38
        "setblock 77 38 -302 smooth_quartz",
        "setblock 81 38 -302 smooth_quartz",
        "setblock 77 38 -299 smooth_quartz",
        "setblock 81 38 -299 smooth_quartz",

        # Bulk inspection intake barrels
        "setblock 77 38 -301 barrel[facing=up]",
        "setblock 77 38 -300 barrel[facing=up]",
        "setblock 79 38 -301 barrel[facing=up]",
        "setblock 79 38 -300 barrel[facing=up]",
        "setblock 81 38 -301 barrel[facing=up]",
        "setblock 81 38 -300 barrel[facing=up]",

        # Inspection intake hoppers above barrels at Y: 39
        "setblock 77 39 -301 hopper[facing=down]",
        "setblock 79 39 -301 hopper[facing=down]",
        "setblock 81 39 -301 hopper[facing=down]",

        # Appraisal and fabrication stations at Y: 38
        "setblock 78 38 -302 crafting_table",
        "setblock 80 38 -302 smithing_table",
        "setblock 78 38 -299 grindstone[face=floor,facing=north]",
        "setblock 80 38 -299 cartography_table",

        # Heavy metallurgical testing station at West flank
        "setblock 76 38 -301 anvil[facing=east]",
        "setblock 76 38 -300 heavy_core",

        # Manifest inspection podium at East flank
        "setblock 82 38 -300 lectern[facing=east]",

        # Redstone comparators and repeaters reading bulk intake barrels
        "setblock 78 38 -301 smooth_quartz",
        "setblock 78 39 -302 comparator[facing=north,mode=compare]",
        "setblock 80 38 -301 smooth_quartz",
        "setblock 80 39 -302 comparator[facing=north,mode=compare]",
        "setblock 78 39 -299 repeater[facing=south,delay=1]",
        "setblock 80 39 -299 repeater[facing=south,delay=1]",
        "setblock 79 39 -302 copper_bulb[lit=true,powered=false]",
        "setblock 79 39 -299 copper_bulb[lit=true,powered=false]",

        # Overhead inspection lighting canopy at Y: 42
        "fill 77 42 -301 81 42 -300 deepslate_tiles",
        "setblock 78 42 -301 copper_bulb[lit=true,powered=false]",
        "setblock 80 42 -301 sea_lantern",
        "setblock 78 42 -300 sea_lantern",
        "setblock 80 42 -300 copper_bulb[lit=true,powered=false]",
        "fill 77 39 -302 77 41 -302 polished_deepslate_wall",
        "fill 81 39 -302 81 41 -302 polished_deepslate_wall",
        "fill 77 39 -299 77 41 -299 polished_deepslate_wall",
        "fill 81 39 -299 81 41 -299 polished_deepslate_wall",

        # Transit Platform Hazard Striping along track edges (X: 84..93)
        # Hazard stripe along North edge of Line 1 track (Z: -302)
        "setblock 84 37 -302 yellow_concrete",
        "setblock 85 37 -302 black_concrete",
        "setblock 86 37 -302 yellow_concrete",
        "setblock 87 37 -302 black_concrete",
        "setblock 88 37 -302 yellow_concrete",
        "setblock 89 37 -302 black_concrete",
        "setblock 90 37 -302 yellow_concrete",
        "setblock 91 37 -302 black_concrete",
        "setblock 92 37 -302 yellow_concrete",
        "setblock 93 37 -302 black_concrete",

        # Hazard stripe between tracks (Z: -300)
        "setblock 84 37 -300 black_concrete",
        "setblock 85 37 -300 yellow_concrete",
        "setblock 86 37 -300 black_concrete",
        "setblock 87 37 -300 yellow_concrete",
        "setblock 88 37 -300 black_concrete",
        "setblock 89 37 -300 yellow_concrete",
        "setblock 90 37 -300 black_concrete",
        "setblock 91 37 -300 yellow_concrete",
        "setblock 92 37 -300 black_concrete",
        "setblock 93 37 -300 yellow_concrete",

        # Hazard stripe along South edge of departure track (Z: -298)
        "setblock 84 37 -298 yellow_concrete",
        "setblock 85 37 -298 black_concrete",
        "setblock 86 37 -298 yellow_concrete",
        "setblock 87 37 -298 black_concrete",
        "setblock 88 37 -298 yellow_concrete",
        "setblock 89 37 -298 black_concrete",
        "setblock 90 37 -298 yellow_concrete",
        "setblock 91 37 -298 black_concrete",
        "setblock 92 37 -298 yellow_concrete",
        "setblock 93 37 -298 black_concrete",

        # Line 1 West Arrival Terminus (Z: -301)
        "setblock 86 38 -301 detector_rail[shape=east_west]",
        "setblock 85 37 -301 smooth_basalt",
        "setblock 85 38 -301 powered_rail[shape=east_west]",
        "setblock 84 37 -301 chest[facing=north]",
        "setblock 84 38 -301 hopper[facing=down]",
        "setblock 83 38 -301 polished_blackstone",
        "setblock 83 39 -301 iron_bars",

        # Line 1 West Departure Bay (Z: -299)
        "setblock 83 38 -299 polished_blackstone",
        "setblock 83 39 -299 dispenser[facing=east]{Items:[{Slot:0b,id:\"minecraft:minecart\",count:64}]}",
        "setblock 83 40 -299 stone_button[facing=north,face=floor]",
        "setblock 84 37 -299 redstone_block",
        "setblock 84 38 -299 powered_rail[shape=east_west]",
        "fill 85 38 -299 93 38 -299 rail[shape=east_west]",
        "setblock 89 37 -299 redstone_block",
        "setblock 89 38 -299 powered_rail[shape=east_west]",

        # Staging cargo barrels along transit platform
        "setblock 88 38 -303 barrel[facing=up]",
        "setblock 89 38 -303 barrel[facing=up]",
        "setblock 91 38 -303 barrel[facing=up]",
        "setblock 88 38 -298 barrel[facing=up]",
        "setblock 89 38 -298 barrel[facing=up]",
        "setblock 91 38 -298 barrel[facing=up]",
    ]
    return cmds

def build_illumination_grid():
    """Generates complete overhead and perimeter illumination ensuring light level at or above 10."""
    cmds = [
        "# Illumination Grid (Lit Copper Bulbs and Recessed Sea Lanterns)",
        # Overhead ceiling grid at Y: 45
        # Row 1 at Z: -304
        "setblock 76 45 -304 copper_bulb[lit=true,powered=false]",
        "setblock 80 45 -304 sea_lantern",
        "setblock 84 45 -304 copper_bulb[lit=true,powered=false]",
        "setblock 88 45 -304 sea_lantern",
        "setblock 92 45 -304 copper_bulb[lit=true,powered=false]",

        # Row 2 at Z: -301
        "setblock 76 45 -301 sea_lantern",
        "setblock 80 45 -301 copper_bulb[lit=true,powered=false]",
        "setblock 85 45 -301 sea_lantern",
        "setblock 90 45 -301 copper_bulb[lit=true,powered=false]",

        # Row 3 at Z: -298
        "setblock 76 45 -298 copper_bulb[lit=true,powered=false]",
        "setblock 80 45 -298 sea_lantern",
        "setblock 84 45 -298 copper_bulb[lit=true,powered=false]",
        "setblock 88 45 -298 sea_lantern",
        "setblock 92 45 -298 copper_bulb[lit=true,powered=false]",

        # Floor recessed safety lanterns at Y: 37 along walkway centerlines
        "setblock 78 37 -304 sea_lantern",
        "setblock 86 37 -304 sea_lantern",
        "setblock 90 37 -304 sea_lantern",
        "setblock 78 37 -298 sea_lantern",
        "setblock 88 37 -298 sea_lantern",
        "setblock 92 37 -298 sea_lantern",

        # Task lighting on West inspection console
        "setblock 77 40 -301 copper_bulb[lit=true,powered=false]",
        "setblock 81 40 -301 copper_bulb[lit=true,powered=false]",
    ]
    return cmds

def execute_remote_batch(commands, host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Executes list of commands over RCON socket via SSH on production server."""
    batch_size = 80
    total = len(commands)
    print(f"Executing {total} commands in batches of {batch_size}...")

    for i in range(0, total, batch_size):
        batch = commands[i:i + batch_size]
        py_code = f"""
import socket, struct

with open('/home/ubuntu/minecraft-server/server.properties') as f:
    props = dict(line.strip().split('=', 1) for line in f if '=' in line and not line.startswith('#'))

rcon_port = int(props.get('rcon.port', 25575))
rcon_pass = props.get('rcon.password', '')

s = socket.create_connection(('127.0.0.1', rcon_port), timeout=15)
s.sendall(struct.pack('<iii', len(rcon_pass) + 10, 1, 3) + rcon_pass.encode('utf-8') + b'\\x00\\x00')
s.recv(4096)

cmds = {repr(batch)}
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
    """Verifies live blockstates of constructed Sector 14 facilities via RCON."""
    checks = [
        # North wall vertical double chest column checks
        ("North Col 1 Tier 1 Double Chest (X: 76)", "execute if block 76 38 -306 chest[facing=south,type=right]"),
        ("North Col 1 Tier 1 Double Chest (X: 77)", "execute if block 77 38 -306 chest[facing=south,type=left]"),
        ("North Col 1 Tier 1 Hopper (X: 76)", "execute if block 76 39 -306 hopper[facing=down]"),
        ("North Col 1 Tier 2 Double Chest (X: 76)", "execute if block 76 40 -306 chest[facing=south,type=right]"),
        ("North Col 1 Tier 3 Double Chest (X: 76)", "execute if block 76 42 -306 chest[facing=south,type=right]"),
        ("North Col 1 Tier 4 Double Chest (X: 76)", "execute if block 76 44 -306 chest[facing=south,type=right]"),
        ("North Col 4 Tier 4 Double Chest (X: 84)", "execute if block 84 44 -306 chest[facing=south,type=left]"),
        ("North Col 7 Tier 4 Double Chest (X: 92)", "execute if block 92 44 -306 chest[facing=south,type=left]"),
        ("North Feed Line Hopper (X: 80)", "execute if block 80 45 -305 hopper[facing=west]"),
        ("North Redstone Comparator (X: 80)", "execute if block 80 44 -305 comparator[facing=south]"),
        ("North Redstone Repeater (X: 80)", "execute if block 80 44 -304 repeater[facing=south]"),

        # South wall vertical double chest column checks
        ("South Col 1 Tier 1 Double Chest (X: 76)", "execute if block 76 38 -296 chest[facing=north,type=left]"),
        ("South Col 1 Tier 1 Double Chest (X: 77)", "execute if block 77 38 -296 chest[facing=north,type=right]"),
        ("South Col 1 Tier 4 Double Chest (X: 76)", "execute if block 76 44 -296 chest[facing=north,type=left]"),
        ("South Col 6 Tier 4 Double Chest (X: 93)", "execute if block 93 44 -296 chest[facing=north,type=right]"),
        ("South Feed Line Hopper (X: 80)", "execute if block 80 45 -297 hopper[facing=east]"),
        ("South Redstone Comparator (X: 80)", "execute if block 80 44 -297 comparator[facing=north]"),

        # Dual water bubble elevator checks
        ("Soul Sand Elevator Base (X: 83)", "execute if block 83 36 -296 soul_sand"),
        ("Soul Sand Bubble Column (X: 83, Y: 37)", "execute if block 83 37 -296 bubble_column[drag=false]"),
        ("Soul Sand Bubble Column Top (X: 83, Y: 46)", "execute if block 83 46 -296 bubble_column[drag=false]"),
        ("Magma Elevator Base (X: 85)", "execute if block 85 36 -296 magma_block"),
        ("Magma Bubble Column (X: 85, Y: 37)", "execute if block 85 37 -296 bubble_column[drag=true]"),
        ("Magma Bubble Column Top (X: 85, Y: 46)", "execute if block 85 46 -296 bubble_column[drag=true]"),
        ("Elevator Tinted Divider (X: 84, Y: 40)", "execute if block 84 40 -296 tinted_glass"),
        ("Elevator Lower Sign Barrier", "execute if block 83 38 -297 spruce_wall_sign[facing=east]"),
        ("Elevator Upper Sign Barrier", "execute if block 83 47 -297 spruce_wall_sign[facing=east]"),
        ("Elevator Upper Up Indicator", "execute if block 83 48 -296 emerald_block"),
        ("Elevator Upper Down Indicator", "execute if block 85 48 -296 redstone_block"),

        # Central inspection console checks
        ("Console Quartz Floor", "execute if block 79 37 -300 smooth_quartz"),
        ("Console Intake Barrel 1", "execute if block 77 38 -301 barrel[facing=up]"),
        ("Console Intake Hopper 1", "execute if block 77 39 -301 hopper[facing=down]"),
        ("Console Crafting Table", "execute if block 78 38 -302 crafting_table"),
        ("Console Smithing Table", "execute if block 80 38 -302 smithing_table"),
        ("Console Testing Anvil", "execute if block 76 38 -301 anvil[facing=east]"),
        ("Console Heavy Core", "execute if block 76 38 -300 heavy_core"),
        ("Console Manifest Lectern", "execute if block 82 38 -300 lectern[facing=east]"),
        ("Console Redstone Comparator", "execute if block 78 39 -302 comparator[facing=north]"),

        # Hazard concrete striping checks
        ("Console Hazard Stripe (Yellow)", "execute if block 76 37 -303 yellow_concrete"),
        ("Console Hazard Stripe (Black)", "execute if block 77 37 -303 black_concrete"),
        ("Rail Hazard Stripe (Yellow)", "execute if block 84 37 -302 yellow_concrete"),
        ("Rail Hazard Stripe (Black)", "execute if block 85 37 -302 black_concrete"),

        # Rail terminus checks
        ("Line 1 Hopper Terminus", "execute if block 84 38 -301 hopper[facing=down]"),
        ("Line 1 Storage Chest", "execute if block 84 37 -301 chest[facing=north]"),
        ("Line 1 Detector Rail", "execute if block 86 38 -301 detector_rail[shape=east_west]"),
        ("Line 1 Departure Dispenser", "execute if block 83 39 -299 dispenser[facing=east]"),
        ("Line 1 Departure Powered Rail", "execute if block 84 38 -299 powered_rail[shape=east_west,powered=true]"),

        # Illumination checks
        ("Overhead Copper Bulb (Lit)", "execute if block 76 45 -304 copper_bulb[lit=true,powered=false]"),
        ("Overhead Sea Lantern", "execute if block 80 45 -304 sea_lantern"),
        ("Mid Pilaster Copper Bulb", "execute if block 80 41 -306 copper_bulb[lit=true,powered=false]"),
        ("Floor Recessed Sea Lantern", "execute if block 78 37 -304 sea_lantern"),
    ]

    py_code = f"""
import socket, struct

with open('/home/ubuntu/minecraft-server/server.properties') as f:
    props = dict(line.strip().split('=', 1) for line in f if '=' in line and not line.startswith('#'))

rcon_port = int(props.get('rcon.port', 25575))
rcon_pass = props.get('rcon.password', '')

s = socket.create_connection(('127.0.0.1', rcon_port), timeout=15)
s.sendall(struct.pack('<iii', len(rcon_pass) + 10, 1, 3) + rcon_pass.encode('utf-8') + b'\\x00\\x00')
s.recv(4096)

checks = {repr(checks)}
results = []
all_passed = True
for label, cmd in checks:
    s.sendall(struct.pack('<iii', len(cmd) + 10, 50, 2) + cmd.encode('utf-8') + b'\\x00\\x00')
    resp = s.recv(4096)
    txt = resp[12:-2].decode('utf-8', errors='ignore')
    status = 'PASSED' if 'passed' in txt else 'FAILED (' + txt + ')'
    if 'passed' not in txt:
        all_passed = False
    results.append((label, status))

# Datapack reload verification
cmd = 'reload'
s.sendall(struct.pack('<iii', len(cmd) + 10, 51, 2) + cmd.encode('utf-8') + b'\\x00\\x00')
resp = s.recv(4096)
reload_txt = resp[12:-2].decode('utf-8', errors='ignore')
results.append(('Datapack Reload', reload_txt))

s.close()
for label, status in results:
    print(f'{{label}}: {{status}}')

if not all_passed:
    exit(1)
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
    if res.returncode != 0:
        print("Verification failures detected:", res.stderr, file=sys.stderr)
        sys.exit(res.returncode)

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
    commands.extend(build_perimeter_and_structure())
    commands.extend(build_north_storage_columns())
    commands.extend(build_south_storage_columns())
    commands.extend(build_bubble_elevator())
    commands.extend(build_inspection_console_and_hazard_striping())
    commands.extend(build_illumination_grid())

    print(f"Generated {len(commands)} commands.")
    write_mcfunction(FUNCTION_PATH, commands)
    print(f"Wrote native mcfunction to {FUNCTION_PATH}.")

    print("Deploying datapack file to production server...")
    deploy_datapack_file()

    print("Executing batch construction over RCON...")
    execute_remote_batch([c for c in commands if not c.startswith("#")])

    print("Pausing briefly for block ticks and water column stabilization...")
    time.sleep(2)

    print("Verifying live blockstates...")
    verify_live_blockstates()
    print("Sector 14 Automated Storage Silo and Sorting System complete.")
