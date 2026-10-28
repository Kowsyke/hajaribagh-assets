#!/usr/bin/env python3
"""Build Sector 17: The Subterranean Arboretum and Exotic Flora Sanctuary.

Constructs Tier 2 Subterranean Arboretum for King Abir's bunker at X: 96..114, Z: -276..-262, Y: 46..53.
Features include:
1. Floor level at Y: 46 with lush moss, grass, podzol, and winding stone walkways.
2. Strictly capped ceiling vault at Y: 53 (never exceeds Y: 53).
3. Structural perimeter walls of deepslate bricks, mossy stone bricks, and tuff bricks with mud brick pilasters.
4. East double portal into South Boulevard (X: 114..115, Z: -270..-268) with green banner valances.
5. North Breezeway garden archway into Sector 5 Farm (Z: -276..-277, X: 104..106).
6. Central Ancient Canopy Tree with twisted mangrove and dark oak trunk, roots, and azalea canopy with hidden lights.
7. Subterranean Koi Pond winding stream with clay, gravel, sea pickles, lily pads, and big/small dripleaf.
8. Exotic Flora beds featuring sniffer crops (pitcher plants, torchflowers), azaleas, and pink petals.
9. Ceiling flora with hanging cave vines, berries, hanging roots, and spore blossoms.
10. Botanical Research Pavilion with polished tuff benches, lectern, and decorated pots with ferns.
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

def build_arboretum_shell():
    """Excavates and constructs the structural shell within strictly Y: 46..53."""
    cmds = [
        "# Sector 17: Subterranean Arboretum Shell (X: 96..114, Z: -276..-262, Y: 46..53)",
        # 1. Excavate clear interior chamber volume
        "fill 97 46 -275 113 52 -263 air",
        # 2. Subfloor foundation at Y: 45
        "fill 96 45 -276 114 45 -262 moss_block",
        # 3. Main flooring at Y: 46 with moss, grass, podzol, and rooted dirt
        "fill 97 46 -275 113 46 -263 moss_block",
        "fill 98 46 -274 103 46 -270 grass_block",
        "fill 107 46 -267 112 46 -263 grass_block",
        "fill 104 46 -271 106 46 -267 rooted_dirt",
        "fill 108 46 -274 112 46 -271 podzol",
        # Winding garden path connecting North Breezeway through tree to East Portal and Pavilion
        "fill 104 46 -275 106 46 -273 packed_mud",
        "setblock 104 46 -275 mud_brick_slab[type=bottom]",
        "setblock 105 46 -274 polished_tuff_slab[type=bottom]",
        "setblock 106 46 -273 mossy_stone_brick_slab[type=bottom]",
        "setblock 106 46 -272 mud_brick_slab[type=bottom]",
        "setblock 107 46 -271 polished_tuff_slab[type=bottom]",
        "setblock 108 46 -270 packed_mud",
        "setblock 109 46 -269 mud_brick_slab[type=bottom]",
        "setblock 110 46 -269 polished_tuff_slab[type=bottom]",
        "setblock 111 46 -269 packed_mud",
        "setblock 112 46 -269 mud_brick_slab[type=bottom]",
        "setblock 113 46 -269 polished_tuff_slab[type=bottom]",
        "setblock 107 46 -269 packed_mud",
        "setblock 107 46 -268 mud_brick_slab[type=bottom]",
        "setblock 108 46 -267 polished_tuff_slab[type=bottom]",
        "setblock 109 46 -266 packed_mud",
        "setblock 110 46 -265 mud_brick_slab[type=bottom]",
        # 4. Strict ceiling cap at Y: 53
        "fill 96 53 -276 114 53 -262 deepslate_tiles",
        # 5. Perimeter outer walls
        "fill 96 46 -276 114 52 -276 deepslate_bricks",
        "fill 96 46 -262 114 52 -262 deepslate_bricks",
        "fill 96 46 -276 96 52 -262 deepslate_bricks",
        "fill 114 46 -276 114 52 -262 deepslate_bricks",
        # Textural variation: mossy stone bricks and tuff bricks
        "fill 96 47 -274 96 50 -268 mossy_stone_bricks",
        "fill 114 47 -275 114 50 -272 mossy_stone_bricks",
        "fill 114 47 -266 114 50 -264 mossy_stone_bricks",
        "fill 98 47 -262 103 50 -262 tuff_bricks",
        "fill 107 47 -262 112 50 -262 tuff_bricks",
        "fill 98 47 -276 102 50 -276 tuff_bricks",
        "fill 108 47 -276 112 50 -276 tuff_bricks",
    ]
    return cmds

def build_pilasters_and_archways():
    """Constructs decorative pilasters and the East and North access portals."""
    cmds = [
        "# Pilasters and Structural Doorways",
    ]
    # West wall pilasters at X: 97
    for z in [-274, -271, -267, -264]:
        cmds.extend([
            f"fill 97 46 {z} 97 48 {z} mud_bricks",
            f"setblock 97 49 {z} chiseled_tuff",
            f"setblock 97 50 {z} polished_tuff_stairs[facing=east,half=top]",
        ])
    # East wall pilasters at X: 113 (skipping doorway at -270..-268)
    for z in [-274, -264]:
        cmds.extend([
            f"fill 113 46 {z} 113 48 {z} mud_bricks",
            f"setblock 113 49 {z} chiseled_tuff",
            f"setblock 113 50 {z} polished_tuff_stairs[facing=west,half=top]",
        ])
    # North wall pilasters at Z: -275 (skipping breezeway at 104..106)
    for x in [99, 102, 108, 111]:
        cmds.extend([
            f"fill {x} 46 -275 {x} 48 -275 mud_bricks",
            f"setblock {x} 49 -275 chiseled_tuff",
            f"setblock {x} 50 -275 polished_tuff_stairs[facing=south,half=top]",
        ])
    # South wall pilasters at Z: -263
    for x in [99, 102, 105, 108, 111]:
        cmds.extend([
            f"fill {x} 46 -263 {x} 48 -263 mud_bricks",
            f"setblock {x} 49 -263 chiseled_tuff",
            f"setblock {x} 50 -263 polished_tuff_stairs[facing=north,half=top]",
        ])

    # East Portal into South Boulevard (X: 114..115, Z: -270..-268, Y: 46..50)
    cmds.extend([
        "# East Portal into South Boulevard (X: 114..115, Z: -270..-268)",
        "fill 114 46 -270 115 48 -268 air",
        "fill 114 46 -270 115 46 -268 polished_deepslate",
        "fill 114 46 -271 114 48 -271 polished_tuff",
        "fill 114 46 -267 114 48 -267 polished_tuff",
        "setblock 114 49 -270 polished_tuff_stairs[facing=south,half=top]",
        "setblock 114 49 -268 polished_tuff_stairs[facing=north,half=top]",
        "setblock 114 49 -269 polished_tuff_slab[type=top]",
        "setblock 113 48 -270 green_wall_banner[facing=west]",
        "setblock 113 48 -269 green_wall_banner[facing=west]",
        "setblock 113 48 -268 green_wall_banner[facing=west]",
        "setblock 116 48 -270 green_wall_banner[facing=east]",
        "setblock 116 48 -269 green_wall_banner[facing=east]",
        "setblock 116 48 -268 green_wall_banner[facing=east]",
        "setblock 114 50 -269 copper_bulb[lit=true,powered=false]",
    ])

    # North Breezeway into Sector 5 Farm (Z: -276..-277, X: 104..106, Y: 46..50)
    cmds.extend([
        "# North Breezeway into Sector 5 Farm (Z: -276..-277, X: 104..106)",
        "fill 104 46 -277 106 48 -276 air",
        "fill 104 46 -277 106 46 -276 moss_block",
        "fill 103 46 -276 103 48 -276 mud_bricks",
        "fill 107 46 -276 107 48 -276 mud_bricks",
        "setblock 104 49 -276 polished_tuff_stairs[facing=east,half=top]",
        "setblock 106 49 -276 polished_tuff_stairs[facing=west,half=top]",
        "setblock 105 49 -276 polished_tuff_slab[type=top]",
        "setblock 105 50 -276 copper_bulb[lit=true,powered=false]",
        "setblock 105 48 -276 spore_blossom",
    ])
    return cmds

def build_coffered_vault_ceilings():
    """Constructs coffered barrel vaults curving from Y: 49 up to keystone apex at Y: 53."""
    cmds = [
        "# Coffered Barrel Vaults with Lit Copper Bulbs and Hanging Soul Lanterns",
    ]
    rib_z_coords = [-276, -273, -269, -265, -262]
    for z in rib_z_coords:
        cmds.append(f"# Transverse Vault Rib at Z = {z}")
        # Springing stairs at Y: 50..52
        cmds.append(f"setblock 98 50 {z} tuff_brick_stairs[facing=east,half=top]")
        cmds.append(f"setblock 99 51 {z} tuff_brick_stairs[facing=east,half=top]")
        cmds.append(f"setblock 100 51 {z} tuff_brick_stairs[facing=east,half=top]")
        cmds.append(f"setblock 101 52 {z} tuff_brick_stairs[facing=east,half=top]")
        cmds.append(f"setblock 102 52 {z} tuff_brick_stairs[facing=east,half=top]")
        cmds.append(f"setblock 112 50 {z} tuff_brick_stairs[facing=west,half=top]")
        cmds.append(f"setblock 111 51 {z} tuff_brick_stairs[facing=west,half=top]")
        cmds.append(f"setblock 110 51 {z} tuff_brick_stairs[facing=west,half=top]")
        cmds.append(f"setblock 109 52 {z} tuff_brick_stairs[facing=west,half=top]")
        cmds.append(f"setblock 108 52 {z} tuff_brick_stairs[facing=west,half=top]")
        # Transverse apex beam at Y: 53
        cmds.append(f"fill 103 53 {z} 107 53 {z} polished_tuff")
        # Keystone bulb, chain, and soul lantern
        cmds.append(f"setblock 105 53 {z} copper_bulb[lit=true,powered=false]")
        cmds.append(f"setblock 105 52 {z} iron_chain[axis=y]")
        cmds.append(f"setblock 105 51 {z} soul_lantern[hanging=true]")

    # Coffered Bays between ribs
    bays = [
        (-275, -274, -274),
        (-272, -270, -271),
        (-268, -266, -267),
        (-264, -263, -263),
    ]
    for z1, z2, z_mid in bays:
        cmds.append(f"# Coffered Bay: Z = {z1}..{z2}")
        # Recessed center panels at Y: 53
        cmds.append(f"fill 104 53 {z1} 106 53 {z2} waxed_copper_grate")
        cmds.append(f"fill 102 53 {z1} 103 53 {z2} mossy_stone_bricks")
        cmds.append(f"fill 107 53 {z1} 108 53 {z2} mossy_stone_bricks")
        for z in range(z1, z2 + 1):
            cmds.append(f"setblock 98 50 {z} tuff_brick_stairs[facing=east,half=top]")
            cmds.append(f"setblock 99 51 {z} tuff_brick_stairs[facing=east,half=top]")
            cmds.append(f"setblock 101 52 {z} tuff_brick_stairs[facing=east,half=top]")
            cmds.append(f"setblock 112 50 {z} tuff_brick_stairs[facing=west,half=top]")
            cmds.append(f"setblock 111 51 {z} tuff_brick_stairs[facing=west,half=top]")
            cmds.append(f"setblock 109 52 {z} tuff_brick_stairs[facing=west,half=top]")
        # Secondary bay bulbs
        cmds.append(f"setblock 100 52 {z_mid} copper_bulb[lit=true,powered=false]")
        cmds.append(f"setblock 110 52 {z_mid} copper_bulb[lit=true,powered=false]")

    return cmds

def build_central_ancient_canopy_tree():
    """Constructs the central twisted ancient canopy tree with azalea foliage and hidden shroomlights."""
    cmds = [
        "# Central Ancient Canopy Tree (X: 104..106, Z: -269..-268, Y: 46..52)",
        # Root buttresses anchoring into rooted dirt
        "setblock 104 46 -269 mangrove_roots",
        "setblock 106 46 -268 mangrove_roots",
        "setblock 105 46 -270 mangrove_roots",
        "setblock 105 46 -267 mangrove_roots",
        "setblock 103 46 -269 rooted_dirt",
        "setblock 107 46 -268 rooted_dirt",
        # Twisted trunk core
        "setblock 105 46 -269 stripped_mangrove_wood",
        "setblock 105 46 -268 stripped_dark_oak_wood",
        "setblock 104 47 -269 mangrove_roots",
        "setblock 105 47 -269 stripped_mangrove_wood",
        "setblock 105 47 -268 stripped_dark_oak_wood",
        "setblock 106 47 -268 mangrove_roots",
        "setblock 105 48 -269 stripped_mangrove_wood",
        "setblock 105 48 -268 stripped_dark_oak_wood",
        "setblock 104 48 -268 stripped_mangrove_wood",
        "setblock 106 48 -269 stripped_dark_oak_wood",
        "setblock 105 49 -269 stripped_mangrove_wood",
        "setblock 105 49 -268 stripped_dark_oak_wood",
        # Branch forks at Y: 49
        "setblock 104 49 -269 flowering_azalea_leaves",
        "setblock 106 49 -268 flowering_azalea_leaves",
        "setblock 105 49 -270 flowering_azalea_leaves",
        "setblock 105 49 -267 flowering_azalea_leaves",
        # Cloud Canopy at Y: 50
        "fill 103 50 -270 107 50 -267 flowering_azalea_leaves",
        "fill 102 50 -269 108 50 -268 azalea_leaves",
        # Hidden shroomlights embedded in canopy
        "setblock 104 50 -269 shroomlight",
        "setblock 106 50 -268 shroomlight",
        # Cloud Canopy at Y: 51
        "fill 103 51 -270 107 51 -267 flowering_azalea_leaves",
        "setblock 105 51 -269 shroomlight",
        "fill 104 51 -271 106 51 -266 azalea_leaves",
        # Cloud Canopy at Y: 52
        "fill 104 52 -269 106 52 -268 flowering_azalea_leaves",
        "setblock 103 52 -268 azalea_leaves",
        "setblock 107 52 -269 azalea_leaves",
        # Hanging flora beneath canopy
        "setblock 105 48 -269 spore_blossom",
        "setblock 103 48 -268 spore_blossom",
        "setblock 107 48 -269 spore_blossom",
    ]
    return cmds

def build_subterranean_koi_pond():
    """Constructs the winding subterranean koi pond stream with clay, gravel, sea pickles, and dripleaves."""
    cmds = [
        "# Subterranean Koi Pond Stream (X: 98..102, Z: -273..-266, Y: 45..46)",
        # Stream bed foundation at Y: 45
        "fill 98 45 -273 102 45 -266 gravel",
        "fill 99 45 -272 101 45 -267 clay",
        # Clay foundation directly beneath dripleaf anchors
        "setblock 98 45 -273 clay",
        "setblock 102 45 -266 clay",
        # Excavate stream channel at Y: 46
        "fill 99 46 -272 101 46 -267 water",
        "setblock 102 46 -266 clay",
        # Underwater lighting with waterlogged sea pickles
        "setblock 99 46 -271 sea_pickle[waterlogged=true,pickles=4]",
        "setblock 100 46 -269 sea_pickle[waterlogged=true,pickles=3]",
        "setblock 101 46 -267 sea_pickle[waterlogged=true,pickles=4]",
        # Surface water plants
        "setblock 100 47 -272 lily_pad",
        "setblock 99 47 -268 lily_pad",
        "setblock 98 46 -273 big_dripleaf[facing=north]",
        "setblock 102 46 -266 big_dripleaf[facing=east]",
        "setblock 101 46 -270 small_dripleaf[facing=south,half=lower]",
        "setblock 101 47 -270 small_dripleaf[facing=south,half=upper]",
    ]
    return cmds

def build_exotic_flora_and_pavilion():
    """Constructs sniffer crop beds, ceiling flora, and botanical research pavilion."""
    cmds = [
        "# Exotic Flora Beds and Research Pavilion",
        # Sniffer crops: Pitcher Plants (2-block tall plants)
        "setblock 110 46 -273 pitcher_plant[half=lower]",
        "setblock 110 47 -273 pitcher_plant[half=upper]",
        "setblock 111 46 -265 pitcher_plant[half=lower]",
        "setblock 111 47 -265 pitcher_plant[half=upper]",
        # Torchflowers
        "setblock 109 46 -274 torchflower",
        "setblock 111 46 -273 torchflower",
        "setblock 108 46 -265 torchflower",
        # Flowering azalea bushes
        "setblock 108 46 -273 flowering_azalea",
        "setblock 112 46 -264 flowering_azalea",
        "setblock 98 46 -264 flowering_azalea",
        # Pink petals clusters
        "setblock 107 46 -272 pink_petals[flower_amount=4]",
        "setblock 109 46 -266 pink_petals[flower_amount=3]",
        "setblock 102 46 -264 pink_petals[flower_amount=4]",
        # Spore blossoms hanging from ceiling
        "setblock 100 52 -270 spore_blossom",
        "setblock 110 52 -268 spore_blossom",
        "setblock 105 52 -264 spore_blossom",
        # Hanging cave vines with berries
        "setblock 101 52 -274 cave_vines[berries=true,age=24]",
        "setblock 102 52 -267 cave_vines[berries=true,age=24]",
        "setblock 108 52 -271 cave_vines[berries=true,age=24]",
        "setblock 111 52 -266 cave_vines[berries=true,age=24]",
        # Hanging roots
        "setblock 99 52 -268 hanging_roots",
        "setblock 107 52 -274 hanging_roots",
        "setblock 109 52 -263 hanging_roots",
        # Botanical Research Pavilion at South-East
        "setblock 110 46 -263 polished_tuff_stairs[facing=south,half=bottom]",
        "setblock 111 46 -263 polished_tuff_slab[type=bottom]",
        "setblock 112 46 -263 polished_tuff_stairs[facing=south,half=bottom]",
        "setblock 110 46 -264 lectern[facing=west]",
        "setblock 112 46 -264 decorated_pot",
        "setblock 112 47 -264 potted_fern",
        "setblock 109 46 -263 decorated_pot",
        "setblock 109 47 -263 potted_fern",
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
    """Verifies that all critical Sector 17 structures, canopy tree, pond, and flora exist live."""
    test_blocks = [
        # Subfloor and Perimeter Boundaries
        ("105 45 -269", "moss_block", "Shell Subfloor Foundation at Y: 45"),
        ("96 48 -270", "mossy_stone_bricks", "West Perimeter Wall Mossy Bricks at Y: 48"),
        ("96 48 -264", "deepslate_bricks", "West Perimeter Wall Deepslate Bricks at Y: 48"),
        ("114 48 -265", "mossy_stone_bricks", "East Perimeter Wall Mossy Bricks at Y: 48"),
        ("114 48 -276", "deepslate_bricks", "East Perimeter Wall Deepslate Bricks at Y: 48"),
        ("100 48 -276", "tuff_bricks", "North Perimeter Wall Tuff Bricks at Y: 48"),
        ("97 48 -276", "deepslate_bricks", "North Perimeter Wall Deepslate Bricks at Y: 48"),
        ("105 48 -262", "deepslate_bricks", "South Perimeter Outer Wall at Y: 48"),
        ("100 48 -262", "tuff_bricks", "South Perimeter Wall Tuff Bricks at Y: 48"),
        ("105 53 -269", "copper_bulb[lit=true,powered=false]", "Ceiling Vault Cap at Y: 53"),
        # Pilasters along Walls
        ("97 47 -271", "mud_bricks", "West Wall Pilaster Mud Bricks at Y: 47"),
        ("97 49 -271", "chiseled_tuff", "West Wall Pilaster Chiseled Tuff at Y: 49"),
        ("102 47 -275", "mud_bricks", "North Wall Pilaster Mud Bricks at Y: 47"),
        ("102 49 -275", "chiseled_tuff", "North Wall Pilaster Chiseled Tuff at Y: 49"),
        ("108 47 -263", "mud_bricks", "South Wall Pilaster Mud Bricks at Y: 47"),
        ("108 49 -263", "chiseled_tuff", "South Wall Pilaster Chiseled Tuff at Y: 49"),
        ("113 47 -264", "mud_bricks", "East Wall Pilaster Mud Bricks at Y: 47"),
        ("113 49 -264", "chiseled_tuff", "East Wall Pilaster Chiseled Tuff at Y: 49"),
        # East Portal into South Boulevard
        ("114 47 -269", "air", "East Portal Opening at Y: 47"),
        ("114 47 -271", "polished_tuff", "East Portal Jamb at Y: 47"),
        ("114 49 -270", "polished_tuff_stairs[facing=south,half=top]", "East Portal Corbel Stairs at Y: 49"),
        ("113 48 -269", "green_wall_banner[facing=west]", "East Portal Green Banner Valance at Y: 48"),
        ("114 50 -269", "copper_bulb[lit=true,powered=false]", "East Portal Keystone Copper Bulb at Y: 50"),
        # North Breezeway into Sector 5 Farm
        ("105 47 -276", "air", "North Breezeway Opening at Y: 47"),
        ("103 47 -276", "mud_bricks", "North Breezeway Jamb Mud Bricks at Y: 47"),
        ("104 49 -276", "polished_tuff_stairs[facing=east,half=top]", "North Breezeway Corbel Stairs at Y: 49"),
        ("105 50 -276", "copper_bulb[lit=true,powered=false]", "North Breezeway Keystone Copper Bulb at Y: 50"),
        ("105 48 -276", "spore_blossom", "North Breezeway Hanging Spore Blossom at Y: 48"),
        # Central Ancient Canopy Tree
        ("104 46 -269", "mangrove_roots", "Ancient Tree Root Buttress West at Y: 46"),
        ("106 46 -268", "mangrove_roots", "Ancient Tree Root Buttress East at Y: 46"),
        ("105 47 -269", "stripped_mangrove_wood", "Ancient Tree Trunk Wood at Y: 47"),
        ("105 48 -268", "stripped_dark_oak_wood", "Ancient Tree Trunk Wood at Y: 48"),
        ("105 50 -270", "flowering_azalea_leaves", "Ancient Tree Canopy Foliage at Y: 50"),
        ("103 51 -270", "flowering_azalea_leaves", "Ancient Tree Canopy Flowering Foliage at Y: 51"),
        ("104 51 -268", "azalea_leaves", "Ancient Tree Canopy Azalea Foliage at Y: 51"),
        ("104 50 -269", "shroomlight", "Ancient Tree Hidden Shroomlight at Y: 50"),
        ("105 48 -269", "spore_blossom", "Ancient Tree Hanging Spore Blossom at Y: 48"),
        # Subterranean Koi Pond
        ("100 45 -270", "clay", "Koi Pond Bed Clay at Y: 45"),
        ("100 46 -270", "water", "Koi Pond Water at Y: 46"),
        ("99 46 -271", "sea_pickle[waterlogged=true,pickles=4]", "Koi Pond Waterlogged Sea Pickles at Y: 46"),
        ("100 47 -272", "lily_pad", "Koi Pond Surface Lily Pad at Y: 47"),
        ("98 46 -273", "big_dripleaf[facing=north]", "Koi Pond Big Dripleaf at Y: 46"),
        ("101 46 -270", "small_dripleaf[facing=south,half=lower]", "Koi Pond Small Dripleaf Lower at Y: 46"),
        ("101 47 -270", "small_dripleaf[facing=south,half=upper]", "Koi Pond Small Dripleaf Upper at Y: 47"),
        # Exotic Flora Beds
        ("110 46 -273", "pitcher_plant[half=lower]", "Exotic Flora Pitcher Plant Lower Half at Y: 46"),
        ("110 47 -273", "pitcher_plant[half=upper]", "Exotic Flora Pitcher Plant Upper Half at Y: 47"),
        ("111 46 -265", "pitcher_plant[half=lower]", "Exotic Flora Second Pitcher Plant Lower at Y: 46"),
        ("111 47 -265", "pitcher_plant[half=upper]", "Exotic Flora Second Pitcher Plant Upper at Y: 47"),
        ("109 46 -274", "torchflower", "Exotic Flora Torchflower at Y: 46"),
        ("108 46 -265", "torchflower", "Exotic Flora Second Torchflower at Y: 46"),
        ("108 46 -273", "flowering_azalea", "Exotic Flora Flowering Azalea Bush at Y: 46"),
        ("107 46 -272", "pink_petals[flower_amount=4]", "Exotic Flora Pink Petals Cluster at Y: 46"),
        ("109 46 -266", "pink_petals[flower_amount=3]", "Exotic Flora Second Pink Petals at Y: 46"),
        # Ceiling Flora
        ("110 52 -268", "spore_blossom", "Ceiling Hanging Spore Blossom at Y: 52"),
        ("101 52 -274", "cave_vines[berries=true,age=24]", "Ceiling Hanging Cave Vines with Berries at Y: 52"),
        ("108 52 -271", "cave_vines[berries=true,age=24]", "Ceiling Second Hanging Cave Vines at Y: 52"),
        ("99 52 -268", "hanging_roots", "Ceiling Hanging Roots at Y: 52"),
        # Botanical Research Pavilion
        ("110 46 -264", "lectern[facing=west]", "Pavilion Botanical Research Lectern at Y: 46"),
        ("111 46 -263", "polished_tuff_slab[type=bottom]", "Pavilion Polished Tuff Bench at Y: 46"),
        ("112 46 -264", "decorated_pot", "Pavilion Ornamental Decorated Pot at Y: 46"),
        ("112 47 -264", "potted_fern", "Pavilion Potted Fern on Decorated Pot at Y: 47"),
        ("109 46 -263", "decorated_pot", "Pavilion Ornamental Decorated Pot West at Y: 46"),
        ("109 47 -263", "potted_fern", "Pavilion Potted Fern on Decorated Pot West at Y: 47"),
        # Vault Ribs and Coffered Ceilings
        ("105 53 -273", "copper_bulb[lit=true,powered=false]", "Vault Rib Z-273 Keystone Bulb at Y: 53"),
        ("105 52 -273", "iron_chain[axis=y]", "Vault Rib Z-273 Hanging Iron Chain at Y: 52"),
        ("105 51 -273", "soul_lantern[hanging=true]", "Vault Rib Z-273 Hanging Soul Lantern at Y: 51"),
        ("105 53 -265", "copper_bulb[lit=true,powered=false]", "Vault Rib Z-265 Keystone Bulb at Y: 53"),
        ("105 53 -271", "waxed_copper_grate", "Coffered Bay Recessed Grate Panel at Y: 53"),
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
    print("Beginning Sector 17 Subterranean Arboretum construction...")
    all_cmds = []
    all_cmds.extend(build_arboretum_shell())
    all_cmds.extend(build_pilasters_and_archways())
    all_cmds.extend(build_coffered_vault_ceilings())
    all_cmds.extend(build_central_ancient_canopy_tree())
    all_cmds.extend(build_subterranean_koi_pond())
    all_cmds.extend(build_exotic_flora_and_pavilion())

    # Write local mcfunction file
    write_mcfunction("bunker_arboretum.mcfunction", all_cmds)

    # Sync file to remote server datapack
    sync_remote_mcfunction("bunker_arboretum.mcfunction")

    # Execute all commands over RCON socket protocol
    print("\nExecuting Sector 17 construction commands via RCON...")
    execute_remote_batch(all_cmds)

    # Verify live blockstates
    success = verify_live_blockstates()
    if success:
        print("\nAll Sector 17 Subterranean Arboretum structures, flora, and aquatic features verified successfully!")
    else:
        print("\nVerification encountered issues. Inspect above logs.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
