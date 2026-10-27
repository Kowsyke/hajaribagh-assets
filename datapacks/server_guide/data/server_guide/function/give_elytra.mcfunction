# Give Maxed Enhanced Elytra and Sovereign Flight Rockets
execute if entity @s[name=Kowsyke] run return 1

give @s elytra[enchantments={"minecraft:unbreaking":3,"minecraft:mending":1,"minecraft:protection":4,"minecraft:thorns":3},custom_name='{"text":"✦ Wings of the Realm ✦","color":"aqua","bold":true,"italic":false}',lore=['{"text":"Sovereign wings blessed with eternal flight and protection","color":"gray","italic":false}']] 1
give @s firework_rocket[fireworks={flight_duration:3},custom_name='{"text":"✦ Sovereign Flight Rocket ✦","color":"light_purple","bold":true,"italic":false}',lore=['{"text":"Duration 3 high velocity flight propulsion","color":"gray","italic":false}']] 64
playsound minecraft:item.armor.equip_elytra player @s ~ ~ ~ 1.5 1
tellraw @s [{"text":"[Hajaribagh] ","color":"gold","bold":true},{"text":"Maxed Enhanced Elytra and Sovereign Flight Rockets received.","color":"aqua"}]
