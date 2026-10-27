tag @s[scores={scope_timer=1..}] add gz_offhand
tag @s[scores={scope_timer=1..}] remove gz_mainhand

function thepa:projectiles/spawn/bullet_1 with entity @s

execute anchored eyes positioned ^ ^0.2 ^1.2 run particle block{block_state:"minecraft:diamond_block"} ~ ~ ~ 0 0 0 0 5
execute if score GLOBAL recoil matches 1 run tp @s ~ ~ ~ ~ ~-1.5

execute at @s run playsound minecraft:entity.slime.jump master @a ~ ~ ~ 0.5 2
execute at @s run playsound minecraft:entity.firework_rocket.blast player @a ~ ~ ~ 0.5 1.5