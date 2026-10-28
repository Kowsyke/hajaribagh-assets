#!/usr/bin/env python3
"""Build Sector 15: The Alchemical Distillation Catacombs in Tier 3.

Constructs Tier 3 Alchemical Catacombs for King Abir's bunker at X: 140..160, Z: -291..-275, Y: 36..45
directly beneath Sector 4 Brewing Lab (Y: 46..53).
Features include:
1. Subfloor at Y: 36, floor at Y: 37 with polished deepslate and smooth basalt trim.
2. Ceiling vault strictly capped at Y: 45 to preserve Sector 4 floor at Y: 46.
3. Access gallery connecting south from Forbidden Apocrypha Archive (Z: -296).
4. Industrial copper alembic distillery with condensation column, grates, brewing stands, and vapor chamber.
5. Multi-level hydroponic nether wart terraces along east wall with recessed shroomlights and soul lanterns.
6. Automated potion bottling line with varied water cauldrons, hoppers, and stocked potion barrels.
7. Coffered barrel vault ceilings with transverse arch ribs, lit copper bulbs, and hanging soul lanterns.
8. Dual water bubble elevator connecting Sector 15 (Y: 36) up to Sector 4 Brewing Lab floor (Y: 46).
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

def build_catacombs_shell():
    """Excavates and constructs the reinforced shell within strictly Y: 36..45."""
    cmds = [
        "# Sector 15: Alchemical Catacombs Shell (X: 140..160, Z: -291..-275, Y: 36..45)",
        # 1. Excavate clear interior chamber volume
        "fill 141 37 -290 159 44 -276 air",
        # 2. Subfloor foundation at Y: 36
        "fill 140 36 -291 160 36 -275 deepslate_tiles",
        # 3. Main flooring at Y: 37 with smooth basalt trim and polished deepslate
        "fill 141 37 -290 159 37 -290 smooth_basalt",
        "fill 141 37 -276 159 37 -276 smooth_basalt",
        "fill 141 37 -290 141 37 -276 smooth_basalt",
        "fill 159 37 -290 159 37 -276 smooth_basalt",
        "fill 142 37 -289 158 37 -277 polished_deepslate",
        "fill 146 37 -289 146 37 -277 deepslate_tiles",
        "fill 154 37 -289 154 37 -277 deepslate_tiles",
        "fill 142 37 -283 158 37 -283 smooth_basalt",
        "fill 150 37 -289 150 37 -277 smooth_basalt",
        # 4. Strict vault ceiling cap at Y: 45
        "fill 140 45 -291 160 45 -275 deepslate_tiles",
        # 5. Perimeter outer walls
        "fill 140 36 -291 160 45 -291 deepslate_bricks",
        "fill 140 36 -275 160 45 -275 deepslate_bricks",
        "fill 140 36 -291 140 45 -275 deepslate_bricks",
        "fill 160 36 -291 160 45 -275 deepslate_bricks",
        # Corner structural columns
        "fill 140 36 -291 140 45 -291 crying_obsidian",
        "fill 160 36 -291 160 45 -291 crying_obsidian",
        "fill 140 36 -275 140 45 -275 crying_obsidian",
        "fill 160 36 -275 160 45 -275 crying_obsidian",
    ]
    return cmds

def build_entrance_and_gallery():
    """Builds access gallery connecting south of Forbidden Apocrypha Archive into Sector 15."""
    cmds = [
        "# Access Gallery and Entry Portal from Forbidden Apocrypha (Z: -296 to -291)",
        # Break through south wall of Apocrypha Archive at Z: -296
        "fill 149 38 -296 151 41 -296 air",
        "fill 149 37 -296 151 37 -296 polished_deepslate",
        # Gallery excavation and architecture (Z: -295..-292)
        "fill 149 38 -295 151 41 -292 air",
        "fill 148 36 -295 152 36 -292 deepslate_tiles",
        "fill 149 37 -295 151 37 -292 polished_deepslate",
        "fill 148 37 -295 148 37 -292 smooth_basalt",
        "fill 152 37 -295 152 37 -292 smooth_basalt",
        "fill 148 38 -295 148 42 -292 deepslate_bricks",
        "fill 152 38 -295 152 42 -292 deepslate_bricks",
        "fill 149 42 -295 151 42 -292 deepslate_tiles",
        "setblock 150 42 -294 copper_bulb[lit=true,powered=false]",
        # North entrance portal at Z: -291
        "fill 149 38 -291 151 41 -291 air",
        "fill 148 38 -291 148 40 -291 waxed_copper_block",
        "fill 152 38 -291 152 40 -291 waxed_copper_block",
        "setblock 148 41 -291 waxed_cut_copper_stairs[facing=east,half=top]",
        "setblock 152 41 -291 waxed_cut_copper_stairs[facing=west,half=top]",
        "setblock 149 42 -291 waxed_copper_block",
        "setblock 151 42 -291 waxed_copper_block",
        "setblock 150 42 -291 copper_bulb[lit=true,powered=false]",
    ]
    return cmds

def build_coffered_vault_ceilings():
    """Constructs coffered barrel vaults curving from Y: 45 down to Y: 42 with ribs and lit copper bulbs."""
    cmds = [
        "# Coffered Barrel Vaults with Pilasters and Lit Copper Bulbs (Y: 42..45)",
    ]
    rib_z_coords = [-291, -287, -283, -279, -275]
    for z in rib_z_coords:
        cmds.append(f"# Structural Rib at Z = {z}")
        # Pilasters at west (141) and east (159)
        cmds.append(f"fill 141 37 {z} 141 40 {z} deepslate_bricks")
        cmds.append(f"setblock 141 41 {z} chiseled_deepslate")
        cmds.append(f"setblock 141 42 {z} deepslate_brick_stairs[facing=east,half=top]")
        cmds.append(f"fill 159 37 {z} 159 40 {z} deepslate_bricks")
        cmds.append(f"setblock 159 41 {z} chiseled_deepslate")
        cmds.append(f"setblock 159 42 {z} deepslate_brick_stairs[facing=west,half=top]")
        # Arch stairs curving up to Y: 44
        cmds.append(f"setblock 142 43 {z} deepslate_tile_stairs[facing=east,half=top]")
        cmds.append(f"setblock 143 43 {z} deepslate_tile_stairs[facing=east,half=top]")
        cmds.append(f"setblock 144 44 {z} deepslate_tile_stairs[facing=east,half=top]")
        cmds.append(f"setblock 145 44 {z} deepslate_tile_stairs[facing=east,half=top]")
        cmds.append(f"setblock 158 43 {z} deepslate_tile_stairs[facing=west,half=top]")
        cmds.append(f"setblock 157 43 {z} deepslate_tile_stairs[facing=west,half=top]")
        cmds.append(f"setblock 156 44 {z} deepslate_tile_stairs[facing=west,half=top]")
        cmds.append(f"setblock 155 44 {z} deepslate_tile_stairs[facing=west,half=top]")
        # Transverse apex beam at Y: 45
        cmds.append(f"fill 146 45 {z} 154 45 {z} polished_deepslate")
        # Keystone bulb and hanging soul lantern
        cmds.append(f"setblock 150 45 {z} copper_bulb[lit=true,powered=false]")
        cmds.append(f"setblock 150 44 {z} iron_chain[axis=y]")
        cmds.append(f"setblock 150 43 {z} soul_lantern[hanging=true]")

    # Coffered Bays between ribs
    bays = [
        (-290, -288, -289),
        (-286, -284, -285),
        (-282, -280, -281),
        (-278, -276, -277),
    ]
    for z1, z2, z_mid in bays:
        cmds.append(f"# Coffered Bay: Z = {z1}..{z2}")
        # Recessed copper grates in center apex panel at Y: 45
        cmds.append(f"fill 148 45 {z1} 152 45 {z2} waxed_copper_grate")
        cmds.append(f"fill 145 45 {z1} 147 45 {z2} deepslate_tiles")
        cmds.append(f"fill 153 45 {z1} 155 45 {z2} deepslate_tiles")
        for z in range(z1, z2 + 1):
            cmds.append(f"setblock 142 43 {z} deepslate_tile_stairs[facing=east,half=top]")
            cmds.append(f"setblock 143 43 {z} deepslate_tile_stairs[facing=east,half=top]")
            cmds.append(f"setblock 144 44 {z} deepslate_tile_stairs[facing=east,half=top]")
            cmds.append(f"setblock 158 43 {z} deepslate_tile_stairs[facing=west,half=top]")
            cmds.append(f"setblock 157 43 {z} deepslate_tile_stairs[facing=west,half=top]")
            cmds.append(f"setblock 156 44 {z} deepslate_tile_stairs[facing=west,half=top]")
        # Flanking copper bulbs in bay
        cmds.append(f"setblock 146 44 {z_mid} copper_bulb[lit=true,powered=false]")
        cmds.append(f"setblock 154 44 {z_mid} copper_bulb[lit=true,powered=false]")

    return cmds

def build_industrial_copper_alembic():
    """Constructs the central copper alembic distillery with condensation column and vapor chamber."""
    cmds = [
        "# Industrial Copper Alembic Distillery (Center: 150, Y, -283)",
        # Subfloor illumination beneath grates at Y: 36
        "fill 147 36 -286 153 36 -280 sea_lantern",
        # Raised copper platform at Y: 37
        "fill 147 37 -286 153 37 -280 waxed_copper_grate",
        "fill 148 37 -285 152 37 -281 waxed_cut_copper",
        "setblock 148 37 -285 waxed_copper_block",
        "setblock 152 37 -285 waxed_copper_block",
        "setblock 148 37 -281 waxed_copper_block",
        "setblock 152 37 -281 waxed_copper_block",
        "setblock 147 37 -284 waxed_cut_copper_stairs[facing=east,half=bottom]",
        "setblock 147 37 -282 waxed_cut_copper_stairs[facing=east,half=bottom]",
        "setblock 153 37 -284 waxed_cut_copper_stairs[facing=west,half=bottom]",
        "setblock 153 37 -282 waxed_cut_copper_stairs[facing=west,half=bottom]",
        # Central boiler at Y: 37..38
        "setblock 150 37 -283 magma_block",
        "setblock 150 38 -283 cauldron",
        # Corner pedestals at Y: 38
        "setblock 149 38 -284 waxed_copper_block",
        "setblock 151 38 -284 waxed_copper_block",
        "setblock 149 38 -282 waxed_copper_block",
        "setblock 151 38 -282 waxed_copper_block",
        # Four cardinal brewing stands at Y: 38
        "setblock 150 38 -284 brewing_stand",
        "setblock 150 38 -282 brewing_stand",
        "setblock 149 38 -283 brewing_stand",
        "setblock 151 38 -283 brewing_stand",
        # Vapor chamber at Y: 39..40
        "setblock 149 39 -283 tinted_glass",
        "setblock 151 39 -283 tinted_glass",
        "setblock 150 39 -284 tinted_glass",
        "setblock 150 39 -282 tinted_glass",
        "setblock 149 40 -283 tinted_glass",
        "setblock 151 40 -283 tinted_glass",
        "setblock 150 40 -284 tinted_glass",
        "setblock 150 40 -282 tinted_glass",
        "setblock 150 39 -283 waxed_copper_grate",
        "setblock 150 40 -283 waxed_copper_grate",
        "setblock 149 39 -284 waxed_cut_copper_stairs[facing=north,half=bottom]",
        "setblock 151 39 -284 waxed_cut_copper_stairs[facing=north,half=bottom]",
        "setblock 149 39 -282 waxed_cut_copper_stairs[facing=south,half=bottom]",
        "setblock 151 39 -282 waxed_cut_copper_stairs[facing=south,half=bottom]",
        # Vertical condensation column at Y: 41..44
        "setblock 150 41 -283 waxed_copper_block",
        "setblock 150 42 -283 waxed_copper_grate",
        "setblock 150 43 -283 waxed_copper_block",
        "setblock 150 44 -283 lightning_rod[facing=up]",
        # Distillation tubes (lightning rods) branching at Y: 41
        "setblock 149 41 -283 lightning_rod[facing=up]",
        "setblock 151 41 -283 lightning_rod[facing=up]",
        "setblock 150 41 -284 lightning_rod[facing=up]",
        "setblock 150 41 -282 lightning_rod[facing=up]",
    ]
    return cmds

def build_hydroponic_terraces():
    """Constructs stepped hydroponic nether wart terraces with recessed shroomlights along the east wall."""
    cmds = [
        "# Hydroponic Nether Wart Terraces along East Wall (X: 156..159, Z: -288..-278)",
        # End retaining buttresses
        "fill 156 37 -288 159 41 -288 deepslate_bricks",
        "fill 156 37 -278 159 41 -278 deepslate_bricks",
        "setblock 156 41 -288 crying_obsidian",
        "setblock 156 41 -278 crying_obsidian",
        "setblock 156 38 -288 soul_lantern[hanging=false]",
        "setblock 156 38 -278 soul_lantern[hanging=false]",
        # Front retaining curb at X: 156, Y: 37
        "fill 156 37 -287 156 37 -279 polished_deepslate_stairs[facing=west,half=bottom]",
        # Tier 1: Low Terrace (X: 157, Z: -287..-279)
        "fill 157 36 -287 157 36 -279 shroomlight",
        "fill 157 37 -287 157 37 -279 soul_sand",
        "fill 157 38 -287 157 38 -279 nether_wart[age=3]",
        # Tier 2: Middle Terrace (X: 158, Z: -287..-279)
        "fill 158 37 -287 158 37 -279 shroomlight",
        "fill 158 38 -287 158 38 -279 soul_sand",
        "fill 158 39 -287 158 39 -279 nether_wart[age=3]",
        # Tier 3: High Terrace (X: 159, Z: -287..-279)
        "fill 159 38 -287 159 38 -279 shroomlight",
        "fill 159 39 -287 159 39 -279 soul_sand",
        "fill 159 40 -287 159 40 -279 nether_wart[age=3]",
        # Overhead hanging soul lanterns
        "setblock 158 44 -285 iron_chain[axis=y]",
        "setblock 158 43 -285 soul_lantern[hanging=true]",
        "setblock 158 44 -281 iron_chain[axis=y]",
        "setblock 158 43 -281 soul_lantern[hanging=true]",
    ]
    return cmds


def build_automated_potion_bottling_line():
    """Constructs the automated potion bottling line with cauldrons, hoppers, and stocked potion barrels."""
    cmds = [
        "# Automated Potion Bottling Line (West Wall: X: 141..144, Z: -289..-283)",
        # Foundation and counter
        "fill 141 37 -289 143 37 -283 smooth_basalt",
        "fill 141 37 -289 141 37 -283 polished_blackstone",
        # Cauldrons with varied water levels along X: 141, Y: 38
        "setblock 141 38 -289 water_cauldron[level=3]",
        "setblock 141 38 -288 water_cauldron[level=2]",
        "setblock 141 38 -287 water_cauldron[level=1]",
        "setblock 141 38 -286 water_cauldron[level=3]",
        "setblock 141 38 -285 water_cauldron[level=2]",
        "setblock 141 38 -284 cauldron",
        # Conveyor hoppers along X: 142, Y: 38
        "fill 142 38 -289 142 38 -284 hopper[facing=south]",
        # Stocked barrels along X: 143, Y: 38
        # Barrel 1: Splash Potions of Healing
        'setblock 143 38 -289 barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:splash_potion",count:16b,components:{"minecraft:potion_contents":{potion:"minecraft:healing"}}},{Slot:1b,id:"minecraft:splash_potion",count:16b,components:{"minecraft:potion_contents":{potion:"minecraft:strong_healing"}}}]}',
        # Barrel 2: Splash Potions of Speed (Swiftness)
        'setblock 143 38 -288 barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:splash_potion",count:16b,components:{"minecraft:potion_contents":{potion:"minecraft:swiftness"}}},{Slot:1b,id:"minecraft:splash_potion",count:16b,components:{"minecraft:potion_contents":{potion:"minecraft:strong_swiftness"}}}]}',
        # Barrel 3: Splash Potions of Night Vision
        'setblock 143 38 -286 barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:splash_potion",count:16b,components:{"minecraft:potion_contents":{potion:"minecraft:night_vision"}}},{Slot:1b,id:"minecraft:splash_potion",count:16b,components:{"minecraft:potion_contents":{potion:"minecraft:long_night_vision"}}}]}',
        # Barrel 4: Splash Potions of Fire Resistance
        'setblock 143 38 -285 barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:splash_potion",count:16b,components:{"minecraft:potion_contents":{potion:"minecraft:fire_resistance"}}},{Slot:1b,id:"minecraft:splash_potion",count:16b,components:{"minecraft:potion_contents":{potion:"minecraft:long_fire_resistance"}}}]}',
        # Master Apothecary Reserve Barrel
        'setblock 143 38 -284 barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:splash_potion",count:16b,components:{"minecraft:potion_contents":{potion:"minecraft:healing"}}},{Slot:1b,id:"minecraft:splash_potion",count:16b,components:{"minecraft:potion_contents":{potion:"minecraft:swiftness"}}},{Slot:2b,id:"minecraft:splash_potion",count:16b,components:{"minecraft:potion_contents":{potion:"minecraft:night_vision"}}},{Slot:3b,id:"minecraft:splash_potion",count:16b,components:{"minecraft:potion_contents":{potion:"minecraft:fire_resistance"}}}]}',
        # Overhead brewing stand and feed hopper
        "setblock 143 39 -287 brewing_stand",
        "setblock 142 39 -287 hopper[facing=down]",
        "setblock 142 41 -287 copper_bulb[lit=true,powered=false]",
        "setblock 141 40 -289 soul_lantern[hanging=false]",
        "setblock 141 40 -284 soul_lantern[hanging=false]",
    ]
    return cmds

def build_dual_water_bubble_elevators():
    """Constructs dual water bubble elevators connecting Sector 15 at Y: 36 to Sector 4 at Y: 46."""
    cmds = [
        "# Dual Water Bubble Elevators (Soul Sand Ascent X: 142, Magma Descent X: 144, Z: -277)",
        # Shaft excavation
        "fill 141 36 -278 145 49 -276 air",
        # Enclosure walls
        "fill 141 36 -276 145 49 -276 deepslate_tiles",
        "fill 141 36 -278 141 49 -277 deepslate_tiles",
        "fill 145 36 -278 145 49 -277 deepslate_tiles",
        "fill 143 36 -278 143 49 -277 tinted_glass",
        # Lower foundation at Y: 36
        "setblock 142 36 -277 soul_sand",
        "setblock 144 36 -277 magma_block",
        "setblock 143 36 -277 deepslate_tiles",
        "fill 141 36 -278 145 36 -278 polished_deepslate",
        # Sector 15 Lower Doorways at Y: 37..38 (containment signs)
        "fill 142 37 -278 142 38 -278 air",
        "fill 144 37 -278 144 38 -278 air",
        "setblock 142 37 -278 spruce_wall_sign[facing=east]",
        "setblock 142 38 -278 spruce_wall_sign[facing=east]",
        "setblock 144 37 -278 spruce_wall_sign[facing=west]",
        "setblock 144 38 -278 spruce_wall_sign[facing=west]",
        # Observation glass on lower shaft front (Y: 39..45)
        "fill 142 39 -278 142 45 -278 tinted_glass",
        "fill 144 39 -278 144 45 -278 tinted_glass",
        # Lower Indicator Header at Y: 39
        "setblock 142 39 -278 emerald_block",
        "setblock 144 39 -278 redstone_block",
        "setblock 143 39 -278 copper_bulb[lit=true,powered=false]",
        # Bubble columns spanning Y: 37 to Y: 46
        "fill 142 37 -277 142 46 -277 bubble_column[drag=false]",
        "fill 144 37 -277 144 46 -277 bubble_column[drag=true]",
        # Sector 4 Upper Doorways at Y: 47..48 (Sector 4 floor is Y: 46)
        "fill 141 46 -278 145 46 -278 polished_andesite",
        "fill 142 47 -278 142 48 -278 air",
        "fill 144 47 -278 144 48 -278 air",
        "setblock 142 47 -278 spruce_wall_sign[facing=east]",
        "setblock 142 48 -278 spruce_wall_sign[facing=east]",
        "setblock 144 47 -278 spruce_wall_sign[facing=west]",
        "setblock 144 48 -278 spruce_wall_sign[facing=west]",
        # Upper Indicator Header at Y: 49
        "setblock 142 49 -278 emerald_block",
        "setblock 144 49 -278 redstone_block",
        "setblock 143 49 -278 copper_bulb[lit=true,powered=false]",
        # Shaft top ceiling cap at Y: 49
        "fill 141 49 -277 145 49 -276 deepslate_tiles",
        "setblock 142 49 -277 sea_lantern",
        "setblock 144 49 -277 sea_lantern",
    ]
    return cmds

def execute_remote_batch(all_cmds, host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Executes all commands via RCON in batches under 75 commands per socket invocation."""
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
            f"python3 -c {subprocess.list2cmdline([py_code])}"
        ]
        res = subprocess.run(ssh_cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"Batch {i//batch_size + 1} error: {res.stderr}", file=sys.stderr)
            sys.exit(res.returncode)
        print(f"Batch {i//batch_size + 1}/{(total + batch_size - 1)//batch_size} ({min(i + batch_size, total)}/{total}) complete.")

def verify_live_blockstates(host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Verifies that all critical Sector 15 structures, alembic, terraces, bottling, and elevator exist live."""
    test_blocks = [
        # Subfloor and Floor Boundaries
        ("145 36 -287", "deepslate_tiles", "Subfloor Foundation at Y: 36"),
        ("145 37 -287", "polished_deepslate", "Main Floor Field at Y: 37"),
        ("141 37 -290", "smooth_basalt", "West Perimeter Floor Trim at Y: 37"),
        ("159 37 -290", "smooth_basalt", "East Perimeter Floor Trim at Y: 37"),
        ("141 37 -285", "polished_blackstone", "Bottling Line Foundation Counter at Y: 37"),
        # Outer Perimeter Walls
        ("145 40 -291", "deepslate_bricks", "North Perimeter Wall at Y: 40"),
        ("150 40 -275", "deepslate_bricks", "South Perimeter Wall at Y: 40"),
        ("140 40 -283", "deepslate_bricks", "West Perimeter Wall at Y: 40"),
        ("160 40 -283", "deepslate_bricks", "East Perimeter Wall at Y: 40"),
        # Strict Ceiling Height Invariant
        ("150 45 -283", "copper_bulb[lit=true,powered=false]", "Ceiling Vault Cap at Y: 45"),
        ("150 46 -283", "polished_andesite", "Preserved Sector 4 Brewing Lab Floor at Y: 46"),
        # Access Gallery and Entrance
        ("150 37 -294", "polished_deepslate", "Access Gallery Floor at Z: -294"),
        ("150 42 -294", "copper_bulb[lit=true,powered=false]", "Access Gallery Keystone Bulb at Y: 42"),
        ("150 42 -291", "copper_bulb[lit=true,powered=false]", "North Portal Keystone Bulb at Z: -291"),
        # Industrial Copper Alembic Distillery
        ("149 37 -285", "waxed_cut_copper", "Central Alembic Copper Plinth at Y: 37"),
        ("147 37 -283", "waxed_copper_grate", "Central Alembic Inspection Grate at Y: 37"),
        ("150 38 -283", "cauldron", "Central Alembic Boiler Cauldron at Y: 38"),
        ("150 38 -284", "brewing_stand", "Central Alembic North Brewing Stand"),
        ("150 38 -282", "brewing_stand", "Central Alembic South Brewing Stand"),
        ("149 38 -283", "brewing_stand", "Central Alembic West Brewing Stand"),
        ("151 38 -283", "brewing_stand", "Central Alembic East Brewing Stand"),
        ("149 39 -283", "tinted_glass", "Alembic Vapor Chamber West Wall at Y: 39"),
        ("151 39 -283", "tinted_glass", "Alembic Vapor Chamber East Wall at Y: 39"),
        ("150 41 -283", "waxed_copper_block", "Alembic Condensation Column at Y: 41"),
        ("149 41 -283", "lightning_rod[facing=up]", "Alembic Distillation Coil Rod West at Y: 41"),
        ("150 44 -283", "lightning_rod[facing=up]", "Alembic Condenser Column Peak Rod at Y: 44"),
        # Hydroponic Nether Wart Terraces
        ("157 36 -283", "shroomlight", "Terrace Tier 1 Recessed Shroomlight at Y: 36"),
        ("157 37 -283", "soul_sand", "Terrace Tier 1 Soul Sand Bed at Y: 37"),
        ("157 38 -283", "nether_wart[age=3]", "Terrace Tier 1 Mature Nether Wart at Y: 38"),
        ("158 37 -283", "shroomlight", "Terrace Tier 2 Recessed Shroomlight at Y: 37"),
        ("158 38 -283", "soul_sand", "Terrace Tier 2 Soul Sand Bed at Y: 38"),
        ("158 39 -283", "nether_wart[age=3]", "Terrace Tier 2 Mature Nether Wart at Y: 39"),
        ("159 38 -283", "shroomlight", "Terrace Tier 3 Recessed Shroomlight at Y: 38"),
        ("159 39 -283", "soul_sand", "Terrace Tier 3 Soul Sand Bed at Y: 39"),
        ("159 40 -283", "nether_wart[age=3]", "Terrace Tier 3 Mature Nether Wart at Y: 40"),
        ("156 38 -288", "soul_lantern[hanging=false]", "Terrace North Boundary Soul Lantern"),
        ("156 38 -278", "soul_lantern[hanging=false]", "Terrace South Boundary Soul Lantern"),
        # Automated Potion Bottling Line
        ("141 38 -289", "water_cauldron[level=3]", "Bottling Line Primary Purification Cauldron Level 3"),
        ("141 38 -288", "water_cauldron[level=2]", "Bottling Line Dilution Cauldron Level 2"),
        ("141 38 -287", "water_cauldron[level=1]", "Bottling Line Reagent Cauldron Level 1"),
        ("142 38 -288", "hopper[facing=south]", "Bottling Line Conveyor Hopper at Y: 38"),
        ("143 38 -289", "barrel[facing=up]", "Stocked Healing Potion Barrel at Y: 38"),
        ("143 38 -288", "barrel[facing=up]", "Stocked Speed Potion Barrel at Y: 38"),
        ("143 38 -286", "barrel[facing=up]", "Stocked Night Vision Potion Barrel at Y: 38"),
        ("143 38 -285", "barrel[facing=up]", "Stocked Fire Resistance Potion Barrel at Y: 38"),
        ("143 38 -284", "barrel[facing=up]", "Master Apothecary Reserve Potion Barrel at Y: 38"),
        ("143 39 -287", "brewing_stand", "Bottling Line Overhead Brewing Stand at Y: 39"),
        # Coffered Vault Ceilings and Ribs
        ("150 45 -287", "copper_bulb[lit=true,powered=false]", "Vault Rib Z-287 Keystone Bulb at Y: 45"),
        ("150 43 -287", "soul_lantern[hanging=true]", "Vault Rib Z-287 Hanging Soul Lantern at Y: 43"),
        ("150 45 -279", "copper_bulb[lit=true,powered=false]", "Vault Rib Z-279 Keystone Bulb at Y: 45"),
        ("150 45 -285", "waxed_copper_grate", "Coffered Bay Recessed Panel at Y: 45"),
        # Dual Water Bubble Elevators
        ("142 36 -277", "soul_sand", "Dual Elevator Ascent Soul Sand Engine at Y: 36"),
        ("144 36 -277", "magma_block", "Dual Elevator Descent Magma Engine at Y: 36"),
        ("142 40 -277", "bubble_column[drag=false]", "Dual Elevator Mid-Shaft Ascent Bubble Column"),
        ("144 40 -277", "bubble_column[drag=true]", "Dual Elevator Mid-Shaft Descent Bubble Column"),
        ("142 37 -278", "spruce_wall_sign[facing=east]", "Sector 15 Lower Ascent Doorway Containment Sign"),
        ("144 37 -278", "spruce_wall_sign[facing=west]", "Sector 15 Lower Descent Doorway Containment Sign"),
        ("142 39 -278", "emerald_block", "Sector 15 Lower Ascent Emerald Indicator at Y: 39"),
        ("144 39 -278", "redstone_block", "Sector 15 Lower Descent Redstone Indicator at Y: 39"),
        ("142 46 -277", "bubble_column[drag=false]", "Dual Elevator Upper Ascent Bubble Exit at Y: 46"),
        ("144 46 -277", "bubble_column[drag=true]", "Dual Elevator Upper Descent Bubble Entry at Y: 46"),
        ("142 47 -278", "spruce_wall_sign[facing=east]", "Sector 4 Upper Ascent Doorway Containment Sign"),
        ("144 47 -278", "spruce_wall_sign[facing=west]", "Sector 4 Upper Descent Doorway Containment Sign"),
        ("142 49 -278", "emerald_block", "Sector 4 Upper Ascent Emerald Indicator at Y: 49"),
        ("144 49 -278", "redstone_block", "Sector 4 Upper Descent Redstone Indicator at Y: 49"),
    ]

    py_code = f"""
import socket, struct, sys

with open('/home/ubuntu/minecraft-server/server.properties') as f:
    props = dict(line.strip().split('=', 1) for line in f if '=' in line and not line.startswith('#'))

rcon_port = int(props.get('rcon.port', 25575))
rcon_pass = props.get('rcon.password', '')

s = socket.create_connection(('127.0.0.1', rcon_port), timeout=10)
s.sendall(struct.pack('<iii', len(rcon_pass) + 10, 1, 3) + rcon_pass.encode('utf-8') + b'\\x00\\x00')
auth_resp = s.recv(4096)

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
    sys.exit(1)
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
    print("Beginning Sector 15 Alchemical Catacombs construction...")
    all_cmds = []
    all_cmds.extend(build_catacombs_shell())
    all_cmds.extend(build_entrance_and_gallery())
    all_cmds.extend(build_coffered_vault_ceilings())
    all_cmds.extend(build_industrial_copper_alembic())
    all_cmds.extend(build_hydroponic_terraces())
    all_cmds.extend(build_automated_potion_bottling_line())
    all_cmds.extend(build_dual_water_bubble_elevators())

    # Write local mcfunction file
    write_mcfunction("bunker_alchemical_catacombs.mcfunction", all_cmds)

    # Sync file to remote server datapack
    sync_remote_mcfunction("bunker_alchemical_catacombs.mcfunction")

    # Execute all commands over RCON socket protocol
    print("\nExecuting Sector 15 construction commands via RCON...")
    execute_remote_batch(all_cmds)

    # Verify live blockstates
    success = verify_live_blockstates()
    if success:
        print("\nAll Sector 15 Alchemical Catacombs structures, alembic, terraces, bottling, and elevators verified successfully!")
    else:
        print("\nVerification encountered issues. Inspect above logs.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
