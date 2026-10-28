#
# Description:	Enable/disable vanishing dragons that are ridden
# Called by:	ridedragon:admin via chat link
# Entity @s:	player
#
execute store success score #rd_success rd_help run data modify storage ridedragon:settings rd_admin.vanish_ridden set value "Immune"
execute unless score #rd_success rd_help matches 1 run data modify storage ridedragon:settings rd_admin.vanish_ridden set value "Vanishable"
#
tellraw @s [{"text":"Dragon that are mouted are ","color":"aqua"},{"storage":"ridedragon:settings", "nbt":"rd_admin.vanish_ridden"}]
#
function ridedragon:admin

