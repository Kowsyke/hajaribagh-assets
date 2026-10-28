#!/usr/bin/env python3
"""Build Sector 16 Subterranean Cryo-Vault and Ancient Relic Conservatory.

Generates Tier 3 cryogenic exhibition vault directly beneath Sector 13 War Room.
Coordinates: X: 111..123, Z: -320..-308, Y: 36..45.
Ceiling limit: Strictly Y <= 45 preserving War Room floor at Y: 46.
Includes:
1. Ancient Relic Containment Pods displaying heavy cores, dragon heads, ominous vaults, sniffer eggs, and trial spawners.
2. Cryo-Stasis Chamber with blue ice floor, submerged sea lanterns, packed ice borders, and soul fire braziers.
3. Armored Security Portcullis at Z: -308 with calibrated sculk sensor access trigger and copper bulb status lamps.
4. Vaulted ceiling at Y: 45 with exposed copper grate ventilation shafts, hanging soul lanterns, and end rods.
"""

import math
import os
import subprocess
import sys
import time

DEFAULT_HOST = os.environ.get("HZ_HOST", "132.226.135.26")
DEFAULT_USER = os.environ.get("HZ_USER", "ubuntu")
DEFAULT_KEY = os.environ.get("HZ_KEY", os.path.expanduser("~/.ssh/id_ed25519"))

FUNCTION_PATH = "datapacks/underground_citadel/data/citadel/function/bunker_cryo_relic_vault.mcfunction"

def write_mcfunction(filepath, lines):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    clean_lines = [line.strip() for line in lines if line.strip()]
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(clean_lines) + "\n")
    return clean_lines

def build_perimeter_and_structure():
    """Generates structural excavation, walls, subfloor, and ceiling cap."""
    cmds = [
        "# Sector 16 Perimeter and Foundation (X: 111..123, Z: -320..-308, Y: 36..45)",
        # Clear interior volume from Y: 36 to Y: 45
        "fill 111 36 -320 123 45 -308 air",
        # Subfloor foundation layer at Y: 36
        "fill 111 36 -320 123 36 -308 polished_blackstone",
        # Enclosing perimeter walls (Y: 36..45)
        # North wall at Z: -320
        "fill 111 36 -320 123 45 -320 deepslate_bricks",
        # South wall at Z: -308
        "fill 111 36 -308 123 45 -308 deepslate_bricks",
        # West wall at X: 111
        "fill 111 36 -320 111 45 -308 deepslate_bricks",
        # East wall at X: 123
        "fill 123 36 -320 123 45 -308 deepslate_bricks",
        # Ceiling cap strictly at Y: 45 directly beneath War Room floor at Y: 46
        "fill 111 45 -320 123 45 -308 deepslate_tiles",
        # Structural pilasters at corners and intermediate bays
        "fill 111 36 -320 111 45 -320 chiseled_deepslate",
        "fill 123 36 -320 123 45 -320 chiseled_deepslate",
        "fill 111 36 -308 111 45 -308 chiseled_deepslate",
        "fill 123 36 -308 123 45 -308 chiseled_deepslate",
        "fill 111 36 -314 111 45 -314 chiseled_deepslate",
        "fill 123 36 -314 123 45 -314 chiseled_deepslate",
        "fill 117 36 -320 117 45 -320 chiseled_deepslate",
        # Northern connecting passage into Hyperloop Terminal concourse at Z: -307
        "fill 116 38 -307 118 42 -307 air",
        "fill 116 37 -307 118 37 -307 polished_blackstone",
        "setblock 115 38 -307 chiseled_deepslate",
        "setblock 115 39 -307 chiseled_deepslate",
        "setblock 115 40 -307 chiseled_deepslate",
        "setblock 115 41 -307 chiseled_deepslate",
        "setblock 115 42 -307 chiseled_deepslate",
        "setblock 119 38 -307 chiseled_deepslate",
        "setblock 119 39 -307 chiseled_deepslate",
        "setblock 119 40 -307 chiseled_deepslate",
        "setblock 119 41 -307 chiseled_deepslate",
        "setblock 119 42 -307 chiseled_deepslate",
        "fill 116 43 -307 118 43 -307 polished_deepslate",
    ]
    return cmds

def build_cryo_stasis_floor():
    """Generates frosted blue ice floor, submerged sea lanterns, and soul fire braziers."""
    cmds = [
        "# Cryo-Stasis Chamber Floor (Y: 36..37)",
        # Polished blackstone perimeter border at Y: 37
        "fill 112 37 -319 122 37 -319 polished_blackstone",
        "fill 112 37 -309 122 37 -309 polished_blackstone",
        "fill 112 37 -319 112 37 -309 polished_blackstone",
        "fill 122 37 -319 122 37 -309 polished_blackstone",
        # Packed ice sub-border at Y: 37
        "fill 113 37 -318 121 37 -318 packed_ice",
        "fill 113 37 -310 121 37 -310 packed_ice",
        "fill 113 37 -318 113 37 -310 packed_ice",
        "fill 121 37 -318 121 37 -310 packed_ice",
        # Submerged sea lanterns at Y: 36 beneath central ice sheet
        "setblock 115 36 -316 sea_lantern",
        "setblock 119 36 -316 sea_lantern",
        "setblock 117 36 -314 sea_lantern",
        "setblock 115 36 -312 sea_lantern",
        "setblock 119 36 -312 sea_lantern",
        "setblock 117 36 -317 sea_lantern",
        "setblock 117 36 -311 sea_lantern",
        "setblock 114 36 -314 sea_lantern",
        "setblock 120 36 -314 sea_lantern",
        # Frosted blue ice main floor at Y: 37
        "fill 114 37 -317 120 37 -311 blue_ice",
        # Soul fire cryogenic braziers in the four corners
        # Northwest brazier (X: 113, Z: -318)
        "setblock 113 37 -318 soul_soil",
        "setblock 113 38 -318 soul_fire",
        "setblock 112 38 -318 iron_bars",
        "setblock 114 38 -318 iron_bars",
        "setblock 113 38 -319 iron_bars",
        "setblock 113 38 -317 iron_bars",
        "setblock 113 39 -318 iron_trapdoor[half=top]",
        # Northeast brazier (X: 121, Z: -318)
        "setblock 121 37 -318 soul_soil",
        "setblock 121 38 -318 soul_fire",
        "setblock 120 38 -318 iron_bars",
        "setblock 122 38 -318 iron_bars",
        "setblock 121 38 -319 iron_bars",
        "setblock 121 38 -317 iron_bars",
        "setblock 121 39 -318 iron_trapdoor[half=top]",
        # Southwest brazier (X: 113, Z: -310)
        "setblock 113 37 -310 soul_soil",
        "setblock 113 38 -310 soul_fire",
        "setblock 112 38 -310 iron_bars",
        "setblock 114 38 -310 iron_bars",
        "setblock 113 38 -311 iron_bars",
        "setblock 113 38 -309 iron_bars",
        "setblock 113 39 -310 iron_trapdoor[half=top]",
        # Southeast brazier (X: 121, Z: -310)
        "setblock 121 37 -310 soul_soil",
        "setblock 121 38 -310 soul_fire",
        "setblock 120 38 -310 iron_bars",
        "setblock 122 38 -310 iron_bars",
        "setblock 121 38 -311 iron_bars",
        "setblock 121 38 -309 iron_bars",
        "setblock 121 39 -310 iron_trapdoor[half=top]",
        # Perimeter iron bar security screens at Y: 38..39 along outer walls
        "fill 112 38 -316 112 39 -315 iron_bars",
        "fill 112 38 -313 112 39 -312 iron_bars",
        "fill 122 38 -316 122 39 -315 iron_bars",
        "fill 122 38 -313 122 39 -312 iron_bars",
        "fill 115 38 -319 116 39 -319 iron_bars",
        "fill 118 38 -319 119 39 -319 iron_bars",
    ]
    return cmds

def build_relic_containment_pods():
    """Generates central cryogenic exhibition pedestals and reinforced containment pods."""
    cmds = [
        "# Ancient Relic Containment Pods",
        # Pod 1: Northwest Pod displaying Heavy Core (X: 115, Z: -316)
        "setblock 115 37 -316 sea_lantern",
        "setblock 115 38 -316 crying_obsidian",
        "setblock 115 39 -316 heavy_core",
        "setblock 114 39 -316 tinted_glass",
        "setblock 116 39 -316 tinted_glass",
        "setblock 115 39 -317 tinted_glass",
        "setblock 115 39 -315 tinted_glass",
        "setblock 114 40 -316 tinted_glass",
        "setblock 116 40 -316 tinted_glass",
        "setblock 115 40 -317 tinted_glass",
        "setblock 115 40 -315 tinted_glass",
        "setblock 115 40 -316 air",
        "setblock 115 41 -316 polished_deepslate_slab[type=top]",

        # Pod 2: Northeast Pod displaying Dragon Head (X: 119, Z: -316)
        "setblock 119 37 -316 sea_lantern",
        "setblock 119 38 -316 crying_obsidian",
        "setblock 119 39 -316 dragon_head[rotation=8]",
        "setblock 118 39 -316 tinted_glass",
        "setblock 120 39 -316 tinted_glass",
        "setblock 119 39 -317 tinted_glass",
        "setblock 119 39 -315 tinted_glass",
        "setblock 118 40 -316 tinted_glass",
        "setblock 120 40 -316 tinted_glass",
        "setblock 119 40 -317 tinted_glass",
        "setblock 119 40 -315 tinted_glass",
        "setblock 119 40 -316 air",
        "setblock 119 41 -316 polished_deepslate_slab[type=top]",

        # Pod 3: Southwest Pod displaying Ominous Vault (X: 115, Z: -312)
        "setblock 115 37 -312 sea_lantern",
        "setblock 115 38 -312 crying_obsidian",
        "setblock 115 39 -312 vault[ominous=true]",
        "setblock 114 39 -312 tinted_glass",
        "setblock 116 39 -312 tinted_glass",
        "setblock 115 39 -313 tinted_glass",
        "setblock 115 39 -311 tinted_glass",
        "setblock 114 40 -312 tinted_glass",
        "setblock 116 40 -312 tinted_glass",
        "setblock 115 40 -313 tinted_glass",
        "setblock 115 40 -311 tinted_glass",
        "setblock 115 40 -312 air",
        "setblock 115 41 -312 polished_deepslate_slab[type=top]",

        # Pod 4: Southeast Pod displaying Sniffer Egg (X: 119, Z: -312)
        "setblock 119 37 -312 sea_lantern",
        "setblock 119 38 -312 crying_obsidian",
        "setblock 119 39 -312 sniffer_egg[hatch=0]",
        "setblock 118 39 -312 tinted_glass",
        "setblock 120 39 -312 tinted_glass",
        "setblock 119 39 -313 tinted_glass",
        "setblock 119 39 -311 tinted_glass",
        "setblock 118 40 -312 tinted_glass",
        "setblock 120 40 -312 tinted_glass",
        "setblock 119 40 -313 tinted_glass",
        "setblock 119 40 -311 tinted_glass",
        "setblock 119 40 -312 air",
        "setblock 119 41 -312 polished_deepslate_slab[type=top]",

        # Pod 5: Center Apex Pod displaying Ominous Trial Spawner (X: 117, Z: -314)
        "setblock 117 37 -314 sea_lantern",
        "setblock 117 38 -314 crying_obsidian",
        "setblock 117 39 -314 trial_spawner[ominous=true]",
        "setblock 116 39 -314 tinted_glass",
        "setblock 118 39 -314 tinted_glass",
        "setblock 117 39 -315 tinted_glass",
        "setblock 117 39 -313 tinted_glass",
        "setblock 116 40 -314 tinted_glass",
        "setblock 118 40 -314 tinted_glass",
        "setblock 117 40 -315 tinted_glass",
        "setblock 117 40 -313 tinted_glass",
        "setblock 117 40 -314 air",
        "setblock 117 41 -314 copper_bulb[lit=true,powered=false]",
    ]
    return cmds

def build_security_portcullis():
    """Generates armored double iron bar portcullis, sculk trigger, and status lamps."""
    cmds = [
        "# Armored Security Portcullis at Z: -308",
        # Archway frame at Z: -308 (X: 115..119, Y: 38..42)
        "fill 115 38 -308 115 42 -308 chiseled_deepslate",
        "fill 119 38 -308 119 42 -308 chiseled_deepslate",
        "fill 116 42 -308 118 42 -308 polished_deepslate",
        # Double layer iron bar portcullis lattice (Z: -308 and Z: -309)
        "fill 116 38 -308 118 41 -308 iron_bars",
        "fill 116 38 -309 118 41 -309 iron_bars",
        # Calibrated sculk sensor access trigger console on West plinth
        "setblock 115 37 -308 amethyst_block",
        "setblock 115 38 -308 calibrated_sculk_sensor[facing=south]",
        # Portcullis status lamps on frame pillars
        "setblock 115 41 -308 copper_bulb[lit=true,powered=false]",
        "setblock 119 41 -308 copper_bulb[lit=true,powered=false]",
        # Security appraisal workstations flanking the entrance inside the vault (Z: -309)
        "setblock 114 38 -309 chiseled_bookshelf[facing=north]",
        "setblock 114 39 -309 lectern[facing=north]",
        "setblock 120 38 -309 chiseled_bookshelf[facing=north]",
        "setblock 120 39 -309 stonecutter[facing=north]",
        # Security status lamp indicators on inside jambs
        "setblock 115 41 -309 copper_bulb[lit=true,powered=false]",
        "setblock 119 41 -309 copper_bulb[lit=true,powered=false]",
    ]
    return cmds

def build_vaulted_ceiling_and_cooling_ducts():
    """Generates vaulted ceiling, copper grate ventilation shafts, hanging lanterns, and end rods."""
    cmds = [
        "# Vaulted Ceiling and Cryogenic Cooling Ducts at Y: 45",
        # Coffered perimeter and ribs
        "fill 111 45 -320 123 45 -320 polished_deepslate",
        "fill 111 45 -308 123 45 -308 polished_deepslate",
        "fill 111 45 -320 111 45 -308 polished_deepslate",
        "fill 123 45 -320 123 45 -308 polished_deepslate",
        "fill 111 45 -314 123 45 -314 polished_deepslate",
        "fill 117 45 -320 117 45 -308 polished_deepslate",
        # Exposed copper grate ventilation duct running North-South along X: 117 at Y: 45
        "fill 117 45 -319 117 45 -309 copper_grate",
        # Exposed copper grate ventilation duct running East-West along Z: -314 at Y: 45
        "fill 113 45 -314 121 45 -314 copper_grate",
        # End rods providing cryogenic illumination at Y: 44
        "setblock 115 44 -314 end_rod[facing=down]",
        "setblock 119 44 -314 end_rod[facing=down]",
        "setblock 117 44 -316 end_rod[facing=down]",
        "setblock 117 44 -312 end_rod[facing=down]",
        # Hanging soul lanterns suspended from iron chains
        "setblock 114 44 -317 iron_chain[axis=y]",
        "setblock 114 43 -317 soul_lantern[hanging=true]",
        "setblock 120 44 -317 iron_chain[axis=y]",
        "setblock 120 43 -317 soul_lantern[hanging=true]",
        "setblock 114 44 -311 iron_chain[axis=y]",
        "setblock 114 43 -311 soul_lantern[hanging=true]",
        "setblock 120 44 -311 iron_chain[axis=y]",
        "setblock 120 43 -311 soul_lantern[hanging=true]",
        # Central apex lighting cluster
        "setblock 116 45 -315 sea_lantern",
        "setblock 118 45 -315 sea_lantern",
        "setblock 116 45 -313 sea_lantern",
        "setblock 118 45 -313 sea_lantern",
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
    """Verifies live blockstates of constructed Sector 16 facilities via RCON."""
    checks = [
        # Relic containment pods
        ("Relic Heavy Core (NW Pod)", "execute if block 115 39 -316 heavy_core"),
        ("Relic Dragon Head (NE Pod)", "execute if block 119 39 -316 dragon_head[rotation=8]"),
        ("Relic Ominous Vault (SW Pod)", "execute if block 115 39 -312 vault[ominous=true]"),
        ("Relic Sniffer Egg (SE Pod)", "execute if block 119 39 -312 sniffer_egg[hatch=0]"),
        ("Relic Ominous Spawner (Center Pod)", "execute if block 117 39 -314 trial_spawner[ominous=true]"),
        ("NW Pod Tinted Glass Enclosure", "execute if block 114 39 -316 tinted_glass"),
        ("NE Pod Tinted Glass Enclosure", "execute if block 120 39 -316 tinted_glass"),
        ("SW Pod Tinted Glass Enclosure", "execute if block 114 39 -312 tinted_glass"),
        ("SE Pod Tinted Glass Enclosure", "execute if block 120 39 -312 tinted_glass"),
        ("Center Pod Tinted Glass Enclosure", "execute if block 116 39 -314 tinted_glass"),
        ("Center Pod Apex Status Lamp", "execute if block 117 41 -314 copper_bulb[lit=true,powered=false]"),

        # Cryo-Stasis floor and ambient lighting
        ("Frosted Blue Ice Main Floor", "execute if block 117 37 -313 blue_ice"),
        ("Packed Ice Sub-Border", "execute if block 113 37 -314 packed_ice"),
        ("Polished Blackstone Floor Perimeter", "execute if block 112 37 -314 polished_blackstone"),
        ("Submerged Floor Sea Lantern (Center)", "execute if block 117 36 -314 sea_lantern"),
        ("Submerged Floor Sea Lantern (NW)", "execute if block 115 36 -316 sea_lantern"),
        ("Submerged Floor Sea Lantern (SE)", "execute if block 119 36 -312 sea_lantern"),
        ("NW Soul Fire Brazier", "execute if block 113 38 -318 soul_fire"),
        ("NE Soul Fire Brazier", "execute if block 121 38 -318 soul_fire"),
        ("SW Soul Fire Brazier", "execute if block 113 38 -310 soul_fire"),
        ("SE Soul Fire Brazier", "execute if block 121 38 -310 soul_fire"),

        # Armored Security Portcullis and Triggers
        ("Portcullis Iron Bars (Outer)", "execute if block 117 39 -308 iron_bars"),
        ("Portcullis Iron Bars (Inner)", "execute if block 117 39 -309 iron_bars"),
        ("Calibrated Sculk Sensor Trigger", "execute if block 115 38 -308 calibrated_sculk_sensor[facing=south]"),
        ("Sculk Sensor Amethyst Resonance Base", "execute if block 115 37 -308 amethyst_block"),
        ("Portcullis West Copper Bulb", "execute if block 115 41 -308 copper_bulb[lit=true,powered=false]"),
        ("Portcullis East Copper Bulb", "execute if block 119 41 -308 copper_bulb[lit=true,powered=false]"),

        # Vaulted Ceiling and Cooling Ducts
        ("North-South Copper Grate Duct", "execute if block 117 45 -315 copper_grate"),
        ("East-West Copper Grate Duct", "execute if block 115 45 -314 copper_grate"),
        ("Cryogenic End Rod Light", "execute if block 115 44 -314 end_rod[facing=down]"),
        ("Hanging Soul Lantern", "execute if block 114 43 -317 soul_lantern[hanging=true]"),
        ("Ceiling Deepslate Tile Vault", "execute if block 114 45 -318 deepslate_tiles"),
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
    commands.extend(build_cryo_stasis_floor())
    commands.extend(build_relic_containment_pods())
    commands.extend(build_security_portcullis())
    commands.extend(build_vaulted_ceiling_and_cooling_ducts())

    print(f"Generated {len(commands)} commands.")
    write_mcfunction(FUNCTION_PATH, commands)
    print(f"Wrote native mcfunction to {FUNCTION_PATH}.")

    print("Deploying datapack file to production server...")
    deploy_datapack_file()

    print("Executing batch construction over RCON...")
    execute_remote_batch([c for c in commands if not c.startswith("#")])

    print("Pausing briefly for block ticks and ambient lighting stabilization...")
    time.sleep(2)

    print("Verifying live blockstates...")
    verify_live_blockstates()
    print("Sector 16 Cryo-Vault and Ancient Relic Conservatory complete.")
