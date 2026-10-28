# called as dragon_visible, at same

# Fireball cooldown handling
scoreboard players remove @s[scores={rd_fire_cooldown=1..}] rd_fire_cooldown 1

# Find all the parts of the flying stack and tag them as
# dragonvisible_selected, dragonhelper_selected, dragonseat_selected, dragonrider_selected

scoreboard players operation #rd_selected_id rd_id = @s rd_id
tag @s add dragonvisible_selected
execute as @e[type=marker,tag=dragonhelper,distance=..7] if score @s rd_id = #rd_selected_id rd_id run tag @s add dragonhelper_selected
execute as @e[type=horse,tag=dragonseat,distance=..7] if score @s rd_id = #rd_selected_id rd_id run tag @s add dragonseat_selected
tag @a[nbt={RootVehicle:{Entity:{Tags:["dragonseat_selected"]}}},distance=..7,limit=1] add dragonrider_selected

# Reset HurtTime to keep the knockback effect of the dragon disabled. It seems to be reset 
# by actual harming of the dragon, so set it back to 2.
data modify entity @s HurtTime set value 2b

# If there is a rider
# Only update the horse and thus player position every other tick to give time for the player 
# rotation to be updated from client to the server. Update corresponding to two ticks worth
# of movement instead.
# Background: Teleporting the horse seems to inhibit player rotation update from the client 
# for the remaining duration of that tick. On high-latency connections this casued severe issues. 
execute if score @s rd_tick_phase matches 0 as @a[tag=dragonrider_selected,distance=..7,limit=1] run function ridedragon:z_player_motion_update_tick
# The other ticks we move the assembly forward one step.
execute if score @s rd_tick_phase matches 1 as @a[tag=dragonrider_selected,distance=..7,limit=1] run function ridedragon:z_player_motion_non_update_tick

scoreboard players add @s rd_tick_phase 1
execute if score @s rd_tick_phase matches 2.. run scoreboard players set @s rd_tick_phase 0

# Single tick variation of player momvment. Not used currently.
#execute as @a[tag=dragonrider_selected,distance=..7,limit=1] run function ridedragon:z_player_motion

# If no rider perform default movement
execute as @e[type=marker,tag=dragonhelper_selected,distance=..7,limit=1] unless entity @a[distance=..7,limit=1,tag=dragonrider_selected] run function ridedragon:z_no_player_motion

tag @s remove dragonvisible_selected
tag @a[distance=..7,tag=dragonrider_selected,limit=1] remove dragonrider_selected
tag @e[type=marker,distance=..7,tag=dragonhelper_selected,limit=1] remove dragonhelper_selected
tag @e[type=horse,distance=..7,tag=dragonseat_selected,limit=1] remove dragonseat_selected

