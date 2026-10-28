#
# Description:	Enable/disable dragon voice on summoning
# Called by:	ridedragon:admin via chat link
# Entity @s:	player
#
execute store success score #rd_success rd_help run data modify storage ridedragon:settings rd_admin.summon_silent set value "Roaring"
execute unless score #rd_success rd_help matches 1 run data modify storage ridedragon:settings rd_admin.summon_silent set value "Silent"
#
tellraw @s [{"text":"Summoned dragon's voice is set to ","color":"aqua"},{"storage":"ridedragon:settings", "nbt":"rd_admin.summon_silent"}]
#
function ridedragon:admin

