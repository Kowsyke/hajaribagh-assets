
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
execute as @a unless score @s guide_version matches 12.. at @s run function server_guide:update_player_guide
execute as @a[scores={guide=1..}] at @s run function server_guide:give_book
scoreboard players set @a[scores={guide=1..}] guide 0

execute as @a[tag=!vanilla_recipes_unlocked] at @s run function server_guide:unlock_all_recipes
tag @a[tag=!vanilla_recipes_unlocked] add vanilla_recipes_unlocked
