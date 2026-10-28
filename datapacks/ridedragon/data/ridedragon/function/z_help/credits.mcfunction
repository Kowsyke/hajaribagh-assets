#
# Description:	Display credits in chat
# Called by:	ridedragon:z_help_trigger
# Entity @s:	Player
#
tellraw @s [{"text":"Rideable Dragons - Credits","color":"yellow","bold":true}]
tellraw @s [{"text":"Created by:             ","color":"aqua"},{"text":"ptefar","color":"#87325d","bold":true,"click_event":{"action":"open_url","url":"https://www.youtube.com/channel/UC3ro2x7YnyNt8V1t1bUYfXA"}}]
tellraw @s [{"text":"Based on an idea from:  ","color":"aqua"},{"text":"John Paul Inso","color":"#0072e5","bold":true,"click_event":{"action":"open_url","url":"https://youtu.be/vBUknTYjylc"}}]
tellraw @s [{"text":"Some frameworks from:   ","color":"aqua"},{"text":"Armor Statues datapack","color":"#0072e5","bold":true,"click_event":{"action":"open_url","url":"https://www.curseforge.com/minecraft/customization/armor-statues-datapack"}}]
tellraw @s [{"text":"--------------------------","color":"yellow","bold":true}]
