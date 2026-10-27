execute as @s[scores={gz_id=62},tag=minigun_autofire] at @s run return run tag @s remove minigun_autofire



execute as @s[scores={gz_id=62},tag=!minigun_autofire,tag=!inf_reload] at @s if data entity @s Inventory[{id:"minecraft:clock",components:{"minecraft:custom_data":{gz_data:{bullet_type:6b}}}}] positioned as @s run function thepa:shoot/guns/gun_62
execute as @s[scores={gz_id=62},tag=!minigun_autofire,tag=!inf_reload] at @s if data entity @s Inventory[{id:"minecraft:clock",components:{"minecraft:custom_data":{gz_data:{bullet_type:6b}}}}] run tag @s add minigun_autofire

execute as @s[scores={gz_id=62},tag=!minigun_autofire,tag=inf_reload] at @s positioned as @s run function thepa:shoot/guns/gun_62
execute as @s[scores={gz_id=62},tag=!minigun_autofire,tag=inf_reload] at @s run tag @s add minigun_autofire
