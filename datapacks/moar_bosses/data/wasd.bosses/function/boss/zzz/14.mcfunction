#mc-build WASD content
playsound block.glass.break player @a ~ ~ ~ 1 0
playsound entity.firework_rocket.blast player @a ~ ~ ~ 1 2
summon item_display ~ ~ ~ {CustomName:"an ice spike",item_display:"head",Tags:["wasd.lib_entity_tick","wasd.ability","wasd.ice_spike"],teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]},item:{id:"minecraft:armor_stand",count:1,components:{"minecraft:item_model":"wasd:abilities/ice_spike"}}}
tp @e[tag=wasd.lib_entity_tick,tag=wasd.ability,tag=wasd.ice_spike,sort=nearest,limit=1] ~ ~ ~ ~ ~-5