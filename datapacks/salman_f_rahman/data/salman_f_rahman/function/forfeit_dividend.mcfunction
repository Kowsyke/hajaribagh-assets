title @s reset
title @s title {"text":"DIVIDEND FORFEITED!","color":"dark_red","bold":true}
title @s subtitle {"text":"State treasury absorbed your daily ore.","color":"gray"}
tellraw @s [{"text":"[Salman F Rahman] ","color":"gold","bold":true},{"text":"Ten seconds elapsed without an open inventory slot. Your daily tycoon ore dividend has been forfeited to the state treasury!","color":"dark_red"}]
playsound minecraft:block.anvil.land master @s ~ ~ ~ 1 0.6
