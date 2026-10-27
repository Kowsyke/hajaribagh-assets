execute store result storage gz:single_item save_data.id int 1 run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.id
execute store result storage gz:single_item save_data.reload_time double 1 run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.reload_time
execute store result storage gz:single_item save_data.capacity int 1 run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.capacity
execute store result storage gz:single_item save_data.bullets int 1 run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.bullets
execute store result storage gz:single_item save_data.debuff double 0.1 run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.debuff 10
$execute store result storage gz:single_item save_data.shooting_delay int 1 run data get storage gz:shooting_delays shooting_delays[$(id)]
$data modify storage gz:single_item save_data.item_model set $(path)

function thepa:utilities/single_ammo_model_dummy with storage gz:single_item save_data
