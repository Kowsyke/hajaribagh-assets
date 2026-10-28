#
# Description:	Display help in chat
# Called by:	ridedragon:z_main
# Entity @s:	player
#
execute if score @s rd_help matches 10 if data storage ridedragon:settings rd_admin{book_help:"Enabled"} run function ridedragon:z_help/get_book
execute if score @s rd_help matches 11 run function ridedragon:z_help/credits
execute if score @s rd_help matches 1..9 run function ridedragon:z_help/main

#
# Reset trigger score
#
scoreboard players set @s rd_help 0
scoreboard players enable @s rd_help
