scoreboard players set #max sfr_score 0
execute as @a if score @s sfr_score > #max sfr_score run scoreboard players operation #max sfr_score = @s sfr_score

execute as @a[team=sfr_tycoon,tag=!is_sfr] run function salman_f_rahman:dethrone
execute as @a[tag=is_sfr] if score @s sfr_score < #max sfr_score run function salman_f_rahman:dethrone
execute as @a[tag=!is_sfr] if score @s sfr_score = #max sfr_score if score #max sfr_score matches 1.. unless entity @a[tag=is_sfr] run function salman_f_rahman:crown_winner

execute as @a[tag=is_sfr,team=!sfr_tycoon] run team join sfr_tycoon @s

