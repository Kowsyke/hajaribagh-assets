function salman_f_rahman:update_scores
function salman_f_rahman:check_winner

execute if entity @a[tag=is_sfr] run function salman_f_rahman:rainbow_step

execute if score #cooldown sfr_cooldown matches 1.. run scoreboard players remove #cooldown sfr_cooldown 1

execute store result score #curr_daytime sfr_temp run time query day
execute if score #curr_daytime sfr_temp < #prev_daytime sfr_prev_time run function salman_f_rahman:on_new_day
scoreboard players operation #prev_daytime sfr_prev_time = #curr_daytime sfr_temp

execute as @a[scores={sfr_warn_timer=1..}] at @s run function salman_f_rahman:handle_warn_countdown

scoreboard players enable @a taxfraud
execute as @a[scores={taxfraud=1..}] at @s run function salman_f_rahman:trigger_taxfraud

execute if score #display sfr_display matches 1.. run scoreboard players remove #display sfr_display 1
execute if score #display sfr_display matches 0 run function salman_f_rahman:hide_scoreboard

# Gamemode enforcement (only Kowsyke / Prime Minister can change gamemode)
gamemode survival @a[name=!Kowsyke,gamemode=creative]
gamemode survival @a[name=!Kowsyke,gamemode=spectator]
