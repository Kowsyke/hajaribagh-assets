scoreboard objectives add sfr_score dummy "Salman F Rahman"
scoreboard objectives setdisplay sidebar sfr_score

scoreboard objectives add m_gold minecraft.mined:minecraft.gold_ore
scoreboard objectives add m_dgold minecraft.mined:minecraft.deepslate_gold_ore
scoreboard objectives add m_ngold minecraft.mined:minecraft.nether_gold_ore

scoreboard objectives add sfr_base dummy
scoreboard objectives add sfr_warn_timer dummy
scoreboard objectives add sfr_has_space dummy
scoreboard objectives add sfr_rainbow dummy
scoreboard objectives add sfr_temp dummy
scoreboard objectives add sfr_prev_time dummy
scoreboard objectives add sfr_cooldown dummy
scoreboard objectives add leaderboard trigger

team add sfr_tycoon "Salman F Rahman"
team modify sfr_tycoon prefix [{"text":"[Salman F Rahman] ","color":"gold","bold":true}]
team modify sfr_tycoon color gold

execute store result score #prev_daytime sfr_prev_time run time query day
scoreboard players set #cooldown sfr_cooldown 0

function salman_f_rahman:init_base_stats
function salman_f_rahman:update_scores
