
execute store result score @s gz_capacity run clear @s minecraft:clock[minecraft:custom_data~{gz_data:{bullet_type:6b}}|minecraft:custom_data~{gz_data:{bullet_type:6}}] 0
execute store result score @s gz_bullets run clear @s minecraft:clock[minecraft:custom_data~{gz_data:{bullet_type:6b}}|minecraft:custom_data~{gz_data:{bullet_type:6}}] 0
execute if entity @s[tag=inf_reload] run scoreboard players set @s gz_bullets 999
execute if entity @s[tag=inf_reload] run scoreboard players set @s gz_capacity 999