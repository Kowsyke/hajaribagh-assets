#mc-build WASD content
particle end_rod ~ ~1 ~ 0.2 0.3 0.2 0.02 2 normal
particle dust_color_transition{from_color:[1.0, 0.984, 0.02], scale:1.0, to_color:[1.0, 0.969, 0.557]} ~ ~1 ~ 0.2 0.3 0.2 0.02 2 normal
particle falling_dust{block_state:{id:"minecraft:yellow_concrete"}} ~ ~0.1 ~ 0.2 0.05 0.2 0 2 normal
execute unless entity @s[nbt={Fire:-1s}] run data merge entity @s {Fire:-1s}
execute if entity @a[gamemode=!creative,gamemode=!spectator,distance=..25] run scoreboard players add @s wasd.timer 1
execute as @s[scores={wasd.timer=130..}] run function wasd.bosses:boss/zzz/19