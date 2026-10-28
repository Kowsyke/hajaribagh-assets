#
# Description:	Enable/disable dragon invulnerability on summoning
# Called by:	ridedragon:admin via chat link
# Entity @s:	player
#
execute store success score #rd_success rd_help run data modify storage ridedragon:settings rd_admin.summon_invulnerable set value "Invulnerable"
execute unless score #rd_success rd_help matches 1 run data modify storage ridedragon:settings rd_admin.summon_invulnerable set value "Mortal"
#
tellraw @s [{"text":"Summoned dragon is set to ","color":"aqua"},{"storage":"ridedragon:settings", "nbt":"rd_admin.summon_invulnerable"}]
#
function ridedragon:admin

