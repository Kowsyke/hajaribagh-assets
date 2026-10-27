loot give @s loot salman_f_rahman:daily_ore
playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1
tellraw @s [{"text":"[Salman F Rahman] ","color":"gold","bold":true},{"text":"Daily tycoon dividend delivered: 1 random armor trim template has been added to your inventory!","color":"yellow"}]
tellraw @a[tag=!is_sfr] [{"text":"[Salman F Rahman] ","color":"gold","bold":true},{"selector":"@s","color":"yellow"},{"text":" received their daily tycoon armor trim dividend!","color":"gray"}]
