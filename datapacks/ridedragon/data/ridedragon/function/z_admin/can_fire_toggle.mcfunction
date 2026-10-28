#
# Description:	Disable fireing of dragon fireballs
# Called by:	ridedragon:admin via chat link
# Entity @s:	player
#
execute store success score #rd_success rd_help run data modify storage ridedragon:settings rd_admin.can_fire set value "Disabled"
execute unless score #rd_success rd_help matches 1 run data modify storage ridedragon:settings rd_admin.can_fire set value "Enabled"
#
tellraw @s [{"text":"Player fireing of dragon fireballs has been ","color":"aqua"},{"storage":"ridedragon:settings", "nbt":"rd_admin.can_fire"}]
#
function ridedragon:admin

