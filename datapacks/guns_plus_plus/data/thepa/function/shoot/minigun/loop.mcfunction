execute if entity @a[scores={gz_id=62}] as @a[scores={gz_id=62}] store result score @s gz_capacity run clear @s minecraft:clock[minecraft:custom_data~{gz_data:{bullet_type:6b}}|minecraft:custom_data~{gz_data:{bullet_type:6}}] 0
scoreboard players remove @a[scores={minigun_sounds=1..}] minigun_sounds 1
scoreboard players reset @a[scores={minigun_sounds=0}] minigun_sounds
execute as @a[scores={minigun_sounds=0}] at @s run playsound guns:mini_stop master @s ~ ~ ~ 1


execute if entity @e[scores={minigunCharge=1..},nbt={SelectedItem:{components:{"minecraft:custom_data":{gz_data:{id:5b}}}}}] run scoreboard players add @e[nbt={SelectedItem:{"minecraft:custom_data":{gz_data:{id:5b}}}},scores={minigunCharge=1..}] chargeTime 10
execute if entity @e[scores={minigunCharge=1..},nbt={equipment:{offhand:{ components:{"minecraft:custom_data":{gz_data:{id:5b}}}}}}] run scoreboard players add @e[nbt={equipment:{offhand:{ "minecraft:custom_data":{gz_data:{id:5b}}}}},scores={minigunCharge=1..}] chargeTime 10
scoreboard players reset @a[scores={chargeTime=301..}] chargeTime