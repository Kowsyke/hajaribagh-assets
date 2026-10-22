tag @s add is_sfr
team join sfr_tycoon @s
playsound minecraft:ui.toast.challenge_complete master @a ~ ~ ~ 1 1
title @s times 10 70 20
title @s title {"text":"SALMAN F RAHMAN","color":"gold","bold":true}
title @s subtitle {"text":"Supreme Resource Oligarch of Hajaribagh","color":"yellow"}
tellraw @a [{"text":"[Salman F Rahman] ","color":"gold","bold":true},{"selector":"@s","color":"yellow","bold":true},{"text":" has claimed the supreme title of Salman F Rahman with ","color":"gold"},{"score":{"name":"@s","objective":"sfr_score"},"color":"white","bold":true},{"text":" blocks mined! All hail the oligarch!","color":"gold"}]
