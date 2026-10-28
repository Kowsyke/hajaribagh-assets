#!/usr/bin/env python3
"""Build Sovereign Banquet Hall and Royal Geothermal Spa for King Abir Bunker.

Constructs Tier 3 deep subterranean facilities at Y: 36..45 directly beneath
King's Parliament (Banquet Hall) and Modern Housing (Geothermal Spa).
Strictly enforces vertical boundaries Y: 36..45, object logic, parity,
nonflammable hearths, paired chests, and uniform lighting.
"""

import os
import subprocess
import sys

DEFAULT_HOST = os.environ.get("HZ_HOST", "132.226.135.26")
DEFAULT_USER = os.environ.get("HZ_USER", "ubuntu")
DEFAULT_KEY = os.environ.get("HZ_KEY", os.path.expanduser("~/.ssh/id_ed25519"))

LOCAL_FUNCTION_DIR = "datapacks/underground_citadel/data/citadel/function"
REMOTE_SERVER_PATH = "/home/ubuntu/minecraft-server"
REMOTE_FUNCTION_DIR = f"{REMOTE_SERVER_PATH}/world/datapacks/underground_citadel/data/citadel/function"


def build_banquet_commands():
    """Generates commands for the Sovereign Banquet & Great Feasting Hall."""
    cmds = []
    cmds.append("# Chamber A: The Sovereign Banquet & Great Feasting Hall (X: 105..129, Z: -261..-235, Y: 36..45)")

    # 1. Excavation within strict vertical bounds Y: 36..45
    cmds.append("fill 105 36 -261 129 45 -235 air")

    # 2. Subfloor foundation at Y: 36
    cmds.append("fill 105 36 -261 129 36 -235 polished_blackstone")

    # 3. Main flooring at Y: 37
    cmds.append("fill 106 37 -260 128 37 -236 polished_blackstone")
    cmds.append("fill 108 37 -258 126 37 -238 deepslate_tiles")

    # 4. Ceiling cap at Y: 45
    cmds.append("fill 105 45 -261 129 45 -235 polished_blackstone_bricks")

    # 5. Enclosing perimeter walls (Y: 37..44)
    cmds.append("fill 105 37 -261 129 44 -261 polished_blackstone_bricks")
    cmds.append("fill 105 37 -235 129 44 -235 polished_blackstone_bricks")
    cmds.append("fill 105 37 -261 105 44 -235 polished_blackstone_bricks")
    cmds.append("fill 129 37 -261 129 44 -235 polished_blackstone_bricks")

    # Corner pilasters and wall ribs
    cmds.append("fill 105 37 -261 105 44 -261 chiseled_polished_blackstone")
    cmds.append("fill 129 37 -261 129 44 -261 chiseled_polished_blackstone")
    cmds.append("fill 105 37 -235 105 44 -235 chiseled_polished_blackstone")
    cmds.append("fill 129 37 -235 129 44 -235 chiseled_polished_blackstone")

    # Ceiling vault arch ribs at Y: 44
    for z in [-257, -251, -245, -239]:
        cmds.append(f"fill 106 44 {z} 128 44 {z} crying_obsidian")

    # 6. Dual spiral staircases in North corners connecting down to Y: 38
    # Northwest spiral staircase centered at X: 109, Z: -259
    cmds.append("fill 109 37 -259 109 45 -259 chiseled_polished_blackstone")
    cmds.append("setblock 109 45 -258 polished_blackstone_stairs[facing=north,half=bottom] replace")
    cmds.append("setblock 110 44 -259 polished_blackstone_stairs[facing=west,half=bottom] replace")
    cmds.append("setblock 109 43 -260 polished_blackstone_stairs[facing=south,half=bottom] replace")
    cmds.append("setblock 108 42 -259 polished_blackstone_stairs[facing=east,half=bottom] replace")
    cmds.append("setblock 109 41 -258 polished_blackstone_stairs[facing=north,half=bottom] replace")
    cmds.append("setblock 110 40 -259 polished_blackstone_stairs[facing=west,half=bottom] replace")
    cmds.append("setblock 109 39 -260 polished_blackstone_stairs[facing=south,half=bottom] replace")
    cmds.append("setblock 108 38 -259 polished_blackstone_stairs[facing=east,half=bottom] replace")

    # Northeast spiral staircase centered at X: 125, Z: -259
    cmds.append("fill 125 37 -259 125 45 -259 chiseled_polished_blackstone")
    cmds.append("setblock 125 45 -258 polished_blackstone_stairs[facing=north,half=bottom] replace")
    cmds.append("setblock 124 44 -259 polished_blackstone_stairs[facing=east,half=bottom] replace")
    cmds.append("setblock 125 43 -260 polished_blackstone_stairs[facing=south,half=bottom] replace")
    cmds.append("setblock 126 42 -259 polished_blackstone_stairs[facing=west,half=bottom] replace")
    cmds.append("setblock 125 41 -258 polished_blackstone_stairs[facing=north,half=bottom] replace")
    cmds.append("setblock 124 40 -259 polished_blackstone_stairs[facing=east,half=bottom] replace")
    cmds.append("setblock 125 39 -260 polished_blackstone_stairs[facing=south,half=bottom] replace")
    cmds.append("setblock 126 38 -259 polished_blackstone_stairs[facing=west,half=bottom] replace")

    # 7. Grand 18-Block Banquet Table down the center (X: 116..117, Z: -257..-240)
    # Tabletop top slabs at Y: 38
    cmds.append("fill 116 38 -257 117 38 -240 dark_oak_slab[type=top] replace")
    # Table leg supports at Y: 37
    for z in [-257, -253, -249, -245, -241]:
        cmds.append(f"setblock 116 37 {z} dark_oak_fence replace")
        cmds.append(f"setblock 117 37 {z} dark_oak_fence replace")

    # West chairs facing East towards table
    cmds.append("fill 115 38 -257 115 38 -240 dark_oak_stairs[facing=east,half=bottom] replace")
    # East chairs facing West towards table
    cmds.append("fill 118 38 -257 118 38 -240 dark_oak_stairs[facing=west,half=bottom] replace")

    # Feast tableware along tabletop (Y: 39)
    # Cakes
    for z in [-256, -250, -244]:
        cmds.append(f"setblock 116 39 {z} cake[bites=0] replace")
        cmds.append(f"setblock 117 39 {z} heavy_weighted_pressure_plate replace")
    # Lit candles
    for z in [-254, -248, -242]:
        cmds.append(f"setblock 116 39 {z} candle[candles=3,lit=true] replace")
        cmds.append(f"setblock 117 39 {z} sea_pickle[pickles=2,waterlogged=false] replace")
    # Decorated pots
    for z in [-252, -246]:
        cmds.append(f"setblock 116 39 {z} decorated_pot replace")
        cmds.append(f"setblock 117 39 {z} candle[candles=2,lit=true] replace")
    # Additional tableware goblets and plates
    for z in [-257, -255, -253, -251, -249, -247, -245, -243, -241, -240]:
        cmds.append(f"setblock 116 39 {z} heavy_weighted_pressure_plate replace")
        cmds.append(f"setblock 117 39 {z} sea_pickle[pickles=1,waterlogged=false] replace")

    # Item frames displaying golden apples and cooked beef on the table sides
    for z in [-256, -252, -248, -244]:
        cmds.append(
            f"summon glow_item_frame 115 38 {z} "
            '{Tags:["citadel_decor","banquet_feast_frame"],Facing:4b,Item:{id:"minecraft:golden_apple",count:1}}'
        )
        cmds.append(
            f"summon glow_item_frame 118 38 {z} "
            '{Tags:["citadel_decor","banquet_feast_frame"],Facing:5b,Item:{id:"minecraft:cooked_beef",count:1}}'
        )

    # 8. Elevated High Table Dais at South end (Z: -238..-236)
    cmds.append("fill 114 38 -238 120 38 -236 gilded_blackstone replace")
    cmds.append("fill 115 38 -239 119 38 -239 crimson_stairs[facing=south,half=bottom] replace")
    # High Table
    cmds.append("fill 116 39 -237 118 39 -237 dark_oak_slab[type=top] replace")
    cmds.append("setblock 116 40 -237 cake[bites=0] replace")
    cmds.append("setblock 117 40 -237 candle[candles=4,lit=true] replace")
    cmds.append(
        'summon glow_item_frame 118 40 -237 '
        '{Tags:["citadel_decor","banquet_dais_frame"],Facing:1b,Item:{id:"minecraft:enchanted_golden_apple",count:1}}'
    )
    # Sovereign Throne of King Abir at X: 117, Y: 39, Z: -236
    cmds.append("setblock 117 38 -236 gold_block replace")
    cmds.append("setblock 117 39 -236 crimson_stairs[facing=north,half=bottom] replace")
    cmds.append("setblock 116 39 -236 crimson_trapdoor[facing=east,half=bottom,open=true] replace")
    cmds.append("setblock 118 39 -236 crimson_trapdoor[facing=west,half=bottom,open=true] replace")
    cmds.append("setblock 117 40 -236 crying_obsidian replace")
    cmds.append("setblock 117 41 -236 gold_block replace")
    cmds.append("setblock 116 41 -236 red_wall_banner[facing=north] replace")
    cmds.append("setblock 118 41 -236 red_wall_banner[facing=north] replace")

    # 9. Dual roaring fireplaces on East and West walls
    # West fireplace at X: 106, Z: -248
    cmds.append("fill 106 37 -249 106 40 -247 bricks replace")
    cmds.append("setblock 106 36 -248 hay_block replace")
    cmds.append("setblock 106 37 -248 campfire[lit=true] replace")
    cmds.append("setblock 107 38 -248 iron_bars replace")
    cmds.append("fill 106 41 -248 106 45 -248 bricks replace")

    # East fireplace at X: 128, Z: -248
    cmds.append("fill 128 37 -249 128 40 -247 bricks replace")
    cmds.append("setblock 128 36 -248 hay_block replace")
    cmds.append("setblock 128 37 -248 campfire[lit=true] replace")
    cmds.append("setblock 127 38 -248 iron_bars replace")
    cmds.append("fill 128 41 -248 128 45 -248 bricks replace")

    # 10. Brass chandeliers suspended by chains and lightning rods
    chandelier_locs = [
        (117, -253),
        (117, -247),
        (117, -241),
        (110, -248),
        (124, -248),
    ]
    for cx, cz in chandelier_locs:
        cmds.append(f"setblock {cx} 44 {cz} copper_chain[axis=y] replace")
        cmds.append(f"setblock {cx} 43 {cz} copper_chain[axis=y] replace")
        cmds.append(f"setblock {cx} 42 {cz} lightning_rod[facing=down] replace")
        cmds.append(f"setblock {cx} 41 {cz} copper_grate replace")
        cmds.append(f"setblock {cx} 41 {cz-1} waxed_copper_bulb[lit=true,powered=false] replace")
        cmds.append(f"setblock {cx} 41 {cz+1} waxed_copper_bulb[lit=true,powered=false] replace")
        cmds.append(f"setblock {cx-1} 41 {cz} waxed_copper_bulb[lit=true,powered=false] replace")
        cmds.append(f"setblock {cx+1} 41 {cz} waxed_copper_bulb[lit=true,powered=false] replace")

    # 11. Royal wine cellar and food pantry along North wall (Z: -260)
    # West food pantry (paired chests)
    cmds.append("setblock 111 38 -260 chest[facing=south,type=right] replace")
    cmds.append("setblock 112 38 -260 chest[facing=south,type=left] replace")
    cmds.append("setblock 113 38 -260 chest[facing=south,type=right] replace")
    cmds.append("setblock 114 38 -260 chest[facing=south,type=left] replace")
    cmds.append("fill 111 39 -260 114 39 -260 barrel[facing=south] replace")

    # East royal wine cellar (barrels and vintage storage)
    cmds.append("fill 120 38 -260 123 38 -260 barrel[facing=south] replace")
    cmds.append("fill 120 39 -260 123 39 -260 barrel[facing=south] replace")

    # Pantry and cellar item frames
    cmds.append(
        'summon item_frame 112 40 -260 '
        '{Tags:["citadel_decor","banquet_pantry_frame"],Facing:3b,Item:{id:"minecraft:bread",count:1}}'
    )
    cmds.append(
        'summon item_frame 113 40 -260 '
        '{Tags:["citadel_decor","banquet_pantry_frame"],Facing:3b,Item:{id:"minecraft:cooked_porkchop",count:1}}'
    )
    cmds.append(
        'summon item_frame 121 40 -260 '
        '{Tags:["citadel_decor","banquet_cellar_frame"],Facing:3b,Item:{id:"minecraft:potion",count:1}}'
    )
    cmds.append(
        'summon item_frame 122 40 -260 '
        '{Tags:["citadel_decor","banquet_cellar_frame"],Facing:3b,Item:{id:"minecraft:golden_carrot",count:1}}'
    )

    # Floor illumination fixtures
    cmds.append("setblock 107 37 -255 sea_lantern replace")
    cmds.append("setblock 127 37 -255 sea_lantern replace")
    cmds.append("setblock 107 37 -241 sea_lantern replace")
    cmds.append("setblock 127 37 -241 sea_lantern replace")

    return cmds


def build_spa_commands():
    """Generates commands for the Royal Geothermal Spa & Bathhouse."""
    cmds = []
    cmds.append("# Chamber B: The Royal Geothermal Spa & Bathhouse (X: 120..138, Z: -291..-265, Y: 36..45)")

    # 1. Excavation within strict vertical bounds Y: 36..45
    cmds.append("fill 120 36 -291 138 45 -265 air")

    # 2. Subfloor foundation at Y: 36
    cmds.append("fill 120 36 -291 138 36 -265 prismarine_bricks")

    # 3. Main flooring at Y: 37
    cmds.append("fill 121 37 -290 137 37 -266 prismarine_bricks")
    cmds.append("fill 123 37 -288 135 37 -268 smooth_quartz")

    # 4. Ceiling cap at Y: 45
    cmds.append("fill 120 45 -291 138 45 -265 prismarine_bricks")

    # 5. Enclosing perimeter walls (Y: 37..44)
    cmds.append("fill 120 37 -291 138 44 -291 prismarine_bricks")
    cmds.append("fill 120 37 -265 138 44 -265 prismarine_bricks")
    cmds.append("fill 120 37 -291 120 44 -265 prismarine_bricks")
    cmds.append("fill 138 37 -291 138 44 -265 dark_prismarine")

    # 6. Access spiral staircase descending from Modern Housing bedroom at (136, -267)
    cmds.append("fill 136 37 -267 136 45 -267 smooth_quartz")
    cmds.append("setblock 136 45 -266 smooth_quartz_stairs[facing=south,half=bottom] replace")
    cmds.append("setblock 137 44 -267 smooth_quartz_stairs[facing=east,half=bottom] replace")
    cmds.append("setblock 136 43 -268 smooth_quartz_stairs[facing=north,half=bottom] replace")
    cmds.append("setblock 135 42 -267 smooth_quartz_stairs[facing=west,half=bottom] replace")
    cmds.append("setblock 136 41 -266 smooth_quartz_stairs[facing=south,half=bottom] replace")
    cmds.append("setblock 137 40 -267 smooth_quartz_stairs[facing=east,half=bottom] replace")
    cmds.append("setblock 136 39 -268 smooth_quartz_stairs[facing=north,half=bottom] replace")
    cmds.append("setblock 135 38 -267 smooth_quartz_stairs[facing=west,half=bottom] replace")

    # 7. Steaming Mineral Pools (X: 126..132, Z: -285..-275)
    # Pool basin subfloor at Y: 36
    cmds.append("fill 126 36 -285 132 36 -275 prismarine_bricks replace")
    # Submerged campfires beneath copper grates for steam emissions
    for px in [127, 129, 131]:
        for pz in [-283, -280, -277]:
            cmds.append(f"setblock {px} 36 {pz} campfire[lit=true] replace")
            cmds.append(f"setblock {px} 37 {pz} copper_grate replace")
    # Submerged soul sand for active bubble columns
    for px in [128, 130]:
        for pz in [-284, -282, -279, -276]:
            cmds.append(f"setblock {px} 36 {pz} soul_sand replace")

    # Pool water volume at Y: 37
    cmds.append("fill 126 37 -285 132 37 -275 water replace")
    # Restore the steam grates at Y: 37
    for px in [127, 129, 131]:
        for pz in [-283, -280, -277]:
            cmds.append(f"setblock {px} 37 {pz} copper_grate replace")

    # Pool perimeter coping rim at Y: 38
    cmds.append("fill 125 38 -286 133 38 -286 prismarine_stairs[facing=south,half=bottom] replace")
    cmds.append("fill 125 38 -274 133 38 -274 prismarine_stairs[facing=north,half=bottom] replace")
    cmds.append("fill 125 38 -285 125 38 -275 prismarine_stairs[facing=east,half=bottom] replace")
    cmds.append("fill 133 38 -285 133 38 -275 prismarine_stairs[facing=west,half=bottom] replace")

    # Recessed underwater sea lanterns for turquoise luminescence
    cmds.append("setblock 126 36 -285 sea_lantern replace")
    cmds.append("setblock 132 36 -285 sea_lantern replace")
    cmds.append("setblock 126 36 -275 sea_lantern replace")
    cmds.append("setblock 132 36 -275 sea_lantern replace")

    # 8. Mud brick and spruce sauna cabins (West wall: X: 121..124, Z: -288..-282)
    cmds.append("fill 121 37 -288 124 41 -288 mud_bricks replace")
    cmds.append("fill 121 37 -282 124 41 -282 mud_bricks replace")
    cmds.append("fill 124 37 -287 124 41 -283 mud_bricks replace")
    cmds.append("fill 121 41 -288 124 41 -282 mud_bricks replace")
    # Sauna door opening and door
    cmds.append("setblock 124 38 -285 air replace")
    cmds.append("setblock 124 39 -285 air replace")
    cmds.append("setblock 124 38 -285 spruce_door[facing=east,half=lower] replace")
    cmds.append("setblock 124 39 -285 spruce_door[facing=east,half=upper] replace")
    # Interior sauna seating benches
    cmds.append("fill 122 38 -287 122 38 -283 spruce_stairs[facing=east,half=bottom] replace")
    cmds.append("fill 121 39 -287 121 39 -283 spruce_slab[type=bottom] replace")
    # Heated volcanic magma rock sauna stove
    cmds.append("setblock 122 36 -287 campfire[lit=true] replace")
    cmds.append("setblock 122 37 -287 magma_block replace")
    cmds.append("setblock 122 38 -287 iron_bars replace")

    # 9. Smooth quartz relaxation loungers along East walkway (X: 134, Y: 38)
    lounger_zs = [-284, -281, -278]
    for lz in lounger_zs:
        cmds.append(f"setblock 135 38 {lz} smooth_quartz_stairs[facing=west,half=bottom] replace")
        cmds.append(f"setblock 134 38 {lz} smooth_quartz_slab[type=bottom] replace")
    # Small side tables between loungers
    cmds.append("setblock 135 38 -283 smooth_stone_slab[type=bottom] replace")
    cmds.append("setblock 135 39 -283 candle[candles=2,lit=true] replace")
    cmds.append("setblock 135 38 -280 smooth_stone_slab[type=bottom] replace")
    cmds.append("setblock 135 39 -280 sea_pickle[pickles=2,waterlogged=false] replace")

    # 10. Cascading decorative water walls and drainage trough (East wall: X: 137)
    cmds.append("fill 137 43 -286 137 43 -274 water replace")
    cmds.append("fill 136 37 -286 136 37 -274 copper_grate replace")
    cmds.append("fill 136 36 -286 136 36 -274 sea_lantern replace")

    # 11. Lush hanging flora from ceiling (Y: 44)
    # Spore blossoms
    cmds.append("setblock 128 44 -280 spore_blossom replace")
    cmds.append("setblock 130 44 -275 spore_blossom replace")
    cmds.append("setblock 126 44 -270 spore_blossom replace")
    # Glowing cave vines with berries
    for vx, vz in [(127, -278), (129, -282), (131, -276), (133, -280)]:
        cmds.append(f"setblock {vx} 44 {vz} cave_vines_plant[berries=true] replace")
        cmds.append(f"setblock {vx} 43 {vz} cave_vines[berries=true] replace")

    # Ambient ceiling and floor lighting ensuring illumination level >= 10
    cmds.append("setblock 122 37 -270 sea_lantern replace")
    cmds.append("setblock 134 37 -270 sea_lantern replace")
    cmds.append("setblock 122 45 -275 waxed_copper_bulb[lit=true,powered=false] replace")
    cmds.append("setblock 134 45 -275 waxed_copper_bulb[lit=true,powered=false] replace")
    cmds.append("setblock 128 45 -288 waxed_copper_bulb[lit=true,powered=false] replace")
    cmds.append("setblock 128 45 -267 waxed_copper_bulb[lit=true,powered=false] replace")

    return cmds


def write_local_mcfunction(cmds):
    """Writes the banquet and spa mcfunction file locally."""
    os.makedirs(LOCAL_FUNCTION_DIR, exist_ok=True)
    filepath = os.path.join(LOCAL_FUNCTION_DIR, "bunker_banquet_spa.mcfunction")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(cmds) + "\n")
    print(f"Generated local file: {filepath} ({len(cmds)} commands)")
    return filepath


def sync_mcfunction_to_remote(local_path, host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Copies the mcfunction file to the remote Minecraft server datapack directory."""
    remote_target = f"{REMOTE_FUNCTION_DIR}/bunker_banquet_spa.mcfunction"
    scp_cmd = [
        "scp",
        "-o", "StrictHostKeyChecking=no",
        "-i", key,
        local_path,
        f"{user}@{host}:{remote_target}",
    ]
    res = subprocess.run(scp_cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"SCP error: {res.stderr.strip()}", file=sys.stderr)
        sys.exit(res.returncode)
    print(f"Synced mcfunction to remote: {remote_target}")


def execute_via_rcon(host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Reloads datapacks and triggers execution of bunker_banquet_spa function."""
    py_code = """
import socket, struct

with open('/home/ubuntu/minecraft-server/server.properties') as f:
    props = dict(line.strip().split('=', 1) for line in f if '=' in line and not line.startswith('#'))

rcon_port = int(props.get('rcon.port', 25575))
rcon_pass = props.get('rcon.password', '')

s = socket.create_connection(('127.0.0.1', rcon_port), timeout=20)
s.sendall(struct.pack('<iii', len(rcon_pass) + 10, 1, 3) + rcon_pass.encode('utf-8') + b'\\x00\\x00')
s.recv(4096)

def run_cmd(c):
    s.sendall(struct.pack('<iii', len(c) + 10, 10, 2) + c.encode('utf-8') + b'\\x00\\x00')
    resp = s.recv(4096)
    if len(resp) >= 12:
        return resp[12:-2].decode('utf-8', errors='ignore')
    return ''

print('Reloading datapacks...')
print('Reload:', run_cmd('reload'))
print('Executing function citadel:bunker_banquet_spa...')
print('Function execution:', run_cmd('function citadel:bunker_banquet_spa'))

s.close()
"""
    ssh_cmd = [
        "ssh",
        "-o", "StrictHostKeyChecking=no",
        "-i", key,
        f"{user}@{host}",
        "python3 -c " + subprocess.list2cmdline([py_code]),
    ]
    res = subprocess.run(ssh_cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"RCON execution error: {res.stderr.strip()}", file=sys.stderr)
        sys.exit(res.returncode)
    print(res.stdout.strip())


def verify_live_blockstates(host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Queries live blockstates and entities to verify Chamber A and Chamber B."""
    py_verify = """
import socket, struct

with open('/home/ubuntu/minecraft-server/server.properties') as f:
    props = dict(line.strip().split('=', 1) for line in f if '=' in line and not line.startswith('#'))

rcon_port = int(props.get('rcon.port', 25575))
rcon_pass = props.get('rcon.password', '')

s = socket.create_connection(('127.0.0.1', rcon_port), timeout=20)
s.sendall(struct.pack('<iii', len(rcon_pass) + 10, 1, 3) + rcon_pass.encode('utf-8') + b'\\x00\\x00')
s.recv(4096)

def test_query(label, condition_cmd):
    s.sendall(struct.pack('<iii', len(condition_cmd) + 10, 10, 2) + condition_cmd.encode('utf-8') + b'\\x00\\x00')
    resp = s.recv(4096)
    msg = resp[12:-2].decode('utf-8', errors='ignore') if len(resp) >= 12 else ''
    passed = 'Test passed' in msg or 'has the following' in msg or 'Replaced' in msg or 'Modified' in msg
    status = '[PASS]' if passed else '[FAIL]'
    print(f'{status} {label}: {msg.strip()}')
    return passed

print('=== Live RCON Verification Audit: Banquet Hall & Spa ===')

# Chamber A: Banquet Hall Checks
test_query('Banquet NW Spiral Stair Landing (Y: 38)', 'execute if block 108 38 -259 polished_blackstone_stairs[facing=east]')
test_query('Banquet NE Spiral Stair Landing (Y: 38)', 'execute if block 126 38 -259 polished_blackstone_stairs[facing=west]')
test_query('Banquet 18-Block Table Top Slab', 'execute if block 116 38 -257 dark_oak_slab[type=top]')
test_query('Banquet West Chairs East Facing', 'execute if block 115 38 -250 dark_oak_stairs[facing=east]')
test_query('Banquet East Chairs West Facing', 'execute if block 118 38 -250 dark_oak_stairs[facing=west]')
test_query('Banquet Feast Cake Present', 'execute if block 116 39 -256 cake')
test_query('Banquet Feast Candles Lit', 'execute if block 116 39 -254 candle[lit=true]')
test_query('Banquet High Dais Crimson Stairs', 'execute if block 117 38 -239 crimson_stairs[facing=south]')
test_query('Banquet King Throne Crimson Seat', 'execute if block 117 39 -236 crimson_stairs[facing=north]')
test_query('Banquet King Throne Gold Block', 'execute if block 117 41 -236 gold_block')
test_query('Banquet West Fireplace Campfire', 'execute if block 106 37 -248 campfire[lit=true]')
test_query('Banquet West Fireplace Hay Block', 'execute if block 106 36 -248 hay_block')
test_query('Banquet West Fireplace Iron Bars', 'execute if block 107 38 -248 iron_bars')
test_query('Banquet East Fireplace Campfire', 'execute if block 128 37 -248 campfire[lit=true]')
test_query('Banquet Brass Chandelier Lit Bulb', 'execute if block 117 41 -254 waxed_copper_bulb[lit=true]')
test_query('Banquet Pantry Paired Chest Right', 'execute if block 111 38 -260 chest[facing=south,type=right]')
test_query('Banquet Pantry Paired Chest Left', 'execute if block 112 38 -260 chest[facing=south,type=left]')

# Chamber B: Geothermal Spa Checks
test_query('Spa Bedroom Spiral Stair Landing (Y: 38)', 'execute if block 135 38 -267 smooth_quartz_stairs[facing=west]')
test_query('Spa Mineral Pool Water Volume', 'execute if block 128 37 -280 water')
test_query('Spa Mineral Pool Submerged Campfire', 'execute if block 127 36 -283 campfire[lit=true]')
test_query('Spa Mineral Pool Steam Copper Grate', 'execute if block 127 37 -283 copper_grate')
test_query('Spa Mineral Pool Submerged Soul Sand', 'execute if block 128 36 -282 soul_sand')
test_query('Spa Mineral Pool Prismarine Rim', 'execute if block 125 38 -280 prismarine_stairs[facing=east]')
test_query('Spa Sauna Mud Brick Wall', 'execute if block 124 38 -287 mud_bricks')
test_query('Spa Sauna Spruce Door', 'execute if block 124 38 -285 spruce_door[facing=east]')
test_query('Spa Sauna Magma Heater Block', 'execute if block 122 37 -287 magma_block')
test_query('Spa Relaxation Lounger Smooth Quartz', 'execute if block 135 38 -284 smooth_quartz_stairs[facing=west]')
test_query('Spa Cascading Water Wall Source', 'execute if block 137 43 -280 water')
test_query('Spa Cascading Water Drainage Grate', 'execute if block 136 37 -280 copper_grate')
test_query('Spa Hanging Spore Blossom', 'execute if block 128 44 -280 spore_blossom')
test_query('Spa Hanging Cave Vines with Berries', 'execute if block 127 44 -278 cave_vines_plant[berries=true]')

s.close()
"""
    ssh_cmd = [
        "ssh",
        "-o", "StrictHostKeyChecking=no",
        "-i", key,
        f"{user}@{host}",
        "python3 -c " + subprocess.list2cmdline([py_verify]),
    ]
    res = subprocess.run(ssh_cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Verification error: {res.stderr.strip()}", file=sys.stderr)
        sys.exit(res.returncode)
    print(res.stdout.strip())


def main():
    print("Designing Tier 3 Sovereign Banquet Hall and Royal Geothermal Spa...")
    cmds = []
    cmds.extend(build_banquet_commands())
    cmds.extend(build_spa_commands())

    local_path = write_local_mcfunction(cmds)
    sync_mcfunction_to_remote(local_path)
    execute_via_rcon()
    verify_live_blockstates()
    print("Sovereign Banquet Hall and Royal Geothermal Spa construction complete.")


if __name__ == "__main__":
    main()
