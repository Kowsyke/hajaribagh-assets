# Reset gold mining counters and title holder for a fresh competition.

scoreboard objectives remove m_gold
scoreboard objectives remove m_dgold
scoreboard objectives remove m_ngold

scoreboard objectives add m_gold minecraft.mined:minecraft.gold_ore
scoreboard objectives add m_dgold minecraft.mined:minecraft.deepslate_gold_ore
scoreboard objectives add m_ngold minecraft.mined:minecraft.nether_gold_ore

scoreboard players reset * sfr_score
scoreboard players reset * sfr_base
scoreboard players reset * m_gold
scoreboard players reset * m_dgold
scoreboard players reset * m_ngold

execute as @a[tag=is_sfr] run function salman_f_rahman:dethrone

scoreboard players set #reset_marker sfr_temp 1

tellraw @a [{"text":"[Salman F Rahman] ","color":"gold","bold":true},{"text":"Gold mining scores have been reset. Mine the most gold ore to claim the title!","color":"yellow"}]
