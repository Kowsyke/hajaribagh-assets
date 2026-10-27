execute as @e[tag=energy_ball] at @s run tag @e[type=!#thepa:unaffected,distance=..6] add bfgtarget
execute as @e[tag=energy_ball] at @s run tag @e[type=!#thepa:unaffected,distance=6..] remove bfgtarget
execute as @e[tag=energy_ball] at @s run tag @e[type=!#thepa:unaffected,distance=6..] remove bfguser
execute as @e[tag=bfgtarget] at @s if entity @e[tag=bfgray,distance=..1.5] run tag @s remove bfgtarget
kill @e[tag=bfgray]

execute as @e[tag=bfgtarget,tag=!bfguser] run damage @s 1.1 thepa:pulse by @n[tag=gz_bullet_54]