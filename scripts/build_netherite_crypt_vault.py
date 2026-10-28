#!/usr/bin/env python3
"""Build Sector 12: High Security Netherite Crypt and Royal Treasury Vault.

Constructs Tier 3 Deep Vault for King Abir's bunker at X: 111..123, Z: -234..-215, Y: 36..44
directly south of the Sovereign Banquet Hall dais.
Features include:
1. Subfloor at Y: 36, floor at Y: 37, and strict ceiling vault cap at Y: 44.
2. Reinforced perimeter walls of reinforced deepslate, crying obsidian, and gilded blackstone.
3. Entry airlock with heavy iron vault door, calibrated sculk sensor, and redstone line.
4. Central 3x3 treasure pedestal pyramid of netherite blocks and diamond blocks with a Heavy Core peak.
5. Vault alcoves with gold blocks, emerald blocks, and reinforced chests.
6. Coffered barrel vault with crying obsidian ribs, lit copper bulbs, and hanging soul lanterns.
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

def build_vault_shell():
    """Excavates and constructs the reinforced vault shell within strictly Y: 36..44."""
    cmds = [
        "# Sector 12: High Security Netherite Crypt Vault Shell (X: 111..123, Z: -234..-215, Y: 36..44)",
        # 1. Excavate clear interior vault volume
        "fill 112 37 -233 122 43 -216 air",
        # 2. Heavy reinforced subfloor foundation at Y: 36
        "fill 111 36 -234 123 36 -215 reinforced_deepslate",
        # 3. Main flooring at Y: 37
        "fill 112 37 -233 122 37 -216 polished_blackstone",
        # Decorative perimeter floor border at Y: 37
        "fill 112 37 -233 122 37 -233 crying_obsidian",
        "fill 112 37 -216 122 37 -216 crying_obsidian",
        "fill 112 37 -233 112 37 -216 crying_obsidian",
        "fill 122 37 -233 122 37 -216 crying_obsidian",
        # 4. Strict vault ceiling cap at Y: 44
        "fill 111 44 -234 123 44 -215 reinforced_deepslate",
        # 5. Reinforced perimeter outer walls (Y: 36..44)
        "fill 111 36 -234 123 44 -234 reinforced_deepslate",
        "fill 111 36 -215 123 44 -215 reinforced_deepslate",
        "fill 111 36 -234 111 44 -215 reinforced_deepslate",
        "fill 123 36 -234 123 44 -215 reinforced_deepslate",
        # 6. Inner corner structural pillars
        "fill 112 37 -233 112 43 -233 crying_obsidian",
        "fill 122 37 -233 122 43 -233 crying_obsidian",
        "fill 112 37 -216 112 43 -216 crying_obsidian",
        "fill 122 37 -216 122 43 -216 crying_obsidian",
    ]
    return cmds

def build_entry_airlock():
    """Constructs the heavy iron vault airlock with calibrated sculk sensor trigger line."""
    cmds = [
        "# Vault Entry Airlock and Trigger Line (Connecting from Banquet Hall Dais)",
        # Passage excavation connecting from Banquet Hall south wall (Z: -235)
        "fill 116 37 -235 118 41 -234 air",
        # Airlock floor at Y: 36..37
        "fill 116 36 -235 118 36 -234 reinforced_deepslate",
        "fill 116 37 -235 118 37 -234 polished_blackstone",
        # Airlock ceiling at Y: 42..44
        "fill 116 42 -235 118 42 -234 crying_obsidian",
        "fill 116 43 -235 118 44 -234 reinforced_deepslate",
        # Airlock portal jambs
        "fill 115 37 -235 115 41 -234 crying_obsidian",
        "fill 119 37 -235 119 41 -234 crying_obsidian",
        # Heavy Iron Vault Door at Z = -234
        "setblock 117 37 -234 iron_door[facing=south,half=lower,open=false]",
        "setblock 117 38 -234 iron_door[facing=south,half=upper,open=false]",
        # Heavy security portcullis bars flanking the door
        "fill 116 37 -234 116 39 -234 iron_bars",
        "fill 118 37 -234 118 39 -234 iron_bars",
        # Calibrated Sculk Sensor Security Checkpoint
        "setblock 115 38 -234 calibrated_sculk_sensor[facing=north]",
        "setblock 115 38 -235 amethyst_block",
        # Redstone trigger line linking sculk sensor and door threshold
        "setblock 115 37 -234 redstone_wire",
        "setblock 116 37 -235 redstone_wire",
        "setblock 116 36 -234 redstone_wire",
        # Security Status Indicator Lamps
        "setblock 116 40 -234 copper_bulb[lit=true,powered=false]",
        "setblock 118 40 -234 copper_bulb[lit=true,powered=false]",
        "setblock 117 41 -234 copper_bulb[lit=true,powered=false]",
    ]
    return cmds

def build_vault_ceiling_and_ribs():
    """Constructs coffered barrel vault with crying obsidian ribs and lit keystones."""
    cmds = [
        "# Coffered Barrel Vault and Crying Obsidian Structural Ribs (Y: 41..44)",
    ]

    # Transverse crying obsidian arch ribs along Z: -233, -229, -225, -221, -217
    rib_z_coords = [-233, -229, -225, -221, -217]

    # Coffered Bays between ribs at Y: 43..44
    for i in range(len(rib_z_coords) - 1):
        z_start = rib_z_coords[i] + 1
        z_end = rib_z_coords[i + 1] - 1
        cmds.append(f"# Coffered Bay: Z = {z_start}..{z_end}")
        # Recessed Gilded Blackstone panels at ceiling apex Y: 44
        cmds.append(f"fill 115 44 {z_start} 119 44 {z_end} gilded_blackstone")
        # Inverted arch stairs contouring the vault at Y: 43
        for z in range(z_start, z_end + 1):
            cmds.append(f"setblock 113 43 {z} deepslate_tile_stairs[facing=east,half=top]")
            cmds.append(f"setblock 121 43 {z} deepslate_tile_stairs[facing=west,half=top]")
            cmds.append(f"setblock 114 43 {z} deepslate_tile_stairs[facing=east,half=top]")
            cmds.append(f"setblock 120 43 {z} deepslate_tile_stairs[facing=west,half=top]")

    # Build the structural arch ribs and pilasters
    for rz in rib_z_coords:
        cmds.append(f"# Structural Vault Rib at Z = {rz}")
        # Transverse crying obsidian rib beam at Y: 44
        cmds.append(f"fill 112 44 {rz} 122 44 {rz} crying_obsidian")
        # Supportive Wall Pilasters and Corbels at Y: 41
        # West Wall Pilaster (X: 112)
        cmds.append(f"fill 112 37 {rz} 112 40 {rz} crying_obsidian")
        cmds.append(f"setblock 112 41 {rz} polished_blackstone_stairs[facing=east,half=top]")
        cmds.append(f"setblock 112 42 {rz} polished_blackstone_stairs[facing=east,half=top]")
        cmds.append(f"setblock 113 43 {rz} polished_blackstone_stairs[facing=east,half=top]")
        # East Wall Pilaster (X: 122)
        cmds.append(f"fill 122 37 {rz} 122 40 {rz} crying_obsidian")
        cmds.append(f"setblock 122 41 {rz} polished_blackstone_stairs[facing=west,half=top]")
        cmds.append(f"setblock 122 42 {rz} polished_blackstone_stairs[facing=west,half=top]")
        cmds.append(f"setblock 121 43 {rz} polished_blackstone_stairs[facing=west,half=top]")
        # Keystone Assembly at Center (X: 117)
        cmds.append(f"setblock 117 44 {rz} copper_bulb[lit=true,powered=false]")
        cmds.append(f"setblock 117 43 {rz} iron_chain[axis=y]")
        cmds.append(f"setblock 117 42 {rz} soul_lantern[hanging=true]")

    return cmds

def build_central_treasure_pedestal():
    """Constructs the central 3x3 pyramid of Netherite, Diamond, and the Heavy Core."""
    cmds = [
        "# Central Royal Treasure Pedestal: 3x3 Netherite and Diamond Pyramid",
        # Pedestal moat border at Y: 37
        "fill 115 37 -226 119 37 -222 gilded_blackstone",
        # 4 Corner Altar Lantern Pedestals at Y: 37..38
        "setblock 115 37 -226 crying_obsidian",
        "setblock 115 38 -226 soul_lantern[hanging=false]",
        "setblock 119 37 -226 crying_obsidian",
        "setblock 119 38 -226 soul_lantern[hanging=false]",
        "setblock 115 37 -222 crying_obsidian",
        "setblock 115 38 -222 soul_lantern[hanging=false]",
        "setblock 119 37 -222 crying_obsidian",
        "setblock 119 38 -222 soul_lantern[hanging=false]",
        # Pyramid Tier 1 (3x3 base at Y: 38: Diamond outer ring with Netherite core)
        "fill 116 38 -225 118 38 -223 diamond_block",
        "setblock 117 38 -224 netherite_block",
        # Pyramid Tier 2 (Netherite plinth at Y: 39)
        "setblock 117 39 -224 netherite_block",
        # Pyramid Tier 3 (Heavy Core apex relic at Y: 40)
        "setblock 117 40 -224 heavy_core",
        # Overhead illumination hanging directly above the Heavy Core at Y: 44..42
        "setblock 117 44 -224 copper_bulb[lit=true,powered=false]",
        "setblock 117 43 -224 iron_chain[axis=y]",
        "setblock 117 42 -224 soul_lantern[hanging=true]",
    ]
    return cmds

def build_wall_alcoves():
    """Constructs treasure alcoves with Gold blocks, Emerald blocks, and reinforced chests."""
    cmds = [
        "# Royal Vault Wall Alcoves (Gold, Emerald, Diamond, and Locked Chests)",
        # West Alcove 1: Gold Treasury (Z: -232..-230, Center Z = -231, X: 112)
        "fill 112 37 -232 112 37 -230 gilded_blackstone",
        "fill 112 38 -232 112 38 -230 gold_block",
        "setblock 112 39 -232 gold_block",
        "setblock 112 39 -230 gold_block",
        "setblock 112 39 -231 chest[facing=east]",
        "setblock 112 40 -231 iron_trapdoor[facing=east,half=bottom]",
        "fill 112 41 -232 112 41 -230 crying_obsidian",
        # West Alcove 2: Emerald Treasury (Z: -220..-218, Center Z = -219, X: 112)
        "fill 112 37 -220 112 37 -218 gilded_blackstone",
        "fill 112 38 -220 112 38 -218 emerald_block",
        "setblock 112 39 -220 emerald_block",
        "setblock 112 39 -218 emerald_block",
        "setblock 112 39 -219 chest[facing=east]",
        "setblock 112 40 -219 iron_trapdoor[facing=east,half=bottom]",
        "fill 112 41 -220 112 41 -218 crying_obsidian",
        # East Alcove 1: Netherite Treasury (Z: -232..-230, Center Z = -231, X: 122)
        "fill 122 37 -232 122 37 -230 gilded_blackstone",
        "fill 122 38 -232 122 38 -230 gilded_blackstone",
        "setblock 122 39 -232 netherite_block",
        "setblock 122 39 -230 netherite_block",
        "setblock 122 39 -231 chest[facing=west]",
        "setblock 122 40 -231 iron_trapdoor[facing=west,half=bottom]",
        "fill 122 41 -232 122 41 -230 crying_obsidian",
        # East Alcove 2: Diamond Treasury (Z: -220..-218, Center Z = -219, X: 122)
        "fill 122 37 -220 122 37 -218 gilded_blackstone",
        "fill 122 38 -220 122 38 -218 diamond_block",
        "setblock 122 39 -220 diamond_block",
        "setblock 122 39 -218 diamond_block",
        "setblock 122 39 -219 chest[facing=west]",
        "setblock 122 40 -219 iron_trapdoor[facing=west,half=bottom]",
        "fill 122 41 -220 122 41 -218 crying_obsidian",
        # South Wall Royal Sovereign Plinth (Z = -216, X: 116..118)
        "fill 116 37 -216 118 37 -216 gilded_blackstone",
        "setblock 116 38 -216 gold_block",
        "setblock 118 38 -216 gold_block",
        "setblock 117 38 -216 netherite_block",
        "setblock 117 39 -216 chest[facing=north]",
        "fill 116 41 -216 118 41 -216 crying_obsidian",
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
    """Verifies that all critical Netherite Crypt structures, pedestals, and fixtures exist live on the server."""
    test_blocks = [
        # Vault Shell & Bounds
        ("117 36 -224", "reinforced_deepslate", "Subfloor Foundation at Y: 36"),
        ("117 37 -220", "polished_blackstone", "Main Vault Floor at Y: 37"),
        ("111 40 -224", "reinforced_deepslate", "West Perimeter Reinforced Wall"),
        ("123 40 -224", "reinforced_deepslate", "East Perimeter Reinforced Wall"),
        ("117 40 -215", "reinforced_deepslate", "South Perimeter Reinforced Wall"),
        ("117 44 -215", "reinforced_deepslate", "Ceiling Vault Cap at Y: 44"),

        # Entry Airlock
        ("117 37 -234", "iron_door[facing=south,half=lower]", "Heavy Iron Vault Door Lower Half"),
        ("117 38 -234", "iron_door[facing=south,half=upper]", "Heavy Iron Vault Door Upper Half"),
        ("115 38 -234", "calibrated_sculk_sensor[facing=north]", "Calibrated Sculk Sensor Security Checkpoint"),
        ("115 38 -235", "amethyst_block", "Airlock Sculk Amethyst Calibration Block"),
        ("115 37 -234", "redstone_wire", "Sculk Sensor Redstone Output Line"),
        ("116 40 -234", "copper_bulb[lit=true,powered=false]", "Airlock Security Status Indicator Bulb"),

        # Central Royal Treasure Pedestal
        ("117 40 -224", "heavy_core", "Central Pyramid Apex Heavy Core"),
        ("117 39 -224", "netherite_block", "Central Pyramid Tier 2 Netherite Plinth"),
        ("117 38 -224", "netherite_block", "Central Pyramid Tier 1 Netherite Core"),
        ("116 38 -225", "diamond_block", "Central Pyramid Tier 1 Diamond Outer NW"),
        ("118 38 -223", "diamond_block", "Central Pyramid Tier 1 Diamond Outer SE"),
        ("115 38 -226", "soul_lantern[hanging=false]", "Pedestal NW Corner Altar Soul Lantern"),
        ("119 38 -222", "soul_lantern[hanging=false]", "Pedestal SE Corner Altar Soul Lantern"),
        ("117 44 -224", "copper_bulb[lit=true,powered=false]", "Pedestal Overhead Keystone Copper Bulb"),
        ("117 43 -224", "iron_chain[axis=y]", "Pedestal Overhead Iron Chain"),
        ("117 42 -224", "soul_lantern[hanging=true]", "Pedestal Overhead Hanging Soul Lantern"),

        # Wall Alcoves
        ("112 38 -231", "gold_block", "West Alcove 1 Gold Block Reserve"),
        ("112 39 -231", "chest[facing=east]", "West Alcove 1 Gold Treasury Chest"),
        ("112 38 -219", "emerald_block", "West Alcove 2 Emerald Block Reserve"),
        ("112 39 -219", "chest[facing=east]", "West Alcove 2 Emerald Treasury Chest"),
        ("122 39 -232", "netherite_block", "East Alcove 1 Netherite Ingot Reserve"),
        ("122 39 -231", "chest[facing=west]", "East Alcove 1 Netherite Treasury Chest"),
        ("122 38 -219", "diamond_block", "East Alcove 2 Diamond Gem Reserve"),
        ("122 39 -219", "chest[facing=west]", "East Alcove 2 Diamond Treasury Chest"),

        # Vault Ceiling Ribs and Keystones
        ("117 44 -229", "copper_bulb[lit=true,powered=false]", "Vault Rib Z-229 Keystone Bulb at Y: 44"),
        ("117 43 -229", "iron_chain[axis=y]", "Vault Rib Z-229 Iron Chain at Y: 43"),
        ("117 42 -229", "soul_lantern[hanging=true]", "Vault Rib Z-229 Hanging Soul Lantern at Y: 42"),
        ("114 44 -229", "crying_obsidian", "Vault Rib Z-229 Crying Obsidian Beam"),
        ("112 41 -229", "polished_blackstone_stairs[facing=east,half=top]", "Vault Rib Z-229 West Wall Corbel at Y: 41"),
        ("122 41 -229", "polished_blackstone_stairs[facing=west,half=top]", "Vault Rib Z-229 East Wall Corbel at Y: 41"),
        ("117 44 -221", "copper_bulb[lit=true,powered=false]", "Vault Rib Z-221 Keystone Bulb at Y: 44"),
        ("117 44 -217", "copper_bulb[lit=true,powered=false]", "Vault Rib Z-217 Keystone Bulb at Y: 44"),
        ("117 44 -227", "gilded_blackstone", "Coffered Ceiling Bay Recessed Panel at Y: 44"),
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
    print("Beginning Sector 12 Netherite Crypt Vault construction...")
    all_cmds = []
    all_cmds.extend(build_vault_shell())
    all_cmds.extend(build_entry_airlock())
    all_cmds.extend(build_vault_ceiling_and_ribs())
    all_cmds.extend(build_central_treasure_pedestal())
    all_cmds.extend(build_wall_alcoves())

    # Write local mcfunction file
    write_mcfunction("bunker_crypt_vault.mcfunction", all_cmds)

    # Sync file to remote server datapack
    sync_remote_mcfunction("bunker_crypt_vault.mcfunction")

    # Execute all commands over RCON socket protocol
    print("\nExecuting Sector 12 construction commands via RCON...")
    execute_remote_batch(all_cmds)

    # Verify live blockstates
    success = verify_live_blockstates()
    if success:
        print("\nAll Sector 12 Netherite Crypt structures, pedestals, and security fixtures verified successfully!")
    else:
        print("\nVerification encountered issues. Inspect above logs.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
