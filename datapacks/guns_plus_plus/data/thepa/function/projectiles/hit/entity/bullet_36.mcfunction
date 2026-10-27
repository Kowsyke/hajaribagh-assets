
execute if entity @e[distance=0,type=!#thepa:unaffected,type=!player] run tag @e[distance=0,type=!#thepa:unaffected,type=!player] add dolnonplayer
execute if entity @e[distance=0,type=player] run tag @e[distance=0,type=player] add dolplayer
execute if entity @e[distance=0,type=player] run tag @e[distance=0,type=player] add dolplayer1

execute positioned ^ ^ ^-0.2 run particle minecraft:splash ~ ~ ~ 0 0 0 0 5
