item replace entity @s armor.head with leather_helmet
item replace entity @s armor.chest with leather_chestplate
item replace entity @s armor.legs with leather_leggings
item replace entity @s armor.feet with leather_boots
give @s stone_sword 1
give @s stone_pickaxe 1
give @s stone_axe 1
give @s stone_hoe 1
give @s torch 10
give @s cooked_beef 10
give @s map[item_name="{\"text\":\"Starter Map\",\"color\":\"gold\"}"] 1
recipe give @s *
function server_guide:give_book
tellraw @s [{"text":"[Hajaribagh] ","color":"green","bold":true},{"text":"Welcome to the server! You have received full leather armor, stone tools, 10 torches, 10 beef steaks, a starter map, and your guide book.","color":"yellow"}]
tellraw @s [{"text":"[Hajaribagh Base] ","color":"gold","bold":true},{"text":"The main base, houses, and farms are located around X: 163, Z: -307 (east of spawn).","color":"aqua"}]
