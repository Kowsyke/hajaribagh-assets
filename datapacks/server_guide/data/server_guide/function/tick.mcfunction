
# GTA Wasted Death Sound & Banner
execute as @a[scores={gta_deaths=1..}] at @s run playsound minecraft:gta.wasted player @s ~ ~ ~ 2 1
execute as @a[scores={gta_deaths=1..}] at @s run title @s times 5 40 10
execute as @a[scores={gta_deaths=1..}] at @s run title @s subtitle {"text":"W A S T E D","color":"dark_red","bold":true}
execute as @a[scores={gta_deaths=1..}] at @s run title @s title {"text":""}
scoreboard players set @a[scores={gta_deaths=1..}] gta_deaths 0


# Enable GTA Triggers
scoreboard players enable @a tp_base
scoreboard players enable @a tp_spawn
scoreboard players enable @a gtp
scoreboard players enable @a minimap

# Handle Triggers
execute as @a[scores={tp_base=1..}] at @s run function server_guide:gtp_base
scoreboard players set @a[scores={tp_base=1..}] tp_base 0

execute as @a[scores={tp_spawn=1..}] at @s run function server_guide:gtp_spawn
scoreboard players set @a[scores={tp_spawn=1..}] tp_spawn 0

execute as @a[scores={gtp=1..}] at @s run function server_guide:gtp_menu
scoreboard players set @a[scores={gtp=1..}] gtp 0

execute as @a[scores={minimap=1..}] at @s run function server_guide:minimap
scoreboard players set @a[scores={minimap=1..}] minimap 0

# GTA Transit Flight Controller
execute as @a[scores={gtp_timer=1..}] run scoreboard players add @s gtp_timer 1

# Stage 2: Aerial Stratosphere Transit at tick 15
execute as @a[scores={gtp_timer=15},tag=gtp_to_base] run tp @s 163 240 -307
execute as @a[scores={gtp_timer=15},tag=gtp_to_spawn] run tp @s 0 240 0
execute as @a[scores={gtp_timer=15}] at @s run playsound minecraft:item.elytra.flying player @s ~ ~ ~ 1.8 1.1
execute as @a[scores={gtp_timer=15}] at @s run particle minecraft:cloud ~ ~ ~ 2 0.5 2 0.05 40 force
execute as @a[scores={gtp_timer=15}] run title @s subtitle {"text":"Cruising through stratosphere...","color":"aqua"}
execute as @a[scores={gtp_timer=15}] run title @s title {"text":"✦ TRANSIT GLIDE ✦","color":"gold","bold":true}

# Stage 3: Dive & Impact Landing at tick 28
execute as @a[scores={gtp_timer=28},tag=gtp_to_base] run tp @s 163 100 -307
execute as @a[scores={gtp_timer=28},tag=gtp_to_spawn] run tp @s 0 70 0
execute as @a[scores={gtp_timer=28}] at @s run playsound minecraft:entity.warden.sonic_boom player @s ~ ~ ~ 1.2 1.8
execute as @a[scores={gtp_timer=28}] at @s run playsound minecraft:entity.iron_golem.damage player @s ~ ~ ~ 1 0.7
execute as @a[scores={gtp_timer=28}] at @s run particle minecraft:explosion ~ ~ ~ 1 0.1 1 0 20 force
execute as @a[scores={gtp_timer=28}] at @s run particle minecraft:cloud ~ ~0.2 ~ 1.5 0.1 1.5 0.05 35 force
execute as @a[scores={gtp_timer=28}] run effect clear @s minecraft:levitation
execute as @a[scores={gtp_timer=28}] run effect clear @s minecraft:blindness
execute as @a[scores={gtp_timer=28}] run effect give @s minecraft:slow_falling 3 1 true
execute as @a[scores={gtp_timer=28},tag=gtp_to_base] run title @s subtitle {"text":"Welcome to Hajaribagh Base","color":"green"}
execute as @a[scores={gtp_timer=28},tag=gtp_to_spawn] run title @s subtitle {"text":"Arrived at World Spawn","color":"green"}
execute as @a[scores={gtp_timer=28}] run title @s title {"text":"✦ TRANSIT COMPLETE ✦","color":"gold","bold":true}

tag @a[scores={gtp_timer=28}] remove gtp_to_base
tag @a[scores={gtp_timer=28}] remove gtp_to_spawn
scoreboard players set @a[scores={gtp_timer=28}] gtp_timer 0

scoreboard players enable @a guide
execute as @a unless score @s has_starter_kit matches 1.. at @s run function server_guide:give_starter_kit
execute as @a unless score @s has_starter_kit matches 1.. run scoreboard players set @s has_starter_kit 1
execute as @a unless score @s guide_version matches 13.. at @s run function server_guide:update_player_guide
execute as @a[scores={guide=1..}] at @s run function server_guide:give_book
scoreboard players set @a[scores={guide=1..}] guide 0

execute as @a[tag=!vanilla_recipes_unlocked] at @s run function server_guide:unlock_all_recipes
tag @a[tag=!vanilla_recipes_unlocked] add vanilla_recipes_unlocked

# TNT Arrow Trigger and Shot Detection
scoreboard players enable @a tnt_arrow
execute as @a[scores={tnt_arrow=1..}] at @s run function server_guide:toggle_tnt_arrow
scoreboard players set @a[scores={tnt_arrow=1..}] tnt_arrow 0

execute as @a[scores={used_bow=1..,tnt_mode=1}] at @s run function server_guide:tag_tnt_arrow
execute as @a[scores={used_cbow=1..,tnt_mode=1}] at @s run function server_guide:tag_tnt_arrow
execute as @a[scores={used_bow=1..},nbt={Inventory:[{Slot:-106b,id:"minecraft:tnt"}]}] at @s run function server_guide:tag_tnt_arrow
execute as @a[scores={used_cbow=1..},nbt={Inventory:[{Slot:-106b,id:"minecraft:tnt"}]}] at @s run function server_guide:tag_tnt_arrow
scoreboard players set @a[scores={used_bow=1..}] used_bow 0
scoreboard players set @a[scores={used_cbow=1..}] used_cbow 0

# TNT Arrow Flight Particle Trail
execute at @e[type=arrow,tag=tnt_arrow,nbt={inGround:0b}] run particle minecraft:flame ~ ~ ~ 0.05 0.05 0.05 0.01 2 normal
execute at @e[type=arrow,tag=tnt_arrow,nbt={inGround:0b}] run particle minecraft:smoke ~ ~ ~ 0.05 0.05 0.05 0.01 3 normal
execute at @e[type=spectral_arrow,tag=tnt_arrow,nbt={inGround:0b}] run particle minecraft:flame ~ ~ ~ 0.05 0.05 0.05 0.01 2 normal
execute at @e[type=spectral_arrow,tag=tnt_arrow,nbt={inGround:0b}] run particle minecraft:smoke ~ ~ ~ 0.05 0.05 0.05 0.01 3 normal

# TNT Arrow Detonation on Contact with Blocks
execute as @e[type=arrow,tag=tnt_arrow,nbt={inGround:1b}] at @s run function server_guide:detonate_arrow
execute as @e[type=spectral_arrow,tag=tnt_arrow,nbt={inGround:1b}] at @s run function server_guide:detonate_arrow

# TNT Arrow Detonation on Contact with Mobs and Monsters
execute as @e[type=arrow,tag=tnt_arrow,nbt={inGround:0b}] at @s if entity @e[type=!player,type=!arrow,type=!spectral_arrow,type=!item,type=!experience_orb,distance=..1.5] run function server_guide:detonate_arrow
execute as @e[type=spectral_arrow,tag=tnt_arrow,nbt={inGround:0b}] at @s if entity @e[type=!player,type=!arrow,type=!spectral_arrow,type=!item,type=!experience_orb,distance=..1.5] run function server_guide:detonate_arrow

# TNT Arrow Detonation on Contact with Other Players
execute as @e[type=arrow,tag=tnt_arrow,nbt={inGround:0b}] at @s if entity @a[distance=0.8..1.5] run function server_guide:detonate_arrow
execute as @e[type=spectral_arrow,tag=tnt_arrow,nbt={inGround:0b}] at @s if entity @a[distance=0.8..1.5] run function server_guide:detonate_arrow

# Kit Platinum and Dev Bundle Triggers
scoreboard players enable @a kit_platinum
execute as @a[scores={kit_platinum=1..}] at @s run function server_guide:kit_platinum
scoreboard players set @a[scores={kit_platinum=1..}] kit_platinum 0

scoreboard players enable @a[team=pm] kit_dev
execute as @a[scores={kit_dev=1..},team=pm] at @s run function server_guide:kit_dev
scoreboard players set @a[scores={kit_dev=1..}] kit_dev 0

scoreboard players enable @a kit_shears
execute as @a[scores={kit_shears=1..}] at @s run function server_guide:give_shears
scoreboard players set @a[scores={kit_shears=1..}] kit_shears 0

scoreboard players enable @a kit_shield
execute as @a[scores={kit_shield=1..}] at @s run function server_guide:give_shield
scoreboard players set @a[scores={kit_shield=1..}] kit_shield 0

scoreboard players enable @a kit_boots
execute as @a[scores={kit_boots=1..}] at @s run function server_guide:give_boots
scoreboard players set @a[scores={kit_boots=1..}] kit_boots 0
