#!/usr/bin/env python3
"""Build vaulted ceilings and architectural upgrades for King Abir's bunker.

Upgrades the ceilings and walls across the Central Command Rotunda,
the South Sovereign Boulevard, and all arterial corridors.
Replaces flat ceilings with coffered barrel vaults, structural arch ribs every 4 blocks,
and supportive pilasters with corbels.
Ceiling upper limit is strictly Y: 53.
Corridors have floor at Y: 46 with arch ribs curving down from Y: 53 to Y: 50.
Integrates lit copper bulbs and hanging soul lanterns into every vault keystone.
Generates the mcfunction file bunker_vaults.mcfunction and executes commands via RCON.
"""

import os
import subprocess
import sys

DEFAULT_HOST = os.environ.get("HZ_HOST", "132.226.135.26")
DEFAULT_USER = os.environ.get("HZ_USER", "ubuntu")
DEFAULT_KEY = os.environ.get("HZ_KEY", os.path.expanduser("~/.ssh/id_ed25519"))

# Support execution from repo root or parent workspace
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

def build_rotunda_vaults():
    """Generates coffered vault, arch ribs, and pilasters for Central Command Rotunda."""
    cmds = [
        "# Sector 0: Central Command Rotunda Vaulting (X: 111..123, Z: -307..-295, Y: 46..53)",
        # Solid ceiling backing at strictly Y: 53
        "fill 111 53 -307 123 53 -295 deepslate_tiles",

        # Outer Wall Reinforcement and Pilasters
        # Corner Pilasters with Corbels
        "fill 111 46 -307 111 49 -307 chiseled_deepslate",
        "setblock 111 50 -307 polished_deepslate_stairs[facing=south,half=top]",
        "fill 123 46 -307 123 49 -307 chiseled_deepslate",
        "setblock 123 50 -307 polished_deepslate_stairs[facing=south,half=top]",
        "fill 111 46 -295 111 49 -295 chiseled_deepslate",
        "setblock 111 50 -295 polished_deepslate_stairs[facing=north,half=top]",
        "fill 123 46 -295 123 49 -295 chiseled_deepslate",
        "setblock 123 50 -295 polished_deepslate_stairs[facing=north,half=top]",

        # North Wall Pilasters flanking Grand Staircase (Z = -307)
        "fill 114 46 -307 114 49 -307 chiseled_deepslate",
        "setblock 114 50 -307 polished_deepslate_stairs[facing=south,half=top]",
        "fill 120 46 -307 120 49 -307 chiseled_deepslate",
        "setblock 120 50 -307 polished_deepslate_stairs[facing=south,half=top]",

        # South Wall Pilasters flanking South Boulevard (Z = -295)
        "fill 114 46 -295 114 49 -295 chiseled_deepslate",
        "setblock 114 50 -295 polished_deepslate_stairs[facing=north,half=top]",
        "fill 120 46 -295 120 49 -295 chiseled_deepslate",
        "setblock 120 50 -295 polished_deepslate_stairs[facing=north,half=top]",

        # West Wall Pilasters flanking West Corridor (X = 111)
        "fill 111 46 -304 111 49 -304 chiseled_deepslate",
        "setblock 111 50 -304 polished_deepslate_stairs[facing=east,half=top]",
        "fill 111 46 -298 111 49 -298 chiseled_deepslate",
        "setblock 111 50 -298 polished_deepslate_stairs[facing=east,half=top]",

        # East Wall Pilasters flanking East Corridor (X = 123)
        "fill 123 46 -304 123 49 -304 chiseled_deepslate",
        "setblock 123 50 -304 polished_deepslate_stairs[facing=west,half=top]",
        "fill 123 46 -298 123 49 -298 chiseled_deepslate",
        "setblock 123 50 -298 polished_deepslate_stairs[facing=west,half=top]",

        # Wall Skirting and Cornice Trims
        # North Wall bays
        "fill 112 46 -307 113 46 -307 polished_blackstone",
        "fill 112 47 -307 113 47 -307 polished_deepslate_stairs[facing=south,half=bottom]",
        "fill 112 48 -307 113 49 -307 deepslate_bricks",
        "fill 112 50 -307 113 50 -307 deepslate_tile_stairs[facing=south,half=top]",
        "fill 121 46 -307 122 46 -307 polished_blackstone",
        "fill 121 47 -307 122 47 -307 polished_deepslate_stairs[facing=south,half=bottom]",
        "fill 121 48 -307 122 49 -307 deepslate_bricks",
        "fill 121 50 -307 122 50 -307 deepslate_tile_stairs[facing=south,half=top]",

        # South Wall bays
        "fill 112 46 -295 113 46 -295 polished_blackstone",
        "fill 112 47 -295 113 47 -295 polished_deepslate_stairs[facing=north,half=bottom]",
        "fill 112 48 -295 113 49 -295 deepslate_bricks",
        "fill 112 50 -295 113 50 -295 deepslate_tile_stairs[facing=north,half=top]",
        "fill 121 46 -295 122 46 -295 polished_blackstone",
        "fill 121 47 -295 122 47 -295 polished_deepslate_stairs[facing=north,half=bottom]",
        "fill 121 48 -295 122 49 -295 deepslate_bricks",
        "fill 121 50 -295 122 50 -295 deepslate_tile_stairs[facing=north,half=top]",

        # West Wall bays
        "fill 111 46 -306 111 46 -305 polished_blackstone",
        "fill 111 47 -306 111 47 -305 polished_deepslate_stairs[facing=east,half=bottom]",
        "fill 111 48 -306 111 49 -305 deepslate_bricks",
        "fill 111 50 -306 111 50 -305 deepslate_tile_stairs[facing=east,half=top]",
        "fill 111 46 -297 111 46 -296 polished_blackstone",
        "fill 111 47 -297 111 47 -296 polished_deepslate_stairs[facing=east,half=bottom]",
        "fill 111 48 -297 111 49 -296 deepslate_bricks",
        "fill 111 50 -297 111 50 -296 deepslate_tile_stairs[facing=east,half=top]",

        # East Wall bays
        "fill 123 46 -306 123 46 -305 polished_blackstone",
        "fill 123 47 -306 123 47 -305 polished_deepslate_stairs[facing=west,half=bottom]",
        "fill 123 48 -306 123 49 -305 deepslate_bricks",
        "fill 123 50 -306 123 50 -305 deepslate_tile_stairs[facing=west,half=top]",
        "fill 123 46 -297 123 46 -296 polished_blackstone",
        "fill 123 47 -297 123 47 -296 polished_deepslate_stairs[facing=west,half=bottom]",
        "fill 123 48 -297 123 49 -296 deepslate_bricks",
        "fill 123 50 -297 123 50 -296 deepslate_tile_stairs[facing=west,half=top]",

        # Structural Arch Rib Framework at Y: 52
        # North-South rib beams at X: 114, 117, 120
        "fill 114 52 -306 114 52 -296 polished_deepslate",
        "fill 117 52 -306 117 52 -296 polished_deepslate",
        "fill 120 52 -306 120 52 -296 polished_deepslate",
        # East-West rib beams at Z: -304, -301, -298
        "fill 112 52 -304 122 52 -304 polished_deepslate",
        "fill 112 52 -301 122 52 -301 polished_deepslate",
        "fill 112 52 -298 122 52 -298 polished_deepslate",

        # Arch Rib Springers Curving down to Y: 50 at perimeter
        # North perimeter arch curves
        "setblock 114 51 -306 polished_deepslate_stairs[facing=south,half=top]",
        "setblock 117 51 -306 polished_deepslate_stairs[facing=south,half=top]",
        "setblock 120 51 -306 polished_deepslate_stairs[facing=south,half=top]",
        "setblock 114 50 -306 polished_deepslate_stairs[facing=south,half=top]",
        "setblock 117 50 -306 polished_deepslate_stairs[facing=south,half=top]",
        "setblock 120 50 -306 polished_deepslate_stairs[facing=south,half=top]",

        # South perimeter arch curves
        "setblock 114 51 -296 polished_deepslate_stairs[facing=north,half=top]",
        "setblock 117 51 -296 polished_deepslate_stairs[facing=north,half=top]",
        "setblock 120 51 -296 polished_deepslate_stairs[facing=north,half=top]",
        "setblock 114 50 -296 polished_deepslate_stairs[facing=north,half=top]",
        "setblock 117 50 -296 polished_deepslate_stairs[facing=north,half=top]",
        "setblock 120 50 -296 polished_deepslate_stairs[facing=north,half=top]",

        # West perimeter arch curves
        "setblock 112 51 -304 polished_deepslate_stairs[facing=east,half=top]",
        "setblock 112 51 -301 polished_deepslate_stairs[facing=east,half=top]",
        "setblock 112 51 -298 polished_deepslate_stairs[facing=east,half=top]",
        "setblock 112 50 -304 polished_deepslate_stairs[facing=east,half=top]",
        "setblock 112 50 -301 polished_deepslate_stairs[facing=east,half=top]",
        "setblock 112 50 -298 polished_deepslate_stairs[facing=east,half=top]",

        # East perimeter arch curves
        "setblock 122 51 -304 polished_deepslate_stairs[facing=west,half=top]",
        "setblock 122 51 -301 polished_deepslate_stairs[facing=west,half=top]",
        "setblock 122 51 -298 polished_deepslate_stairs[facing=west,half=top]",
        "setblock 122 50 -304 polished_deepslate_stairs[facing=west,half=top]",
        "setblock 122 50 -301 polished_deepslate_stairs[facing=west,half=top]",
        "setblock 122 50 -298 polished_deepslate_stairs[facing=west,half=top]",

        # Recessed Coffered Bay Ceiling Panels (Y: 53 polished blackstone, framed by stairs at Y: 52)
        # Bay NW (X: 112..113, Z: -306..-305)
        "fill 112 53 -306 113 53 -305 polished_blackstone",
        "setblock 112 52 -306 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 113 52 -306 deepslate_tile_stairs[facing=west,half=top]",
        "setblock 112 52 -305 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 113 52 -305 deepslate_tile_stairs[facing=west,half=top]",

        # Bay NC1 (X: 115..116, Z: -306..-305)
        "fill 115 53 -306 116 53 -305 polished_blackstone",
        "setblock 115 52 -306 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 116 52 -306 deepslate_tile_stairs[facing=west,half=top]",
        "setblock 115 52 -305 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 116 52 -305 deepslate_tile_stairs[facing=west,half=top]",

        # Bay NC2 (X: 118..119, Z: -306..-305)
        "fill 118 53 -306 119 53 -305 polished_blackstone",
        "setblock 118 52 -306 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 119 52 -306 deepslate_tile_stairs[facing=west,half=top]",
        "setblock 118 52 -305 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 119 52 -305 deepslate_tile_stairs[facing=west,half=top]",

        # Bay NE (X: 121..122, Z: -306..-305)
        "fill 121 53 -306 122 53 -305 polished_blackstone",
        "setblock 121 52 -306 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 122 52 -306 deepslate_tile_stairs[facing=west,half=top]",
        "setblock 121 52 -305 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 122 52 -305 deepslate_tile_stairs[facing=west,half=top]",

        # Bay WN (X: 112..113, Z: -303..-302)
        "fill 112 53 -303 113 53 -302 polished_blackstone",
        "setblock 112 52 -303 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 113 52 -303 deepslate_tile_stairs[facing=west,half=top]",
        "setblock 112 52 -302 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 113 52 -302 deepslate_tile_stairs[facing=west,half=top]",

        # Bay CN1 (X: 115..116, Z: -303..-302)
        "fill 115 53 -303 116 53 -302 polished_blackstone",
        "setblock 115 52 -303 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 116 52 -303 deepslate_tile_stairs[facing=west,half=top]",
        "setblock 115 52 -302 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 116 52 -302 deepslate_tile_stairs[facing=west,half=top]",

        # Bay CN2 (X: 118..119, Z: -303..-302)
        "fill 118 53 -303 119 53 -302 polished_blackstone",
        "setblock 118 52 -303 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 119 52 -303 deepslate_tile_stairs[facing=west,half=top]",
        "setblock 118 52 -302 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 119 52 -302 deepslate_tile_stairs[facing=west,half=top]",

        # Bay EN (X: 121..122, Z: -303..-302)
        "fill 121 53 -303 122 53 -302 polished_blackstone",
        "setblock 121 52 -303 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 122 52 -303 deepslate_tile_stairs[facing=west,half=top]",
        "setblock 121 52 -302 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 122 52 -302 deepslate_tile_stairs[facing=west,half=top]",

        # Bay WS (X: 112..113, Z: -300..-299)
        "fill 112 53 -300 113 53 -299 polished_blackstone",
        "setblock 112 52 -300 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 113 52 -300 deepslate_tile_stairs[facing=west,half=top]",
        "setblock 112 52 -299 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 113 52 -299 deepslate_tile_stairs[facing=west,half=top]",

        # Bay CS1 (X: 115..116, Z: -300..-299)
        "fill 115 53 -300 116 53 -299 polished_blackstone",
        "setblock 115 52 -300 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 116 52 -300 deepslate_tile_stairs[facing=west,half=top]",
        "setblock 115 52 -299 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 116 52 -299 deepslate_tile_stairs[facing=west,half=top]",

        # Bay CS2 (X: 118..119, Z: -300..-299)
        "fill 118 53 -300 119 53 -299 polished_blackstone",
        "setblock 118 52 -300 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 119 52 -300 deepslate_tile_stairs[facing=west,half=top]",
        "setblock 118 52 -299 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 119 52 -299 deepslate_tile_stairs[facing=west,half=top]",

        # Bay ES (X: 121..122, Z: -300..-299)
        "fill 121 53 -300 122 53 -299 polished_blackstone",
        "setblock 121 52 -300 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 122 52 -300 deepslate_tile_stairs[facing=west,half=top]",
        "setblock 121 52 -299 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 122 52 -299 deepslate_tile_stairs[facing=west,half=top]",

        # Bay SW (X: 112..113, Z: -297..-296)
        "fill 112 53 -297 113 53 -296 polished_blackstone",
        "setblock 112 52 -297 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 113 52 -297 deepslate_tile_stairs[facing=west,half=top]",
        "setblock 112 52 -296 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 113 52 -296 deepslate_tile_stairs[facing=west,half=top]",

        # Bay SC1 (X: 115..116, Z: -297..-296)
        "fill 115 53 -297 116 53 -296 polished_blackstone",
        "setblock 115 52 -297 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 116 52 -297 deepslate_tile_stairs[facing=west,half=top]",
        "setblock 115 52 -296 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 116 52 -296 deepslate_tile_stairs[facing=west,half=top]",

        # Bay SC2 (X: 118..119, Z: -297..-296)
        "fill 118 53 -297 119 53 -296 polished_blackstone",
        "setblock 118 52 -297 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 119 52 -297 deepslate_tile_stairs[facing=west,half=top]",
        "setblock 118 52 -296 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 119 52 -296 deepslate_tile_stairs[facing=west,half=top]",

        # Bay SE (X: 121..122, Z: -297..-296)
        "fill 121 53 -297 122 53 -296 polished_blackstone",
        "setblock 121 52 -297 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 122 52 -297 deepslate_tile_stairs[facing=west,half=top]",
        "setblock 121 52 -296 deepslate_tile_stairs[facing=east,half=top]",
        "setblock 122 52 -296 deepslate_tile_stairs[facing=west,half=top]",
    ]

    # Integrate Lit Copper Bulbs and Hanging Soul Lanterns into every Rotunda vault keystone
    keystones = [
        (117, -301),  # Center Grand Keystone
        (114, -301),  # West Axial Keystone
        (120, -301),  # East Axial Keystone
        (117, -304),  # North Axial Keystone
        (117, -298),  # South Axial Keystone
        (114, -304),  # NW Diagonal Keystone
        (120, -304),  # NE Diagonal Keystone
        (114, -298),  # SW Diagonal Keystone
        (120, -298),  # SE Diagonal Keystone
    ]
    for kx, kz in keystones:
        cmds.append(f"setblock {kx} 53 {kz} copper_bulb[lit=true,powered=false]")
        cmds.append(f"setblock {kx} 52 {kz} iron_chain[axis=y]")
        cmds.append(f"setblock {kx} 51 {kz} soul_lantern[hanging=true]")

    return cmds

def build_boulevard_vaults():
    """Generates coffered barrel vault, arch ribs every 4 blocks, and pilasters along South Boulevard."""
    cmds = [
        "# South Sovereign Boulevard Vaulting (X: 115..119, Z: -294..-262, Floor Y: 46, Cap Y: 53)",
        # Solid ceiling backing at strictly Y: 53
        "fill 116 53 -294 118 53 -262 deepslate_tiles",
    ]

    # Structural arch ribs every 4 blocks along Z
    # Rib coordinates: -294, -290, -286, -282, -278, -274, -270, -266, -262
    rib_z_coords = list(range(-294, -261, 4))

    for rz in rib_z_coords:
        cmds.append(f"# Structural Arch Rib at Z = {rz}")
        # Keystone at Center (X: 117)
        cmds.append(f"setblock 117 53 {rz} copper_bulb[lit=true,powered=false]")
        cmds.append(f"setblock 117 52 {rz} iron_chain[axis=y]")
        cmds.append(f"setblock 117 51 {rz} soul_lantern[hanging=true]")
        cmds.append(f"setblock 117 50 {rz} air")

        # Arch Rib curve down from Y: 53 to Y: 50
        # West side of rib (X: 116)
        cmds.append(f"setblock 116 53 {rz} deepslate_bricks")
        cmds.append(f"setblock 116 52 {rz} polished_deepslate_stairs[facing=east,half=top]")
        cmds.append(f"setblock 116 51 {rz} polished_deepslate_stairs[facing=east,half=top]")
        cmds.append(f"setblock 116 50 {rz} polished_deepslate_stairs[facing=east,half=top]")

        # East side of rib (X: 118)
        cmds.append(f"setblock 118 53 {rz} deepslate_bricks")
        cmds.append(f"setblock 118 52 {rz} polished_deepslate_stairs[facing=west,half=top]")
        cmds.append(f"setblock 118 51 {rz} polished_deepslate_stairs[facing=west,half=top]")
        cmds.append(f"setblock 118 50 {rz} polished_deepslate_stairs[facing=west,half=top]")

        # Supportive Pilasters and Corbels on Wall (X: 115 and 119)
        # Note: Z = -278 is inside the Farm and Housing portal doorway (Z: -279..-277)
        if rz != -278:
            # West Wall Pilaster (X: 115)
            cmds.append(f"setblock 115 46 {rz} chiseled_deepslate")
            cmds.append(f"setblock 115 47 {rz} chiseled_deepslate")
            cmds.append(f"setblock 115 48 {rz} polished_deepslate")
            cmds.append(f"setblock 115 49 {rz} polished_deepslate")
            cmds.append(f"setblock 115 50 {rz} polished_deepslate_stairs[facing=east,half=top]")
            cmds.append(f"setblock 115 51 {rz} deepslate_tiles")
            cmds.append(f"setblock 115 52 {rz} deepslate_tiles")

            # East Wall Pilaster (X: 119)
            cmds.append(f"setblock 119 46 {rz} chiseled_deepslate")
            cmds.append(f"setblock 119 47 {rz} chiseled_deepslate")
            cmds.append(f"setblock 119 48 {rz} polished_deepslate")
            cmds.append(f"setblock 119 49 {rz} polished_deepslate")
            cmds.append(f"setblock 119 50 {rz} polished_deepslate_stairs[facing=west,half=top]")
            cmds.append(f"setblock 119 51 {rz} deepslate_tiles")
            cmds.append(f"setblock 119 52 {rz} deepslate_tiles")
        else:
            # Arch Header above side room cross-connectors at Z = -278
            cmds.append(f"setblock 115 52 {rz} polished_deepslate")
            cmds.append(f"setblock 115 51 {rz} polished_deepslate_stairs[facing=east,half=top]")
            cmds.append(f"setblock 119 52 {rz} polished_deepslate")
            cmds.append(f"setblock 119 51 {rz} polished_deepslate_stairs[facing=west,half=top]")

    # Coffered Bays between ribs along South Boulevard
    # Each bay spans 3 blocks along Z between consecutive ribs
    for i in range(len(rib_z_coords) - 1):
        z_start = rib_z_coords[i] + 1
        z_end = rib_z_coords[i + 1] - 1
        z_mid = (z_start + z_end) // 2

        cmds.append(f"# Coffered Bay: Z = {z_start}..{z_end}")
        # Ceiling vault contour at Y: 52
        for z in range(z_start, z_end + 1):
            cmds.append(f"setblock 116 52 {z} deepslate_tile_stairs[facing=east,half=top]")
            cmds.append(f"setblock 118 52 {z} deepslate_tile_stairs[facing=west,half=top]")

        # Coffer frame along corridor axis
        cmds.append(f"setblock 117 52 {z_start} deepslate_tile_stairs[facing=south,half=top]")
        cmds.append(f"setblock 117 52 {z_mid} air")
        cmds.append(f"setblock 117 52 {z_end} deepslate_tile_stairs[facing=north,half=top]")
        # Sunken coffer ceiling block at Y: 53
        cmds.append(f"setblock 117 53 {z_mid} polished_blackstone")

        # Wall bays between pilasters (skip doorway at Z: -279..-277)
        for z in range(z_start, z_end + 1):
            if -279 <= z <= -277:
                # Keep doorway open into Farm and Housing
                cmds.append(f"fill 115 47 {z} 115 50 {z} air")
                cmds.append(f"fill 119 47 {z} 119 50 {z} air")
            else:
                # West Wall bay (X: 115)
                cmds.append(f"setblock 115 46 {z} polished_blackstone")
                cmds.append(f"setblock 115 47 {z} polished_deepslate_stairs[facing=east,half=bottom]")
                cmds.append(f"setblock 115 48 {z} deepslate_bricks")
                cmds.append(f"setblock 115 49 {z} deepslate_bricks")
                cmds.append(f"setblock 115 50 {z} deepslate_tile_stairs[facing=east,half=top]")
                cmds.append(f"setblock 115 51 {z} deepslate_tiles")
                cmds.append(f"setblock 115 52 {z} deepslate_tiles")

                # East Wall bay (X: 119)
                cmds.append(f"setblock 119 46 {z} polished_blackstone")
                cmds.append(f"setblock 119 47 {z} polished_deepslate_stairs[facing=west,half=bottom]")
                cmds.append(f"setblock 119 48 {z} deepslate_bricks")
                cmds.append(f"setblock 119 49 {z} deepslate_bricks")
                cmds.append(f"setblock 119 50 {z} deepslate_tile_stairs[facing=west,half=top]")
                cmds.append(f"setblock 119 51 {z} deepslate_tiles")
                cmds.append(f"setblock 119 52 {z} deepslate_tiles")

    return cmds

def build_arterial_corridors_vaults():
    """Generates coffered barrel vaults, arch ribs every 4 blocks, and pilasters across the four arterial corridors."""
    cmds = [
        "# Four Arterial Corridors: Barrel Vaults and Structural Ribs",
    ]

    # Corridor 1: West Arterial Corridor to Tool Armory (X: 95..110, Z: -302..-300, Width 3, Center Z = -301)
    cmds.append("# Corridor 1: West Arterial Corridor (Rotunda to Tool Armory)")
    cmds.append("fill 95 53 -302 110 53 -300 deepslate_tiles")

    # Structural arch ribs every 4 blocks along X
    west_rib_x = [95, 99, 103, 107, 110]
    for rx in west_rib_x:
        cmds.append(f"# Arch Rib at X = {rx}")
        # Keystone at Center Z = -301
        cmds.append(f"setblock {rx} 53 -301 copper_bulb[lit=true,powered=false]")
        cmds.append(f"setblock {rx} 52 -301 iron_chain[axis=y]")
        cmds.append(f"setblock {rx} 51 -301 soul_lantern[hanging=true]")
        cmds.append(f"setblock {rx} 50 -301 air")

        # North arch curve (Z = -302)
        cmds.append(f"setblock {rx} 53 -302 deepslate_bricks")
        cmds.append(f"setblock {rx} 52 -302 polished_deepslate_stairs[facing=south,half=top]")
        cmds.append(f"setblock {rx} 51 -302 polished_deepslate_stairs[facing=south,half=top]")
        cmds.append(f"setblock {rx} 50 -302 polished_deepslate_stairs[facing=south,half=top]")

        # South arch curve (Z = -300)
        cmds.append(f"setblock {rx} 53 -300 deepslate_bricks")
        cmds.append(f"setblock {rx} 52 -300 polished_deepslate_stairs[facing=north,half=top]")
        cmds.append(f"setblock {rx} 51 -300 polished_deepslate_stairs[facing=north,half=top]")
        cmds.append(f"setblock {rx} 50 -300 polished_deepslate_stairs[facing=north,half=top]")

        # North Wall Pilaster (Z = -303)
        cmds.append(f"setblock {rx} 46 -303 chiseled_deepslate")
        cmds.append(f"setblock {rx} 47 -303 chiseled_deepslate")
        cmds.append(f"setblock {rx} 48 -303 polished_deepslate")
        cmds.append(f"setblock {rx} 49 -303 polished_deepslate")
        cmds.append(f"setblock {rx} 50 -303 polished_deepslate_stairs[facing=south,half=top]")
        cmds.append(f"setblock {rx} 51 -303 deepslate_tiles")
        cmds.append(f"setblock {rx} 52 -303 deepslate_tiles")

        # South Wall Pilaster (Z = -299)
        cmds.append(f"setblock {rx} 46 -299 chiseled_deepslate")
        cmds.append(f"setblock {rx} 47 -299 chiseled_deepslate")
        cmds.append(f"setblock {rx} 48 -299 polished_deepslate")
        cmds.append(f"setblock {rx} 49 -299 polished_deepslate")
        cmds.append(f"setblock {rx} 50 -299 polished_deepslate_stairs[facing=north,half=top]")
        cmds.append(f"setblock {rx} 51 -299 deepslate_tiles")
        cmds.append(f"setblock {rx} 52 -299 deepslate_tiles")

    # Coffered Bays along West Corridor
    for i in range(len(west_rib_x) - 1):
        x_start = west_rib_x[i] + 1
        x_end = west_rib_x[i + 1] - 1
        x_mid = (x_start + x_end) // 2
        for x in range(x_start, x_end + 1):
            cmds.append(f"setblock {x} 52 -302 deepslate_tile_stairs[facing=south,half=top]")
            cmds.append(f"setblock {x} 52 -300 deepslate_tile_stairs[facing=north,half=top]")
            # Wall bays North (Z = -303)
            cmds.append(f"setblock {x} 46 -303 polished_blackstone")
            cmds.append(f"setblock {x} 47 -303 polished_deepslate_stairs[facing=south,half=bottom]")
            cmds.append(f"setblock {x} 48 -303 deepslate_bricks")
            cmds.append(f"setblock {x} 49 -303 deepslate_bricks")
            cmds.append(f"setblock {x} 50 -303 deepslate_tile_stairs[facing=south,half=top]")
            cmds.append(f"setblock {x} 51 -303 deepslate_tiles")
            cmds.append(f"setblock {x} 52 -303 deepslate_tiles")
            # Wall bays South (Z = -299)
            cmds.append(f"setblock {x} 46 -299 polished_blackstone")
            cmds.append(f"setblock {x} 47 -299 polished_deepslate_stairs[facing=north,half=bottom]")
            cmds.append(f"setblock {x} 48 -299 deepslate_bricks")
            cmds.append(f"setblock {x} 49 -299 deepslate_bricks")
            cmds.append(f"setblock {x} 50 -299 deepslate_tile_stairs[facing=north,half=top]")
            cmds.append(f"setblock {x} 51 -299 deepslate_tiles")
            cmds.append(f"setblock {x} 52 -299 deepslate_tiles")
        # Center coffer recess
        cmds.append(f"setblock {x_start} 52 -301 deepslate_tile_stairs[facing=east,half=top]")
        cmds.append(f"setblock {x_mid} 52 -301 air")
        cmds.append(f"setblock {x_end} 52 -301 deepslate_tile_stairs[facing=west,half=top]")
        cmds.append(f"setblock {x_mid} 53 -301 polished_blackstone")

    # Corridor 2: East Arterial Corridor to Arcane Library (X: 124..139, Z: -302..-300, Width 3, Center Z = -301)
    cmds.append("# Corridor 2: East Arterial Corridor (Rotunda to Arcane Library)")
    cmds.append("fill 124 53 -302 139 53 -300 deepslate_tiles")

    east_rib_x = [124, 127, 131, 135, 139]
    for rx in east_rib_x:
        cmds.append(f"# Arch Rib at X = {rx}")
        # Keystone at Center Z = -301
        cmds.append(f"setblock {rx} 53 -301 copper_bulb[lit=true,powered=false]")
        cmds.append(f"setblock {rx} 52 -301 iron_chain[axis=y]")
        cmds.append(f"setblock {rx} 51 -301 soul_lantern[hanging=true]")
        cmds.append(f"setblock {rx} 50 -301 air")

        # North arch curve (Z = -302)
        cmds.append(f"setblock {rx} 53 -302 deepslate_bricks")
        cmds.append(f"setblock {rx} 52 -302 polished_deepslate_stairs[facing=south,half=top]")
        cmds.append(f"setblock {rx} 51 -302 polished_deepslate_stairs[facing=south,half=top]")
        cmds.append(f"setblock {rx} 50 -302 polished_deepslate_stairs[facing=south,half=top]")

        # South arch curve (Z = -300)
        cmds.append(f"setblock {rx} 53 -300 deepslate_bricks")
        cmds.append(f"setblock {rx} 52 -300 polished_deepslate_stairs[facing=north,half=top]")
        cmds.append(f"setblock {rx} 51 -300 polished_deepslate_stairs[facing=north,half=top]")
        cmds.append(f"setblock {rx} 50 -300 polished_deepslate_stairs[facing=north,half=top]")

        # North Wall Pilaster (Z = -303)
        cmds.append(f"setblock {rx} 46 -303 chiseled_deepslate")
        cmds.append(f"setblock {rx} 47 -303 chiseled_deepslate")
        cmds.append(f"setblock {rx} 48 -303 polished_deepslate")
        cmds.append(f"setblock {rx} 49 -303 polished_deepslate")
        cmds.append(f"setblock {rx} 50 -303 polished_deepslate_stairs[facing=south,half=top]")
        cmds.append(f"setblock {rx} 51 -303 deepslate_tiles")
        cmds.append(f"setblock {rx} 52 -303 deepslate_tiles")

        # South Wall Pilaster (Z = -299)
        cmds.append(f"setblock {rx} 46 -299 chiseled_deepslate")
        cmds.append(f"setblock {rx} 47 -299 chiseled_deepslate")
        cmds.append(f"setblock {rx} 48 -299 polished_deepslate")
        cmds.append(f"setblock {rx} 49 -299 polished_deepslate")
        cmds.append(f"setblock {rx} 50 -299 polished_deepslate_stairs[facing=north,half=top]")
        cmds.append(f"setblock {rx} 51 -299 deepslate_tiles")
        cmds.append(f"setblock {rx} 52 -299 deepslate_tiles")

    # Coffered Bays along East Corridor
    for i in range(len(east_rib_x) - 1):
        x_start = east_rib_x[i] + 1
        x_end = east_rib_x[i + 1] - 1
        x_mid = (x_start + x_end) // 2
        for x in range(x_start, x_end + 1):
            cmds.append(f"setblock {x} 52 -302 deepslate_tile_stairs[facing=south,half=top]")
            cmds.append(f"setblock {x} 52 -300 deepslate_tile_stairs[facing=north,half=top]")
            # Wall bays North (Z = -303)
            cmds.append(f"setblock {x} 46 -303 polished_blackstone")
            cmds.append(f"setblock {x} 47 -303 polished_deepslate_stairs[facing=south,half=bottom]")
            cmds.append(f"setblock {x} 48 -303 deepslate_bricks")
            cmds.append(f"setblock {x} 49 -303 deepslate_bricks")
            cmds.append(f"setblock {x} 50 -303 deepslate_tile_stairs[facing=south,half=top]")
            cmds.append(f"setblock {x} 51 -303 deepslate_tiles")
            cmds.append(f"setblock {x} 52 -303 deepslate_tiles")
            # Wall bays South (Z = -299)
            cmds.append(f"setblock {x} 46 -299 polished_blackstone")
            cmds.append(f"setblock {x} 47 -299 polished_deepslate_stairs[facing=north,half=bottom]")
            cmds.append(f"setblock {x} 48 -299 deepslate_bricks")
            cmds.append(f"setblock {x} 49 -299 deepslate_bricks")
            cmds.append(f"setblock {x} 50 -299 deepslate_tile_stairs[facing=north,half=top]")
            cmds.append(f"setblock {x} 51 -299 deepslate_tiles")
            cmds.append(f"setblock {x} 52 -299 deepslate_tiles")
        # Center coffer recess
        cmds.append(f"setblock {x_start} 52 -301 deepslate_tile_stairs[facing=east,half=top]")
        cmds.append(f"setblock {x_mid} 52 -301 air")
        cmds.append(f"setblock {x_end} 52 -301 deepslate_tile_stairs[facing=west,half=top]")
        cmds.append(f"setblock {x_mid} 53 -301 polished_blackstone")

    # Corridor 3: West Inter-Room Arterial (Armory to Blacksmith: X: 83..85, Z: -294..-292, Width 3, Center X = 84)
    cmds.append("# Corridor 3: West Inter-Room Arterial (Armory to Blacksmith)")
    cmds.append("fill 83 53 -294 85 53 -292 deepslate_tiles")
    # Keystone and rib at Z = -293
    cmds.append("setblock 84 53 -293 copper_bulb[lit=true,powered=false]")
    cmds.append("setblock 84 52 -293 iron_chain[axis=y]")
    cmds.append("setblock 84 51 -293 soul_lantern[hanging=true]")
    cmds.append("setblock 83 52 -293 polished_deepslate_stairs[facing=east,half=top]")
    cmds.append("setblock 83 51 -293 polished_deepslate_stairs[facing=east,half=top]")
    cmds.append("setblock 83 50 -293 polished_deepslate_stairs[facing=east,half=top]")
    cmds.append("setblock 85 52 -293 polished_deepslate_stairs[facing=west,half=top]")
    cmds.append("setblock 85 51 -293 polished_deepslate_stairs[facing=west,half=top]")
    cmds.append("setblock 85 50 -293 polished_deepslate_stairs[facing=west,half=top]")
    # Pilasters with corbels
    cmds.append("setblock 82 46 -293 chiseled_deepslate")
    cmds.append("setblock 82 47 -293 chiseled_deepslate")
    cmds.append("setblock 82 48 -293 polished_deepslate")
    cmds.append("setblock 82 49 -293 polished_deepslate")
    cmds.append("setblock 82 50 -293 polished_deepslate_stairs[facing=east,half=top]")
    cmds.append("setblock 86 46 -293 chiseled_deepslate")
    cmds.append("setblock 86 47 -293 chiseled_deepslate")
    cmds.append("setblock 86 48 -293 polished_deepslate")
    cmds.append("setblock 86 49 -293 polished_deepslate")
    cmds.append("setblock 86 50 -293 polished_deepslate_stairs[facing=west,half=top]")
    # Coffered vault ends at Z = -294 and Z = -292
    cmds.append("setblock 83 52 -294 deepslate_tile_stairs[facing=east,half=top]")
    cmds.append("setblock 85 52 -294 deepslate_tile_stairs[facing=west,half=top]")
    cmds.append("setblock 83 52 -292 deepslate_tile_stairs[facing=east,half=top]")
    cmds.append("setblock 85 52 -292 deepslate_tile_stairs[facing=west,half=top]")

    # Corridor 4: East Inter-Room Arterial (Library to Brewing: X: 149..151, Z: -294..-292, Width 3, Center X = 150)
    cmds.append("# Corridor 4: East Inter-Room Arterial (Library to Brewing)")
    cmds.append("fill 149 53 -294 151 53 -292 deepslate_tiles")
    # Keystone and rib at Z = -293
    cmds.append("setblock 150 53 -293 copper_bulb[lit=true,powered=false]")
    cmds.append("setblock 150 52 -293 iron_chain[axis=y]")
    cmds.append("setblock 150 51 -293 soul_lantern[hanging=true]")
    cmds.append("setblock 149 52 -293 polished_deepslate_stairs[facing=east,half=top]")
    cmds.append("setblock 149 51 -293 polished_deepslate_stairs[facing=east,half=top]")
    cmds.append("setblock 149 50 -293 polished_deepslate_stairs[facing=east,half=top]")
    cmds.append("setblock 151 52 -293 polished_deepslate_stairs[facing=west,half=top]")
    cmds.append("setblock 151 51 -293 polished_deepslate_stairs[facing=west,half=top]")
    cmds.append("setblock 151 50 -293 polished_deepslate_stairs[facing=west,half=top]")
    # Pilasters with corbels
    cmds.append("setblock 148 46 -293 chiseled_deepslate")
    cmds.append("setblock 148 47 -293 chiseled_deepslate")
    cmds.append("setblock 148 48 -293 polished_deepslate")
    cmds.append("setblock 148 49 -293 polished_deepslate")
    cmds.append("setblock 148 50 -293 polished_deepslate_stairs[facing=east,half=top]")
    cmds.append("setblock 152 46 -293 chiseled_deepslate")
    cmds.append("setblock 152 47 -293 chiseled_deepslate")
    cmds.append("setblock 152 48 -293 polished_deepslate")
    cmds.append("setblock 152 49 -293 polished_deepslate")
    cmds.append("setblock 152 50 -293 polished_deepslate_stairs[facing=west,half=top]")
    # Coffered vault ends at Z = -294 and Z = -292
    cmds.append("setblock 149 52 -294 deepslate_tile_stairs[facing=east,half=top]")
    cmds.append("setblock 151 52 -294 deepslate_tile_stairs[facing=west,half=top]")
    cmds.append("setblock 149 52 -292 deepslate_tile_stairs[facing=east,half=top]")
    cmds.append("setblock 151 52 -292 deepslate_tile_stairs[facing=west,half=top]")

    # Additional Arterial Branch Crossways: Farm to Boulevard, Housing to Boulevard, Blacksmith to Farm, Brewing to Housing
    cmds.append("# Additional Arterial Branch Crossways")
    # Farm to Boulevard crossway (X: 114..116, Z: -279..-277, Center Z = -278)
    cmds.append("fill 114 53 -279 116 53 -277 deepslate_tiles")
    cmds.append("setblock 115 53 -278 copper_bulb[lit=true,powered=false]")
    cmds.append("setblock 115 52 -278 iron_chain[axis=y]")
    cmds.append("setblock 115 51 -278 soul_lantern[hanging=true]")
    cmds.append("setblock 115 52 -279 deepslate_tile_stairs[facing=south,half=top]")
    cmds.append("setblock 115 52 -277 deepslate_tile_stairs[facing=north,half=top]")

    # Housing to Boulevard crossway (X: 118..120, Z: -279..-277, Center Z = -278)
    cmds.append("fill 118 53 -279 120 53 -277 deepslate_tiles")
    cmds.append("setblock 119 53 -278 copper_bulb[lit=true,powered=false]")
    cmds.append("setblock 119 52 -278 iron_chain[axis=y]")
    cmds.append("setblock 119 51 -278 soul_lantern[hanging=true]")
    cmds.append("setblock 119 52 -279 deepslate_tile_stairs[facing=south,half=top]")
    cmds.append("setblock 119 52 -277 deepslate_tile_stairs[facing=north,half=top]")

    # Blacksmith to Farm crossway (X: 94..96, Z: -284..-282, Center Z = -283)
    cmds.append("fill 94 53 -284 96 53 -282 deepslate_tiles")
    cmds.append("setblock 95 53 -283 copper_bulb[lit=true,powered=false]")
    cmds.append("setblock 95 52 -283 iron_chain[axis=y]")
    cmds.append("setblock 95 51 -283 soul_lantern[hanging=true]")
    cmds.append("setblock 95 52 -284 deepslate_tile_stairs[facing=south,half=top]")
    cmds.append("setblock 95 52 -282 deepslate_tile_stairs[facing=north,half=top]")

    # Brewing to Housing crossway (X: 138..140, Z: -284..-282, Center Z = -283)
    cmds.append("fill 138 53 -284 140 53 -282 deepslate_tiles")
    cmds.append("setblock 139 53 -283 copper_bulb[lit=true,powered=false]")
    cmds.append("setblock 139 52 -283 iron_chain[axis=y]")
    cmds.append("setblock 139 51 -283 soul_lantern[hanging=true]")
    cmds.append("setblock 139 52 -284 deepslate_tile_stairs[facing=south,half=top]")
    cmds.append("setblock 139 52 -282 deepslate_tile_stairs[facing=north,half=top]")

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
    """Verifies that key vaulted ceiling blocks and lighting fixtures exist on the server."""
    test_blocks = [
        # Rotunda Keystones
        ("117 53 -301", "copper_bulb[lit=true,powered=false]", "Rotunda Center Vault Keystone Bulb"),
        ("117 52 -301", "iron_chain[axis=y]", "Rotunda Center Vault Chain"),
        ("117 51 -301", "soul_lantern[hanging=true]", "Rotunda Center Vault Soul Lantern"),
        ("114 53 -301", "copper_bulb[lit=true,powered=false]", "Rotunda West Vault Keystone Bulb"),
        ("120 53 -301", "copper_bulb[lit=true,powered=false]", "Rotunda East Vault Keystone Bulb"),
        ("117 53 -304", "copper_bulb[lit=true,powered=false]", "Rotunda North Vault Keystone Bulb"),
        ("117 53 -298", "copper_bulb[lit=true,powered=false]", "Rotunda South Vault Keystone Bulb"),

        # South Boulevard Keystones and Ribs
        ("117 53 -294", "copper_bulb[lit=true,powered=false]", "Boulevard North Vault Keystone Bulb"),
        ("117 51 -294", "soul_lantern[hanging=true]", "Boulevard North Vault Soul Lantern"),
        ("117 53 -290", "copper_bulb[lit=true,powered=false]", "Boulevard Rib 1 Vault Keystone Bulb"),
        ("117 51 -290", "soul_lantern[hanging=true]", "Boulevard Rib 1 Vault Soul Lantern"),
        ("116 50 -290", "polished_deepslate_stairs[facing=east,half=top]", "Boulevard Rib 1 West Springer at Y50"),
        ("118 50 -290", "polished_deepslate_stairs[facing=west,half=top]", "Boulevard Rib 1 East Springer at Y50"),
        ("115 50 -290", "polished_deepslate_stairs[facing=east,half=top]", "Boulevard Rib 1 West Corbel at Y50"),
        ("119 50 -290", "polished_deepslate_stairs[facing=west,half=top]", "Boulevard Rib 1 East Corbel at Y50"),
        ("117 53 -262", "copper_bulb[lit=true,powered=false]", "Boulevard South Vault Keystone Bulb"),
        ("117 51 -262", "soul_lantern[hanging=true]", "Boulevard South Vault Soul Lantern"),

        # West Arterial Corridor Keystones and Ribs
        ("107 53 -301", "copper_bulb[lit=true,powered=false]", "West Corridor Rib Keystone Bulb"),
        ("107 51 -301", "soul_lantern[hanging=true]", "West Corridor Rib Soul Lantern"),
        ("107 50 -302", "polished_deepslate_stairs[facing=south,half=top]", "West Corridor Rib North Springer at Y50"),
        ("107 50 -300", "polished_deepslate_stairs[facing=north,half=top]", "West Corridor Rib South Springer at Y50"),
        ("107 50 -303", "polished_deepslate_stairs[facing=south,half=top]", "West Corridor North Corbel at Y50"),

        # East Arterial Corridor Keystones and Ribs
        ("127 53 -301", "copper_bulb[lit=true,powered=false]", "East Corridor Rib Keystone Bulb"),
        ("127 51 -301", "soul_lantern[hanging=true]", "East Corridor Rib Soul Lantern"),
        ("127 50 -302", "polished_deepslate_stairs[facing=south,half=top]", "East Corridor Rib North Springer at Y50"),
        ("127 50 -300", "polished_deepslate_stairs[facing=north,half=top]", "East Corridor Rib South Springer at Y50"),

        # Inter-Room Arterials
        ("84 53 -293", "copper_bulb[lit=true,powered=false]", "West Inter-Room Connector Keystone Bulb"),
        ("84 51 -293", "soul_lantern[hanging=true]", "West Inter-Room Connector Soul Lantern"),
        ("150 53 -293", "copper_bulb[lit=true,powered=false]", "East Inter-Room Connector Keystone Bulb"),
        ("150 51 -293", "soul_lantern[hanging=true]", "East Inter-Room Connector Soul Lantern"),
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
    print("Beginning architectural vaulting generation...")
    all_cmds = []
    all_cmds.extend(build_rotunda_vaults())
    all_cmds.extend(build_boulevard_vaults())
    all_cmds.extend(build_arterial_corridors_vaults())

    # Write local mcfunction file
    write_mcfunction("bunker_vaults.mcfunction", all_cmds)

    # Sync file to remote server datapack
    sync_remote_mcfunction("bunker_vaults.mcfunction")

    # Execute all commands over RCON socket protocol
    print("\nExecuting vault construction commands via RCON socket protocol...")
    execute_remote_batch(all_cmds)

    # Verify live blockstates
    success = verify_live_blockstates()
    if success:
        print("\nAll vaulted ceilings, arch ribs, corbels, and illuminated keystones successfully verified!")
    else:
        print("\nVerification encountered issues. Inspect above logs.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
