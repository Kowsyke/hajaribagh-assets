# Known Issues and Open Questions

Findings from a review on 2026-10-22, right after the move to Oracle Cloud. Each item says what was observed, why it matters, and what to do. Items marked "verify" are suspicions that need a test in game or on the VM, because they could not be confirmed from the repo alone.

---

## A. Fix First

### 1. The painting pack cannot be downloaded
* **Observed**: `resource-pack` in `configs/server.properties` points at `raw.githubusercontent.com/Kowsyke/hajaribagh-assets/main/Hajaribagh-Paintings.zip`. A request without a login returns HTTP 404, because the repo is not publicly visible. `python scripts/check-server.py` shows the same failure.
* **Why it matters**: `require-resource-pack` is `false`, so players still join, but they never receive the custom painting art. Nothing on screen tells them why.
* **Verify first**: the live `server.properties` on the VM may point somewhere else. Check it.
* **Fix**: host the zip at a URL that needs no login (for example a small public repo, a release asset on a public repo, or a static host), put that URL in `resource-pack`, and keep `resource-pack-sha1` equal to the zip's hash. Steps are in [`OPERATIONS.md`](./OPERATIONS.md).

### 2. No backup of the world
* **Observed**: the world exists only on the VM and `world/` is gitignored. Nothing in the repo backs it up.
* **Why it matters**: one bad disk, deleted instance, or mistaken command loses everything players built.
* **Fix**: turn on Oracle boot volume backups (the Always Free tier includes a small number of backups, check the current limit), and also keep a scheduled copy of `world/` somewhere off the VM. A copy taken while the server runs can be slightly inconsistent, so use `save-all` first or briefly stop the service.

### 3. Oracle can reclaim idle Always Free instances
* **Observed**: this setup has small player counts and `pause-when-empty-seconds=60`, so CPU use will be very low most of the time.
* **Why it matters**: Oracle's Always Free terms allow reclaiming instances that stay idle. Check Oracle's current rules for the thresholds and for whether upgrading the account to Pay As You Go (which keeps Always Free resources free) exempts the instance.
* **Fix**: read Oracle's current policy and decide. Having backups (item 2) limits the damage either way.

### 4. Hardening checklist for a public server
* Port 22 (SSH) is open to `0.0.0.0/0` in the security list. Restrict it to known IP addresses if possible, allow key logins only, and consider `fail2ban`.
* A UDP rule for port 25565 exists. Minecraft Java Edition uses TCP only, so that rule is not needed.
* The copy of `server.properties` has `white-list=false` and `online-mode=false`, which suits offline launchers but means the server accepts any player name. Review whether a whitelist is acceptable for the friend group now that the server has a public IP.

---

## B. Verify in Game

### 5. Custom Paintings needs a client mod
* **Observed**: the mod's Modrinth page lists it as required on client and server. The README invariant says no mod may require a client jar.
* **What is known to work**: the resource pack texture override, which needs no client mod.
* **Verify**: join with an unmodified client, place several paintings, and check that no painting shows a missing texture. If it works, nothing changes. If it does not, the mod can probably be removed, since the zip already does the job. Test a world backup first.

### 6. Joint name and lore format
* **Observed**: `give_joint.mcfunction` and `recipe/joint.json` write custom names and lore as JSON text inside strings, and use `item_name='"Cannabis Joint"'`.
* **Concern**: third-party guides say item text moved to SNBT format in Minecraft 1.21.5, which would make this style show raw JSON or stray quotes. No primary source was found, so this is unconfirmed.
* **Verify**: craft a joint and read its name and lore. If it looks wrong, rewrite as `custom_name={text:"Cannabis Joint",color:"green",bold:true,italic:false}` and similar for `lore`.

### 7. Any warped fungus on a stick acts as a joint
* **Observed**: right-click detection counts every use of `minecraft:warped_fungus_on_a_stick`, and the vanilla recipe (fishing rod + warped fungus) makes the same item.
* **Effect**: a vanilla warped fungus on a stick also triggers the smoke effects.
* **Fix idea**: give joints a `custom_data` marker and check for it with an item predicate before running `smoke.mcfunction`.

### 8. Brewery visuals without Polymer's resource pack
* **Observed**: `configs/polymer/auto-host.json` has `enabled: false`.
* **Effect**: any texture or model pack Polymer generates is not sent to players. Brewery is said to work server-side, but this has not been checked in game.
* **Verify**: brew a drink and look at the items and the barrel. If they look wrong, enable auto-hosting and list the painting zip under `external_resource_packs`.

---

## C. Housekeeping

* `custompaintings/ServerPaintings/update_paintings.py` rebuilds `custompaintings.json` from image proportions. That would change today's hand-set sizes (for example Hasina from 2x3 to 2x2) and set every artist to "Server". It also does not build the zip.
* `custompaintings/ServerPaintings/images/` holds both `.jpg` and `.png` copies of some images, and `pack.png` is a copy of the Hasina image.
* The zip build step is not in the repo.
* `fabric-api` 0.162.0 is installed. Versions 0.163.0 and 0.164.0 exist for 26.3.
* `datapacks/ore_xray/data/ore_xray/function/deny.mcfunction` is never called.
* `datapacks/cannabis_smoke` prints a chat message to every player on every `/reload`.
* `configs/server.properties` is a pre-migration snapshot, so it may not match the VM.
