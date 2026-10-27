execute as @e[type=#thepa:can_shoot_guns,type=!minecraft:player] if score GLOBAL mobWeaponFrequency matches 0 unless score @s randomWeaponSpawn matches 0.. store result score @s randomWeaponSpawn run random value 45..50

execute as @e[type=#thepa:can_shoot_guns,type=!minecraft:player] if score GLOBAL mobWeaponFrequency matches 1 unless score @s randomWeaponSpawn matches 0.. store result score @s randomWeaponSpawn run random value 1..200

execute as @e[type=#thepa:can_shoot_guns,type=!minecraft:player] if score GLOBAL mobWeaponFrequency matches 2 unless score @s randomWeaponSpawn matches 0.. store result score @s randomWeaponSpawn run random value 1..100

execute as @e[type=#thepa:can_shoot_guns,type=!minecraft:player] if score GLOBAL mobWeaponFrequency matches 3 unless score @s randomWeaponSpawn matches 0.. store result score @s randomWeaponSpawn run random value 1..50

execute as @e[type=#thepa:can_shoot_guns,type=!minecraft:player] if score GLOBAL mobWeaponFrequency matches 4 unless score @s randomWeaponSpawn matches 0.. store result score @s randomWeaponSpawn run random value 1..20

#44 Magnum
execute as @e[type=#minecraft:skeletons,nbt=!{equipment:{mainhand:{components:{"minecraft:custom_data":{gz_data:{}}}}}},scores={randomWeaponSpawn=1}] run item replace entity @s weapon.mainhand with minecraft:bow[minecraft:item_model="minecraft:guns/44_magnum",minecraft:custom_data={"gz_data": {"capacity": 6b, "bullets": 0b, "reload_time": 2.7d, "id": 17b, "debuff": -0.5d}, "HideFlags": 32},minecraft:custom_name={"translate": "thepa.item.name.gun_17","color": "yellow","italic": false},minecraft:lore=[{"translate": "thepa.item.desc.line1","color": "gray","italic": false}, {"text": "Reload Time: 3s","color": "blue","italic": false}, {"text":"Uses Bullets"}]]

#Musket
execute as @e[type=#minecraft:skeletons,nbt=!{equipment:{mainhand:{components:{"minecraft:custom_data":{gz_data:{}}}}}},scores={randomWeaponSpawn=2}] run item replace entity @s weapon.mainhand with minecraft:bow[minecraft:item_model="minecraft:guns/musket",minecraft:custom_data={"gz_data": {"capacity": 1b, "bullets": 0b, "reload_time": 3b, "id": 2b, "debuff": -0.8d}, "HideFlags": 32},minecraft:custom_name={"translate": "thepa.item.name.gun_2","color": "yellow","italic": false},minecraft:lore=[{"translate": "thepa.item.desc.line1","color": "gray","italic": false}, {"text": "Reload Time: 3s","color": "blue","italic": false}, {"text":"Uses Musket Balls"}]]


#M1 Garand
execute as @e[type=#minecraft:skeletons,nbt=!{equipment:{mainhand:{components:{"minecraft:custom_data":{gz_data:{}}}}}},scores={randomWeaponSpawn=3}] run item replace entity @s weapon.mainhand with minecraft:bow[minecraft:item_model="minecraft:guns/m1garand",minecraft:custom_data={"gz_data": {"capacity": 8b, "bullets": 0b, "reload_time": 1.5d, "id": 10b, "debuff": -0.5d}, "HideFlags": 32},minecraft:custom_name={"translate": "thepa.item.name.gun_10","color": "yellow","italic": false},minecraft:lore=[{"translate": "thepa.item.desc.line1","color": "gray","italic": false}, {"text": "Reload Time: 1.5s","color": "blue","italic": false}, {"text":"Uses Medium Rounds"}]]

#AR-15
execute as @e[type=#minecraft:skeletons,nbt=!{equipment:{mainhand:{components:{"minecraft:custom_data":{gz_data:{}}}}}},scores={randomWeaponSpawn=4}] run item replace entity @s weapon.mainhand with minecraft:bow[minecraft:item_model="minecraft:guns/ar_15",minecraft:custom_data={"gz_data": {"capacity": 30b, "bullets": 0b, "reload_time": 5b, "id": 16b, "debuff": -0.5d}, "HideFlags": 32},minecraft:custom_name={"translate": "thepa.item.name.gun_16","color": "yellow","italic": false},minecraft:lore=[{"translate": "thepa.item.desc.line1","color": "gray","italic": false}, {"text": "Reload Time: 5s","color": "blue","italic": false}, {"text":"Uses Medium Rounds"}]]

#Shotgun
execute as @e[type=#minecraft:skeletons,nbt=!{equipment:{mainhand:{components:{"minecraft:custom_data":{gz_data:{}}}}}},scores={randomWeaponSpawn=5}] run item replace entity @s weapon.mainhand with minecraft:bow[minecraft:item_model="minecraft:guns/pump_shotgun",minecraft:custom_data={"gz_data": {"capacity": 3b, "bullets": 0b, "reload_time": 1b, "id": 7b, "debuff": -0.5d}, "HideFlags": 32},minecraft:custom_name={"translate": "thepa.item.name.gun_7","color": "yellow","italic": false},minecraft:lore=[{"translate": "thepa.item.desc.line1","color": "gray","italic": false}, {"text": "Reload Time: 1s","color": "blue","italic": false}, {"text":"Uses Shells"}]]




#44 Magnum
execute as @e[type=pillager,nbt=!{equipment:{mainhand:{components:{"minecraft:custom_data":{gz_data:{}}}}}},scores={randomWeaponSpawn=1}] run item replace entity @s weapon.mainhand with minecraft:crossbow[minecraft:item_model="minecraft:guns/44_magnum",minecraft:custom_data={"gz_data": {"capacity": 6b, "bullets": 0b, "reload_time": 2.7d, "id": 17b, "debuff": -0.5d}, "HideFlags": 32},minecraft:custom_name={"translate": "thepa.item.name.gun_17","color": "yellow","italic": false},minecraft:lore=[{"translate": "thepa.item.desc.line1","color": "gray","italic": false}, {"text": "Reload Time: 3s","color": "blue","italic": false}, {"text":"Uses Bullets"}]]

#Musket
execute as @e[type=pillager,nbt=!{equipment:{mainhand:{components:{"minecraft:custom_data":{gz_data:{}}}}}},scores={randomWeaponSpawn=2}] run item replace entity @s weapon.mainhand with minecraft:crossbow[minecraft:item_model="minecraft:guns/musket",minecraft:custom_data={"gz_data": {"capacity": 1b, "bullets": 0b, "reload_time": 3b, "id": 2b, "debuff": -0.8d}, "HideFlags": 32},minecraft:custom_name={"translate": "thepa.item.name.gun_2","color": "yellow","italic": false},minecraft:lore=[{"translate": "thepa.item.desc.line1","color": "gray","italic": false}, {"text": "Reload Time: 3s","color": "blue","italic": false}, {"text":"Uses Musket Balls"}]]


#M1 Garand
execute as @e[type=pillager,nbt=!{equipment:{mainhand:{components:{"minecraft:custom_data":{gz_data:{}}}}}},scores={randomWeaponSpawn=3}] run item replace entity @s weapon.mainhand with minecraft:crossbow[minecraft:item_model="minecraft:guns/m1garand",minecraft:custom_data={"gz_data": {"capacity": 8b, "bullets": 0b, "reload_time": 1.5d, "id": 10b, "debuff": -0.5d}, "HideFlags": 32},minecraft:custom_name={"translate": "thepa.item.name.gun_10","color": "yellow","italic": false},minecraft:lore=[{"translate": "thepa.item.desc.line1","color": "gray","italic": false}, {"text": "Reload Time: 1.5s","color": "blue","italic": false}, {"text":"Uses Medium Rounds"}]]

#AR-15
execute as @e[type=pillager,nbt=!{equipment:{mainhand:{components:{"minecraft:custom_data":{gz_data:{}}}}}},scores={randomWeaponSpawn=4}] run item replace entity @s weapon.mainhand with minecraft:crossbow[minecraft:item_model="minecraft:guns/ar_15",minecraft:custom_data={"gz_data": {"capacity": 30b, "bullets": 0b, "reload_time": 5b, "id": 16b, "debuff": -0.5d}, "HideFlags": 32},minecraft:custom_name={"translate": "thepa.item.name.gun_16","color": "yellow","italic": false},minecraft:lore=[{"translate": "thepa.item.desc.line1","color": "gray","italic": false}, {"text": "Reload Time: 5s","color": "blue","italic": false}, {"text":"Uses Medium Rounds"}]]

#Shotgun
execute as @e[type=minecraft:pillager,nbt=!{equipment:{mainhand:{components:{"minecraft:custom_data":{gz_data:{}}}}}},scores={randomWeaponSpawn=5}] run item replace entity @s weapon.mainhand with minecraft:crossbow[minecraft:item_model="minecraft:guns/pump_shotgun",minecraft:custom_data={"gz_data": {"capacity": 3b, "bullets": 0b, "reload_time": 1b, "id": 7b, "debuff": -0.5d}, "HideFlags": 32},minecraft:custom_name={"translate": "thepa.item.name.gun_7","color": "yellow","italic": false},minecraft:lore=[{"translate": "thepa.item.desc.line1","color": "gray","italic": false}, {"text": "Reload Time: 1s","color": "blue","italic": false}, {"text":"Uses Shells"}]]


execute as @e[type=minecraft:item,nbt={Item:{id:"minecraft:bow",components:{"minecraft:custom_data":{gz_data:{}}}}}] run data merge entity @s {Item:{id:"minecraft:carrot_on_a_stick"}}
execute as @e[type=minecraft:item,nbt={Item:{id:"minecraft:crossbow",components:{"minecraft:custom_data":{gz_data:{}}}}}] run data merge entity @s {Item:{id:"minecraft:carrot_on_a_stick"}}

execute if entity @e[type=#thepa:can_shoot_guns,type=!minecraft:player,scores={randomWeaponSpawn=1..5}] as @e[type=#minecraft:skeletons,nbt={equipment:{mainhand:{components:{"minecraft:custom_data":{gz_data:{}}}}}}] run function thepa:shoot/mobs/skeleton

execute if entity @e[type=#thepa:can_shoot_guns,type=!minecraft:player,scores={randomWeaponSpawn=1..5}] as @e[type=pillager,nbt={equipment:{mainhand:{components:{"minecraft:custom_data":{gz_data:{}}}}}}] run function thepa:shoot/mobs/pillager