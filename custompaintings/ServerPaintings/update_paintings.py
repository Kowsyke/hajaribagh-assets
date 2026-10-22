#!/usr/bin/env python3
import os, sys, json, struct

pack_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(pack_dir, "images")
json_path = os.path.join(pack_dir, "custompaintings.json")

def get_png_dimensions(file_path):
    with open(file_path, "rb") as f:
        header = f.read(24)
        if len(header) >= 24 and header[:8] == b"\x89PNG\r\n\x1a\n":
            w, h = struct.unpack(">II", header[16:24])
            return w, h
    return None, None

paintings = []
if os.path.exists(images_dir):
    for fname in sorted(os.listdir(images_dir)):
        if fname.lower().endswith(".png"):
            pid = os.path.splitext(fname)[0].lower().replace(" ", "_").replace("-", "_")
            title = os.path.splitext(fname)[0].replace("_", " ").title()
            fpath = os.path.join(images_dir, fname)
            pw, ph = get_png_dimensions(fpath)
            
            # Default aspect ratio to blocks (1x1, 2x1, 2x2, 3x2, 4x3, etc.)
            if pw and ph:
                ratio = pw / ph
                if 0.8 <= ratio <= 1.2:
                    bw, bh = 2, 2
                elif 1.2 < ratio <= 1.6:
                    bw, bh = 3, 2
                elif ratio > 1.6:
                    bw, bh = 4, 2
                elif 0.6 <= ratio < 0.8:
                    bw, bh = 2, 3
                else:
                    bw, bh = 1, 2
            else:
                bw, bh = 2, 2

            paintings.append({
                "id": pid,
                "name": title,
                "artist": "Server",
                "width": bw,
                "height": bh
            })

data = {
    "format": 1,
    "id": "server_paintings",
    "name": "Server Custom Paintings",
    "description": "Custom paintings for Hajaribagh server",
    "paintings": paintings
}

with open(json_path, "w") as f:
    json.dump(data, f, indent=2)

print(f"Updated custompaintings.json with {len(paintings)} painting(s).")
