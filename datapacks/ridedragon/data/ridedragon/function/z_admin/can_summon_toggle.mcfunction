#
# Description:	Enable/disable summoning of tame dragons by survival players
# Called by:	ridedragon:admin via chat link
# Entity @s:	player
#
execute store success score #rd_success rd_help run data modify storage ridedragon:settings rd_admin.can_summon set value "Disabled"
execute unless score #rd_success rd_help matches 1 run data modify storage ridedragon:settings rd_admin.can_summon set value "Enabled"
#
tellraw @s [{"text":"Summoning dragons for survival players has been ","color":"aqua"},{"storage":"ridedragon:settings", "nbt":"rd_admin.can_summon"}]
#
function ridedragon:admin

