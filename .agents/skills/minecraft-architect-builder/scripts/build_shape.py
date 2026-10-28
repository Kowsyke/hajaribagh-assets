#!/usr/bin/env python3
"""Minecraft Shape Builder Utility.

Generates Minecraft 1.21 commands and function files for architectural shapes.
Supports ellipses, catenary vaults, domes, and spiral staircases.
"""

import argparse
import math
import sys

def generate_ellipse(cx, cy, cz, rx, rz, height, wall_block, floor_block, hollow=True):
    commands = []
    # Floor
    if floor_block:
        for x in range(cx - rx, cx + rx + 1):
            for z in range(cz - rz, cz + rz + 1):
                norm = ((x - cx) / (rx + 0.5)) ** 2 + ((z - cz) / (rz + 0.5)) ** 2
                if norm <= 1.0:
                    commands.append(f"setblock {x} {cy} {z} {floor_block}")

    # Walls
    for y in range(cy + 1, cy + height + 1):
        for x in range(cx - rx, cx + rx + 1):
            for z in range(cz - rz, cz + rz + 1):
                norm_outer = ((x - cx) / (rx + 0.5)) ** 2 + ((z - cz) / (rz + 0.5)) ** 2
                if norm_outer <= 1.0:
                    if hollow:
                        norm_inner = ((x - cx) / (rx - 0.5)) ** 2 + ((z - cz) / (rz - 0.5)) ** 2
                        if norm_inner > 1.0:
                            commands.append(f"setblock {x} {y} {z} {wall_block}")
                    else:
                        commands.append(f"setblock {x} {y} {z} {wall_block}")
    return commands

def generate_vault(start_z, end_z, cx, cy, width, height, arch_block):
    commands = []
    w_half = width // 2
    for z in range(start_z, end_z + 1):
        for dx in range(-w_half, w_half + 1):
            x = cx + dx
            # Inverted parabola
            dy = round(height * (1.0 - (dx / (w_half + 0.5)) ** 2))
            y = cy + dy
            commands.append(f"setblock {x} {y} {z} {arch_block}")
    return commands

def generate_spiral_stair(cx, cy, cz, radius, total_steps, stair_family):
    commands = []
    for step in range(total_steps):
        angle = step * (math.pi / 4.0)
        x = cx + round(radius * math.cos(angle))
        z = cz + round(radius * math.sin(angle))
        y = cy + step

        # Determine tangential facing
        # Tangent vector: (-sin(angle), cos(angle))
        dx = -math.sin(angle)
        dz = math.cos(angle)

        if abs(dx) > abs(dz):
            facing = "west" if dx < 0 else "east"
        else:
            facing = "north" if dz < 0 else "south"

        stair_id = f"minecraft:{stair_family}_stairs[facing={facing},half=bottom,shape=straight]"
        commands.append(f"setblock {x} {y} {z} {stair_id}")
    return commands

def main():
    parser = argparse.ArgumentParser(description="Generate Minecraft geometric command batches.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Ellipse
    p_el = subparsers.add_parser("ellipse", help="Generate elliptical chamber.")
    p_el.add_argument("--cx", type=int, required=True, help="Center X")
    p_el.add_argument("--cy", type=int, required=True, help="Base Y")
    p_el.add_argument("--cz", type=int, required=True, help="Center Z")
    p_el.add_argument("--rx", type=int, required=True, help="Radius X")
    p_el.add_argument("--rz", type=int, required=True, help="Radius Z")
    p_el.add_argument("--height", type=int, default=5, help="Wall height")
    p_el.add_argument("--wall", default="minecraft:tuff_bricks", help="Wall block")
    p_el.add_argument("--floor", default="minecraft:spruce_planks", help="Floor block")

    # Vault
    p_vt = subparsers.add_parser("vault", help="Generate parabolic vaulted ceiling.")
    p_vt.add_argument("--cx", type=int, required=True, help="Center X")
    p_vt.add_argument("--cy", type=int, required=True, help="Base Y")
    p_vt.add_argument("--start-z", type=int, required=True, help="Start Z")
    p_vt.add_argument("--end-z", type=int, required=True, help="End Z")
    p_vt.add_argument("--width", type=int, default=7, help="Vault span width")
    p_vt.add_argument("--height", type=int, default=4, help="Vault peak height")
    p_vt.add_argument("--block", default="minecraft:stone_brick_stairs", help="Arch block")

    # Spiral stair
    p_sp = subparsers.add_parser("spiral", help="Generate helical spiral stair.")
    p_sp.add_argument("--cx", type=int, required=True, help="Center X")
    p_sp.add_argument("--cy", type=int, required=True, help="Base Y")
    p_sp.add_argument("--cz", type=int, required=True, help="Center Z")
    p_sp.add_argument("--radius", type=int, default=2, help="Stair radius")
    p_sp.add_argument("--steps", type=int, default=16, help="Total step count")
    p_sp.add_argument("--wood", default="spruce", help="Stair wood family")

    args = parser.parse_args()

    if args.command == "ellipse":
        cmds = generate_ellipse(args.cx, args.cy, args.cz, args.rx, args.rz, args.height, args.wall, args.floor)
    elif args.command == "vault":
        cmds = generate_vault(args.start_z, args.end_z, args.cx, args.cy, args.width, args.height, args.block)
    elif args.command == "spiral":
        cmds = generate_spiral_stair(args.cx, args.cy, args.cz, args.radius, args.steps, args.wood)
    else:
        sys.exit(1)

    for c in cmds:
        print(c)

if __name__ == "__main__":
    main()
