#!/usr/bin/env python3
"""Build Sector 18 The Sovereign Trial Chambers and Royal Combat Proving Grounds.

Constructs Tier 2 Combat Proving Grounds at X: 120..138, Z: -276..-262, Y: 46..53.
Includes:
1. Structural shell of deepslate bricks, polished tuff, and reinforced deepslate with pilasters every 3 blocks.
2. Coffered barrel vault ceiling arching from Y: 49 to apex at Y: 53 with lit copper bulbs and hanging lanterns.
3. West Portal into South Boulevard (X: 119..120, Z: -270..-268) with polished blackstone stairs and banner valances.
4. North Breezeway into Sector 6 Modern Housing (Z: -276..-277, X: 128..130).
5. Central Sparring Ring (7x7 raised platform at X: 126..132, Z: -272..-266) with blackstone borders, waxed copper grates, and lit redstone lamps.
6. Archery Range with 3 target lanes, target blocks, indicator redstone lamps, and gold pressure plates.
7. Vanguard Weapon Storage with stocked chests, barrels, and smithing workstations.
8. Gilded blackstone weapon pedestals displaying heavy core, ominous vault, and ominous trial spawner relics.
9. Elevated Spectator Mezzanine at Z: -275..-274, Y: 48 with iron bar railings.
"""

import math
import os
import subprocess
import sys
import time

DEFAULT_HOST = os.environ.get("HZ_HOST", "132.226.135.26")
DEFAULT_USER = os.environ.get("HZ_USER", "ubuntu")
DEFAULT_KEY = os.environ.get("HZ_KEY", os.path.expanduser("~/.ssh/id_ed25519"))

FUNCTION_PATH = "datapacks/underground_citadel/data/citadel/function/bunker_proving_grounds.mcfunction"

def write_mcfunction(filepath, lines):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    clean_lines = [line.strip() for line in lines if line.strip()]
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(clean_lines) + "\n")
    return clean_lines

def build_perimeter_and_shell():
    """Generates structural excavation, walls, floor, and structural pilasters."""
    cmds = [
        "# Sector 18 Perimeter and Structural Shell (X: 120..138, Z: -276..-262, Y: 46..53)",
        # Excavation of interior chamber volume from Y: 46 to Y: 53
        "fill 120 46 -276 138 53 -262 air",
        # Subfloor foundation layer at Y: 45
        "fill 120 45 -276 138 45 -262 polished_blackstone",
        # Arena floor at Y: 46
        "fill 121 46 -275 137 46 -263 polished_tuff",
        "fill 123 46 -273 135 46 -265 deepslate_tiles",
        # Enclosing perimeter walls (Y: 46..53)
        # West wall at X: 120
        "fill 120 46 -276 120 53 -262 deepslate_bricks",
        "fill 120 46 -276 120 49 -262 reinforced_deepslate",
        # East wall at X: 138
        "fill 138 46 -276 138 53 -262 deepslate_bricks",
        "fill 138 46 -276 138 49 -262 reinforced_deepslate",
        # North wall at Z: -276
        "fill 120 46 -276 138 53 -276 deepslate_bricks",
        "fill 120 46 -276 138 49 -276 reinforced_deepslate",
        # South wall at Z: -262
        "fill 120 46 -262 138 53 -262 deepslate_bricks",
        "fill 120 46 -262 138 49 -262 reinforced_deepslate",
        # Pilasters every 3 blocks with chiseled blackstone and deepslate tiles
        # North wall pilasters (Z: -276)
        "fill 120 46 -276 120 48 -276 chiseled_polished_blackstone",
        "fill 120 49 -276 120 52 -276 deepslate_tiles",
        "fill 123 46 -276 123 48 -276 chiseled_polished_blackstone",
        "fill 123 49 -276 123 52 -276 deepslate_tiles",
        "fill 127 46 -276 127 48 -276 chiseled_polished_blackstone",
        "fill 127 49 -276 127 52 -276 deepslate_tiles",
        "fill 131 46 -276 131 48 -276 chiseled_polished_blackstone",
        "fill 131 49 -276 131 52 -276 deepslate_tiles",
        "fill 135 46 -276 135 48 -276 chiseled_polished_blackstone",
        "fill 135 49 -276 135 52 -276 deepslate_tiles",
        "fill 138 46 -276 138 48 -276 chiseled_polished_blackstone",
        "fill 138 49 -276 138 52 -276 deepslate_tiles",
        # South wall pilasters (Z: -262)
        "fill 120 46 -262 120 48 -262 chiseled_polished_blackstone",
        "fill 120 49 -262 120 52 -262 deepslate_tiles",
        "fill 123 46 -262 123 48 -262 chiseled_polished_blackstone",
        "fill 123 49 -262 123 52 -262 deepslate_tiles",
        "fill 127 46 -262 127 48 -262 chiseled_polished_blackstone",
        "fill 127 49 -262 127 52 -262 deepslate_tiles",
        "fill 131 46 -262 131 48 -262 chiseled_polished_blackstone",
        "fill 131 49 -262 131 52 -262 deepslate_tiles",
        "fill 135 46 -262 135 48 -262 chiseled_polished_blackstone",
        "fill 135 49 -262 135 52 -262 deepslate_tiles",
        "fill 138 46 -262 138 48 -262 chiseled_polished_blackstone",
        "fill 138 49 -262 138 52 -262 deepslate_tiles",
        # West wall pilasters (X: 120)
        "fill 120 46 -273 120 48 -273 chiseled_polished_blackstone",
        "fill 120 49 -273 120 52 -273 deepslate_tiles",
        "fill 120 46 -267 120 48 -267 chiseled_polished_blackstone",
        "fill 120 49 -267 120 52 -267 deepslate_tiles",
        "fill 120 46 -264 120 48 -264 chiseled_polished_blackstone",
        "fill 120 49 -264 120 52 -264 deepslate_tiles",
        # East wall pilasters (X: 138)
        "fill 138 46 -273 138 48 -273 chiseled_polished_blackstone",
        "fill 138 49 -273 138 52 -273 deepslate_tiles",
        "fill 138 46 -269 138 48 -269 chiseled_polished_blackstone",
        "fill 138 49 -269 138 52 -269 deepslate_tiles",
        "fill 138 46 -265 138 48 -265 chiseled_polished_blackstone",
        "fill 138 49 -265 138 52 -265 deepslate_tiles",
    ]
    return cmds

def build_barrel_vault_ceiling():
    """Generates coffered barrel vault arching from Y: 49 to apex at Y: 53."""
    cmds = [
        "# Reinforced Coffered Barrel Vault Ceiling (Y: 49..53)",
        # Springing corbels along West (X: 121) and East (X: 137) at Y: 49
        "fill 121 49 -275 121 49 -263 deepslate_tile_stairs[facing=west,half=top]",
        "fill 137 49 -275 137 49 -263 deepslate_tile_stairs[facing=east,half=top]",
        # Tier 2 vault arch at Y: 50
        "fill 122 50 -275 122 50 -263 deepslate_tile_stairs[facing=west,half=top]",
        "fill 136 50 -275 136 50 -263 deepslate_tile_stairs[facing=east,half=top]",
        # Tier 3 vault arch at Y: 51
        "fill 123 51 -275 123 51 -263 deepslate_tile_stairs[facing=west,half=top]",
        "fill 135 51 -275 135 51 -263 deepslate_tile_stairs[facing=east,half=top]",
        # Tier 4 vault arch at Y: 52
        "fill 124 52 -275 124 52 -263 deepslate_tile_stairs[facing=west,half=top]",
        "fill 134 52 -275 134 52 -263 deepslate_tile_stairs[facing=east,half=top]",
        # Central barrel vault ceiling apex at Y: 53
        "fill 125 53 -275 133 53 -263 deepslate_tiles",
        # Transverse vault ribs at pilaster alignments
        "fill 121 53 -273 137 53 -273 polished_deepslate",
        "fill 121 53 -269 137 53 -269 polished_deepslate",
        "fill 121 53 -265 137 53 -265 polished_deepslate",
        # Vault keystones with lit copper bulbs along apex centerline (X: 129, Y: 53)
        "setblock 129 53 -273 copper_bulb[lit=true,powered=false]",
        "setblock 129 53 -269 copper_bulb[lit=true,powered=false]",
        "setblock 129 53 -265 copper_bulb[lit=true,powered=false]",
        # Secondary keystone lamps
        "setblock 126 53 -269 copper_bulb[lit=true,powered=false]",
        "setblock 132 53 -269 copper_bulb[lit=true,powered=false]",
        # Hanging lanterns on iron chains from transverse ribs
        "setblock 126 52 -269 iron_chain[axis=y]",
        "setblock 126 51 -269 iron_chain[axis=y]",
        "setblock 126 50 -269 soul_lantern[hanging=true]",
        "setblock 132 52 -269 iron_chain[axis=y]",
        "setblock 132 51 -269 iron_chain[axis=y]",
        "setblock 132 50 -269 soul_lantern[hanging=true]",
        "setblock 126 52 -273 iron_chain[axis=y]",
        "setblock 126 51 -273 lantern[hanging=true]",
        "setblock 132 52 -273 iron_chain[axis=y]",
        "setblock 132 51 -273 lantern[hanging=true]",
        "setblock 126 52 -265 iron_chain[axis=y]",
        "setblock 126 51 -265 lantern[hanging=true]",
        "setblock 132 52 -265 iron_chain[axis=y]",
        "setblock 132 51 -265 lantern[hanging=true]",
    ]
    return cmds

def build_doorways_and_portals():
    """Generates West Portal into South Boulevard and North Breezeway into Sector 6."""
    cmds = [
        "# West Portal into South Boulevard (X: 119..120, Z: -270..-268, Y: 46..48)",
        # Clear portal opening
        "fill 119 46 -270 120 48 -268 air",
        # Polished blackstone entrance threshold stairs
        "setblock 119 46 -270 polished_blackstone_stairs[facing=east,half=bottom]",
        "setblock 119 46 -269 polished_blackstone_stairs[facing=east,half=bottom]",
        "setblock 119 46 -268 polished_blackstone_stairs[facing=east,half=bottom]",
        # Archway frame pilasters
        "fill 120 46 -271 120 48 -271 chiseled_polished_blackstone",
        "fill 120 46 -267 120 48 -267 chiseled_polished_blackstone",
        # Portal lintel at Y: 49
        "setblock 120 49 -271 polished_blackstone_stairs[facing=south,half=top]",
        "setblock 120 49 -269 polished_blackstone",
        "setblock 120 49 -267 polished_blackstone_stairs[facing=north,half=top]",
        # Crimson banner valances mounted on inner lintel (Y: 48)
        "setblock 120 48 -270 red_wall_banner[facing=east]",
        "setblock 120 48 -269 red_wall_banner[facing=east]",
        "setblock 120 48 -268 red_wall_banner[facing=east]",
        # Status illumination on portal columns
        "setblock 120 47 -271 copper_bulb[lit=true,powered=false]",
        "setblock 120 47 -267 copper_bulb[lit=true,powered=false]",

        "# North Breezeway into Sector 6 Modern Housing (Z: -276..-277, X: 128..130, Y: 46..48)",
        # Clear tactical corridor connection
        "fill 128 46 -277 130 48 -276 air",
        # Tactical corridor floor
        "fill 128 46 -277 130 46 -276 polished_blackstone",
        # Breezeway frame columns
        "fill 127 46 -276 127 48 -276 chiseled_polished_blackstone",
        "fill 131 46 -276 131 48 -276 chiseled_polished_blackstone",
        # Breezeway lintel at Y: 49
        "fill 128 49 -276 130 49 -276 polished_deepslate",
        # Breezeway status light
        "setblock 129 48 -276 copper_bulb[lit=true,powered=false]",
    ]
    return cmds

def build_central_sparring_ring():
    """Generates raised 7x7 combat platform with waxed copper grates and redstone lamps."""
    cmds = [
        "# Central Sparring Ring (7x7 Raised Platform at X: 126..132, Z: -272..-266)",
        # Subfloor redstone power grid at Y: 45
        "fill 127 45 -271 131 45 -267 redstone_block",
        # Underlying illuminated redstone lamps at Y: 46
        "fill 127 46 -271 131 46 -267 redstone_lamp[lit=true]",
        # Platform raised surface at Y: 47 of waxed copper grates
        "fill 127 47 -271 131 47 -267 waxed_copper_grate",
        # Platform perimeter borders with polished blackstone slabs at Y: 47
        "fill 126 47 -272 132 47 -272 polished_blackstone_slab[type=bottom]",
        "fill 126 47 -266 132 47 -266 polished_blackstone_slab[type=bottom]",
        "fill 126 47 -271 126 47 -267 polished_blackstone_slab[type=bottom]",
        "fill 132 47 -271 132 47 -267 polished_blackstone_slab[type=bottom]",
        # Corner plinths at Y: 46..47
        "setblock 126 46 -272 chiseled_polished_blackstone",
        "setblock 132 46 -272 chiseled_polished_blackstone",
        "setblock 126 46 -266 chiseled_polished_blackstone",
        "setblock 132 46 -266 chiseled_polished_blackstone",
        # Step access stairs on four cardinal entrances at Y: 46
        "setblock 129 46 -273 polished_blackstone_stairs[facing=south,half=bottom]",
        "setblock 129 46 -265 polished_blackstone_stairs[facing=north,half=bottom]",
        "setblock 125 46 -269 polished_blackstone_stairs[facing=east,half=bottom]",
        "setblock 133 46 -269 polished_blackstone_stairs[facing=west,half=bottom]",
        # Combat ring corner bounding torches
        "setblock 126 48 -272 soul_torch",
        "setblock 132 48 -272 soul_torch",
        "setblock 126 48 -266 soul_torch",
        "setblock 132 48 -266 soul_torch",
    ]
    return cmds

def build_archery_range():
    """Generates 3 target lanes with target blocks, lamps, and gold pressure plates."""
    cmds = [
        "# Archery Range (3 Target Lanes along East Wall at X: 136..137)",
        # Lane 1 (Z: -271)
        "setblock 137 47 -271 polished_blackstone",
        "setblock 137 48 -271 target",
        "setblock 137 49 -271 redstone_lamp",
        "setblock 134 46 -271 polished_blackstone",
        "setblock 134 47 -271 light_weighted_pressure_plate[power=0]",
        # Lane 2 (Z: -269)
        "setblock 137 47 -269 polished_blackstone",
        "setblock 137 48 -269 target",
        "setblock 137 49 -269 redstone_lamp",
        "setblock 134 46 -269 polished_blackstone",
        "setblock 134 47 -269 light_weighted_pressure_plate[power=0]",
        # Lane 3 (Z: -267)
        "setblock 137 47 -267 polished_blackstone",
        "setblock 137 48 -267 target",
        "setblock 137 49 -267 redstone_lamp",
        "setblock 134 46 -267 polished_blackstone",
        "setblock 134 47 -267 light_weighted_pressure_plate[power=0]",
        # Lane dividing screens
        "fill 135 47 -270 136 48 -270 iron_bars",
        "fill 135 47 -268 136 48 -268 iron_bars",
        # Archery supplies chest and bow rack
        "setblock 134 47 -272 chest[facing=west]{Items:[{Slot:0b,id:\"minecraft:bow\",count:1},{Slot:1b,id:\"minecraft:crossbow\",count:1},{Slot:2b,id:\"minecraft:arrow\",count:64}]}",
        "setblock 134 47 -266 chest[facing=west]{Items:[{Slot:0b,id:\"minecraft:bow\",count:1},{Slot:1b,id:\"minecraft:spectral_arrow\",count:64},{Slot:2b,id:\"minecraft:arrow\",count:64}]}",
    ]
    return cmds

def build_vanguard_storage_and_pedestals():
    """Generates stocked armory chests, barrels, smithing bench, and weapon pedestals."""
    cmds = [
        "# Vanguard Weapon Storage and Relic Pedestals",
        # Stocked Vanguard Wall Chests along South wall
        "setblock 122 47 -263 chest[facing=north]{Items:[{Slot:0b,id:\"minecraft:mace\",count:1},{Slot:1b,id:\"minecraft:netherite_sword\",count:1,components:{\"minecraft:enchantments\":{levels:{\"minecraft:sharpness\":5}}}},{Slot:2b,id:\"minecraft:crossbow\",count:1},{Slot:3b,id:\"minecraft:tipped_arrow\",count:64,components:{\"minecraft:potion_contents\":{potion:\"minecraft:strong_harming\"}}}]}",
        "setblock 123 47 -263 chest[facing=north]{Items:[{Slot:0b,id:\"minecraft:diamond_sword\",count:1,components:{\"minecraft:enchantments\":{levels:{\"minecraft:sharpness\":5}}}},{Slot:1b,id:\"minecraft:shield\",count:1},{Slot:2b,id:\"minecraft:mace\",count:1}]}",
        # Vanguard Storage Barrels
        "setblock 124 47 -263 barrel[facing=north]{Items:[{Slot:0b,id:\"minecraft:wind_charge\",count:64}]}",
        "setblock 125 47 -263 barrel[facing=north]{Items:[{Slot:0b,id:\"minecraft:firework_rocket\",count:64}]}",
        "setblock 133 47 -263 barrel[facing=north]{Items:[{Slot:0b,id:\"minecraft:golden_apple\",count:16}]}",
        "setblock 134 47 -263 barrel[facing=north]{Items:[{Slot:0b,id:\"minecraft:potion\",count:1,components:{\"minecraft:potion_contents\":{potion:\"minecraft:strong_strength\"}}}]}",
        # Weapon Maintenance Bench at Southwest corner
        "setblock 121 47 -264 anvil[facing=east]",
        "setblock 121 47 -265 grindstone[face=floor,facing=north]",
        "setblock 121 47 -266 smithing_table",
        # Gilded Blackstone Relic Pedestals
        # Pedestal 1: Heavy Core display at West flank (X: 124, Z: -269)
        "setblock 124 46 -269 polished_blackstone",
        "setblock 124 47 -269 gilded_blackstone",
        "setblock 124 48 -269 heavy_core",
        # Pedestal 2: Ominous Vault display at Southeast flank (X: 133, Z: -265)
        "setblock 133 46 -265 polished_blackstone",
        "setblock 133 47 -265 gilded_blackstone",
        "setblock 133 48 -265 vault[ominous=true]",
        # Pedestal 3: Ominous Trial Spawner display at South flank (X: 129, Z: -264)
        "setblock 129 46 -264 polished_blackstone",
        "setblock 129 47 -264 gilded_blackstone",
        "setblock 129 48 -264 trial_spawner[ominous=true]",
    ]
    return cmds

def build_spectator_mezzanine():
    """Generates elevated observation platform at Z: -275..-274, Y: 48 with railings."""
    cmds = [
        "# Spectator Mezzanine (Z: -275..-274, Y: 48)",
        # Mezzanine floor slab at Y: 48
        "fill 122 48 -275 136 48 -274 polished_deepslate",
        # Iron bar safety railings overlooking arena floor at Y: 49
        "fill 122 49 -274 127 49 -274 iron_bars",
        "fill 131 49 -274 136 49 -274 iron_bars",
        # Spectator tiered benches along North wall (Z: -275, Y: 49)
        "setblock 123 49 -275 polished_blackstone_stairs[facing=south,half=bottom]",
        "setblock 124 49 -275 polished_blackstone_stairs[facing=south,half=bottom]",
        "setblock 125 49 -275 polished_blackstone_stairs[facing=south,half=bottom]",
        "setblock 126 49 -275 polished_blackstone_stairs[facing=south,half=bottom]",
        "setblock 132 49 -275 polished_blackstone_stairs[facing=south,half=bottom]",
        "setblock 133 49 -275 polished_blackstone_stairs[facing=south,half=bottom]",
        "setblock 134 49 -275 polished_blackstone_stairs[facing=south,half=bottom]",
        "setblock 135 49 -275 polished_blackstone_stairs[facing=south,half=bottom]",
        # Access stairs at West end (X: 122, Y: 46..48)
        "setblock 122 46 -273 polished_deepslate_stairs[facing=north,half=bottom]",
        "setblock 122 47 -274 polished_deepslate_stairs[facing=north,half=bottom]",
        # Access stairs at East end (X: 136, Y: 46..48)
        "setblock 136 46 -273 polished_deepslate_stairs[facing=north,half=bottom]",
        "setblock 136 47 -274 polished_deepslate_stairs[facing=north,half=bottom]",
        # Mezzanine illumination fixtures
        "setblock 124 50 -275 copper_bulb[lit=true,powered=false]",
        "setblock 134 50 -275 copper_bulb[lit=true,powered=false]",
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
    """Verifies live blockstates of constructed Sector 18 facilities via RCON."""
    checks = [
        # Sparring ring checks
        ("Sparring Ring Center Grate", "execute if block 129 47 -269 waxed_copper_grate"),
        ("Sparring Ring Grate NW", "execute if block 127 47 -271 waxed_copper_grate"),
        ("Sparring Ring Grate NE", "execute if block 131 47 -271 waxed_copper_grate"),
        ("Sparring Ring Grate SW", "execute if block 127 47 -267 waxed_copper_grate"),
        ("Sparring Ring Grate SE", "execute if block 131 47 -267 waxed_copper_grate"),
        ("Sparring Ring Lamp Center", "execute if block 129 46 -269 redstone_lamp[lit=true]"),
        ("Sparring Ring Lamp NW", "execute if block 127 46 -271 redstone_lamp[lit=true]"),
        ("Sparring Ring Lamp SE", "execute if block 131 46 -267 redstone_lamp[lit=true]"),
        ("Sparring Ring North Slab Border", "execute if block 129 47 -272 polished_blackstone_slab[type=bottom]"),
        ("Sparring Ring South Slab Border", "execute if block 129 47 -266 polished_blackstone_slab[type=bottom]"),
        ("Sparring Ring West Slab Border", "execute if block 126 47 -269 polished_blackstone_slab[type=bottom]"),
        ("Sparring Ring East Slab Border", "execute if block 132 47 -269 polished_blackstone_slab[type=bottom]"),
        ("Sparring Ring Corner Plinth", "execute if block 126 46 -272 chiseled_polished_blackstone"),

        # Archery range checks
        ("Archery Target Lane 1", "execute if block 137 48 -271 target"),
        ("Archery Lamp Lane 1", "execute if block 137 49 -271 redstone_lamp"),
        ("Archery Gold Plate Lane 1", "execute if block 134 47 -271 light_weighted_pressure_plate"),
        ("Archery Target Lane 2", "execute if block 137 48 -269 target"),
        ("Archery Lamp Lane 2", "execute if block 137 49 -269 redstone_lamp"),
        ("Archery Gold Plate Lane 2", "execute if block 134 47 -269 light_weighted_pressure_plate"),
        ("Archery Target Lane 3", "execute if block 137 48 -267 target"),
        ("Archery Lamp Lane 3", "execute if block 137 49 -267 redstone_lamp"),
        ("Archery Gold Plate Lane 3", "execute if block 134 47 -267 light_weighted_pressure_plate"),
        ("Archery Divider Screen", "execute if block 135 47 -270 iron_bars"),
        ("Archery Supplies Chest", "execute if block 134 47 -272 chest[facing=west]"),

        # Vanguard storage and weapon pedestal checks
        ("Vanguard Mace Chest", "execute if block 122 47 -263 chest[facing=north]"),
        ("Vanguard Blade Chest", "execute if block 123 47 -263 chest[facing=north]"),
        ("Vanguard Wind Charge Barrel", "execute if block 124 47 -263 barrel[facing=north]"),
        ("Vanguard Golden Apple Barrel", "execute if block 133 47 -263 barrel[facing=north]"),
        ("Weapon Bench Anvil", "execute if block 121 47 -264 anvil[facing=east]"),
        ("Weapon Bench Grindstone", "execute if block 121 47 -265 grindstone[facing=north]"),
        ("Weapon Bench Smithing Table", "execute if block 121 47 -266 smithing_table"),
        ("Relic Plinth West", "execute if block 124 47 -269 gilded_blackstone"),
        ("Relic Heavy Core", "execute if block 124 48 -269 heavy_core"),
        ("Relic Plinth Southeast", "execute if block 133 47 -265 gilded_blackstone"),
        ("Relic Ominous Vault", "execute if block 133 48 -265 vault[ominous=true]"),
        ("Relic Plinth South", "execute if block 129 47 -264 gilded_blackstone"),
        ("Relic Ominous Trial Spawner", "execute if block 129 48 -264 trial_spawner[ominous=true]"),

        # Spectator mezzanine checks
        ("Mezzanine Floor Slab", "execute if block 125 48 -274 polished_deepslate"),
        ("Mezzanine Floor Center", "execute if block 130 48 -275 polished_deepslate"),
        ("Mezzanine Iron Railing West", "execute if block 125 49 -274 iron_bars"),
        ("Mezzanine Iron Railing East", "execute if block 133 49 -274 iron_bars"),
        ("Mezzanine Bench West", "execute if block 124 49 -275 polished_blackstone_stairs[facing=south]"),
        ("Mezzanine Bench East", "execute if block 134 49 -275 polished_blackstone_stairs[facing=south]"),
        ("Mezzanine West Access Stair", "execute if block 122 46 -273 polished_deepslate_stairs[facing=north]"),
        ("Mezzanine East Access Stair", "execute if block 136 46 -273 polished_deepslate_stairs[facing=north]"),

        # Portal and breezeway checks
        ("West Portal Blackstone Step", "execute if block 119 46 -269 polished_blackstone_stairs[facing=east]"),
        ("West Portal Banner North", "execute if block 120 48 -270 red_wall_banner[facing=east]"),
        ("West Portal Banner Center", "execute if block 120 48 -269 red_wall_banner[facing=east]"),
        ("West Portal Banner South", "execute if block 120 48 -268 red_wall_banner[facing=east]"),
        ("West Portal Status Lamp", "execute if block 120 47 -271 copper_bulb[lit=true,powered=false]"),
        ("North Breezeway Corridor Floor", "execute if block 129 46 -276 polished_blackstone"),
        ("North Breezeway Pilaster", "execute if block 127 47 -276 chiseled_polished_blackstone"),
        ("North Breezeway Lintel Lamp", "execute if block 129 48 -276 copper_bulb[lit=true,powered=false]"),

        # Ceiling vault and shell checks
        ("Vault Keystone Center Lamp", "execute if block 129 53 -269 copper_bulb[lit=true,powered=false]"),
        ("Vault Keystone North Lamp", "execute if block 129 53 -273 copper_bulb[lit=true,powered=false]"),
        ("Vault Keystone South Lamp", "execute if block 129 53 -265 copper_bulb[lit=true,powered=false]"),
        ("Hanging Soul Lantern West", "execute if block 126 50 -269 soul_lantern[hanging=true]"),
        ("Hanging Soul Lantern East", "execute if block 132 50 -269 soul_lantern[hanging=true]"),
        ("Reinforced Deepslate West Wall", "execute if block 120 48 -275 reinforced_deepslate"),
        ("Reinforced Deepslate East Wall", "execute if block 138 48 -275 reinforced_deepslate"),
        ("Perimeter Deepslate Brick Wall", "execute if block 130 50 -262 deepslate_bricks"),
        ("Arena Polished Tuff Floor", "execute if block 122 46 -270 polished_tuff"),
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
    commands.extend(build_perimeter_and_shell())
    commands.extend(build_barrel_vault_ceiling())
    commands.extend(build_doorways_and_portals())
    commands.extend(build_central_sparring_ring())
    commands.extend(build_archery_range())
    commands.extend(build_vanguard_storage_and_pedestals())
    commands.extend(build_spectator_mezzanine())

    print(f"Generated {len(commands)} commands.")
    write_mcfunction(FUNCTION_PATH, commands)
    print(f"Wrote native mcfunction to {FUNCTION_PATH}.")

    print("Deploying datapack file to production server...")
    deploy_datapack_file()

    print("Executing batch construction over RCON...")
    execute_remote_batch([c for c in commands if not c.startswith("#")])

    print("Pausing briefly for block ticks and lighting stabilization...")
    time.sleep(2)

    print("Verifying live blockstates...")
    verify_live_blockstates()
    print("Sector 18 The Sovereign Trial Chambers and Combat Proving Grounds complete.")
