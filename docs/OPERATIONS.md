# Operations Guide

How the files in this repo map onto the live Oracle Cloud VM, and how to ship a change. Server access commands (SSH, logs, restart) are in [`HOSTING_ROADMAP.md`](./HOSTING_ROADMAP.md).

---

## 1. Where Each Repo File Goes on the VM

The server directory on the VM is `/home/ubuntu/minecraft-server`.

| Repo path | VM path | Sent by `deploy-to-cloud.sh`? | Applied by |
| :--- | :--- | :--- | :--- |
| `datapacks/<pack>/` | `world/datapacks/<pack>/` | Yes | `/reload` in game |
| `configs/lithium.properties` | `config/lithium.properties` | Yes | Restart |
| `configs/ferritecore.mixin.properties` | `config/ferritecore.mixin.properties` | Yes | Restart |
| `configs/custompaintings.toml` | `config/custompaintings.toml` | Yes | Restart |
| `configs/polymer/` | `config/polymer/` | Yes | Restart |
| `configs/server.properties` | `server.properties` (server root) | No, deliberately skipped | Edit on the VM, then restart |
| `custompaintings/ServerPaintings/` | `world/custompaintings/ServerPaintings/` | No, copy by hand | Restart |
| `scripts/start-server.sh` | `start-server.sh` (server root) | No, copy by hand | Restart |
| `Hajaribagh-Paintings.zip` | Not on the VM | No | Players download it from the URL in `server.properties` |

The `world/custompaintings/` location comes from the Custom Paintings mod page. It was not checked on the VM.

`configs/server.properties` is a copy of the live file taken before the move to Oracle, so the VM's real file may differ (view distance, player limit, and so on). Treat the VM as the source of truth for that one file and update the copy when you change it.

---

## 2. Deploying a Change

1. `git pull --ff-only` so you start from the latest `main`.
2. Make and test your change locally.
3. Commit and push to `main` (or merge your branch).
4. Run `./scripts/deploy-to-cloud.sh` from the repo root (Git Bash on Windows).
5. In game, run `/reload` for datapack changes. Config and mod changes need `sudo systemctl restart minecraft.service`.
6. Run `python scripts/check-server.py` to confirm the server still answers.

The deploy script copies your working folder, so uncommitted edits go live too.

---

## 3. Updating the Painting Pack

The pack reaches players through three lines in `server.properties`: `resource-pack` (URL), `resource-pack-sha1` (hash of the zip), and `resource-pack-prompt`.

1. Rebuild `Hajaribagh-Paintings.zip`. Its layout is `pack.mcmeta`, `pack.png`, and `assets/minecraft/textures/painting/<name>.png` for each of the 46 vanilla painting names, using the image-to-texture table in [`MODS_DATAPACKS.md`](./MODS_DATAPACKS.md). The build step is not scripted yet.
2. Compute the new hash: `sha1sum Hajaribagh-Paintings.zip` in Git Bash, or `Get-FileHash Hajaribagh-Paintings.zip -Algorithm SHA1` in PowerShell.
3. Publish the zip at the URL that `resource-pack` points to. The URL must download without any login. A private GitHub repo does not qualify.
4. Put the new hash in `resource-pack-sha1`, both in `configs/server.properties` and in the live `server.properties` on the VM.
5. Restart the server. Players are offered the new pack the next time they join.

Change the file and the hash at the same time. If they disagree, clients reject the download.

`python scripts/check-server.py` verifies that the URL is reachable and that the hash matches.

---

## 4. Updating Mods

1. Check what is available for Minecraft 26.3 (replace the slug with the mod's Modrinth slug):
   ```bash
   curl -s "https://api.modrinth.com/v2/project/fabric-api/version?game_versions=%5B%2226.3%22%5D&loaders=%5B%22fabric%22%5D"
   ```
2. On the VM: stop the service, move the old jar out of `mods/` (keep it until the new one works), drop in the new jar, and start the service.
3. Watch `sudo journalctl -u minecraft -f` for errors on startup.
4. Update the version tables in `docs/ARCHITECTURE.md` and `docs/MODS_DATAPACKS.md`.

Before adding any new mod, check its Modrinth page for the client side. Only add it if the client is listed as optional or unsupported (see the Zero Client Mod Requirement in the README).

---

## 5. Secrets

* Files in `configs/` are copies of live files. Before committing one, blank any password, token, or secret value.
* `management-server-secret` in `configs/server.properties` was committed in plain text earlier and is now blank. The old value is still in git history, so regenerate it on the VM if the management server is ever turned on.
