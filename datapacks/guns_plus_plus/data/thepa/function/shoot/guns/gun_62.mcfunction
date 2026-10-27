
execute as @a[tag=minigun_autofire] at @s run function thepa:projectiles/spawn/bullet_62 with entity @s
execute as @a[tag=minigun_autofire] at @s run tag @s add gz_shoot
execute as @a[tag=minigun_autofire] at @s run execute at @s run playsound guns:mini_shoot player @a ~ ~ ~ 5 1
execute as @a[tag=minigun_autofire] at @s run execute if score GLOBAL camera matches 1 run function thepa:recoil_types/camera/gun_5

execute as @a[tag=minigun_autofire] at @s run execute if score GLOBAL recoil matches 1 run tag @s add gun5recoil
execute as @a[tag=minigun_autofire] at @s run execute if score GLOBAL recoil matches 1 at @s as @s run schedule function thepa:recoil_types/recoil/gun_5_recoil 1t
execute as @a[tag=minigun_autofire,tag=!inf_reload] at @s run clear @s minecraft:clock[minecraft:custom_data~{gz_data:{bullet_type:6b}}|minecraft:custom_data~{gz_data:{bullet_type:6}}] 1

execute as @a[tag=minigun_autofire] at @s if score @s scope_timer matches ..0 run return run tag @s remove minigun_autofire
execute as @a[tag=minigun_autofire] at @s run scoreboard players set @s minigun_sounds 11

schedule function thepa:shoot/guns/gun_62 3t