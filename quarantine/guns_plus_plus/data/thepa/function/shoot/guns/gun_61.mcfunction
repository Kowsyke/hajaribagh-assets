tag @s[scores={scope_timer=1..}] add gz_offhand
tag @s[scores={scope_timer=1..}] remove gz_mainhand


execute if score @s shotcounter matches 5 store result storage gz:update save_data.id int 1 run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.id
execute if score @s shotcounter matches 5 store result storage gz:update save_data.reload_time double 1 run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.reload_time
execute if score @s shotcounter matches 5 store result storage gz:update save_data.capacity int 1 run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.capacity
execute if score @s shotcounter matches 5 store result storage gz:update save_data.bullets int 1 run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.bullets
execute if score @s shotcounter matches 5 store result storage gz:update save_data.debuff double 0.1 run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.debuff 10
execute store result storage gz:update save_data.shooting_delay int 1 run data get storage gz:shooting_delays shooting_delays[61]
execute if score @s shotcounter matches 5 run data modify storage gz:update save_data.item_model set value "minecraft:guns/poweruprifle_hot"

execute if score @s shotcounter matches 5 run function thepa:utilities/update_handler/update_patch_1_21_11 with storage gz:update save_data
execute if score @s shotcounter matches 5 run data remove storage gz:update save_data

execute if score @s shotcounter matches 5 run item modify entity @s weapon.mainhand {type:"set_components",components:{item_model:"minecraft:guns/poweruprifle_hot_sc"}}

function thepa:projectiles/spawn/bullet_61 with entity @s


execute anchored eyes positioned ^ ^1.5 ^1.5 run particle minecraft:explosion ~ ~ ~ 0 0 0 0 1

execute if score GLOBAL camera matches 1 run function thepa:recoil_types/camera/gun_7


execute if score GLOBAL recoil matches 1 run tag @s add gun31recoil
execute if score GLOBAL recoil matches 1 at @s as @s run schedule function thepa:recoil_types/recoil/gun_7_recoil 1t
execute at @s run playsound guns:rampup_shoot master @a ~ ~ ~ 0.3 1
