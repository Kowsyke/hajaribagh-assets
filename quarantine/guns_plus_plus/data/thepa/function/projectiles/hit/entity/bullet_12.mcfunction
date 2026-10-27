
execute as @p[distance=0,nbt={attributes:[{id:"minecraft:scale",base:7.5d}]}] run function thepa:utilities/resize {"s":"8"}
execute as @p[distance=0,nbt={attributes:[{id:"minecraft:scale",base:7.0d}]}] run function thepa:utilities/resize {"s":"7.5"}
execute as @p[distance=0,nbt={attributes:[{id:"minecraft:scale",base:6.5d}]}] run function thepa:utilities/resize {"s":"7"}
execute as @p[distance=0,nbt={attributes:[{id:"minecraft:scale",base:6.0d}]}] run function thepa:utilities/resize {"s":"6.5"}
execute as @p[distance=0,nbt={attributes:[{id:"minecraft:scale",base:5.5d}]}] run function thepa:utilities/resize {"s":"6"}
execute as @p[distance=0,nbt={attributes:[{id:"minecraft:scale",base:5.0d}]}] run function thepa:utilities/resize {"s":"5.5"}
execute as @p[distance=0,nbt={attributes:[{id:"minecraft:scale",base:4.5d}]}] run function thepa:utilities/resize {"s":"5"}
execute as @p[distance=0,nbt={attributes:[{id:"minecraft:scale",base:4.0d}]}] run function thepa:utilities/resize {"s":"4.5"}
execute as @p[distance=0,nbt={attributes:[{id:"minecraft:scale",base:3.5d}]}] run function thepa:utilities/resize {"s":"4"}
execute as @p[distance=0,nbt={attributes:[{id:"minecraft:scale",base:3.0d}]}] run function thepa:utilities/resize {"s":"3.5"}
execute as @p[distance=0,nbt={attributes:[{id:"minecraft:scale",base:2.5d}]}] run function thepa:utilities/resize {"s":"3"}
execute as @p[distance=0,nbt={attributes:[{id:"minecraft:scale",base:2.0d}]}] run function thepa:utilities/resize {"s":"2.5"}
execute as @p[distance=0,nbt={attributes:[{id:"minecraft:scale",base:1.5d}]}] run function thepa:utilities/resize {"s":"2"}
execute as @p[distance=0,nbt=!{attributes:[{id:"minecraft:scale"}]}] run function thepa:utilities/resize {"s":"1.5"}
execute as @p[distance=0,nbt={attributes:[{id:"minecraft:scale",base:1.0d}]}] run function thepa:utilities/resize {"s":"1.5"}
execute as @p[distance=0,nbt={attributes:[{id:"minecraft:scale",base:0.75d}]}] run function thepa:utilities/resize {"s":"1.0"}
execute as @p[distance=0,nbt={attributes:[{id:"minecraft:scale",base:0.5d}]}] run function thepa:utilities/resize {"s":"0.75"}
execute as @p[distance=0,nbt={attributes:[{id:"minecraft:scale",base:0.35d}]}] run function thepa:utilities/resize {"s":"0.5"}
execute as @p[distance=0,nbt={attributes:[{id:"minecraft:scale",base:0.25d}]}] run function thepa:utilities/resize {"s":"0.35"}

scoreboard players set @n[distance=0,nbt={attributes:[{id:"minecraft:scale",base:1.0d}]}] size_time 1000
scoreboard players set @n[distance=0,nbt=!{attributes:[{id:"minecraft:scale"}]}] size_time 1000
scoreboard players add @n[distance=0,scores={size_time=0..}] size_time 500