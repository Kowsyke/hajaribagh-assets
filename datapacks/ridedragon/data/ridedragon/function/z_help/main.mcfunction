#
# Description:	Display main help options
# Called by:	ridedragon:z_help_trigger
# Entity @s:	Player
#
tellraw @s [{"text":"Rideable Dragons - Help","color":"yellow","bold":true},{"text":"\nDragons can be summoned via the ","color":"aqua","bold":false},{"text":"Book of Dragons","color":"light_purple","bold":false},{"text":"\nSummoned dragons are mounted by clicking on their necks\nGet the book by:","color":"aqua","bold":false}]
execute if data storage ridedragon:settings rd_admin{book_help:"Enabled"} run tellraw @s [{"text":" - Clicking ","color":"aqua"},{"text":"here","color":"green","click_event":{"action":"run_command","command":"/trigger rd_help set 10"}}]
execute if data storage ridedragon:settings rd_admin{can_fire:"Enabled"} run tellraw @s [{"text":"Hold an End Crystal and look below the horizon while mounted to launch dragon fireballs","color":"aqua"}]
tellraw @s [{"text":"Credits","color":"green","click_event":{"action":"run_command","command":"/trigger rd_help set 11"}}]
tellraw @s [{"text":"--------------------------","color":"yellow","bold":true}]
