function salman_f_rahman:give_ore
scoreboard players set @s sfr_warn_timer 0
title @s reset
title @s actionbar {"text":"Slot opened in time! Dividend claimed!","color":"green"}
tellraw @s [{"text":"[Salman F Rahman] ","color":"gold","bold":true},{"text":"Inventory space opened in time. Your daily tycoon armor trim dividend has been credited!","color":"green"}]
