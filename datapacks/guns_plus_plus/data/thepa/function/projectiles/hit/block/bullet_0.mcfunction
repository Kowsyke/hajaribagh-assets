
execute if block ~ ~ ~ #thepa:glass_pane run function thepa:projectiles/hit/block/destroy
execute if block ~ ~ ~ minecraft:tnt run function thepa:projectiles/hit/block/explode
execute if block ~ ~ ~ minecraft:bell run playsound block.bell.use block @a[distance=..30] ~ ~ ~ 50
execute if block ~ ~ ~ minecraft:chorus_flower run function thepa:projectiles/hit/block/destroy

