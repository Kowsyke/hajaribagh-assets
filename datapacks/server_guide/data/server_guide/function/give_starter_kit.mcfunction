item replace entity @s armor.head with leather_helmet[custom_name='{"text":"✦ Citizen Cap ✦","color":"green","bold":true,"italic":false}']
item replace entity @s armor.chest with leather_chestplate[custom_name='{"text":"✦ Citizen Tunic ✦","color":"green","bold":true,"italic":false}']
item replace entity @s armor.legs with leather_leggings[custom_name='{"text":"✦ Citizen Pants ✦","color":"green","bold":true,"italic":false}']
item replace entity @s armor.feet with leather_boots[custom_name='{"text":"✦ Citizen Boots ✦","color":"green","bold":true,"italic":false}']
give @s stone_sword[custom_name='{"text":"✦ Citizen Blade ✦","color":"white","bold":true,"italic":false}'] 1
give @s stone_pickaxe[custom_name='{"text":"✦ Citizen Pickaxe ✦","color":"white","bold":true,"italic":false}'] 1
give @s stone_axe[custom_name='{"text":"✦ Citizen Hatchet ✦","color":"white","bold":true,"italic":false}'] 1
give @s stone_hoe[custom_name='{"text":"✦ Citizen Hoe ✦","color":"white","bold":true,"italic":false}'] 1
give @s torch 10
give @s cooked_beef 10
give @s map[custom_name='{"text":"✦ Starter Map of Hajaribagh ✦","color":"gold","bold":true,"italic":false}',lore=['{"text":"Survey chart for newcomers","color":"gray","italic":false}']] 1
function server_guide:give_book
function server_guide:unlock_all_recipes
tellraw @s [{"text":"[Hajaribagh] ","color":"green","bold":true},{"text":"Welcome to the Kingdom of King Abir! You have received full leather armor, stone tools, 10 torches, 10 beef steaks, a starter map, and your guide book.","color":"yellow"}]
tellraw @s [{"text":"[Hajaribagh Base] ","color":"gold","bold":true},{"text":"King Abir's base, houses, and farms are located around X: 163, Z: -307 (east of spawn).","color":"aqua"}]
