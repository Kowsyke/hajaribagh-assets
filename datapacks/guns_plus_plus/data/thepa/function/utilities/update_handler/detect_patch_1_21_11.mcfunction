execute store result storage gz:update save_data.id int 1 run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.id
execute store result storage gz:update save_data.reload_time double 1 run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.reload_time
execute store result storage gz:update save_data.capacity int 1 run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.capacity
execute store result storage gz:update save_data.bullets int 1 run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.bullets
execute store result storage gz:update save_data.debuff double 0.1 run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.debuff 10
$execute store result storage gz:update save_data.shooting_delay int 1 run data get storage gz:shooting_delays shooting_delays[$(id)]

execute store result score @s gz_id run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.id
execute store result score @s gz_bullets run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.bullets

item modify entity @s[scores={gz_id=19}] weapon.mainhand {"type": "minecraft:set_components","components": {"minecraft:item_model": "minecraft:guns/rpg"}}
item modify entity @s[scores={gz_id=11}] weapon.mainhand {"type": "minecraft:set_components","components": {"minecraft:item_model": "minecraft:guns/awp/awp"}}
item modify entity @s[scores={gz_id=30}] weapon.mainhand {"type": "minecraft:set_components","components": {"minecraft:item_model": "minecraft:guns/awp/awp_s"}}
item modify entity @s[scores={gz_id=40}] weapon.mainhand {"type": "minecraft:set_components","components": {"minecraft:item_model": "minecraft:guns/awp/awp_l"}}
item modify entity @s[scores={gz_id=22}] weapon.mainhand {"type": "minecraft:set_components","components": {"minecraft:item_model": "minecraft:guns/ssg08/ssg08"}}
item modify entity @s[scores={gz_id=38}] weapon.mainhand {"type": "minecraft:set_components","components": {"minecraft:item_model": "minecraft:guns/ssg08/ssg08_s"}}
item modify entity @s[scores={gz_id=42}] weapon.mainhand {"type": "minecraft:set_components","components": {"minecraft:item_model": "minecraft:guns/ssg08/ssg08_l"}}
item modify entity @s[scores={gz_id=21}] weapon.mainhand {"type": "minecraft:set_components","components": {"minecraft:item_model": "minecraft:guns/hunting_rifle/hunting_rifle"}}
item modify entity @s[scores={gz_id=36}] weapon.mainhand {"type": "minecraft:set_components","components": {"minecraft:item_model": "minecraft:guns/hunting_rifle/hunting_rifle_s"}}
item modify entity @s[scores={gz_id=41}] weapon.mainhand {"type": "minecraft:set_components","components": {"minecraft:item_model": "minecraft:guns/hunting_rifle/hunting_rifle_l"}}
item modify entity @s[scores={gz_id=43}] weapon.mainhand {"type": "minecraft:set_components","components": {"minecraft:item_model": "minecraft:guns/dragonsniper"}}
item modify entity @s[scores={gz_id=46}] weapon.mainhand {"type": "minecraft:set_components","components": {"minecraft:item_model": "minecraft:guns/autosniper"}}
item modify entity @s[scores={gz_id=51}] weapon.mainhand {"type": "minecraft:set_components","components": {"minecraft:item_model": "minecraft:guns/scoped_revolver"}}


data modify storage gz:update save_data.item_model set from entity @s SelectedItem.components."minecraft:item_model"
function thepa:utilities/update_handler/update_patch_1_21_11 with storage gz:update save_data
data remove storage gz:update save_data
