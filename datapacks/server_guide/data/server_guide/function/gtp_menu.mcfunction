# GTA Fast Travel & Radar Menu
tellraw @s [{"text":"======================================","color":"yellow","bold":true}]
tellraw @s [{"text":"   ✦ HAJARIBAGH RAPID TRANSIT (GTA) ✦","color":"gold","bold":true}]
tellraw @s [{"text":"======================================","color":"yellow","bold":true}]
tellraw @s [{"text":"Click a destination for cinematic sky transit:\n","color":"gray"}]
tellraw @s [{"text":"  [ 🏠 Teleport to Base ]","color":"green","bold":true,"click_event":{"action":"run_command","command":"/trigger tp_base"},"hover_event":{"action":"show_text","value":{"text":"Fly to Base at (163, 100, -307) with GTA sky transit","color":"yellow"}}}]
tellraw @s [{"text":"  [ 📍 Teleport to Spawn ]","color":"aqua","bold":true,"click_event":{"action":"run_command","command":"/trigger tp_spawn"},"hover_event":{"action":"show_text","value":{"text":"Fly to World Spawn with GTA sky transit","color":"yellow"}}}]
tellraw @s [{"text":"  [ 🗺️ Equip Radar Minimap ]","color":"light_purple","bold":true,"click_event":{"action":"run_command","command":"/trigger minimap"},"hover_event":{"action":"show_text","value":{"text":"Equip live radar map in your offhand slot","color":"yellow"}}}]
tellraw @s [{"text":"--------------------------------------","color":"yellow"}]
