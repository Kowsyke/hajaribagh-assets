#mc-build WASD content
scoreboard objectives add wasd_data_packs dummy
scoreboard players set wasd_bosses wasd_data_packs 1
scoreboard objectives add w.bosses_setting dummy
function wasd.bosses:config
schedule function wasd.bosses:check_installed_packs 30t replace
#fire
#water
#electric
#earth
#metal
#air
#chicken
#husk
#skeleton
#piglin_brute