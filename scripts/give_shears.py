import sys
import socket
import struct

def run_rcon(command):
    try:
        with open('/home/ubuntu/minecraft-server/server.properties') as f:
            pw = ''
            for line in f:
                if line.startswith('rcon.password='):
                    pw = line.strip().split('=', 1)[1]
                    break
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect(('127.0.0.1', 25575))
        p = pw.encode('utf-8')
        s.sendall(struct.pack('<iii', len(p) + 10, 1, 3) + p + b'\x00\x00')
        s.recv(4096)
        c = command.encode('utf-8')
        s.sendall(struct.pack('<iii', len(c) + 10, 2, 2) + c + b'\x00\x00')
        resp = s.recv(4096)
        s.close()
        if len(resp) >= 12:
            return resp[12:-2].decode('utf-8', errors='ignore')
    except Exception as e:
        return f'Error: {e}'
    return ''

if len(sys.argv) < 2:
    print('Usage: python3 give_shears.py <player_name>')
    sys.exit(1)

player = sys.argv[1]
cmd = f'execute as {player} at {player} run function server_guide:give_shears'
res = run_rcon(cmd)
print(f'Royal Shears granted to {player}: {res}')
