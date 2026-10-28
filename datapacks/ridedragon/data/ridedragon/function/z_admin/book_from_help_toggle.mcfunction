#
# Description:	Disable option to get the book directly from the help menu
# Called by:	ridedragon:admin via chat link
# Entity @s:	player
#
execute store success score #rd_success rd_help run data modify storage ridedragon:settings rd_admin.book_help set value "Disabled"
execute unless score #rd_success rd_help matches 1 run data modify storage ridedragon:settings rd_admin.book_help set value "Enabled"
#
tellraw @s [{"text":"Getting the book from the help menu has been ","color":"aqua"},{"storage":"ridedragon:settings", "nbt":"rd_admin.book_help"}]
#
function ridedragon:admin

