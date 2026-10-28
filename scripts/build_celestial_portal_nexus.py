#!/usr/bin/env python3
"""Build the Celestial Portal Nexus dimensional chamber for King Abir's bunker.

Constructs the monumental Stargate Chamber immediately south of Parliament.
Features include:
1. Connecting vaulted archway from Parliament dais (Z: -235).
2. Monumental 5-wide by 7-tall active Nether Portal Stargate on south wall.
3. Sunken 5x5 End Portal Sanctum with complete 3x3 ring of 12 eyes and active portal.
4. Integrated Amethyst Geode Sanctuary with tinted glass observation panels.
5. Vaulted ceilings with structural ribs, lit copper bulbs, and hanging soul lanterns.
6. Concealed sea lanterns beneath copper floor grates, soul fire braziers, and respawn anchors.
Strictly obeys ceiling invariant Y <= 53 and floor datum Y: 46 (deep basin Y: 44).
"""

import os
import subprocess
import sys

DEFAULT_HOST = os.environ.get("HZ_HOST", "132.226.135.26")
DEFAULT_USER = os.environ.get("HZ_USER", "ubuntu")
DEFAULT_KEY = os.environ.get("HZ_KEY", os.path.expanduser("~/.ssh/id_ed25519"))

REPO_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FUNCTION_REL = "datapacks/underground_citadel/data/citadel/function"
FUNCTION_DIR = os.path.join(REPO_BASE, FUNCTION_REL)

def write_mcfunction(name, lines):
    os.makedirs(FUNCTION_DIR, exist_ok=True)
    filepath = os.path.join(FUNCTION_DIR, name)
    clean_lines = [line.strip() for line in lines if line.strip()]
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(clean_lines) + "\n")
    print(f"Wrote {len(clean_lines)} commands to {filepath}")
    return clean_lines

def build_chamber_shell():
    """Excavates the main chamber and frames the solid perimeter walls and ceiling."""
    cmds = [
        "# Celestial Portal Nexus Chamber Shell (X: 107..127, Z: -233..-210, Y: 44..53)",
        # Solid ceiling cap strictly at Y: 53
        "fill 107 53 -233 127 53 -210 deepslate_tiles",
        # Clear interior volume
        "fill 108 47 -232 126 52 -211 air",
        # Master floor base at Y: 46
        "fill 107 46 -233 127 46 -210 polished_blackstone",
        # Perimeter Walls
        "fill 107 46 -233 127 52 -233 deepslate_tiles",
        "fill 107 46 -210 127 52 -210 deepslate_tiles",
        "fill 107 46 -233 107 52 -210 deepslate_tiles",
        "fill 127 46 -233 127 52 -210 deepslate_tiles",
        # Corner Structural Pillars
        "fill 107 46 -233 107 52 -233 crying_obsidian",
        "fill 127 46 -233 127 52 -233 crying_obsidian",
        "fill 107 46 -210 107 52 -210 crying_obsidian",
        "fill 127 46 -210 127 52 -210 crying_obsidian",
    ]
    return cmds

def build_connecting_archway():
    """Generates the vaulted passageway connecting Parliament to the Nexus."""
    cmds = [
        "# Connecting Portal Hallway (X: 115..119, Z: -236..-234, Y: 46..51)",
        # Excavate clear interior passage
        "fill 116 47 -236 118 51 -234 air",
        # Floor base
        "fill 115 46 -236 119 46 -234 polished_blackstone",
        # Carpet runner extending from Parliament dais
        "fill 117 47 -236 117 47 -234 red_carpet",
        "fill 116 47 -236 116 47 -234 yellow_carpet",
        "fill 118 47 -236 118 47 -234 yellow_carpet",
        # Ceiling backing at strictly Y: 53
        "fill 115 53 -236 119 53 -234 deepslate_tiles",
        # Hallway archway ceiling at Y: 52
        "fill 116 52 -236 118 52 -234 polished_deepslate",
        "fill 115 52 -236 115 52 -234 polished_deepslate_stairs[facing=east,half=top]",
        "fill 119 52 -236 119 52 -234 polished_deepslate_stairs[facing=west,half=top]",
        # Side Walls and Crying Obsidian Pilasters
        "fill 115 46 -236 115 51 -236 deepslate_bricks",
        "fill 119 46 -236 119 51 -236 deepslate_bricks",
        "fill 115 46 -235 115 51 -235 crying_obsidian",
        "fill 119 46 -235 119 51 -235 crying_obsidian",
        "fill 115 46 -234 115 51 -234 deepslate_bricks",
        "fill 119 46 -234 119 51 -234 deepslate_bricks",
        # Hallway Keystone and Illumination
        "setblock 117 53 -235 copper_bulb[lit=true,powered=false]",
        "setblock 117 52 -235 iron_chain[axis=y]",
        "setblock 117 51 -235 soul_lantern[hanging=true]",
        # North Portal Archway Entry into Chamber at Z = -233
        "fill 116 47 -233 118 51 -233 air",
        "setblock 115 47 -233 crying_obsidian",
        "setblock 115 48 -233 crying_obsidian",
        "setblock 115 49 -233 crying_obsidian",
        "setblock 115 50 -233 crying_obsidian",
        "setblock 115 51 -233 polished_deepslate_stairs[facing=east,half=top]",
        "setblock 119 47 -233 crying_obsidian",
        "setblock 119 48 -233 crying_obsidian",
        "setblock 119 49 -233 crying_obsidian",
        "setblock 119 50 -233 crying_obsidian",
        "setblock 119 51 -233 polished_deepslate_stairs[facing=west,half=top]",
        "setblock 117 52 -233 polished_deepslate",
    ]
    return cmds

def build_floor_and_lighting():
    """Generates geometric floor patterns and concealed sea lanterns under copper grates."""
    cmds = [
        "# Floor Inlays and Concealed Grate Illumination Grid (Floor Y: 46, Deep Y: 45)",
        # Central ceremonial approach aisle
        "fill 116 46 -232 118 46 -226 deepslate_tiles",
        "fill 117 46 -232 117 46 -226 polished_blackstone",
        "fill 116 46 -216 118 46 -212 deepslate_tiles",
        "fill 117 46 -216 117 46 -212 polished_blackstone",
    ]

    # Grid of concealed sea lanterns beneath copper grates at Y: 45..46
    # Provides uniform illumination with zero mob spawning
    grate_locations = [
        # West aisle grates (X: 111)
        (111, -230), (111, -226), (111, -221), (111, -216), (111, -212),
        # East aisle grates (X: 122)
        (122, -230), (122, -226), (122, -221), (122, -216), (122, -212),
        # Intermediate grates flanking central sanctum (X: 113 and 121)
        (113, -230), (121, -230),
        (113, -212), (121, -212),
        # Lateral transverse crossway grates
        (114, -226), (120, -226),
        (114, -216), (120, -216),
    ]

    for gx, gz in grate_locations:
        cmds.append(f"setblock {gx} 45 {gz} sea_lantern")
        cmds.append(f"setblock {gx} 46 {gz} copper_grate")

    return cmds

def build_vaulted_ceiling_nexus():
    """Constructs vaulted barrel arches and structural transverse ribs across the chamber."""
    cmds = [
        "# Vaulted Ceiling and Structural Arch Ribs (Y: 50..53, Ceiling Cap Y: 53)",
        # Solid ceiling cap backing
        "fill 108 53 -232 126 53 -211 deepslate_tiles",
    ]

    # Transverse arch ribs every 4 blocks along Z: -231, -227, -223, -219, -215
    rib_z_coords = [-231, -227, -223, -219, -215]

    for rz in rib_z_coords:
        cmds.append(f"# Transverse Arch Rib at Z = {rz}")
        # Supportive Wall Pilasters and Corbels at Y: 50
        # West Wall Pilaster (X: 108)
        cmds.append(f"fill 108 46 {rz} 108 49 {rz} chiseled_deepslate")
        cmds.append(f"setblock 108 50 {rz} polished_deepslate_stairs[facing=east,half=top]")
        cmds.append(f"setblock 108 51 {rz} deepslate_bricks")
        cmds.append(f"setblock 108 52 {rz} polished_deepslate")

        # East Wall Pilaster (X: 126)
        cmds.append(f"fill 126 46 {rz} 126 49 {rz} chiseled_deepslate")
        cmds.append(f"setblock 126 50 {rz} polished_deepslate_stairs[facing=west,half=top]")
        cmds.append(f"setblock 126 51 {rz} deepslate_bricks")
        cmds.append(f"setblock 126 52 {rz} polished_deepslate")

        # Arch Rib curve down from Y: 53 to Y: 50
        # West springers (X: 109..110)
        cmds.append(f"setblock 109 50 {rz} polished_deepslate_stairs[facing=east,half=top]")
        cmds.append(f"setblock 109 51 {rz} polished_deepslate_stairs[facing=east,half=top]")
        cmds.append(f"setblock 110 51 {rz} polished_deepslate_stairs[facing=east,half=top]")
        cmds.append(f"setblock 110 52 {rz} polished_deepslate")

        # East springers (X: 124..125)
        cmds.append(f"setblock 125 50 {rz} polished_deepslate_stairs[facing=west,half=top]")
        cmds.append(f"setblock 125 51 {rz} polished_deepslate_stairs[facing=west,half=top]")
        cmds.append(f"setblock 124 51 {rz} polished_deepslate_stairs[facing=west,half=top]")
        cmds.append(f"setblock 124 52 {rz} polished_deepslate")

        # Overhead transverse arch beam at Y: 52
        cmds.append(f"fill 111 52 {rz} 123 52 {rz} polished_deepslate")

        # Keystone 1: Center Keystone (X: 117)
        cmds.append(f"setblock 117 53 {rz} copper_bulb[lit=true,powered=false]")
        cmds.append(f"setblock 117 52 {rz} iron_chain[axis=y]")
        cmds.append(f"setblock 117 51 {rz} soul_lantern[hanging=true]")

        # Keystone 2: West Keystone (X: 112)
        cmds.append(f"setblock 112 53 {rz} copper_bulb[lit=true,powered=false]")
        cmds.append(f"setblock 112 52 {rz} iron_chain[axis=y]")
        cmds.append(f"setblock 112 51 {rz} soul_lantern[hanging=true]")

        # Keystone 3: East Keystone (X: 122)
        cmds.append(f"setblock 122 53 {rz} copper_bulb[lit=true,powered=false]")
        cmds.append(f"setblock 122 52 {rz} iron_chain[axis=y]")
        cmds.append(f"setblock 122 51 {rz} soul_lantern[hanging=true]")

    # Coffered Bays between ribs at Y: 52..53
    for i in range(len(rib_z_coords) - 1):
        z_start = rib_z_coords[i] + 1
        z_end = rib_z_coords[i + 1] - 1

        cmds.append(f"# Coffered Bay: Z = {z_start}..{z_end}")
        # Recessed polished blackstone central panels at Y: 53
        cmds.append(f"fill 113 53 {z_start} 116 53 {z_end} polished_blackstone")
        cmds.append(f"fill 118 53 {z_start} 121 53 {z_end} polished_blackstone")

        # Vault side contours at Y: 52
        for z in range(z_start, z_end + 1):
            cmds.append(f"setblock 109 52 {z} deepslate_tile_stairs[facing=east,half=top]")
            cmds.append(f"setblock 125 52 {z} deepslate_tile_stairs[facing=west,half=top]")
            cmds.append(f"setblock 113 52 {z} deepslate_tile_stairs[facing=east,half=top]")
            cmds.append(f"setblock 116 52 {z} deepslate_tile_stairs[facing=west,half=top]")
            cmds.append(f"setblock 118 52 {z} deepslate_tile_stairs[facing=east,half=top]")
            cmds.append(f"setblock 121 52 {z} deepslate_tile_stairs[facing=west,half=top]")

        # Longitudinal coffer framing
        cmds.append(f"fill 114 52 {z_start} 115 52 {z_start} deepslate_tile_stairs[facing=south,half=top]")
        cmds.append(f"fill 114 52 {z_end} 115 52 {z_end} deepslate_tile_stairs[facing=north,half=top]")
        cmds.append(f"fill 119 52 {z_start} 120 52 {z_start} deepslate_tile_stairs[facing=south,half=top]")
        cmds.append(f"fill 119 52 {z_end} 120 52 {z_end} deepslate_tile_stairs[facing=north,half=top]")

    # Southern bay ceiling between Z: -214 and Z: -212
    cmds.append("# Southern Vault Bay (Z: -214..-212)")
    cmds.append("fill 113 53 -214 116 53 -212 polished_blackstone")
    cmds.append("fill 118 53 -214 121 53 -212 polished_blackstone")
    for z in range(-214, -211):
        cmds.append(f"setblock 109 52 {z} deepslate_tile_stairs[facing=east,half=top]")
        cmds.append(f"setblock 125 52 {z} deepslate_tile_stairs[facing=west,half=top]")
        cmds.append(f"setblock 113 52 {z} deepslate_tile_stairs[facing=east,half=top]")
        cmds.append(f"setblock 116 52 {z} deepslate_tile_stairs[facing=west,half=top]")
        cmds.append(f"setblock 118 52 {z} deepslate_tile_stairs[facing=east,half=top]")
        cmds.append(f"setblock 121 52 {z} deepslate_tile_stairs[facing=west,half=top]")
    cmds.append("fill 114 52 -214 115 52 -214 deepslate_tile_stairs[facing=south,half=top]")
    cmds.append("fill 119 52 -214 120 52 -214 deepslate_tile_stairs[facing=south,half=top]")

    return cmds

def build_amethyst_geode_sanctuary():
    """Constructs the integrated Amethyst Geode Sanctuary along the eastern wall."""
    cmds = [
        "# Amethyst Geode Sanctuary (X: 124..127, Z: -225..-217, Y: 46..52)",
        # Outer Smooth Basalt Geode Casing
        "fill 127 46 -225 127 52 -217 smooth_basalt",
        "fill 124 46 -225 126 46 -225 smooth_basalt",
        "fill 124 46 -217 126 46 -217 smooth_basalt",
        "fill 124 52 -225 126 52 -225 smooth_basalt",
        "fill 124 52 -217 126 52 -217 smooth_basalt",
        "fill 124 46 -224 126 46 -218 smooth_basalt",
        "fill 124 52 -224 126 52 -218 smooth_basalt",
        # Calcite Lining Layer
        "fill 126 47 -224 126 51 -218 calcite",
        "fill 125 47 -224 125 47 -218 calcite",
        "fill 125 51 -224 125 51 -218 calcite",
        "fill 125 48 -224 125 50 -224 calcite",
        "fill 125 48 -218 125 50 -218 calcite",
        # Open interior crystal hollow
        "fill 125 48 -223 125 50 -219 air",
        # Amethyst Block Shell and Budding Matrix
        "fill 126 48 -223 126 50 -219 amethyst_block",
        "setblock 126 49 -221 budding_amethyst",
        "setblock 126 49 -222 budding_amethyst",
        "setblock 126 49 -220 budding_amethyst",
        "setblock 125 47 -221 budding_amethyst",
        "setblock 125 51 -221 budding_amethyst",
        # Blooming Amethyst Clusters inside the hollow
        "setblock 125 48 -221 amethyst_cluster[facing=up]",
        "setblock 125 50 -221 amethyst_cluster[facing=down]",
        "setblock 125 49 -221 amethyst_cluster[facing=west]",
        "setblock 125 49 -222 amethyst_cluster[facing=south]",
        "setblock 125 49 -220 amethyst_cluster[facing=north]",
        "setblock 125 48 -222 large_amethyst_bud[facing=up]",
        "setblock 125 48 -220 large_amethyst_bud[facing=up]",
        # Concealed Geode Ambient Illumination
        "setblock 126 47 -221 sea_lantern",
        # Tinted Glass Observation Panels facing into main chamber at X = 124
        "fill 124 47 -224 124 51 -218 tinted_glass",
        # Polished Deepslate Framing and Arch Corbels around Observation Window
        "fill 123 46 -225 123 51 -225 chiseled_deepslate",
        "setblock 123 52 -225 polished_deepslate_stairs[facing=west,half=top]",
        "fill 123 46 -217 123 51 -217 chiseled_deepslate",
        "setblock 123 52 -217 polished_deepslate_stairs[facing=west,half=top]",
        "fill 123 52 -224 123 52 -218 polished_deepslate_stairs[facing=west,half=top]",
        "fill 124 46 -224 124 46 -218 polished_deepslate_stairs[facing=west,half=bottom]",
    ]
    return cmds

def build_west_shrine():
    """Constructs the balancing Occult Relic Shrine along the western wall."""
    cmds = [
        "# West Wall Occult Relic Shrine (X: 107..110, Z: -225..-217, Y: 46..52)",
        # Gilded Blackstone Backing Wall
        "fill 107 46 -225 107 52 -217 gilded_blackstone",
        # Crying Obsidian Niches
        "fill 108 46 -225 108 51 -225 crying_obsidian",
        "fill 108 46 -217 108 51 -217 crying_obsidian",
        "fill 108 52 -224 108 52 -218 polished_blackstone_stairs[facing=east,half=top]",
        # Charged Respawn Anchor Central Altar
        "setblock 108 46 -221 gilded_blackstone",
        "setblock 108 47 -221 respawn_anchor[charges=4]",
        # Soul Fire Braziers on Soul Soil
        "setblock 108 46 -223 soul_soil",
        "setblock 108 47 -223 soul_fire",
        "setblock 108 46 -219 soul_soil",
        "setblock 108 47 -219 soul_fire",
        # Weeping Vines draping the altar
        "setblock 108 51 -222 weeping_vines[age=5]",
        "setblock 108 50 -222 weeping_vines[age=7]",
        "setblock 108 51 -220 weeping_vines[age=5]",
        "setblock 108 50 -220 weeping_vines[age=7]",
        # Chiseled Blackstone Pilasters
        "fill 109 46 -225 109 51 -225 chiseled_polished_blackstone",
        "setblock 109 52 -225 polished_blackstone_stairs[facing=east,half=top]",
        "fill 109 46 -217 109 51 -217 chiseled_polished_blackstone",
        "setblock 109 52 -217 polished_blackstone_stairs[facing=east,half=top]",
    ]
    return cmds

def build_end_portal_sanctum():
    """Constructs the sunken 5x5 ceremonial basin containing the active End Portal."""
    cmds = [
        "# End Portal Sanctum: Sunken 5x5 Basin (X: 115..119, Z: -223..-219, Y: 44..45)",
        # Excavate the 5x5 sunken basin down to Y: 44
        "fill 115 44 -223 119 45 -219 air",
        # Solid Foundation at Y: 44 beneath portal
        "fill 115 44 -223 119 44 -219 polished_blackstone",
        # Concealed Sea Lantern Core at Y: 44 illuminating the cosmic void from below
        "fill 116 44 -222 118 44 -220 sea_lantern",
        # 3x3 Active End Portal void at Y: 45
        "fill 116 45 -222 118 45 -220 end_portal",
        # Ring of 12 End Portal Frames with eye=true facing inward at Y: 45
        # North row facing south
        "setblock 116 45 -223 end_portal_frame[facing=south,eye=true]",
        "setblock 117 45 -223 end_portal_frame[facing=south,eye=true]",
        "setblock 118 45 -223 end_portal_frame[facing=south,eye=true]",
        # South row facing north
        "setblock 116 45 -219 end_portal_frame[facing=north,eye=true]",
        "setblock 117 45 -219 end_portal_frame[facing=north,eye=true]",
        "setblock 118 45 -219 end_portal_frame[facing=north,eye=true]",
        # West row facing east
        "setblock 115 45 -222 end_portal_frame[facing=east,eye=true]",
        "setblock 115 45 -221 end_portal_frame[facing=east,eye=true]",
        "setblock 115 45 -220 end_portal_frame[facing=east,eye=true]",
        # East row facing west
        "setblock 119 45 -222 end_portal_frame[facing=west,eye=true]",
        "setblock 119 45 -221 end_portal_frame[facing=west,eye=true]",
        "setblock 119 45 -220 end_portal_frame[facing=west,eye=true]",
        # 4 Basin Corner Pedestals at Y: 45
        "setblock 115 45 -223 purpur_block",
        "setblock 119 45 -223 purpur_block",
        "setblock 115 45 -219 purpur_block",
        "setblock 119 45 -219 purpur_block",
        # Stepped Basin Perimeter Rim at Y: 46
        "fill 115 46 -224 119 46 -224 purpur_stairs[facing=south,half=bottom]",
        "fill 115 46 -218 119 46 -218 purpur_stairs[facing=north,half=bottom]",
        "fill 114 46 -223 114 46 -219 purpur_stairs[facing=east,half=bottom]",
        "fill 120 46 -223 120 46 -219 purpur_stairs[facing=west,half=bottom]",
        # Corner Sea Lantern Plinths beneath Purpur Slabs at Y: 46
        "setblock 114 46 -224 purpur_slab[type=bottom]",
        "setblock 114 45 -224 sea_lantern",
        "setblock 120 46 -224 purpur_slab[type=bottom]",
        "setblock 120 45 -224 sea_lantern",
        "setblock 114 46 -218 purpur_slab[type=bottom]",
        "setblock 114 45 -218 sea_lantern",
        "setblock 120 46 -218 purpur_slab[type=bottom]",
        "setblock 120 45 -218 sea_lantern",
        # Ceremonial End Stone Brick Walkway ring
        "fill 113 46 -225 121 46 -225 end_stone_bricks",
        "fill 113 46 -217 121 46 -217 end_stone_bricks",
        "fill 113 46 -225 113 46 -217 end_stone_bricks",
        "fill 121 46 -225 121 46 -217 end_stone_bricks",
        # 4 Corner End Rod Beacons on Crying Obsidian
        "setblock 113 46 -225 crying_obsidian",
        "setblock 113 47 -225 end_rod[facing=up]",
        "setblock 121 46 -225 crying_obsidian",
        "setblock 121 47 -225 end_rod[facing=up]",
        "setblock 113 46 -217 crying_obsidian",
        "setblock 113 47 -217 end_rod[facing=up]",
        "setblock 121 46 -217 crying_obsidian",
        "setblock 121 47 -217 end_rod[facing=up]",
    ]
    return cmds

def build_nether_portal_stargate():
    """Constructs monumental active 5-wide by 7-tall Nether Portal Stargate on south wall."""
    cmds = [
        "# Monumental Nether Portal Stargate (X: 115..119, Y: 47..51, Z: -211)",
        # Ensure clean air volume for Stargate frame and portal
        "fill 113 47 -211 121 52 -211 air",
        # Stargate Bottom Threshold at Y: 46 (Crying Obsidian frame, Gilded Blackstone corners)
        "fill 115 46 -211 119 46 -211 crying_obsidian",
        "setblock 114 46 -211 gilded_blackstone",
        "setblock 120 46 -211 gilded_blackstone",
        # Stargate Top Lintel at Y: 52 (Crying Obsidian frame, Gilded Blackstone corners)
        "fill 115 52 -211 119 52 -211 crying_obsidian",
        "setblock 114 52 -211 gilded_blackstone",
        "setblock 120 52 -211 gilded_blackstone",
        # Stargate Vertical Jambs at X: 114 and X: 120 (Crying Obsidian)
        "fill 114 47 -211 114 51 -211 crying_obsidian",
        "fill 120 47 -211 120 51 -211 crying_obsidian",
        # Flanking Chiseled Deepslate Decorative Columns at X: 113 and X: 121
        "fill 113 46 -211 113 51 -211 chiseled_deepslate",
        "setblock 113 52 -211 polished_deepslate_stairs[facing=east,half=top]",
        "fill 121 46 -211 121 51 -211 chiseled_deepslate",
        "setblock 121 52 -211 polished_deepslate_stairs[facing=west,half=top]",
        # Charged Respawn Anchor Altars flanking the gate
        "setblock 113 46 -212 gilded_blackstone",
        "setblock 113 47 -212 respawn_anchor[charges=4]",
        "setblock 121 46 -212 gilded_blackstone",
        "setblock 121 47 -212 respawn_anchor[charges=4]",
        # Ceremonial Soul Fire Braziers on Soul Soil
        "setblock 114 46 -213 soul_soil",
        "setblock 114 47 -213 soul_fire",
        "setblock 120 46 -213 soul_soil",
        "setblock 120 47 -213 soul_fire",
        "setblock 114 46 -214 polished_blackstone_wall",
        "setblock 120 46 -214 polished_blackstone_wall",
        # Weeping Vines draping the celestial portal frame
        "setblock 113 51 -212 weeping_vines[age=5]",
        "setblock 113 50 -212 weeping_vines[age=7]",
        "setblock 121 51 -212 weeping_vines[age=5]",
        "setblock 121 50 -212 weeping_vines[age=7]",
        # Crown Keystone Bulb above portal arch
        "setblock 117 53 -211 copper_bulb[lit=true,powered=false]",
        # Golden Rune Inlays in approach aisle
        "setblock 117 46 -212 gold_block",
        "setblock 117 46 -213 chiseled_polished_blackstone",
        "setblock 117 46 -214 gold_block",
        "setblock 117 46 -215 chiseled_polished_blackstone",
        # Active Nether portal vortex spanning X: 115..119, Y: 47..51 at Z: -211 placed finally
        "fill 115 47 -211 119 51 -211 nether_portal[axis=x]",
    ]
    return cmds

def execute_remote_batch(all_cmds, host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Executes all commands via RCON in batches under 80 commands per socket invocation."""
    batch_size = 75
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

def verify_live_blockstates(host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Verifies that all critical Nexus structures, portals, and fixtures exist live on the server."""
    test_blocks = [
        # Connecting Hallway
        ("117 47 -235", "red_carpet", "Connecting Hallway Red Carpet"),
        ("115 48 -235", "crying_obsidian", "Connecting Hallway West Crying Obsidian Pilaster"),
        ("119 48 -235", "crying_obsidian", "Connecting Hallway East Crying Obsidian Pilaster"),
        ("117 53 -235", "copper_bulb[lit=true,powered=false]", "Connecting Hallway Keystone Bulb"),
        ("117 52 -235", "iron_chain[axis=y]", "Connecting Hallway Iron Chain"),
        ("117 51 -235", "soul_lantern[hanging=true]", "Connecting Hallway Soul Lantern"),

        # Nether Portal Stargate
        ("117 49 -211", "nether_portal[axis=x]", "Nether Portal Active Vortex at Center"),
        ("115 47 -211", "nether_portal[axis=x]", "Nether Portal Active Vortex at West Edge"),
        ("119 51 -211", "nether_portal[axis=x]", "Nether Portal Active Vortex at East Top"),
        ("117 46 -211", "crying_obsidian", "Nether Portal Base Threshold"),
        ("117 52 -211", "crying_obsidian", "Nether Portal Top Lintel"),
        ("114 52 -211", "gilded_blackstone", "Nether Portal NW Corner Gilded Accent"),
        ("120 52 -211", "gilded_blackstone", "Nether Portal NE Corner Gilded Accent"),
        ("114 49 -211", "crying_obsidian", "Nether Portal West Crying Obsidian Jamb"),
        ("120 49 -211", "crying_obsidian", "Nether Portal East Crying Obsidian Jamb"),
        ("113 47 -212", "respawn_anchor[charges=4]", "Nether Portal West Charged Respawn Anchor"),
        ("121 47 -212", "respawn_anchor[charges=4]", "Nether Portal East Charged Respawn Anchor"),
        ("114 47 -213", "soul_fire", "Nether Portal West Soul Fire Brazier"),
        ("120 47 -213", "soul_fire", "Nether Portal East Soul Fire Brazier"),

        # End Portal Sanctum
        ("117 45 -221", "end_portal", "End Portal Active Cosmic Void at Center"),
        ("116 45 -222", "end_portal", "End Portal Active Cosmic Void NW"),
        ("118 45 -220", "end_portal", "End Portal Active Cosmic Void SE"),
        ("117 45 -223", "end_portal_frame[facing=south,eye=true]", "End Portal North Frame with Eye of Ender"),
        ("117 45 -219", "end_portal_frame[facing=north,eye=true]", "End Portal South Frame with Eye of Ender"),
        ("115 45 -221", "end_portal_frame[facing=east,eye=true]", "End Portal West Frame with Eye of Ender"),
        ("119 45 -221", "end_portal_frame[facing=west,eye=true]", "End Portal East Frame with Eye of Ender"),
        ("117 44 -221", "sea_lantern", "End Portal Sub-Basin Concealed Sea Lantern Core"),
        ("114 45 -224", "sea_lantern", "End Portal NW Corner Sea Lantern Pedestal"),
        ("120 45 -218", "sea_lantern", "End Portal SE Corner Sea Lantern Pedestal"),
        ("113 47 -225", "end_rod[facing=up]", "End Portal NW Corner End Rod Beacon"),
        ("121 47 -217", "end_rod[facing=up]", "End Portal SE Corner End Rod Beacon"),

        # Amethyst Geode Sanctuary
        ("124 49 -221", "tinted_glass", "Amethyst Geode Center Tinted Glass Panel"),
        ("125 48 -221", "amethyst_cluster[facing=up]", "Amethyst Geode Upward Blooming Cluster"),
        ("125 50 -221", "amethyst_cluster[facing=down]", "Amethyst Geode Downward Blooming Cluster"),
        ("125 49 -221", "amethyst_cluster[facing=west]", "Amethyst Geode West Blooming Cluster"),
        ("126 49 -221", "budding_amethyst", "Amethyst Geode Budding Amethyst Core"),
        ("126 47 -221", "sea_lantern", "Amethyst Geode Concealed Sea Lantern Core"),
        ("127 49 -221", "smooth_basalt", "Amethyst Geode Outer Smooth Basalt Shell"),

        # Floor Grate Illumination Grid
        ("111 46 -221", "copper_grate", "West Floor Copper Grate"),
        ("111 45 -221", "sea_lantern", "West Sub-Floor Concealed Sea Lantern"),
        ("122 46 -221", "copper_grate", "East Floor Copper Grate"),
        ("122 45 -221", "sea_lantern", "East Sub-Floor Concealed Sea Lantern"),

        # Vaulted Ceiling Ribs and Keystones
        ("117 53 -227", "copper_bulb[lit=true,powered=false]", "Ceiling Rib Z-227 Center Keystone Bulb"),
        ("117 52 -227", "iron_chain[axis=y]", "Ceiling Rib Z-227 Center Iron Chain"),
        ("117 51 -227", "soul_lantern[hanging=true]", "Ceiling Rib Z-227 Center Soul Lantern"),
        ("112 53 -227", "copper_bulb[lit=true,powered=false]", "Ceiling Rib Z-227 West Keystone Bulb"),
        ("122 53 -227", "copper_bulb[lit=true,powered=false]", "Ceiling Rib Z-227 East Keystone Bulb"),
        ("108 50 -227", "polished_deepslate_stairs[facing=east,half=top]", "Ceiling Rib Z-227 West Wall Corbel"),
        ("126 50 -227", "polished_deepslate_stairs[facing=west,half=top]", "Ceiling Rib Z-227 East Wall Corbel"),
    ]

    print("\nVerifying live blockstates via RCON...")
    py_code = f"""
import socket, struct

with open('/home/ubuntu/minecraft-server/server.properties') as f:
    props = dict(line.strip().split('=', 1) for line in f if '=' in line and not line.startswith('#'))

rcon_port = int(props.get('rcon.port', 25575))
rcon_pass = props.get('rcon.password', '')

s = socket.create_connection(('127.0.0.1', rcon_port), timeout=10)
s.sendall(struct.pack('<iii', len(rcon_pass) + 10, 1, 3) + rcon_pass.encode('utf-8') + b'\\x00\\x00')
s.recv(4096)

tests = {repr(test_blocks)}
passed = 0
failed = 0
for pos, expected, label in tests:
    cmd = f'execute if block {{pos}} {{expected}}'
    s.sendall(struct.pack('<iii', len(cmd) + 10, 20, 2) + cmd.encode('utf-8') + b'\\x00\\x00')
    resp = s.recv(4096)
    msg = resp[12:-2].decode('utf-8', errors='ignore') if len(resp) >= 12 else ''
    if 'passed' in msg:
        print(f'[PASS] {{label}} at {{pos}} -> {{expected}}')
        passed += 1
    else:
        print(f'[FAIL] {{label}} at {{pos}} -> expected {{expected}}, got: {{msg}}')
        failed += 1

s.close()
print(f'\\nVerification Summary: {{passed}}/{{len(tests)}} checks passed, {{failed}} failed.')
if failed > 0:
    exit(1)
"""
    ssh_cmd = [
        "ssh", "-o", "StrictHostKeyChecking=no",
        "-i", key,
        f"{user}@{host}",
        f"python3 -c {subprocess.list2cmdline([py_code])}"
    ]
    res = subprocess.run(ssh_cmd, capture_output=True, text=True)
    print(res.stdout)
    if res.returncode != 0:
        print(f"Verification error: {res.stderr}", file=sys.stderr)
        return False
    return True

def sync_remote_mcfunction(local_filename, host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Syncs the generated mcfunction to the remote server datapack directory."""
    local_path = os.path.join(FUNCTION_DIR, local_filename)
    remote_path = f"/home/ubuntu/minecraft-server/world/datapacks/underground_citadel/data/citadel/function/{local_filename}"
    scp_cmd = [
        "scp", "-o", "StrictHostKeyChecking=no",
        "-i", key,
        local_path,
        f"{user}@{host}:{remote_path}"
    ]
    res = subprocess.run(scp_cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Warning: Failed to scp mcfunction file: {res.stderr}", file=sys.stderr)
    else:
        print(f"Successfully synced {local_filename} to remote datapack.")

def main():
    print("Beginning Celestial Portal Nexus dimensional chamber construction...")
    all_cmds = []
    # Construction sequence ordered to protect active portals and crystal matrices
    all_cmds.extend(build_chamber_shell())
    all_cmds.extend(build_connecting_archway())
    all_cmds.extend(build_floor_and_lighting())
    all_cmds.extend(build_vaulted_ceiling_nexus())
    all_cmds.extend(build_amethyst_geode_sanctuary())
    all_cmds.extend(build_west_shrine())
    all_cmds.extend(build_end_portal_sanctum())
    all_cmds.extend(build_nether_portal_stargate())

    # Write local mcfunction file
    write_mcfunction("bunker_portal_nexus.mcfunction", all_cmds)

    # Sync file to remote server datapack
    sync_remote_mcfunction("bunker_portal_nexus.mcfunction")

    # Execute all commands over RCON socket protocol
    print("\nExecuting Celestial Portal Nexus construction commands via RCON...")
    execute_remote_batch(all_cmds)

    # Verify live blockstates
    success = verify_live_blockstates()
    if success:
        print("\nAll celestial portals, sanctums, and dimensional fixtures verified successfully!")
    else:
        print("\nVerification encountered issues. Inspect above logs.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
