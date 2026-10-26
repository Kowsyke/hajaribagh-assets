# Safely deliver Hajaribagh Radar Minimap without deleting offhand item
give @s minecraft:filled_map[minecraft:map_id=0,minecraft:custom_name='{"text":"✦ Hajaribagh Radar Minimap ✦","color":"gold","bold":true}'] 1
playsound minecraft:ui.cartography_table.take_result player @s ~ ~ ~ 1 1
tellraw @s [{"text":"[Hajaribagh] ","color":"gold","bold":true},{"text":"Radar Minimap placed in your inventory. Press [F] to swap it to your left hand whenever you wish. Your shield and offhand items remain safe.","color":"green"}]
