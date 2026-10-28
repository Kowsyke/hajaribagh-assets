#
# Description:	Enable/disable dragonseat (horse) glowing on summoning
# Called by:	ridedragon:admin via chat link
# Entity @s:	player
#
execute store success score #rd_success rd_help run data modify storage ridedragon:settings rd_admin.summon_glowing set value "Glowing"
execute unless score #rd_success rd_help matches 1 run data modify storage ridedragon:settings rd_admin.summon_glowing set value "Invisible"
#
tellraw @s [{"text":"Summoned dragon mount point is set to ","color":"aqua"},{"storage":"ridedragon:settings", "nbt":"rd_admin.summon_glowing"}]
#
function ridedragon:admin

