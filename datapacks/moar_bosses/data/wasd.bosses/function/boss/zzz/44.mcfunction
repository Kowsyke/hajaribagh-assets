#mc-build WASD content
summon marker ~ ~ ~ {Tags:["wasd.check_los"]}
execute positioned ~ ~ ~ as @e[tag=wasd.check_los,sort=nearest,limit=1] run function wasd.bosses:boss/zzz/45