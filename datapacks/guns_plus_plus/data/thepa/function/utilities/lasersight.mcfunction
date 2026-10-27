scoreboard players add @e[tag=sight] gunsights 1
execute as @e[tag=sight] at @s if entity @e[distance=..1,tag=!gunsight,tag=!sight] run particle minecraft:dust{color:[0,1,0],scale:1} ~ ~1.65 ~ 0 0 0 0 1 force @a[tag=gunsight]
execute as @e[tag=sight,scores={gunsights=8..}] at @s run kill @s

execute as @e[tag=sight,tag=laserspawn] at @s run tp @s ~ ~ ~ facing entity @a[sort=nearest,limit=1]
tag @e[tag=laserspawn] remove laserspawn
execute as @e[tag=sight] at @s run tp @s ^ ^ ^-0.4

execute at @s as @s run summon minecraft:marker ^ ^ ^1 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^4 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^7 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^10 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^13 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^16 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^19 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^22 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^25 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^28 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^31 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^34 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^37 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^40 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^43 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^46 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^49 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^52 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^55 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^58 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^61 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^64 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^67 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^70 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^73 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^76 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^79 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^82 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^85 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^88 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^91 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^94 {Tags:["sight","laserspawn"]}
execute at @s as @s run summon minecraft:marker ^ ^ ^97 {Tags:["sight","laserspawn"]}