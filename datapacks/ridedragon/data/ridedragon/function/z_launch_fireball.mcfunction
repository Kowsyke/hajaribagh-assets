# Summon a new dragon fireball
#summon minecraft:dragon_fireball ~ ~4 ~ {Tags:["dragon_fireball_selected","dragon_fireball"],direction:[0.5,0.0,0.0],acceleration_power:[0.1,-0.1,0.0],Owner:[I;1,1,1,1]}
summon minecraft:dragon_fireball ^ ^ ^8 {Tags:["dragon_fireball_selected","dragon_fireball"]}

# Mark the dragon as the owner so that the dragon's breath can be collected from the
# area_effect_cloud after the dragon fireball lands
data modify entity @e[tag=dragon_fireball_selected,distance=..10,limit=1] Owner set from entity @e[tag=dragonvisible_selected,distance=..10,limit=1] UUID

# Start the cooldown for the dragon to fire as configured in the admin menu
execute store result score @e[tag=dragonvisible_selected,limit=1] rd_fire_cooldown run data get storage ridedragon:settings rd_admin.fire_cooldown


# Set up motion. Inspired by
# https://www.reddit.com/r/MinecraftCommands/wiki/questions/shootfacing/
# summon the temporary entity at the players position
summon marker ~ ~ ~ {Tags:["direction_marker"]}

# execute the below function as the marker entity, so it doesn't get lost from being unloaded
# run positioned at the world zero point. this will remove the marker
execute as @e[tag=direction_marker,distance=..10,limit=1] positioned 0.0 0.0 0.0 run function ridedragon:z_fireball_get_motion

# store the previously stored Motion into the projectile entity
# Note that dragon fireballs use "Motion" for the initial direction and 
# "acceleration_power" for the constant acceleration countering drag.
data modify entity @e[tag=dragon_fireball_selected,limit=1] acceleration_power set value 0.1
data modify entity @e[tag=dragon_fireball_selected,limit=1] Motion set from storage ridedragon:tmp Motion2
# clean up the tag
tag @e[tag=dragon_fireball_selected] remove dragon_fireball_selected


