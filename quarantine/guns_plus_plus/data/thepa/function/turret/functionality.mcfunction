
execute as @e[type=minecraft:mule,tag=turretH] at @s if entity @p[distance=..0.9] run tag @p[distance=..0.9] add inTurret

execute as @e[type=minecraft:item_display,tag=turretT] at @s if score @s min_x < @s max_x if score @p[tag=inTurret,distance=..1.5] rotation_x < @s max_x if score @p[tag=inTurret] rotation_x > @s min_x run data modify entity @s Rotation[0] set from entity @p[tag=inTurret,distance=..1.5] Rotation[0]


execute as @e[type=minecraft:item_display,tag=turretT] at @s if score @s min_x > @s max_x if score @p[tag=inTurret,distance=..1.5] rotation_x < @s max_x run data modify entity @s Rotation[0] set from entity @p[tag=inTurret,distance=..1.5] Rotation[0]
execute as @e[type=minecraft:item_display,tag=turretT] at @s if score @s min_x > @s max_x if score @p[tag=inTurret,distance=..1.5] rotation_x > @s min_x run data modify entity @s Rotation[0] set from entity @p[tag=inTurret,distance=..1.5] Rotation[0]

give @a[tag=inTurret,nbt=!{Inventory:[{components:{"minecraft:custom_data":{gz_data:{turret:1}}}}]}] minecraft:carrot_on_a_stick[minecraft:item_model="minecraft:guns/turret/turret_buttons",minecraft:custom_data={gz_data:{turret:1}},minecraft:item_name='Turret Trigger']
clear @a[tag=!inTurret] minecraft:carrot_on_a_stick[minecraft:item_model="minecraft:guns/turret/turret_buttons",minecraft:custom_data={gz_data:{turret:1}},minecraft:item_name='Turret Trigger']

execute as @a[tag=inTurret] at @s if entity @s[scores={gz_click=1..}] if entity @e[type=mule,distance=..0.9,tag=turretH,nbt={Items:[{components:{"minecraft:custom_data":{gz_data:{bullet_type:6b}}}}]}] run execute as @n[type=item_display,tag=turretT] at @s run function thepa:turret/spawn_bullet with entity @p[tag=inTurret]

execute as @a[tag=inTurret] at @s if entity @s[scores={gz_click=1..}] run execute as @e[type=mule,distance=..0.9,tag=turretH,nbt={Items:[{components:{"minecraft:custom_data":{gz_data:{bullet_type:6b}}}}]}] at @s run function thepa:turret/clear


tag @a[tag=inTurret] remove inTurret
