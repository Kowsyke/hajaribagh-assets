
tag @a[tag=gun53recoil,scores={scope_timer=1..}] add gz_offhand
tag @a[tag=gun53recoil,scores={scope_timer=1..}] remove gz_mainhand
execute if score GLOBAL recoil matches 1 as @a[tag=gun53recoil,tag=gz_mainhand] at @a[tag=gun53recoil,tag=gz_mainhand] run tp @a[tag=gun53recoil,tag=gz_mainhand] ~ ~ ~ ~ ~-0.6
execute if score GLOBAL recoil matches 1 as @a[tag=gun53recoil,tag=gz_offhand] at @a[tag=gun53recoil,tag=gz_offhand] run tp @a[tag=gun53recoil,tag=gz_offhand] ~ ~ ~ ~ ~-0.1
tag @a[tag=gun53recoil] remove gun53recoil

