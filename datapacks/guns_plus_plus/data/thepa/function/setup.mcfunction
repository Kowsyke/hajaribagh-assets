execute as @e[nbt={Inventory:[{id:"minecraft:crossbow",components:{"minecraft:custom_data":{gz_data:{}}}}]}] at @s run function thepa:utilities/update_handler/update_patch

scoreboard objectives add deathCount minecraft.custom:minecraft.deaths
scoreboard objectives add gz_sneak minecraft.custom:minecraft.sneak_time
scoreboard objectives add gz_click minecraft.used:minecraft.carrot_on_a_stick
scoreboard objectives add gz_crossbow minecraft.used:minecraft.warped_fungus_on_a_stick
scoreboard objectives add scope_timer dummy
scoreboard objectives add shotgun_clicks dummy
scoreboard objectives add killCredit dummy
scoreboard objectives add scoreboardChecked dummy
scoreboard objectives add timeRemaining dummy
scoreboard objectives add breaksBlocks dummy
scoreboard objectives add minigun_sounds dummy
scoreboard objectives add bfg_idle dummy
scoreboard objectives add bouncyCount dummy
scoreboard objectives add gz_bullets dummy
scoreboard objectives add gz_capacity dummy
scoreboard objectives add gz_damage dummy
scoreboard objectives add gz_reload dummy
scoreboard objectives add gz_reload_time dummy
scoreboard objectives add gz_reload_max dummy
scoreboard objectives add gz_id dummy
scoreboard objectives add bloomRandom dummy
scoreboard objectives add augCount dummy
scoreboard objectives add chargeTime dummy
scoreboard objectives add minigunCharge minecraft.used:minecraft.warped_fungus_on_a_stick
scoreboard objectives add removeBullet dummy
scoreboard objectives add ageflare dummy
scoreboard objectives add _playerlist dummy
scoreboard objectives add gz_teslakill dummy
scoreboard objectives add gz_teslatimer dummy
scoreboard objectives add gunsights dummy
scoreboard objectives add shootingdelay dummy
scoreboard objectives add delay_calculator dummy
scoreboard objectives add 2 dummy
scoreboard objectives add 10 dummy
scoreboard objectives add 50000 dummy
scoreboard objectives add 10000 dummy
scoreboard objectives add size_time dummy
scoreboard players set 2 2 2
scoreboard players set 10 10 10
scoreboard players set 50000 50000 50000
scoreboard players set 10000 10000 10000

schedule function thepa:delayed_loop 1t
data modify storage gz:shooting_delays shooting_delays set value [13,99,25,99,99,1,1,30,2,40,12,1,1,1,1,5,4,12,6,1,3,1,1,5,1,50,25,1,1,4,1,5,3,10,2,1,1,1,1,4,5,5,5,5,20,1,5,15,1,25,13,12,5,12,80,20,20,10,11,15,2,6,1,10]

scoreboard players set @a[tag=!shootinginit] shootingdelay 0
tag @a add shootinginit
scoreboard objectives add SCOREBOARD1 dummy
scoreboard objectives add motion_x1 dummy
scoreboard objectives add motion_y1 dummy
scoreboard objectives add motion_z1 dummy
scoreboard objectives add motion_x2 dummy
scoreboard objectives add motion_y2 dummy
scoreboard objectives add motion_z2 dummy
scoreboard objectives add ztimer dummy
scoreboard players set timer ztimer 0
#Recoil Systems
scoreboard objectives add bloom dummy
scoreboard objectives add recoil dummy
scoreboard objectives add camera dummy
scoreboard objectives add cameraRandom dummy
scoreboard objectives add spray dummy

scoreboard objectives add legacyControls dummy


#Turret Mechanism
scoreboard objectives add rotation_x dummy
scoreboard objectives add max_x dummy
scoreboard objectives add min_x dummy
scoreboard objectives add turretRotsp dummy

scoreboard objectives add mobWeapon dummy
scoreboard objectives add mobWeaponFrequency dummy
scoreboard objectives add randomWeaponSpawn dummy
scoreboard objectives add shootingDelayChecked dummy

scoreboard objectives add prevGun dummy
scoreboard objectives add nowGun dummy

execute store success score BREAKS_BLOCKS scoreboardChecked run scoreboard players get GLOBAL breaksBlocks
execute store success score SPRAY scoreboardChecked run scoreboard players get GLOBAL spray
execute store success score LEGACY_CONTROLS scoreboardChecked run scoreboard players get GLOBAL legacyControls
execute store success score CAMERA scoreboardChecked run scoreboard players get GLOBAL camera
execute store success score BLOOM scoreboardChecked run scoreboard players get GLOBAL bloom
execute store success score RECOIL scoreboardChecked run scoreboard players get GLOBAL recoil
execute store success score mobWeapon scoreboardChecked run scoreboard players get GLOBAL mobWeapon
title @a times 0s 3s 5s
forceload add 0 0

scoreboard players set GLOBAL breaksBlocks 0
scoreboard players set GLOBAL spray 0
scoreboard players set GLOBAL camera 0
scoreboard players set GLOBAL legacyControls 0
scoreboard players set GLOBAL bloom 1
scoreboard players set GLOBAL recoil 0
scoreboard players set GLOBAL mobWeapon 1
scoreboard players set GLOBAL mobWeaponFrequency 2
tag @a add inf_reload

scoreboard objectives add shotcounter dummy
scoreboard objectives add shotcounterdelay dummy

