#
# Description:	Enable/disable summoning of tame dragons without holding the Book of Dragons
# Called by:	ridedragon:admin via chat link
# Entity @s:	player
#
execute store success score #rd_success rd_help run data modify storage ridedragon:settings rd_admin.summon_without_book set value "Disabled"
execute unless score #rd_success rd_help matches 1 run data modify storage ridedragon:settings rd_admin.summon_without_book set value "Enabled"
#
tellraw @s [{"text":"Summoning dragons without the Book of Dragons has been ","color":"aqua"},{"storage":"ridedragon:settings", "nbt":"rd_admin.summon_without_book"}]
#
function ridedragon:admin

