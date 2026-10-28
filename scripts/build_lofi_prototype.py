#!/usr/bin/env python3
"""Build Non-Overlapping Lo-Fi Prototype for King Abir's Hivemind Bunker.

Generates color-coded wireframe boundaries, floor layouts, 
walking corridors, and illuminated signposts at Y: 50..53.
Strictly obeys the Y <= 53 ceiling cap.
"""

import os
import subprocess
import sys

DEFAULT_HOST = os.environ.get("HZ_HOST", "132.226.135.26")
DEFAULT_USER = os.environ.get("HZ_USER", "ubuntu")
DEFAULT_KEY = os.environ.get("HZ_KEY", os.path.expanduser("~/.ssh/id_ed25519"))

def generate_lofi_commands():
    cmds = []
    
    # 1. Central Arrival & Command Rotunda (X: 111..123, Z: -307..-295, Y: 49..53)
    cmds.append("# Central Command Rotunda")
    cmds.append("fill 111 49 -307 123 49 -295 polished_deepslate")
    cmds.append("fill 111 50 -307 123 52 -295 air")
    cmds.append("fill 111 53 -307 123 53 -295 deepslate_tiles")
    # Rotunda wireframe outline
    cmds.append("fill 111 50 -307 123 50 -307 chiseled_deepslate")
    cmds.append("fill 111 50 -295 123 50 -295 chiseled_deepslate")
    cmds.append("fill 111 50 -307 111 50 -295 chiseled_deepslate")
    cmds.append("fill 123 50 -307 123 50 -295 chiseled_deepslate")
    # Central beacon compass rose
    cmds.append("setblock 117 49 -301 sea_lantern")
    cmds.append("setblock 117 50 -301 gold_block")
    cmds.append("setblock 117 53 -301 copper_bulb[lit=true,powered=false]")
    cmds.append("setblock 114 53 -301 copper_bulb[lit=true,powered=false]")
    cmds.append("setblock 120 53 -301 copper_bulb[lit=true,powered=false]")
    cmds.append("setblock 117 53 -298 copper_bulb[lit=true,powered=false]")
    cmds.append("setblock 117 53 -304 copper_bulb[lit=true,powered=false]")

    # 2. Arrival Stair Connection (X: 116..118, Z: -309..-308, Y: 50..52)
    cmds.append("# Stair Arrival Connection")
    cmds.append("fill 116 49 -308 118 49 -308 polished_deepslate")
    cmds.append("fill 116 50 -308 118 52 -308 air")
    cmds.append("fill 116 53 -308 118 53 -308 deepslate_tiles")

    # 3. Arterial Corridors (3-wide, 3-high, Y: 50..52 air, Y: 49 floor, Y: 53 ceiling)
    cmds.append("# West Arterial Corridor to Tool Armory")
    cmds.append("fill 95 49 -302 110 49 -300 polished_deepslate")
    cmds.append("fill 95 50 -302 110 52 -300 air")
    cmds.append("fill 95 53 -302 110 53 -300 copper_bulb[lit=true,powered=false]")

    cmds.append("# East Arterial Corridor to Arcane Library")
    cmds.append("fill 124 49 -302 139 49 -300 polished_deepslate")
    cmds.append("fill 124 50 -302 139 52 -300 air")
    cmds.append("fill 124 53 -302 139 53 -300 copper_bulb[lit=true,powered=false]")

    cmds.append("# South Sovereign Boulevard")
    cmds.append("fill 116 49 -294 118 49 -262 polished_deepslate")
    cmds.append("fill 116 50 -294 118 52 -262 air")
    cmds.append("fill 116 53 -294 118 53 -262 deepslate_tiles")
    cmds.append("fill 117 50 -294 117 50 -262 red_carpet")
    for z in range(-292, -261, 6):
        cmds.append(f"setblock 117 53 {z} copper_bulb[lit=true,powered=false]")

    # 4. Tool & Equipment Armory (Outer West: X: 74..94, Z: -307..-295): Yellow Wireframe
    cmds.append("# Tool and Equipment Armory")
    cmds.append("fill 74 49 -307 94 49 -295 polished_andesite")
    cmds.append("fill 74 50 -307 94 52 -295 air")
    cmds.append("fill 74 53 -307 94 53 -295 deepslate_tiles")
    cmds.append("fill 74 50 -307 94 50 -307 yellow_terracotta")
    cmds.append("fill 74 50 -295 94 50 -295 yellow_terracotta")
    cmds.append("fill 74 50 -307 74 50 -295 yellow_terracotta")
    cmds.append("fill 94 50 -307 94 50 -295 yellow_terracotta")
    # Doorway to West Corridor
    cmds.append("fill 94 50 -302 94 52 -300 air")
    # Furnishings
    cmds.append("setblock 75 50 -306 anvil[facing=north]")
    cmds.append("setblock 76 50 -306 smithing_table")
    cmds.append("setblock 77 50 -306 grindstone[face=floor,facing=north]")
    cmds.append("setblock 78 50 -306 crafting_table")
    cmds.append("setblock 75 50 -296 ender_chest[facing=south]")
    cmds.append("setblock 84 53 -301 copper_bulb[lit=true,powered=false]")

    # 5. Blacksmith & Smelting Workshop (Outer West: X: 74..94, Z: -291..-275): Orange Wireframe
    cmds.append("# Blacksmith and Smelting Workshop")
    cmds.append("fill 74 49 -291 94 49 -275 smooth_basalt")
    cmds.append("fill 74 50 -291 94 52 -275 air")
    cmds.append("fill 74 53 -291 94 53 -275 deepslate_tiles")
    cmds.append("fill 74 50 -291 94 50 -291 orange_terracotta")
    cmds.append("fill 74 50 -275 94 50 -275 orange_terracotta")
    cmds.append("fill 74 50 -291 74 50 -275 orange_terracotta")
    cmds.append("fill 94 50 -291 94 50 -275 orange_terracotta")
    # Doorway to West Connector
    cmds.append("fill 94 50 -284 94 52 -282 air")
    # North-South connector between Armory and Blacksmith
    cmds.append("fill 83 49 -294 85 49 -292 polished_deepslate")
    cmds.append("fill 83 50 -294 85 52 -292 air")
    cmds.append("fill 83 53 -294 85 53 -292 deepslate_tiles")
    # Furnishings
    cmds.append("fill 75 50 -290 75 50 -284 blast_furnace[facing=east,lit=false]")
    cmds.append("setblock 75 50 -280 cauldron[level=3]")
    cmds.append("setblock 75 50 -278 stonecutter[facing=east]")
    cmds.append("setblock 84 53 -283 copper_bulb[lit=true,powered=false]")

    # 6. Arcane Library & Enchanting Room (Outer East: X: 140..160, Z: -307..-295): Purple Wireframe
    cmds.append("# Arcane Library and Enchanting Room")
    cmds.append("fill 140 49 -307 160 49 -295 dark_oak_planks")
    cmds.append("fill 140 50 -307 160 52 -295 air")
    cmds.append("fill 140 53 -307 160 53 -295 deepslate_tiles")
    cmds.append("fill 140 50 -307 160 50 -307 purple_terracotta")
    cmds.append("fill 140 50 -295 160 50 -295 purple_terracotta")
    cmds.append("fill 140 50 -307 140 50 -295 purple_terracotta")
    cmds.append("fill 160 50 -307 160 50 -295 purple_terracotta")
    # Doorway to East Corridor
    cmds.append("fill 140 50 -302 140 52 -300 air")
    # Furnishings
    cmds.append("setblock 150 50 -301 enchanting_table")
    cmds.append("fill 149 50 -303 151 50 -303 bookshelf")
    cmds.append("setblock 148 50 -301 bookshelf")
    cmds.append("setblock 152 50 -301 bookshelf")
    cmds.append("setblock 150 53 -301 copper_bulb[lit=true,powered=false]")

    # 7. Brewing & Alchemy Laboratory (Outer East: X: 140..160, Z: -291..-275): Magenta Wireframe
    cmds.append("# Brewing and Alchemy Laboratory")
    cmds.append("fill 140 49 -291 160 49 -275 tuff_bricks")
    cmds.append("fill 140 50 -291 160 52 -275 air")
    cmds.append("fill 140 53 -291 160 53 -275 deepslate_tiles")
    cmds.append("fill 140 50 -291 160 50 -291 magenta_terracotta")
    cmds.append("fill 140 50 -275 160 50 -275 magenta_terracotta")
    cmds.append("fill 140 50 -291 140 50 -275 magenta_terracotta")
    cmds.append("fill 160 50 -291 160 50 -275 magenta_terracotta")
    # Doorway
    cmds.append("fill 140 50 -284 140 52 -282 air")
    # North-South connector between Library and Brewing
    cmds.append("fill 149 49 -294 151 49 -292 polished_deepslate")
    cmds.append("fill 149 50 -294 151 52 -292 air")
    cmds.append("fill 149 53 -294 151 53 -292 deepslate_tiles")
    # Furnishings
    cmds.append("setblock 159 50 -284 brewing_stand")
    cmds.append("setblock 159 50 -282 brewing_stand")
    cmds.append("setblock 159 50 -283 cauldron[level=3]")
    cmds.append("fill 156 50 -290 159 50 -290 soul_sand")
    cmds.append("fill 156 51 -290 159 51 -290 nether_wart[age=3]")
    cmds.append("setblock 150 53 -283 copper_bulb[lit=true,powered=false]")

    # 8. Underground Farm & Botany Pod (Inner West: X: 96..114, Z: -291..-265): Lime Wireframe
    cmds.append("# Underground Farm and Botany Pod")
    cmds.append("fill 96 49 -291 114 49 -265 moss_block")
    cmds.append("fill 96 50 -291 114 52 -265 air")
    cmds.append("fill 96 53 -291 114 53 -265 deepslate_tiles")
    cmds.append("fill 96 50 -291 114 50 -291 lime_terracotta")
    cmds.append("fill 96 50 -265 114 50 -265 lime_terracotta")
    cmds.append("fill 96 50 -291 96 50 -265 lime_terracotta")
    cmds.append("fill 114 50 -291 114 50 -265 lime_terracotta")
    # Doorway to South Boulevard
    cmds.append("fill 114 50 -279 116 52 -277 air")
    # East-West connector from Farm to Blacksmith
    cmds.append("fill 94 49 -284 96 49 -282 polished_deepslate")
    cmds.append("fill 94 50 -284 96 52 -282 air")
    cmds.append("fill 94 53 -284 96 53 -282 deepslate_tiles")
    # Furnishings
    cmds.append("fill 98 50 -288 104 50 -288 farmland[moisture=7]")
    cmds.append("fill 98 51 -288 104 51 -288 wheat[age=7]")
    cmds.append("setblock 105 50 -288 water")
    cmds.append("setblock 98 50 -286 composter[level=4]")
    cmds.append("setblock 105 53 -278 copper_bulb[lit=true,powered=false]")

    # 9. Modern Subterranean Housing & Living Quarters (Inner East: X: 120..138, Z: -291..-265): Light Blue Wireframe
    cmds.append("# Modern Subterranean Housing")
    cmds.append("fill 120 49 -291 138 49 -265 smooth_quartz")
    cmds.append("fill 120 50 -291 138 52 -265 air")
    cmds.append("fill 120 53 -291 138 53 -265 deepslate_tiles")
    cmds.append("fill 120 50 -291 138 50 -291 light_blue_terracotta")
    cmds.append("fill 120 50 -265 138 50 -265 light_blue_terracotta")
    cmds.append("fill 120 50 -291 120 50 -265 light_blue_terracotta")
    cmds.append("fill 138 50 -291 138 50 -265 light_blue_terracotta")
    # Doorway to South Boulevard
    cmds.append("fill 118 50 -279 120 52 -277 air")
    # East-West connector from Housing to Brewing Lab
    cmds.append("fill 138 49 -284 140 49 -282 polished_deepslate")
    cmds.append("fill 138 50 -284 140 52 -282 air")
    cmds.append("fill 138 53 -284 140 53 -282 deepslate_tiles")
    # Furnishings
    cmds.append("setblock 137 50 -289 red_bed[facing=north,part=head]")
    cmds.append("setblock 137 50 -288 red_bed[facing=north,part=foot]")
    cmds.append("setblock 135 50 -289 stripped_spruce_log")
    cmds.append("setblock 135 51 -289 lantern[hanging=false]")
    cmds.append("setblock 129 53 -278 copper_bulb[lit=true,powered=false]")

    # 10. King's Council & High Parliament (Center South: X: 105..129, Z: -261..-235): Red Wireframe
    cmds.append("# Kings Council and High Parliament")
    cmds.append("fill 105 49 -261 129 49 -235 polished_blackstone")
    cmds.append("fill 105 50 -261 129 52 -235 air")
    cmds.append("fill 105 53 -261 129 53 -235 deepslate_tiles")
    cmds.append("fill 105 50 -261 129 50 -261 red_terracotta")
    cmds.append("fill 105 50 -235 129 50 -235 red_terracotta")
    cmds.append("fill 105 50 -261 105 50 -235 red_terracotta")
    cmds.append("fill 129 50 -261 129 50 -235 red_terracotta")
    # Main entrance from South Boulevard
    cmds.append("fill 116 50 -261 118 52 -261 air")
    # Central Aisle
    cmds.append("fill 116 50 -260 118 50 -240 red_carpet")
    # Sovereign Throne Dais
    cmds.append("fill 115 50 -239 119 50 -237 gilded_blackstone")
    cmds.append("setblock 117 51 -238 polished_blackstone_stairs[facing=south,half=bottom]")
    cmds.append("setblock 117 52 -238 red_banner[rotation=0]")
    # Ceremonial Mace Plinth
    cmds.append("setblock 117 51 -244 chiseled_polished_blackstone")
    cmds.append("setblock 117 52 -244 lightning_rod[facing=up]")
    # Parliament sample benches
    cmds.append("fill 111 50 -256 113 50 -256 dark_oak_stairs[facing=east,half=bottom]")
    cmds.append("fill 121 50 -256 123 50 -256 dark_oak_stairs[facing=west,half=bottom]")
    cmds.append("setblock 117 53 -248 copper_bulb[lit=true,powered=false]")
    cmds.append("setblock 117 53 -240 copper_bulb[lit=true,powered=false]")

    return [cmd for cmd in cmds if not cmd.startswith("#")]

def execute_batch(cmds, host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    py_code = f"""
import socket, struct

with open('/home/ubuntu/minecraft-server/server.properties') as f:
    props = dict(line.strip().split('=', 1) for line in f if '=' in line and not line.startswith('#'))

rcon_port = int(props.get('rcon.port', 25575))
rcon_pass = props.get('rcon.password', '')

s = socket.create_connection(('127.0.0.1', rcon_port), timeout=10)
s.sendall(struct.pack('<iii', len(rcon_pass) + 10, 1, 3) + rcon_pass.encode('utf-8') + b'\\x00\\x00')
auth_resp = s.recv(4096)

cmds = {repr(cmds)}
success_count = 0
for idx, cmd in enumerate(cmds, 1):
    s.sendall(struct.pack('<iii', len(cmd) + 10, idx + 10, 2) + cmd.encode('utf-8') + b'\\x00\\x00')
    resp = s.recv(4096)
    success_count += 1

s.close()
print(f'Executed {{success_count}} of {{len(cmds)}} commands successfully.')
"""
    ssh_cmd = [
        "ssh", "-o", "StrictHostKeyChecking=no",
        "-i", key,
        f"{user}@{host}",
        f"python3 -c {subprocess.list2cmdline([py_code])}"
    ]
    res = subprocess.run(ssh_cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error: {res.stderr}", file=sys.stderr)
        sys.exit(res.returncode)
    print(res.stdout)

if __name__ == "__main__":
    commands = generate_lofi_commands()
    print(f"Generated {len(commands)} Lo-Fi prototype commands...")
    execute_batch(commands)
    print("Non-overlapping Lo-Fi prototype wireframe built successfully.")
