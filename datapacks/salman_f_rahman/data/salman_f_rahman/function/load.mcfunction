scoreboard objectives add sfr_score dummy "Salman F Rahman"
scoreboard objectives setdisplay sidebar sfr_score

scoreboard objectives add m_stone minecraft.mined:minecraft.stone
scoreboard objectives add m_cobble minecraft.mined:minecraft.cobblestone
scoreboard objectives add m_deep minecraft.mined:minecraft.deepslate
scoreboard objectives add m_cdeep minecraft.mined:minecraft.cobbled_deepslate
scoreboard objectives add m_granite minecraft.mined:minecraft.granite
scoreboard objectives add m_diorite minecraft.mined:minecraft.diorite
scoreboard objectives add m_andesite minecraft.mined:minecraft.andesite
scoreboard objectives add m_tuff minecraft.mined:minecraft.tuff
scoreboard objectives add m_netherrack minecraft.mined:minecraft.netherrack
scoreboard objectives add m_blackstone minecraft.mined:minecraft.blackstone
scoreboard objectives add m_basalt minecraft.mined:minecraft.basalt
scoreboard objectives add m_end_stone minecraft.mined:minecraft.end_stone

scoreboard objectives add m_oak minecraft.mined:minecraft.oak_log
scoreboard objectives add m_spruce minecraft.mined:minecraft.spruce_log
scoreboard objectives add m_birch minecraft.mined:minecraft.birch_log
scoreboard objectives add m_jungle minecraft.mined:minecraft.jungle_log
scoreboard objectives add m_acacia minecraft.mined:minecraft.acacia_log
scoreboard objectives add m_dark_oak minecraft.mined:minecraft.dark_oak_log
scoreboard objectives add m_mangrove minecraft.mined:minecraft.mangrove_log
scoreboard objectives add m_cherry minecraft.mined:minecraft.cherry_log
scoreboard objectives add m_crimson minecraft.mined:minecraft.crimson_stem
scoreboard objectives add m_warped minecraft.mined:minecraft.warped_stem

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
