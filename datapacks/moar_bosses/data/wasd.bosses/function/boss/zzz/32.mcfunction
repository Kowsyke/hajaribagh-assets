#mc-build WASD content
playsound block.deepslate.break player @a ~ ~ ~ 1 0
playsound block.deepslate.break player @a ~ ~ ~ 1 0
playsound block.deepslate.break player @a ~ ~ ~ 1 0
playsound entity.firework_rocket.blast_far player @a ~ ~ ~ 1 0
execute positioned ~ ~-1 ~ rotated ~ 0 positioned ^-2 ^ ^1 unless block ~ ~ ~ #wasd.tags:nonsolid run function wasd.bosses:boss/zzz/33