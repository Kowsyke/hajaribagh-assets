#mc-build WASD content
particle falling_water ~ ~1 ~ 0.2 0.3 0.2 0.02 2 normal
particle dust_color_transition{from_color:[0.094, 0.153, 0.988], scale:1.0, to_color:[0.106, 0.643, 1.0]} ~ ~1 ~ 0.2 0.3 0.2 0.02 2 normal
particle falling_dust{block_state:{id:"minecraft:blue_concrete"}} ~ ~0.1 ~ 0.2 0.05 0.2 0 2 normal
execute if entity @a[gamemode=!creative,gamemode=!spectator,distance=..25] run scoreboard players add @s wasd.timer 1
execute as @s[scores={wasd.timer=130..}] run function wasd.bosses:boss/zzz/9