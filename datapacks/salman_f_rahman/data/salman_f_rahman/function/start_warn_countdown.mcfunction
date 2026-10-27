scoreboard players set @s sfr_warn_timer 200
title @s times 10 70 20
title @s title {"text":"INVENTORY FULL!","color":"red","bold":true}
title @s subtitle {"text":"Free 1 slot within 10s to claim daily armor trim!","color":"yellow"}
tellraw @s [{"text":"[Salman F Rahman] ","color":"gold","bold":true},{"text":"WARNING: Your inventory is completely full! Open at least one slot within 10 seconds, or your daily tycoon armor trim dividend will be forfeited!","color":"red"}]
playsound minecraft:block.note_block.bass master @s ~ ~ ~ 1 0.5
