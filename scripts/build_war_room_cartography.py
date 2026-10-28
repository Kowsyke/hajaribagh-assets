#!/usr/bin/env python3
"""Build Sector 13 Subterranean War Room and Strategic Cartography Command.

Constructs Tier 2 Strategic Chamber at X: 111..123, Z: -320..-308, Y: 46..53
along the descent corridor between the Treasury landing and the Rotunda.
Features central illuminated tactical briefing map table, periscope optics,
four royal vanguard armor guards, strategic lecterns, perimeter alerts,
and coffered arch vaults with soul lanterns.
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


def build_war_room_commands():
    """Generates commands for the War Room and Strategic Cartography Command."""
    cmds = []
    cmds.append("# Sector 13: Subterranean War Room & Strategic Cartography Command (X: 111..123, Z: -320..-308, Y: 46..53)")

    # Cleanup prior war room entities to guarantee idempotency
    cmds.append("kill @e[tag=war_vanguard_nw]")
    cmds.append("kill @e[tag=war_vanguard_ne]")
    cmds.append("kill @e[tag=war_vanguard_sw]")
    cmds.append("kill @e[tag=war_vanguard_se]")
    cmds.append("kill @e[tag=war_room_entity]")

    # 1. Excavation within strict vertical bounds Y: 46..53
    cmds.append("fill 111 46 -320 123 52 -308 air")

    # 2. Foundation and Flooring at Y: 46
    cmds.append("fill 111 46 -320 123 46 -308 polished_deepslate")
    cmds.append("fill 113 46 -318 121 46 -310 deepslate_tiles")

    # 3. Ceiling cap strictly at Y: 53
    cmds.append("fill 111 53 -320 123 53 -308 deepslate_tiles")

    # 4. Enclosing perimeter walls (Y: 46..52)
    cmds.append("fill 111 46 -320 123 52 -320 deepslate_bricks")
    cmds.append("fill 111 46 -308 123 52 -308 deepslate_bricks")
    cmds.append("fill 111 46 -320 111 52 -308 deepslate_bricks")
    cmds.append("fill 123 46 -320 123 52 -308 deepslate_bricks")

    # Corner structural pilasters
    cmds.append("fill 111 46 -320 111 52 -320 chiseled_deepslate")
    cmds.append("fill 123 46 -320 123 52 -320 chiseled_deepslate")
    cmds.append("fill 111 46 -308 111 52 -308 chiseled_deepslate")
    cmds.append("fill 123 46 -308 123 52 -308 chiseled_deepslate")

    # Doorway openings connecting corridor and Rotunda transition
    # North doorway to Treasury descent corridor (X: 116..118, Y: 47..51, Z: -320)
    cmds.append("fill 116 47 -320 118 51 -320 air")
    # South doorway to Rotunda grand stairs landing (X: 116..118, Y: 47..51, Z: -308)
    cmds.append("fill 116 47 -308 118 51 -308 air")

    # 5. Central Tactical Briefing Table (X: 115..119, Z: -316..-312, Y: 47)
    # Under-table illumination at Y: 46
    cmds.append("fill 115 46 -316 119 46 -312 sea_lantern replace")

    # Dark oak perimeter table framing at Y: 47
    cmds.append("fill 115 47 -316 119 47 -316 dark_oak_stairs[facing=south,half=bottom] replace")
    cmds.append("fill 115 47 -312 119 47 -312 dark_oak_stairs[facing=north,half=bottom] replace")
    cmds.append("fill 115 47 -315 115 47 -313 dark_oak_stairs[facing=east,half=bottom] replace")
    cmds.append("fill 119 47 -315 119 47 -313 dark_oak_stairs[facing=west,half=bottom] replace")
    cmds.append("setblock 115 47 -316 dark_oak_planks replace")
    cmds.append("setblock 119 47 -316 dark_oak_planks replace")
    cmds.append("setblock 115 47 -312 dark_oak_planks replace")
    cmds.append("setblock 119 47 -312 dark_oak_planks replace")

    # Illuminated stained glass cartography map representing Kingdom territory and waters
    cmds.append("setblock 116 47 -315 lime_stained_glass replace")
    cmds.append("setblock 117 47 -315 yellow_stained_glass replace")
    cmds.append("setblock 118 47 -315 lime_stained_glass replace")
    cmds.append("setblock 116 47 -314 light_blue_stained_glass replace")
    cmds.append("setblock 117 47 -314 yellow_stained_glass replace")
    cmds.append("setblock 118 47 -314 light_blue_stained_glass replace")
    cmds.append("setblock 116 47 -313 lime_stained_glass replace")
    cmds.append("setblock 117 47 -313 yellow_stained_glass replace")
    cmds.append("setblock 118 47 -313 lime_stained_glass replace")

    # 6. Periscope Optical Station (X: 121, Z: -317)
    # Pedestal base
    cmds.append("setblock 121 46 -317 chiseled_polished_blackstone replace")
    cmds.append("setblock 121 47 -317 waxed_copper_grate replace")
    cmds.append("setblock 121 48 -317 lightning_rod[facing=up] replace")
    # Reinforced vertical viewing shaft rising up to ceiling
    cmds.append("setblock 121 49 -317 iron_bars replace")
    cmds.append("setblock 121 50 -317 iron_bars replace")
    cmds.append("setblock 121 51 -317 lightning_rod[facing=down] replace")
    cmds.append("setblock 121 52 -317 end_rod[facing=up] replace")
    cmds.append("setblock 121 53 -317 tinted_glass replace")

    # 7. Four Royal Vanguard Armor Stands in full Netherite Armor
    # Guard 1: Northwest corner (X: 114, Z: -317)
    cmds.append("setblock 114 46 -317 gilded_blackstone replace")
    cmds.append(
        "summon armor_stand 114.5 47.0 -316.5 "
        '{Tags:["citadel_decor","war_vanguard_nw"],ShowArms:1b,NoBasePlate:1b,Rotation:[135.0f,0.0f]}'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_nw,limit=1] armor.head with '
        'netherite_helmet[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_nw,limit=1] armor.chest with '
        'netherite_chestplate[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_nw,limit=1] armor.legs with '
        'netherite_leggings[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_nw,limit=1] armor.feet with '
        'netherite_boots[enchantments={"minecraft:protection":4,"minecraft:feather_falling":4}]'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_nw,limit=1] weapon.mainhand with '
        'netherite_sword[enchantments={"minecraft:sharpness":5}]'
    )
    cmds.append('item replace entity @e[tag=war_vanguard_nw,limit=1] weapon.offhand with spyglass')

    # Guard 2: Northeast corner (X: 120, Z: -317)
    cmds.append("setblock 120 46 -317 gilded_blackstone replace")
    cmds.append(
        "summon armor_stand 119.5 47.0 -316.5 "
        '{Tags:["citadel_decor","war_room_entity","war_vanguard_ne"],ShowArms:1b,NoBasePlate:1b,Rotation:[225.0f,0.0f]}'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_ne,limit=1] armor.head with '
        'netherite_helmet[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_ne,limit=1] armor.chest with '
        'netherite_chestplate[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_ne,limit=1] armor.legs with '
        'netherite_leggings[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_ne,limit=1] armor.feet with '
        'netherite_boots[enchantments={"minecraft:protection":4,"minecraft:feather_falling":4}]'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_ne,limit=1] weapon.mainhand with '
        'netherite_sword[enchantments={"minecraft:sharpness":5}]'
    )
    cmds.append('item replace entity @e[tag=war_vanguard_ne,limit=1] weapon.offhand with shield')

    # Guard 3: Southwest corner (X: 114, Z: -311)
    cmds.append("setblock 114 46 -311 gilded_blackstone replace")
    cmds.append(
        "summon armor_stand 114.5 47.0 -311.5 "
        '{Tags:["citadel_decor","war_room_entity","war_vanguard_sw"],ShowArms:1b,NoBasePlate:1b,Rotation:[45.0f,0.0f]}'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_sw,limit=1] armor.head with '
        'netherite_helmet[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_sw,limit=1] armor.chest with '
        'netherite_chestplate[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_sw,limit=1] armor.legs with '
        'netherite_leggings[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_sw,limit=1] armor.feet with '
        'netherite_boots[enchantments={"minecraft:protection":4,"minecraft:feather_falling":4}]'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_sw,limit=1] weapon.mainhand with '
        'netherite_sword[enchantments={"minecraft:sharpness":5}]'
    )
    cmds.append('item replace entity @e[tag=war_vanguard_sw,limit=1] weapon.offhand with shield')

    # Guard 4: Southeast corner (X: 120, Z: -311)
    cmds.append("setblock 120 46 -311 gilded_blackstone replace")
    cmds.append(
        "summon armor_stand 119.5 47.0 -311.5 "
        '{Tags:["citadel_decor","war_room_entity","war_vanguard_se"],ShowArms:1b,NoBasePlate:1b,Rotation:[315.0f,0.0f]}'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_se,limit=1] armor.head with '
        'netherite_helmet[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_se,limit=1] armor.chest with '
        'netherite_chestplate[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_se,limit=1] armor.legs with '
        'netherite_leggings[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_se,limit=1] armor.feet with '
        'netherite_boots[enchantments={"minecraft:protection":4,"minecraft:feather_falling":4}]'
    )
    cmds.append(
        'item replace entity @e[tag=war_vanguard_se,limit=1] weapon.mainhand with '
        'netherite_sword[enchantments={"minecraft:sharpness":5}]'
    )
    cmds.append('item replace entity @e[tag=war_vanguard_se,limit=1] weapon.offhand with shield')

    # 8. Strategic Lecterns with written standing orders books
    # All titles are 32 characters or fewer
    lecterns = [
        (113, 47, -314, "east", "Royal War Directives"),
        (121, 47, -314, "west", "Citadel Defense Plan"),
        (114, 47, -318, "south", "Frontier Cartography"),
        (120, 47, -310, "north", "Bunker Perimeter Alert"),
    ]
    for lx, ly, lz, facing, title in lecterns:
        cmds.append(f"setblock {lx} {ly} {lz} lectern[facing={facing},has_book=true] replace")
        book_nbt = (
            '{id:"minecraft:written_book",count:1,components:'
            '{"minecraft:written_book_content":{author:"King Abir",'
            'title:"' + title + '",pages:["Official military orders of King Abir."]}}}'
        )
        cmds.append(f"data modify block {lx} {ly} {lz} Book set value {book_nbt}")

    # 9. Wall Displays: Perimeter Alert Sensor, Clocks, and Banners
    # Perimeter Alert Sensor on West Wall
    cmds.append("setblock 112 47 -315 chiseled_polished_blackstone replace")
    cmds.append("setblock 112 48 -315 calibrated_sculk_sensor replace")
    cmds.append("setblock 112 47 -314 polished_blackstone replace")
    cmds.append("setblock 112 48 -314 comparator[facing=east] replace")
    cmds.append("setblock 112 47 -313 chiseled_polished_blackstone replace")
    cmds.append("setblock 112 48 -313 redstone_lamp replace")

    # Strategic Command inventory locker
    cmds.append("setblock 113 47 -316 chest[facing=east] replace")
    cmds.append("item replace block 113 47 -316 container.0 with recovery_compass 1")
    cmds.append("item replace block 113 47 -316 container.1 with clock 1")
    cmds.append("item replace block 113 47 -316 container.2 with compass 1")
    cmds.append("item replace block 113 47 -316 container.3 with spyglass 1")
    cmds.append("item replace block 113 47 -316 container.4 with filled_map 1")

    # Kingdom banners
    cmds.append("setblock 112 49 -318 red_wall_banner[facing=east] replace")
    cmds.append("setblock 112 49 -310 red_wall_banner[facing=east] replace")
    cmds.append("setblock 122 49 -318 red_wall_banner[facing=west] replace")
    cmds.append("setblock 122 49 -310 red_wall_banner[facing=west] replace")

    # 10. Ceiling: Coffered Arch Vault with Copper Bulbs and Soul Lanterns
    # Transverse arch ribs at Y: 52
    for z in [-318, -314, -310]:
        cmds.append(f"fill 112 52 {z} 122 52 {z} chiseled_deepslate replace")

    # Copper chain drops and soul lanterns
    lantern_drops = [
        (117, -314),
        (115, -316),
        (119, -316),
        (115, -312),
        (119, -312),
    ]
    for lx, lz in lantern_drops:
        cmds.append(f"setblock {lx} 52 {lz} copper_chain[axis=y] replace")
        cmds.append(f"setblock {lx} 51 {lz} soul_lantern[hanging=true] replace")

    # Lit waxed copper bulbs recessed at Y: 53
    bulb_positions = [
        (117, -318),
        (117, -314),
        (117, -310),
        (113, -314),
        (121, -314),
    ]
    for bx, bz in bulb_positions:
        cmds.append(f"setblock {bx} 53 {bz} waxed_copper_bulb[lit=true,powered=false] replace")

    return cmds


def write_local_mcfunction(cmds):
    """Writes the war room mcfunction file locally."""
    os.makedirs(LOCAL_FUNCTION_DIR, exist_ok=True)
    filepath = os.path.join(LOCAL_FUNCTION_DIR, "bunker_war_room.mcfunction")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(cmds) + "\n")
    print(f"Generated local file: {filepath} ({len(cmds)} commands)")
    return filepath


def sync_mcfunction_to_remote(local_path, host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Copies the mcfunction file to the remote Minecraft server datapack directory."""
    remote_target = f"{REMOTE_FUNCTION_DIR}/bunker_war_room.mcfunction"
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
    """Reloads datapacks and triggers execution of bunker_war_room function."""
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
print('Executing function citadel:bunker_war_room...')
print('Function execution:', run_cmd('function citadel:bunker_war_room'))

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
    """Queries live blockstates and entities to verify Sector 13 War Room."""
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

print('=== Live RCON Verification Audit: Sector 13 War Room ===')

# Table & Map Checks
test_query('Tactical Table Sea Lantern Under-illumination', 'execute if block 117 46 -314 sea_lantern')
test_query('Tactical Table Lime Stained Glass (NW territory)', 'execute if block 116 47 -315 lime_stained_glass')
test_query('Tactical Table Yellow Stained Glass (Road/Capital)', 'execute if block 117 47 -314 yellow_stained_glass')
test_query('Tactical Table Light Blue Stained Glass (River)', 'execute if block 116 47 -314 light_blue_stained_glass')
test_query('Tactical Table Dark Oak Frame North', 'execute if block 117 47 -316 dark_oak_stairs[facing=south]')
test_query('Tactical Table Dark Oak Frame South', 'execute if block 117 47 -312 dark_oak_stairs[facing=north]')

# Periscope Optical Station Checks
test_query('Periscope Copper Grate Base', 'execute if block 121 47 -317 waxed_copper_grate')
test_query('Periscope Lightning Rod Optic', 'execute if block 121 48 -317 lightning_rod[facing=up]')
test_query('Periscope Reinforced Iron Bars Shaft', 'execute if block 121 50 -317 iron_bars')
test_query('Periscope Ceiling Viewing Aperture', 'execute if block 121 53 -317 tinted_glass')

# Vanguard Armor Guards Checks
test_query('Royal Vanguard Guard NW Present', 'execute if entity @e[tag=war_vanguard_nw]')
test_query('Royal Vanguard Guard NE Present', 'execute if entity @e[tag=war_vanguard_ne]')
test_query('Royal Vanguard Guard SW Present', 'execute if entity @e[tag=war_vanguard_sw]')
test_query('Royal Vanguard Guard SE Present', 'execute if entity @e[tag=war_vanguard_se]')

# Strategic Lecterns Checks
test_query('Strategic Lectern West Facing East', 'execute if block 113 47 -314 lectern[facing=east,has_book=true]')
test_query('Strategic Lectern East Facing West', 'execute if block 121 47 -314 lectern[facing=west,has_book=true]')
test_query('Strategic Lectern North Facing South', 'execute if block 114 47 -318 lectern[facing=south,has_book=true]')
test_query('Strategic Lectern South Facing North', 'execute if block 120 47 -310 lectern[facing=north,has_book=true]')

# Wall Displays & Sensors Checks
test_query('Perimeter Alert Sculk Sensor', 'execute if block 112 48 -315 calibrated_sculk_sensor')
test_query('Perimeter Alert Redstone Comparator', 'execute if block 112 48 -314 comparator[facing=east]')
test_query('Perimeter Alert Redstone Lamp', 'execute if block 112 48 -313 redstone_lamp')
test_query('Kingdom Red Wall Banner', 'execute if block 112 49 -318 red_wall_banner[facing=east]')

# Ceiling & Lighting Checks
test_query('Ceiling Arch Vault Rib', 'execute if block 116 52 -314 chiseled_deepslate')
test_query('Ceiling Hanging Soul Lantern', 'execute if block 117 51 -314 soul_lantern[hanging=true]')
test_query('Ceiling Waxed Copper Bulb', 'execute if block 117 53 -314 waxed_copper_bulb[lit=true]')

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
    print("Designing Sector 13 Subterranean War Room and Cartography Command...")
    cmds = build_war_room_commands()
    local_path = write_local_mcfunction(cmds)
    sync_mcfunction_to_remote(local_path)
    execute_via_rcon()
    verify_live_blockstates()
    print("Sector 13 Subterranean War Room and Cartography Command complete.")


if __name__ == "__main__":
    main()
