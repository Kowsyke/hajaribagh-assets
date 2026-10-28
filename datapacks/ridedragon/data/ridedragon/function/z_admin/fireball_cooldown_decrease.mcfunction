#
# Description:	Decrease the cooldown time for dragon fireballs
# Called by:	ridedragon:admin via chat link
# Entity @s:	player
#

execute store result score #rd_math rd_help run data get storage ridedragon:settings rd_admin.fire_cooldown
execute if score #rd_math rd_help matches 11.. store result storage ridedragon:settings rd_admin.fire_cooldown int 1.0 run scoreboard players remove #rd_math rd_help 10

function ridedragon:admin

