scoreboard players remove @s sfr_warn_timer 1

function salman_f_rahman:check_free_space
execute if score @s sfr_has_space matches 1 run function salman_f_rahman:give_ore_early

execute if score @s sfr_has_space matches 0 if score @s sfr_warn_timer matches 0 run function salman_f_rahman:forfeit_dividend

execute if score @s sfr_has_space matches 0 if score @s sfr_warn_timer matches 1.. run title @s actionbar [{"text":"Salman F Rahman Dividend: ","color":"gold"},{"score":{"name":"@s","objective":"sfr_warn_timer"},"color":"red"},{"text":" ticks remaining! Clear a slot!","color":"yellow"}]

execute if score @s sfr_has_space matches 0 if score @s sfr_warn_timer matches 160 run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1
execute if score @s sfr_has_space matches 0 if score @s sfr_warn_timer matches 120 run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1
execute if score @s sfr_has_space matches 0 if score @s sfr_warn_timer matches 80 run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.2
execute if score @s sfr_has_space matches 0 if score @s sfr_warn_timer matches 40 run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.4
execute if score @s sfr_has_space matches 0 if score @s sfr_warn_timer matches 20 run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.6
