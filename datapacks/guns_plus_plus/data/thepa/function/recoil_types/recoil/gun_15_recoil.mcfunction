tag @a[tag=gun15recoil,scores={scope_timer=1..}] add gz_offhand
tag @a[tag=gun15recoil,scores={scope_timer=1..}] remove gz_mainhand

execute if score GLOBAL recoil matches 1 as @a[tag=gun15recoil,tag=gz_mainhand] at @s run tp @s ~ ~ ~ ~ ~-10
execute if score GLOBAL recoil matches 1 as @a[tag=gun15recoil,tag=gz_offhand] at @s run tp @s ~ ~ ~ ~ ~-3
tag @a[tag=gun15recoil] remove gun15recoil

