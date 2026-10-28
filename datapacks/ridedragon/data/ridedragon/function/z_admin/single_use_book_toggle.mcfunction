#
# Description:	Set the Book of Dragons as a single use item or allow unlimited uses
# Called by:	ridedragon:admin via chat link
# Entity @s:	player
#
execute store success score #rd_success rd_help run data modify storage ridedragon:settings rd_admin.single_use_book set value "Single use"
execute unless score #rd_success rd_help matches 1 run data modify storage ridedragon:settings rd_admin.single_use_book set value "Unlimited uses"
#
tellraw @s [{"text":"A Book of Dragons has ","color":"aqua"},{"storage":"ridedragon:settings", "nbt":"rd_admin.single_use_book"}]
#
function ridedragon:admin

