#!/usr/bin/env python3
"""Clean Citadel to Dirt Script.

Removes all built structures and excavated volumes below Y <= 53
and fills them with solid dirt.
Preserves player safety, the stair descent, and all structures above Y: 53.
"""

import os
import subprocess
import sys

DEFAULT_HOST = os.environ.get("HZ_HOST", "132.226.135.26")
DEFAULT_USER = os.environ.get("HZ_USER", "ubuntu")
DEFAULT_KEY = os.environ.get("HZ_KEY", os.path.expanduser("~/.ssh/id_ed25519"))

# Volume definitions strictly bounded by Y <= 53
FILL_COMMANDS = [
    # Sector 3: Deep Celestial Portal Nexus Cavity (Y: 35..45)
    "fill 104 35 -304 130 45 -278 dirt",
    
    # Sector 0: Bio Dome Atrium lower volume (Y: 46..53)
    "fill 104 46 -304 130 53 -278 dirt",
    
    # Crossroads Landing in front of player (Z: -307 to -305, Y: 48..53)
    "fill 114 48 -307 120 53 -305 dirt",
    
    # West Conduit from Landing to Forge and Athenaeum (Y: 48..53)
    "fill 80 48 -308 113 53 -305 dirt",
    
    # East Conduit from Landing to Biosphere and Banquet (Y: 48..53)
    "fill 121 48 -308 154 53 -305 dirt",
    
    # Sector 1: Dwarven Forge (Y: 48..53)
    "fill 82 48 -301 99 53 -281 dirt",
    
    # Sector 2: Hydroponics Biosphere (Y: 48..53)
    "fill 136 48 -302 154 53 -280 dirt",
    
    # Sector 4: Grand Subterranean Athenaeum Library (Y: 48..53)
    "fill 80 48 -330 102 53 -306 dirt",
    
    # Sector 5: Sovereign Banquet and Gathering Hall (Y: 48..53)
    "fill 132 48 -330 154 53 -306 dirt",
    
    # Sector 6: Subterranean Hyperloop Transit Hub (Y: 48..53)
    "fill 104 48 -345 130 53 -325 dirt",
    
    # Sector 7: Grand High Parliament of the Republic (Y: 48..53)
    "fill 104 48 -276 130 53 -244 dirt",
    
    # Sector 8: Sovereign Residential Suites (Y: 48..53)
    "fill 92 48 -268 142 53 -231 dirt",
    
    # Connecting Corridor between Parliament and Suites (Y: 48..53)
    "fill 114 48 -244 120 53 -231 dirt",
]

def run_remote_batch(commands, host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Executes a list of RCON commands via a persistent local socket on the remote server."""
    py_code = f"""
import socket, struct

with open('/home/ubuntu/minecraft-server/server.properties') as f:
    props = dict(line.strip().split('=', 1) for line in f if '=' in line and not line.startswith('#'))

rcon_port = int(props.get('rcon.port', 25575))
rcon_pass = props.get('rcon.password', '')

s = socket.create_connection(('127.0.0.1', rcon_port), timeout=10)
# Authenticate
s.sendall(struct.pack('<iii', len(rcon_pass) + 10, 1, 3) + rcon_pass.encode('utf-8') + b'\\x00\\x00')
auth_resp = s.recv(4096)

cmds = {repr(commands)}
for idx, cmd in enumerate(cmds, 1):
    s.sendall(struct.pack('<iii', len(cmd) + 10, idx + 10, 2) + cmd.encode('utf-8') + b'\\x00\\x00')
    resp = s.recv(4096)
    msg = resp[12:-2].decode('utf-8', errors='ignore') if len(resp) >= 12 else ''
    print(f'[{{idx}}/{{len(cmds)}}] {{cmd}} -> {{msg}}')

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
        print(f"Error running remote batch: {res.stderr}", file=sys.stderr)
        sys.exit(res.returncode)
    print(res.stdout)

if __name__ == "__main__":
    print(f"Executing {len(FILL_COMMANDS)} fill-dirt commands bounded to Y <= 53...")
    run_remote_batch(FILL_COMMANDS)
    print("All specified sectors below Y <= 53 successfully filled with dirt.")
