# Detonate TNT Arrow
summon tnt ~ ~ ~ {Fuse:0}
playsound minecraft:entity.generic.explode block @a ~ ~ ~ 2 1
particle minecraft:explosion_emitter ~ ~ ~ 0 0 0 0 1 normal
particle minecraft:flame ~ ~ ~ 0.5 0.5 0.5 0.1 30 normal
kill @s
