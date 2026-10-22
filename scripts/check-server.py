#!/usr/bin/env python3
"""Health check for the Hajaribagh server. Standard library only, read only.

Checks:
  1. Each endpoint answers a Minecraft status ping (the same query the multiplayer menu sends).
  2. The resource pack URL in configs/server.properties downloads without a login
     and its SHA-1 matches resource-pack-sha1 in the same file.

Usage:
  python scripts/check-server.py
  python scripts/check-server.py host:port [host:port ...]

Exit code is 0 when every check passes and 1 otherwise.
"""
import hashlib
import json
import os
import socket
import struct
import sys
import time
import urllib.request

DEFAULT_ENDPOINTS = ["132.226.135.26:25565", "cairo-temptation.tun.ply.gg:47309"]
PROPERTIES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "configs", "server.properties")


def varint(n):
    out = b""
    while True:
        b = n & 0x7F
        n >>= 7
        out += bytes([b | (0x80 if n else 0)])
        if not n:
            return out


def read_varint(sock):
    n = 0
    for i in range(5):
        b = sock.recv(1)
        if not b:
            raise EOFError("connection closed")
        n |= (b[0] & 0x7F) << (7 * i)
        if not b[0] & 0x80:
            return n
    raise ValueError("varint too long")


def ping(host, port, timeout=8):
    start = time.time()
    sock = socket.create_connection((host, port), timeout=timeout)
    connect_ms = int((time.time() - start) * 1000)
    sock.settimeout(timeout)
    host_bytes = host.encode()
    handshake = b"\x00" + varint(770) + varint(len(host_bytes)) + host_bytes + struct.pack(">H", port) + varint(1)
    sock.sendall(varint(len(handshake)) + handshake)
    sock.sendall(varint(1) + b"\x00")
    read_varint(sock)
    read_varint(sock)
    length = read_varint(sock)
    data = b""
    while len(data) < length:
        chunk = sock.recv(length - len(data))
        if not chunk:
            break
        data += chunk
    sock.close()
    return connect_ms, json.loads(data.decode("utf-8", "replace"))


def read_properties(path):
    props = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                props[key] = value.replace("\\:", ":")
    return props


def check_endpoint(target):
    host, port = target.rsplit(":", 1)
    try:
        ms, status = ping(host, int(port))
    except Exception as e:
        print("FAIL  %s  %s: %s" % (target, type(e).__name__, e))
        return False
    players = status.get("players", {})
    version = status.get("version", {}).get("name")
    print("ok    %s  Minecraft %s, %s/%s players, connect %d ms" % (target, version, players.get("online"), players.get("max"), ms))
    return True


def check_pack():
    props = read_properties(PROPERTIES)
    url = props.get("resource-pack", "")
    declared = props.get("resource-pack-sha1", "").lower()
    if not url:
        print("skip  resource pack: no resource-pack URL in server.properties")
        return True
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "hajaribagh-check"}), timeout=60) as r:
            body = r.read()
    except Exception as e:
        print("FAIL  resource pack: %s is not downloadable without a login (%s)" % (url, e))
        return False
    served = hashlib.sha1(body).hexdigest()
    if served != declared:
        print("FAIL  resource pack: served SHA-1 %s but server.properties declares %s" % (served, declared))
        return False
    print("ok    resource pack: %d bytes, SHA-1 matches" % len(body))
    return True


def main():
    targets = sys.argv[1:] or DEFAULT_ENDPOINTS
    results = [check_endpoint(t) for t in targets]
    results.append(check_pack())
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
