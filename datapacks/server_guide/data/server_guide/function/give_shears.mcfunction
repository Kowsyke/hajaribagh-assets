# Royal Shears of Hajaribagh
give @s shears[enchantments={"minecraft:efficiency":5,"minecraft:silk_touch":1,"minecraft:unbreaking":3,"minecraft:mending":1},custom_name='{"text":"✦ Shears of Hajaribagh ✦","color":"yellow","bold":true,"italic":false}',lore=['{"text":"Precision shears of the Realm","color":"gray","italic":false}']] 2
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 1 1
tellraw @s [{"text":"[Hajaribagh] ","color":"gold","bold":true},{"text":"Royal Shears received with Silk Touch, Efficiency V, Unbreaking III, and Mending.","color":"green"}]
