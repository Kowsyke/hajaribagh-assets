# Executed as dragonrider, no position

# Remove the glowing effect on the dragonseat, if active
#effect clear @e[type=minecraft:horse,distance=..7,tag=dragonseat_selected,limit=1] glowing

# Low speed default
execute as @s at @s positioned ^ ^ ^0.2 positioned ~ ~-0.85 ~ if block ~ ~-1.3 ~ air run tp @e[type=marker,distance=..7,tag=dragonhelper_selected,limit=1] ~ ~ ~ ~ ~

# High speed when holding the book
execute if entity @s[predicate=ridedragon:book_holder_mainhand] at @s positioned ^ ^ ^1.0 positioned ~ ~-0.85 ~ if block ~ ~-1.3 ~ air run tp @e[type=marker,distance=..7,tag=dragonhelper_selected,limit=1] ~ ~ ~ ~ ~
execute if entity @s[predicate=ridedragon:book_holder_offhand] at @s positioned ^ ^ ^1.0 positioned ~ ~-0.85 ~ if block ~ ~-1.3 ~ air run tp @e[type=marker,distance=..7,tag=dragonhelper_selected,limit=1] ~ ~ ~ ~ ~

#Move the dragonseat (horse) to the helper marker
execute as @e[type=marker,distance=..7,tag=dragonhelper_selected,limit=1] at @s run tp @e[type=horse,distance=..7,tag=dragonseat_selected,limit=1] ~ ~ ~ ~ ~


# Move the dragon to the correct offset relative to the player/dragonseat depending on the low/high speed
# Low speed
execute as @e[type=marker,distance=..7,tag=dragonhelper_selected,limit=1] at @s rotated ~ 0 positioned ^ ^ ^-2.6 rotated as @s run tp @e[type=ender_dragon,tag=dragonvisible_selected,limit=1,sort=nearest,distance=..7] ~ ~-0.7 ~ ~-180 ~
# High speed looking up or forward
execute if entity @s[predicate=ridedragon:book_holder_mainhand] as @e[type=marker,distance=..7,tag=dragonhelper_selected,limit=1] at @s positioned ^ ^ ^-2.7 rotated as @s run tp @e[type=ender_dragon,tag=dragonvisible_selected,limit=1,sort=nearest,distance=..7] ~ ~-0.7 ~ ~-180 ~
execute if entity @s[predicate=ridedragon:book_holder_offhand] as @e[type=marker,distance=..7,tag=dragonhelper_selected,limit=1] at @s positioned ^ ^ ^-2.7 rotated as @s run tp @e[type=ender_dragon,tag=dragonvisible_selected,limit=1,sort=nearest,distance=..7] ~ ~-0.7 ~ ~-180 ~
# High speed looking down
execute if entity @s[x_rotation=10..90,predicate=ridedragon:book_holder_mainhand] as @e[type=marker,distance=..7,tag=dragonhelper_selected,limit=1] at @s rotated ~ 0 positioned ^ ^ ^-2.7 rotated as @s positioned ^ ^ ^-2.2 rotated as @s run tp @e[type=ender_dragon,tag=dragonvisible_selected,limit=1,sort=nearest,distance=..7] ~ ~-0.7 ~ ~-180 ~
execute if entity @s[x_rotation=10..90,predicate=ridedragon:book_holder_offhand] as @e[type=marker,distance=..7,tag=dragonhelper_selected,limit=1] at @s rotated ~ 0 positioned ^ ^ ^-2.7 rotated as @s positioned ^ ^ ^-2.2 rotated as @s run tp @e[type=ender_dragon,tag=dragonvisible_selected,limit=1,sort=nearest,distance=..7] ~ ~-0.7 ~ ~-180 ~


# Check if dragon fireballs are enabled the trigger held and looking sufficiently below the horizon (10 degrees or more)
execute if data storage ridedragon:settings rd_admin{can_fire:"Enabled"} run execute if entity @s[x_rotation=10..90,predicate=ridedragon:is_holding_trigger_item] at @s run execute if entity @e[tag=dragonvisible_selected,limit=1,scores={rd_fire_cooldown=0}] run function ridedragon:z_launch_fireball
