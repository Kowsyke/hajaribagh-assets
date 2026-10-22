scoreboard players enable @a smoke
execute as @a[scores={smoke=1..}] at @s run function cannabis:smoke
execute as @a[scores={use_joint=1..}] at @s run function cannabis:smoke
execute as @a[scores={smoke_timer=1..}] at @s run function cannabis:puff_particles

# Auto-reformat any dropped cannabis items to fix glitched JSON names
execute as @e[type=item,nbt={Item:{id:"minecraft:fern"}}] run data modify entity @s Item.components."minecraft:custom_name" set value {text:"Raw Cannabis Bud",color:"dark_green",bold:true,italic:false}
execute as @e[type=item,nbt={Item:{id:"minecraft:fern"}}] run data modify entity @s Item.components."minecraft:lore" set value [{text:"Dry on a campfire, smoker, or furnace before rolling",color:"gray",italic:false}]

execute as @e[type=item,nbt={Item:{id:"minecraft:pitcher_pod"}}] run data modify entity @s Item.components."minecraft:custom_name" set value {text:"Cannabis Seed",color:"green",bold:true,italic:false}
execute as @e[type=item,nbt={Item:{id:"minecraft:pitcher_pod"}}] run data modify entity @s Item.components."minecraft:lore" set value [{text:"Plant on hydrated farmland to grow cannabis",color:"gray",italic:false}]

execute as @e[type=item,nbt={Item:{id:"minecraft:dried_kelp"}}] run data modify entity @s Item.components."minecraft:custom_name" set value {text:"Cured Cannabis Bud",color:"dark_green",bold:true,italic:false}
execute as @e[type=item,nbt={Item:{id:"minecraft:dried_kelp"}}] run data modify entity @s Item.components."minecraft:lore" set value [{text:"Ready to roll with paper into joints",color:"gray",italic:false}]

execute as @e[type=item,nbt={Item:{id:"minecraft:warped_fungus_on_a_stick"}}] run data modify entity @s Item.components."minecraft:custom_name" set value {text:"Cannabis Joint",color:"green",bold:true,italic:false}
execute as @e[type=item,nbt={Item:{id:"minecraft:warped_fungus_on_a_stick"}}] run data modify entity @s Item.components."minecraft:lore" set value [{text:"Right-click to take a fat puff",color:"gray",italic:true},{text:"Pass it to your friends",color:"dark_green",italic:true}]
