
execute as @e[type=minecraft:item,limit=1,nbt={Item:{components:{"minecraft:item_model":"minecraft:misc/lasersight"}}}] at @s if entity @e[type=minecraft:item,limit=1,nbt={Item:{components:{"minecraft:custom_data":{gz_data:{id:11b}}}}},distance=..1] run tag @e[type=minecraft:item,distance=..1] add laserRem11

execute as @e[tag=laserRem11,limit=1] at @e[tag=laserRem11,limit=1] run summon item ~ ~ ~ {Item:{id:"minecraft:carrot_on_a_stick",count:1,components:{"minecraft:custom_name":{"color":"yellow","italic":false,"translate":"thepa.item.name.gun_11_l"},"minecraft:lore":[{"color":"gray","italic":false,"translate":"thepa.item.desc.line1"},{"color":"blue","italic":false,"text":"Reload Time: 5.5s"},{"text":"Uses Heavy Rounds"}],"minecraft:item_model":"minecraft:guns/awp/awp_l","minecraft:custom_data":{gz_data:{capacity:1b, bullets:0b, debuff:-200d, reload_time:6b, id:40b, laser:1b, sniper:1b},HideFlags:32}}}}
kill @e[tag=laserRem11,type=minecraft:item]

execute as @e[type=minecraft:item,limit=1,nbt={Item:{components:{"minecraft:item_model":"minecraft:misc/lasersight"}}}] at @s if entity @e[type=minecraft:item,limit=1,nbt={Item:{components:{"minecraft:custom_data":{gz_data:{id:21b}}}}},distance=..1] run tag @e[type=minecraft:item,distance=..1] add laserRem21

execute as @e[tag=laserRem21,limit=1] at @e[tag=laserRem21,limit=1] run summon item ~ ~ ~ {Item:{id:"minecraft:carrot_on_a_stick",count:1,components:{"minecraft:item_model":"minecraft:guns/hunting_rifle/hunting_rifle_l", 'minecraft:custom_data': {'gz_data': {'capacity': 1b, 'bullets': 0b, 'reload_time': 3b, 'id': 41b, 'debuff': -200d,'laser':1b, 'sniper': 1b}, 'HideFlags': 32b}, 'minecraft:item_name': {"translate": "thepa.item.name.gun_21_l","color": "yellow","italic": false}, 'minecraft:lore': [{"translate": "thepa.item.desc.line1","color": "gray","italic": false}, {"text": "Reload Time: 3s","color": "blue","italic": false}, {"text":"Uses Heavy Rounds"}]}}}
kill @e[tag=laserRem21,type=minecraft:item]

execute as @e[type=minecraft:item,limit=1,nbt={Item:{components:{"minecraft:item_model":"minecraft:misc/lasersight"}}}] at @s if entity @e[type=minecraft:item,limit=1,nbt={Item:{components:{"minecraft:custom_data":{gz_data:{id:22b}}}}},distance=..1] run tag @e[type=minecraft:item,distance=..1] add laserRem22

execute as @e[tag=laserRem22,limit=1] at @e[tag=laserRem22,limit=1] run summon item ~ ~ ~ {Item:{id:"minecraft:carrot_on_a_stick",count:1,components:{"minecraft:item_model":"minecraft:guns/ssg08/ssg08_l", 'minecraft:custom_data': {'gz_data': {'capacity': 1b, 'bullets': 0b, 'reload_time': 6b, 'id': 42b, 'debuff': -200d,'laser':1b, 'sniper': 1b}, 'HideFlags': 32}, 'minecraft:item_name': {"translate": "thepa.item.name.gun_22_l","color": "yellow","italic": false}, 'minecraft:lore': [{"translate": "thepa.item.desc.line1","color": "gray","italic": false}, {"text": "Reload Time: 6s","color": "blue","italic": false}, {"text":"Uses Heavy Rounds"}]}}}
kill @e[tag=laserRem22,type=minecraft:item]
