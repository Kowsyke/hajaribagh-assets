tag @s[scores={scope_timer=1..}] add gz_offhand
tag @s[scores={scope_timer=1..}] remove gz_mainhand
function thepa:projectiles/spawn/bullet_1 with entity @s

execute anchored eyes positioned ^ ^0.2 ^1.2 run particle block{block_state:"minecraft:diamond_block"} ~ ~ ~ 0 0 0 0 5
execute if score GLOBAL recoil matches 1 run tp @s ~ ~ ~ ~ ~-10



execute at @s run playsound guns:musket_shoot player @s ~ ~ ~ 0.3 1