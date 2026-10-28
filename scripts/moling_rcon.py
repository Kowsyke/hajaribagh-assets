#!/usr/bin/env python3
"""MoLing Minecraft RCON Command Bridge.

Implements the MoLing toolset (fill, setblock, clone, summon, execute, weather, time, effect)
over a direct RCON socket connection to the Minecraft server.
Works locally or via SSH tunneling to the production VM.
"""

import argparse
import os
import socket
import struct
import subprocess
import sys

DEFAULT_HOST = os.environ.get("HZ_HOST", "132.226.135.26")
DEFAULT_USER = os.environ.get("HZ_USER", "ubuntu")
DEFAULT_KEY = os.environ.get("HZ_KEY", os.path.expanduser("~/.ssh/id_ed25519"))

def send_rcon_cmd(command, host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Executes a command via SSH python socket to localhost RCON on the remote server."""
    py_script = f"""
import socket, struct

with open('/home/ubuntu/minecraft-server/server.properties') as f:
    props = dict(line.strip().split('=', 1) for line in f if '=' in line and not line.startswith('#'))

rcon_port = int(props.get('rcon.port', 25575))
rcon_pass = props.get('rcon.password', '')

s = socket.create_connection(('127.0.0.1', rcon_port), timeout=5)
# Authenticate
s.sendall(struct.pack('<iii', len(rcon_pass) + 10, 1, 3) + rcon_pass.encode('utf-8') + b'\\x00\\x00')
s.recv(4096)

# Send Command
cmd = {repr(command)}
s.sendall(struct.pack('<iii', len(cmd) + 10, 2, 2) + cmd.encode('utf-8') + b'\\x00\\x00')
resp = s.recv(4096)
s.close()

if len(resp) >= 12:
    print(resp[12:-2].decode('utf-8', errors='ignore'))
"""
    ssh_cmd = [
        "ssh", "-o", "StrictHostKeyChecking=no",
        "-i", key,
        f"{user}@{host}",
        f"python3 -c {subprocess.list2cmdline([py_script])}"
    ]
    res = subprocess.run(ssh_cmd, capture_output=True, text=True)
    if res.returncode != 0:
        return f"Error executing RCON: {res.stderr.strip()}"
    return res.stdout.strip()

def tool_fill(x1, y1, z1, x2, y2, z2, block, mode=None):
    mode_str = f" {mode}" if mode else ""
    return send_rcon_cmd(f"fill {x1} {y1} {z1} {x2} {y2} {z2} {block}{mode_str}")

def tool_setblock(x, y, z, block, mode=None):
    mode_str = f" {mode}" if mode else ""
    return send_rcon_cmd(f"setblock {x} {y} {z} {block}{mode_str}")

def tool_clone(x1, y1, z1, x2, y2, z2, x, y, z, mask_mode=None, clone_mode=None, filter_block=None):
    cmd = f"clone {x1} {y1} {z1} {x2} {y2} {z2} {x} {y} {z}"
    if mask_mode:
        cmd += f" {mask_mode}"
        if clone_mode:
            cmd += f" {clone_mode}"
            if filter_block and mask_mode == "filtered":
                cmd += f" {filter_block}"
    return send_rcon_cmd(cmd)

def tool_summon(entity, x, y, z, nbt=None):
    nbt_str = f" {nbt}" if nbt else ""
    return send_rcon_cmd(f"summon {entity} {x} {y} {z}{nbt_str}")

def tool_execute(subcommands):
    return send_rcon_cmd(f"execute {subcommands}")

def tool_time(subcommand, value=None):
    val_str = f" {value}" if value else ""
    return send_rcon_cmd(f"time {subcommand}{val_str}")

def tool_weather(weather_type, duration=None):
    dur_str = f" {duration}" if duration else ""
    return send_rcon_cmd(f"weather {weather_type}{dur_str}")

def main():
    parser = argparse.ArgumentParser(description="MoLing RCON Minecraft Tool Bridge")
    subparsers = parser.add_subparsers(dest="action", required=True)

    # setblock
    p_sb = subparsers.add_parser("setblock")
    p_sb.add_argument("x")
    p_sb.add_argument("y")
    p_sb.add_argument("z")
    p_sb.add_argument("block")
    p_sb.add_argument("--mode", default=None, choices=["replace", "destroy", "keep"])

    # fill
    p_fl = subparsers.add_parser("fill")
    p_fl.add_argument("x1")
    p_fl.add_argument("y1")
    p_fl.add_argument("z1")
    p_fl.add_argument("x2")
    p_fl.add_argument("y2")
    p_fl.add_argument("z2")
    p_fl.add_argument("block")
    p_fl.add_argument("--mode", default=None, choices=["replace", "destroy", "keep", "hollow", "outline"])

    # clone
    p_cl = subparsers.add_parser("clone")
    p_cl.add_argument("x1")
    p_cl.add_argument("y1")
    p_cl.add_argument("z1")
    p_cl.add_argument("x2")
    p_cl.add_argument("y2")
    p_cl.add_argument("z2")
    p_cl.add_argument("x")
    p_cl.add_argument("y")
    p_cl.add_argument("z")
    p_cl.add_argument("--mask", default=None, choices=["replace", "masked", "filtered"])
    p_cl.add_argument("--clone", default=None, choices=["normal", "force", "move"])
    p_cl.add_argument("--filter-block", default=None)

    # summon
    p_sm = subparsers.add_parser("summon")
    p_sm.add_argument("entity")
    p_sm.add_argument("x")
    p_sm.add_argument("y")
    p_sm.add_argument("z")
    p_sm.add_argument("--nbt", default=None)

    # execute
    p_ex = subparsers.add_parser("execute")
    p_ex.add_argument("subcommands")

    # raw
    p_rw = subparsers.add_parser("raw")
    p_rw.add_argument("command")

    args = parser.parse_args()

    if args.action == "setblock":
        print(tool_setblock(args.x, args.y, args.z, args.block, args.mode))
    elif args.action == "fill":
        print(tool_fill(args.x1, args.y1, args.z1, args.x2, args.y2, args.z2, args.block, args.mode))
    elif args.action == "clone":
        print(tool_clone(args.x1, args.y1, args.z1, args.x2, args.y2, args.z2, args.x, args.y, args.z, args.mask, args.clone, args.filter_block))
    elif args.action == "summon":
        print(tool_summon(args.entity, args.x, args.y, args.z, args.nbt))
    elif args.action == "execute":
        print(tool_execute(args.subcommands))
    elif args.action == "raw":
        print(send_rcon_cmd(args.command))

if __name__ == "__main__":
    main()
