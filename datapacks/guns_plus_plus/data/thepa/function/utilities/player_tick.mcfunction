#Fix Broken Items
#execute if items entity @s weapon.mainhand *[!minecraft:custom_data~{gz_data:{}},minecraft:equippable~{}] run item modify entity @s weapon.mainhand [{"function":"minecraft:set_components","components":{"!minecraft:equippable":{}}}]


execute if entity @s[tag=gz_shoot] run function thepa:shoot/shoot
execute if entity @s[tag=gz_reloading] run function thepa:reload/timer
execute if entity @s[scores={gz_click=1..}] at @s run function thepa:items/select_click

execute if score GLOBAL bloom matches 0 run scoreboard players set @a bloomRandom 21
execute if score GLOBAL bloom matches 1 run scoreboard players add @a bloomRandom 1

execute if score GLOBAL camera matches 0 run scoreboard players set @a cameraRandom 21
execute if score GLOBAL camera matches 1 run scoreboard players add @a cameraRandom 1

execute if entity @e[scores={cameraRandom=22..}] run scoreboard players reset @a[scores={cameraRandom=22..}] cameraRandom
execute if entity @e[scores={bloomRandom=22..}] run scoreboard players reset @a[scores={bloomRandom=22..}] bloomRandom

execute as @e[scores={ageflare=7..8},tag=gz_bullet_9] at @e[scores={ageflare=7..8},tag=gz_bullet_9] run playsound guns:flare_explode master @a[distance=..50] ~ ~ ~ 10 1

execute if entity @s[nbt={SelectedItem:{components:{"minecraft:custom_data":{gz_data:{}}}}}] unless data entity @s SelectedItem.components."minecraft:custom_data".gz_data.normal_model run function thepa:utilities/update_handler/detect_patch_1_21_11 with entity @s SelectedItem.components."minecraft:custom_data".gz_data

execute if entity @s[nbt={SelectedItem:{components:{"minecraft:custom_data":{gz_data:{}}}}}] unless data entity @s SelectedItem.components."minecraft:custom_data".gz_data.shooting_delay run function thepa:utilities/update_handler/detect_patch_1_21_11 with entity @s SelectedItem.components."minecraft:custom_data".gz_data

execute store result score @s[nbt={SelectedItem:{components:{"minecraft:custom_data":{gz_data:{}}}}}] gz_id run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.id
execute store result score @s[nbt={SelectedItem:{components:{"minecraft:custom_data":{gz_data:{}}}}}] gz_bullets run data get entity @s SelectedItem.components.minecraft:custom_data.gz_data.bullets

execute if score GLOBAL legacyControls matches 0 if score @s scope_timer matches 1.. run function thepa:utilities/scopes
execute if score GLOBAL legacyControls matches 0 run function thepa:utilities/modern_controls