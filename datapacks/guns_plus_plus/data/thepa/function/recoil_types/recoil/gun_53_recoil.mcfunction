
tag @a[tag=gun53recoil,scores={scope_timer=1..}] add gz_offhand
tag @a[tag=gun53recoil,scores={scope_timer=1..}] remove gz_mainhand
execute as @a[tag=gun53recoil,tag=gz_mainhand] at @a[tag=gun53recoil,tag=gz_mainhand] run tp @a[tag=gun53recoil,tag=gz_mainhand] ~ ~ ~ ~ ~-6
execute as @a[tag=gun53recoil,tag=gz_offhand] at @a[tag=gun53recoil,tag=gz_offhand] run tp @a[tag=gun53recoil,tag=gz_offhand] ~ ~ ~ ~ ~-1
tag @a[tag=gun53recoil] remove gun53recoil

