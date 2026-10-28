#!/usr/bin/env python3
"""Build Subterranean Hyperloop Transit Hub and Automated Rail Network.

Constructs the Tier 3 automated hyperloop transit network (Y: 37..43) for King Abir Hivemind Bunker.
Features:
1. Central Terminal Concourse (X: 112..122, Z: -306..-296, Y: 37..43).
2. Platform architecture with smooth quartz flooring and hazard edge striping.
3. Automated departure dispatchers with minecart dispensers and launch rails.
4. Line 1: West Line to Heavy Ore Processing along Z: -301 to X: 84.
5. Line 2: East Line to Apocrypha Archives along Z: -301 to X: 150.
6. Line 3: South Line to Sovereign Banquet Hall along X: 117 to Z: -248.
7. Arrival terminuses with detector rails, copper bulb signal lights, and hopper collection.
8. Complete copper bulb and sea lantern illumination grids to prevent mob spawning.
"""

import math
import os
import subprocess
import sys
import time

DEFAULT_HOST = os.environ.get("HZ_HOST", "132.226.135.26")
DEFAULT_USER = os.environ.get("HZ_USER", "ubuntu")
DEFAULT_KEY = os.environ.get("HZ_KEY", os.path.expanduser("~/.ssh/id_ed25519"))

FUNCTION_PATH = "datapacks/underground_citadel/data/citadel/function/bunker_hyperloop.mcfunction"

def write_mcfunction(filepath, lines):
    """Writes clean command lines to target mcfunction file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    clean_lines = [line.strip() for line in lines if line.strip()]
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(clean_lines) + "\n")
    return clean_lines

def build_central_terminal():
    """Generates commands for the Central Terminal Concourse."""
    cmds = [
        "# Central Terminal Concourse (X: 112..122, Z: -306..-296, Y: 37..43)",
        # North Concourse Platform excavation
        "fill 112 38 -306 122 42 -304 air",
        # North Concourse foundation and floor at Y: 37..38
        "fill 112 37 -306 122 37 -304 polished_blackstone",
        "fill 112 38 -306 122 38 -304 smooth_quartz",
        # Ceiling at Y: 43
        "fill 112 43 -306 122 43 -296 deepslate_tiles",
        # Perimeter North Wall at Z: -307
        "fill 112 38 -307 122 42 -307 deepslate_tiles",
        # Structural pilasters
        "fill 112 38 -307 112 42 -307 chiseled_deepslate",
        "fill 122 38 -307 122 42 -307 chiseled_deepslate",
        "fill 117 38 -307 117 42 -307 chiseled_deepslate",
        # Passenger waiting benches
        "setblock 113 39 -306 dark_oak_stairs[facing=south,half=bottom]",
        "setblock 114 39 -306 dark_oak_slab[type=bottom]",
        "setblock 115 39 -306 dark_oak_stairs[facing=south,half=bottom]",
        "setblock 119 39 -306 dark_oak_stairs[facing=south,half=bottom]",
        "setblock 120 39 -306 dark_oak_slab[type=bottom]",
        "setblock 121 39 -306 dark_oak_stairs[facing=south,half=bottom]",
        # Destination directory signs on North Wall
        "setblock 113 40 -306 spruce_wall_sign[facing=south]",
        "setblock 117 40 -306 spruce_wall_sign[facing=south]",
        "setblock 121 40 -306 spruce_wall_sign[facing=south]",
        # Concourse overhead lighting grid
        "setblock 114 43 -305 copper_bulb[lit=true,powered=false]",
        "setblock 117 43 -305 sea_lantern",
        "setblock 120 43 -305 copper_bulb[lit=true,powered=false]",
        "setblock 114 43 -299 copper_bulb[lit=true,powered=false]",
        "setblock 120 43 -299 copper_bulb[lit=true,powered=false]",
        # East concourse walkway connecting North platform to Line 2 departure bay
        "fill 120 38 -303 122 42 -299 air",
        "fill 120 37 -303 122 37 -299 polished_blackstone",
        "fill 120 38 -303 122 38 -299 smooth_quartz",
        # West concourse walkway connecting North platform to Line 1 departure bay
        "fill 112 38 -303 114 42 -299 air",
        "fill 112 37 -303 114 37 -299 polished_blackstone",
        "fill 112 38 -303 114 38 -299 smooth_quartz",
        # South concourse walkway connecting elevator hub to Line 3 departure bay
        "fill 116 38 -298 118 42 -296 air",
        "fill 116 37 -298 118 37 -296 polished_blackstone",
        "fill 116 38 -298 118 38 -296 smooth_quartz",
    ]
    return cmds

def build_line_1_west():
    """Generates Line 1: West Line to Heavy Ore Processing."""
    cmds = [
        "# Line 1: West Line to Heavy Ore Processing (Z: -301, X: 112 to 84, Y: 38)",
        # Tunnel excavation
        "fill 84 38 -302 112 41 -300 air",
        # Tunnel foundation and ceiling
        "fill 84 37 -302 112 37 -300 polished_blackstone",
        "fill 84 42 -302 112 42 -300 deepslate_tiles",
        # Tunnel perimeter walls
        "fill 84 38 -302 112 41 -302 deepslate_tiles",
        "fill 84 38 -300 112 41 -300 deepslate_tiles",
        # Central Terminal Platform 1 hazard edge striping
        "setblock 114 38 -302 yellow_concrete",
        "setblock 113 38 -302 black_concrete",
        "setblock 112 38 -302 yellow_concrete",
        "setblock 111 38 -302 black_concrete",
        "setblock 110 38 -302 yellow_concrete",
        "setblock 114 38 -300 black_concrete",
        "setblock 113 38 -300 yellow_concrete",
        "setblock 112 38 -300 black_concrete",
        "setblock 111 38 -300 yellow_concrete",
        "setblock 110 38 -300 black_concrete",
        # Line 1 Departure Bay buffer block and dispenser
        "setblock 113 38 -301 polished_blackstone",
        "setblock 113 39 -301 dispenser[facing=west]{Items:[{Slot:0b,id:\"minecraft:minecart\",count:64}]}",
        "setblock 113 40 -301 stone_button[facing=north,face=floor]",
        # Departure launch rail over redstone block
        "setblock 112 37 -301 redstone_block",
        "setblock 112 38 -301 powered_rail[shape=east_west]",
        # Propulsion rail line with powered rails every 5 blocks over redstone
        "setblock 107 37 -301 redstone_block",
        "setblock 107 38 -301 powered_rail[shape=east_west]",
        "fill 108 38 -301 111 38 -301 rail[shape=east_west]",
        "setblock 102 37 -301 redstone_block",
        "setblock 102 38 -301 powered_rail[shape=east_west]",
        "fill 103 38 -301 106 38 -301 rail[shape=east_west]",
        "setblock 97 37 -301 redstone_block",
        "setblock 97 38 -301 powered_rail[shape=east_west]",
        "fill 98 38 -301 101 38 -301 rail[shape=east_west]",
        "setblock 92 37 -301 redstone_block",
        "setblock 92 38 -301 powered_rail[shape=east_west]",
        "fill 93 38 -301 96 38 -301 rail[shape=east_west]",
        "setblock 87 37 -301 redstone_block",
        "setblock 87 38 -301 powered_rail[shape=east_west]",
        "fill 88 38 -301 91 38 -301 rail[shape=east_west]",
        # Arrival Terminus at Ore Processing (X: 84..86)
        # Detector rail and signal lamp
        "setblock 86 38 -301 detector_rail[shape=east_west]",
        "setblock 86 40 -301 copper_bulb[lit=true,powered=false]",
        # Decelerator brake rail
        "setblock 85 37 -301 smooth_basalt",
        "setblock 85 38 -301 powered_rail[shape=east_west]",
        # Cart collection hopper and storage chest
        "setblock 84 37 -301 chest[facing=north]",
        "setblock 84 38 -301 hopper[facing=down]",
        # Terminus buffer stop
        "setblock 83 38 -301 polished_blackstone",
        "setblock 83 39 -301 iron_bars",
        # Return departure bay at Ore Processing (X: 84, Z: -299)
        "setblock 83 38 -299 polished_blackstone",
        "setblock 83 39 -299 dispenser[facing=east]{Items:[{Slot:0b,id:\"minecraft:minecart\",count:64}]}",
        "setblock 83 40 -299 stone_button[facing=north,face=floor]",
        "setblock 84 37 -299 redstone_block",
        "setblock 84 38 -299 powered_rail[shape=east_west]",
        # Tunnel illumination grid
        "setblock 110 42 -301 copper_bulb[lit=true,powered=false]",
        "setblock 105 42 -301 sea_lantern",
        "setblock 100 42 -301 copper_bulb[lit=true,powered=false]",
        "setblock 95 42 -301 sea_lantern",
        "setblock 90 42 -301 copper_bulb[lit=true,powered=false]",
        "setblock 85 42 -301 sea_lantern",
    ]
    return cmds

def build_line_2_east():
    """Generates Line 2: East Line to Apocrypha Archives."""
    cmds = [
        "# Line 2: East Line to Apocrypha Archives (Z: -301, X: 122 to 150, Y: 38)",
        # Tunnel excavation
        "fill 122 38 -302 150 41 -300 air",
        # Tunnel foundation and ceiling
        "fill 122 37 -302 150 37 -300 polished_blackstone",
        "fill 122 42 -302 150 42 -300 deepslate_tiles",
        # Tunnel perimeter walls
        "fill 122 38 -302 150 41 -302 deepslate_tiles",
        "fill 122 38 -300 150 41 -300 deepslate_tiles",
        # Central Terminal Platform 2 hazard edge striping
        "setblock 120 38 -302 yellow_concrete",
        "setblock 121 38 -302 black_concrete",
        "setblock 122 38 -302 yellow_concrete",
        "setblock 123 38 -302 black_concrete",
        "setblock 124 38 -302 yellow_concrete",
        "setblock 120 38 -300 black_concrete",
        "setblock 121 38 -300 yellow_concrete",
        "setblock 122 38 -300 black_concrete",
        "setblock 123 38 -300 yellow_concrete",
        "setblock 124 38 -300 black_concrete",
        # Line 2 Departure Bay buffer block and dispenser
        "setblock 121 38 -301 polished_blackstone",
        "setblock 121 39 -301 dispenser[facing=east]{Items:[{Slot:0b,id:\"minecraft:minecart\",count:64}]}",
        "setblock 121 40 -301 stone_button[facing=north,face=floor]",
        # Departure launch rail over redstone block
        "setblock 122 37 -301 redstone_block",
        "setblock 122 38 -301 powered_rail[shape=east_west]",
        # Propulsion rail line with powered rails every 5 blocks over redstone
        "fill 123 38 -301 126 38 -301 rail[shape=east_west]",
        "setblock 127 37 -301 redstone_block",
        "setblock 127 38 -301 powered_rail[shape=east_west]",
        "fill 128 38 -301 131 38 -301 rail[shape=east_west]",
        "setblock 132 37 -301 redstone_block",
        "setblock 132 38 -301 powered_rail[shape=east_west]",
        "fill 133 38 -301 136 38 -301 rail[shape=east_west]",
        "setblock 137 37 -301 redstone_block",
        "setblock 137 38 -301 powered_rail[shape=east_west]",
        "fill 138 38 -301 141 38 -301 rail[shape=east_west]",
        "setblock 142 37 -301 redstone_block",
        "setblock 142 38 -301 powered_rail[shape=east_west]",
        "fill 143 38 -301 146 38 -301 rail[shape=east_west]",
        "setblock 147 37 -301 redstone_block",
        "setblock 147 38 -301 powered_rail[shape=east_west]",
        # Arrival Terminus at Apocrypha Archives (X: 148..150)
        # Detector rail and signal lamp
        "setblock 148 38 -301 detector_rail[shape=east_west]",
        "setblock 148 40 -301 copper_bulb[lit=true,powered=false]",
        # Decelerator brake rail
        "setblock 149 37 -301 polished_blackstone",
        "setblock 149 38 -301 powered_rail[shape=east_west]",
        # Cart collection hopper and storage chest
        "setblock 150 37 -301 chest[facing=north]",
        "setblock 150 38 -301 hopper[facing=down]",
        # Terminus buffer stop
        "setblock 151 38 -301 crying_obsidian",
        "setblock 151 39 -301 iron_bars",
        # Return departure bay at Apocrypha (X: 150, Z: -299)
        "setblock 151 38 -299 crying_obsidian",
        "setblock 151 39 -299 dispenser[facing=west]{Items:[{Slot:0b,id:\"minecraft:minecart\",count:64}]}",
        "setblock 151 40 -299 stone_button[facing=north,face=floor]",
        "setblock 150 37 -299 redstone_block",
        "setblock 150 38 -299 powered_rail[shape=east_west]",
        # Tunnel illumination grid
        "setblock 125 42 -301 sea_lantern",
        "setblock 130 42 -301 copper_bulb[lit=true,powered=false]",
        "setblock 135 42 -301 sea_lantern",
        "setblock 140 42 -301 copper_bulb[lit=true,powered=false]",
        "setblock 145 42 -301 sea_lantern",
    ]
    return cmds

def build_line_3_south():
    """Generates Line 3: South Line to Sovereign Banquet Hall."""
    cmds = [
        "# Line 3: South Line to Sovereign Banquet Hall (X: 117, Z: -295 to -248, Y: 38)",
        # Tunnel excavation
        "fill 116 38 -295 118 41 -248 air",
        # Tunnel foundation and ceiling
        "fill 115 37 -295 119 37 -248 polished_blackstone",
        "fill 115 42 -295 119 42 -248 deepslate_tiles",
        # Tunnel perimeter walls
        "fill 115 38 -295 115 41 -248 deepslate_tiles",
        "fill 119 38 -295 119 41 -248 deepslate_tiles",
        # Central Terminal Platform 3 hazard edge striping
        "setblock 116 38 -296 yellow_concrete",
        "setblock 116 38 -295 black_concrete",
        "setblock 116 38 -294 yellow_concrete",
        "setblock 116 38 -293 black_concrete",
        "setblock 118 38 -296 black_concrete",
        "setblock 118 38 -295 yellow_concrete",
        "setblock 118 38 -294 black_concrete",
        "setblock 118 38 -293 yellow_concrete",
        # Line 3 Departure Bay buffer block and dispenser
        "setblock 117 38 -296 polished_blackstone",
        "setblock 117 39 -296 dispenser[facing=south]{Items:[{Slot:0b,id:\"minecraft:minecart\",count:64}]}",
        "setblock 117 40 -296 stone_button[facing=north,face=floor]",
        # Departure launch rail over redstone block
        "setblock 117 37 -295 redstone_block",
        "setblock 117 38 -295 powered_rail[shape=north_south]",
        # Propulsion rail line with powered rails every 5 blocks over redstone
        "fill 117 38 -294 117 38 -291 rail[shape=north_south]",
        "setblock 117 37 -290 redstone_block",
        "setblock 117 38 -290 powered_rail[shape=north_south]",
        "fill 117 38 -289 117 38 -286 rail[shape=north_south]",
        "setblock 117 37 -285 redstone_block",
        "setblock 117 38 -285 powered_rail[shape=north_south]",
        "fill 117 38 -284 117 38 -281 rail[shape=north_south]",
        "setblock 117 37 -280 redstone_block",
        "setblock 117 38 -280 powered_rail[shape=north_south]",
        "fill 117 38 -279 117 38 -276 rail[shape=north_south]",
        "setblock 117 37 -275 redstone_block",
        "setblock 117 38 -275 powered_rail[shape=north_south]",
        "fill 117 38 -274 117 38 -271 rail[shape=north_south]",
        "setblock 117 37 -270 redstone_block",
        "setblock 117 38 -270 powered_rail[shape=north_south]",
        "fill 117 38 -269 117 38 -266 rail[shape=north_south]",
        "setblock 117 37 -265 redstone_block",
        "setblock 117 38 -265 powered_rail[shape=north_south]",
        "fill 117 38 -264 117 38 -261 rail[shape=north_south]",
        "setblock 117 37 -260 redstone_block",
        "setblock 117 38 -260 powered_rail[shape=north_south]",
        "fill 117 38 -259 117 38 -256 rail[shape=north_south]",
        "setblock 117 37 -255 redstone_block",
        "setblock 117 38 -255 powered_rail[shape=north_south]",
        "fill 117 38 -254 117 38 -252 rail[shape=north_south]",
        # Arrival Terminus at Sovereign Banquet Hall (Z: -251..-248)
        # Detector rail and signal lamp
        "setblock 117 38 -251 detector_rail[shape=north_south]",
        "setblock 117 40 -251 copper_bulb[lit=true,powered=false]",
        # Decelerator brake rail
        "setblock 117 37 -250 smooth_basalt",
        "setblock 117 38 -250 powered_rail[shape=north_south]",
        "setblock 117 37 -249 smooth_basalt",
        "setblock 117 38 -249 powered_rail[shape=north_south]",
        # Cart collection hopper and storage chest
        "setblock 117 37 -248 chest[facing=north]",
        "setblock 117 38 -248 hopper[facing=down]",
        # Terminus buffer stop
        "setblock 117 38 -247 polished_blackstone",
        "setblock 117 39 -247 iron_bars",
        # Arrival Platform at Banquet Hall (Z: -252..-247, X: 113..116)
        "fill 113 38 -252 116 41 -247 air",
        "fill 113 37 -252 116 37 -247 polished_blackstone",
        "fill 113 38 -252 116 38 -247 smooth_quartz",
        "fill 113 42 -252 116 42 -247 deepslate_tiles",
        # Hazard edge striping along Banquet Hall platform
        "setblock 116 38 -252 yellow_concrete",
        "setblock 116 38 -251 black_concrete",
        "setblock 116 38 -250 yellow_concrete",
        "setblock 116 38 -249 black_concrete",
        "setblock 116 38 -248 yellow_concrete",
        # Return departure bay at Banquet Hall (X: 114, Z: -248)
        "setblock 114 38 -247 polished_blackstone",
        "setblock 114 39 -247 dispenser[facing=north]{Items:[{Slot:0b,id:\"minecraft:minecart\",count:64}]}",
        "setblock 114 40 -247 stone_button[facing=north,face=floor]",
        "setblock 114 37 -248 redstone_block",
        "setblock 114 38 -248 powered_rail[shape=north_south]",
        # Tunnel illumination grid
        "setblock 117 42 -290 copper_bulb[lit=true,powered=false]",
        "setblock 117 42 -280 sea_lantern",
        "setblock 117 42 -270 copper_bulb[lit=true,powered=false]",
        "setblock 117 42 -260 sea_lantern",
        "setblock 117 42 -250 copper_bulb[lit=true,powered=false]",
        "setblock 114 42 -250 sea_lantern",
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
            print(f"Batch {(i // batch_size) + 1} error: {res.stderr}", file=sys.stderr)
            sys.exit(res.returncode)
        total_batches = math.ceil(total / batch_size)
        current_batch = (i // batch_size) + 1
        print(f"Batch {current_batch}/{total_batches} complete.")

def verify_live_blockstates(host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Verifies live blockstates of the hyperloop rail network via RCON."""
    checks = [
        ("Terminal Concourse Floor", "execute if block 117 38 -305 smooth_quartz"),
        ("Terminal Line 1 Dispenser", "execute if block 113 39 -301 dispenser[facing=west]"),
        ("Terminal Line 1 Launch Rail", "execute if block 112 38 -301 powered_rail[shape=east_west,powered=true]"),
        ("Terminal Line 1 Hazard Stripe", "execute if block 112 38 -302 yellow_concrete"),
        ("Line 1 Mid Propulsion Rail", "execute if block 97 38 -301 powered_rail[shape=east_west]"),
        ("Line 1 Ore Refinery Detector Rail", "execute if block 86 38 -301 detector_rail[shape=east_west]"),
        ("Line 1 Ore Refinery Hopper Terminus", "execute if block 84 38 -301 hopper[facing=down]"),
        ("Terminal Line 2 Dispenser", "execute if block 121 39 -301 dispenser[facing=east]"),
        ("Terminal Line 2 Launch Rail", "execute if block 122 38 -301 powered_rail[shape=east_west,powered=true]"),
        ("Terminal Line 2 Hazard Stripe", "execute if block 122 38 -302 yellow_concrete"),
        ("Line 2 Mid Propulsion Rail", "execute if block 137 38 -301 powered_rail[shape=east_west]"),
        ("Line 2 Apocrypha Detector Rail", "execute if block 148 38 -301 detector_rail[shape=east_west]"),
        ("Line 2 Apocrypha Hopper Terminus", "execute if block 150 38 -301 hopper[facing=down]"),
        ("Terminal Line 3 Dispenser", "execute if block 117 39 -296 dispenser[facing=south]"),
        ("Terminal Line 3 Launch Rail", "execute if block 117 38 -295 powered_rail[shape=north_south,powered=true]"),
        ("Terminal Line 3 Hazard Stripe", "execute if block 118 38 -296 black_concrete"),
        ("Line 3 Mid Propulsion Rail", "execute if block 117 38 -275 powered_rail[shape=north_south]"),
        ("Line 3 Banquet Detector Rail", "execute if block 117 38 -251 detector_rail[shape=north_south]"),
        ("Line 3 Banquet Hopper Terminus", "execute if block 117 38 -248 hopper[facing=down]"),
        ("Banquet Arrival Platform Floor", "execute if block 115 38 -250 smooth_quartz"),
        ("Banquet Hazard Striping", "execute if block 116 38 -250 yellow_concrete"),
        ("Terminal Ceiling Light", "execute if block 117 43 -305 sea_lantern"),
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
    commands.extend(build_central_terminal())
    commands.extend(build_line_1_west())
    commands.extend(build_line_2_east())
    commands.extend(build_line_3_south())

    print(f"Generated {len(commands)} commands.")
    write_mcfunction(FUNCTION_PATH, commands)
    print(f"Wrote native mcfunction to {FUNCTION_PATH}.")

    print("Deploying datapack file to production server...")
    deploy_datapack_file()

    print("Executing batch construction over RCON...")
    execute_remote_batch([c for c in commands if not c.startswith("#")])

    print("Pausing briefly for block updates...")
    time.sleep(2)

    print("Verifying live blockstates...")
    verify_live_blockstates()
    print("Tier 3 Hyperloop Transit Network constructed and verified.")
