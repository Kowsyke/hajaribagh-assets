#mc-build WASD content
particle block{block_state:{id:"minecraft:stone"}} ~ ~1 ~ 0.1 0.3 0.1 0.02 2 normal
particle smoke ~ ~1 ~ 0.1 0.3 0.1 0.04 2 normal
particle falling_dust{block_state:{id:"minecraft:gray_concrete"}} ~ ~0.1 ~ 0.2 0.05 0.2 0 2 normal
execute if entity @a[gamemode=!creative,gamemode=!spectator,distance=..25] run scoreboard players add @s wasd.timer 1
execute as @s[scores={wasd.timer=80..}] run function wasd.bosses:boss/zzz/35