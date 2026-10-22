function salman_f_rahman:update_scores
function salman_f_rahman:check_winner

execute if entity @a[tag=is_sfr] run function salman_f_rahman:rainbow_step

execute if score #cooldown sfr_cooldown matches 1.. run scoreboard players remove #cooldown sfr_cooldown 1

execute store result score #curr_daytime sfr_temp run time query day
execute if score #curr_daytime sfr_temp < #prev_daytime sfr_prev_time run function salman_f_rahman:on_new_day
scoreboard players operation #prev_daytime sfr_prev_time = #curr_daytime sfr_temp

execute as @a[scores={sfr_warn_timer=1..}] at @s run function salman_f_rahman:handle_warn_countdown

scoreboard players enable @a leaderboard
execute as @a[scores={leaderboard=1..}] at @s run scoreboard objectives setdisplay sidebar sfr_score
execute as @a[scores={leaderboard=1..}] at @s run tellraw @s [{"text":"[Salman F Rahman] ","color":"gold","bold":true},{"text":"Leaderboard sidebar display refreshed!","color":"green"}]
scoreboard players set @a[scores={leaderboard=1..}] leaderboard 0
