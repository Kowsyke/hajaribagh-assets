# Enforce zero block destruction and infinite reload
scoreboard players set GLOBAL breaksBlocks 0
tag @a[tag=!inf_reload] add inf_reload
execute as @a at @s store success score @s shootingDelayChecked run scoreboard players get @s shootingdelay
execute as @a if score @s shootingDelayChecked matches 0 run scoreboard players set @s shootingdelay 0

scoreboard players add @e[scores={gz_teslatimer=1..}] gz_teslatimer 1

#Prefs
scoreboard players set @a[tag=!shootinginit] shootingdelay 0
tag @a[scores={shootingdelay=0..}] add shootinginit

scoreboard players set @a[tag=!shootcountinit] shotcounterdelay 0
tag @a[scores={shotcounterdelay=0..}] add shootcountinit


execute as @e[type=#thepa:can_shoot_guns] if items entity @s weapon.* *[minecraft:custom_data~{gz_data:{}}] unless predicate {"type":"minecraft:entity_scores","entity":"this","scores":{"killCredit":{}}} store result score @s killCredit run data get entity @s UUID[0]
execute as @e[type=#thepa:can_shoot_guns] if items entity @s weapon.* *[minecraft:custom_data~{gz_data:{}}] if score @s killCredit matches 0 store result score @s killCredit run data get entity @s UUID[0]

execute as @e[tag=gz_projectile] unless predicate {"type":"minecraft:entity_scores","entity":"this","scores":{"killCredit":{}}} store result score @s killCredit run data get entity @s Owner[0]


scoreboard players add @e[tag=gz_projectile,tag=!gz_bullet_54] removeBullet 1
kill @e[scores={removeBullet=50..}]

scoreboard players remove @a[scores={timeRemaining=1..}] timeRemaining 1


scoreboard players add timer ztimer 1
execute if score timer ztimer matches 2.. run scoreboard players set timer ztimer 0

execute as @e[type=tnt,tag=motion_added2] at @s unless block ~ ~-0.5 ~ air run data merge entity @s {fuse:1s}

scoreboard players remove @a[scores={shotcounterdelay=0..}] shotcounterdelay 1
scoreboard players set @a[scores={shotcounterdelay=0}] shotcounter 0


execute if score GLOBAL mobWeapon matches 1 run function thepa:utilities/tick_mobs
execute as @a run function thepa:utilities/player_tick


scoreboard players remove @e[type=#thepa:can_shoot_guns,scores={shootingdelay=1..}] shootingdelay 1

execute if entity @e[type=area_effect_cloud,tag=gz_projectile] as @e[type=area_effect_cloud,tag=gz_projectile] run function thepa:projectiles/init_move


#minigun
function thepa:shoot/minigun/loop


scoreboard players add @e[type=minecraft:area_effect_cloud,tag=gz_bullet_9] ageflare 1
execute at @e[tag=gz_bullet_9,scores={ageflare=5..6}] as @e[tag=gz_bullet_9,scores={ageflare=5..6}] run effect give @e[distance=..50,type=!armor_stand,type=!donkey] minecraft:glowing 25 0 true
kill @e[tag=gz_bullet_9,scores={ageflare=8..}]

execute if entity @e[tag=stickyBombTarget] as @e[tag=stickyBombTarget] at @s run tp @e[tag=stickyBomb,limit=1,distance=..3,sort=furthest] ~ ~0.9 ~
execute if entity @e[tag=stickyBombTarget] as @e[tag=stickyBombTarget] at @s unless entity @n[tag=stickyBomb,distance=..3] run tag @s remove stickyBombTarget

kill @e[type=minecraft:arrow,nbt={damage:15.0d},nbt={inGround:1b}]

execute as @e[type=minecraft:item,nbt={Item:{components:{"minecraft:custom_data":{gz_data:{id:25b}}}}}] at @s if block ~ ~-1 ~ minecraft:lightning_rod run data merge entity @e[type=minecraft:item,nbt={Item:{components:{"minecraft:custom_data":{gz_data:{id:25b}}}}},limit=1] {Invulnerable:1b}

execute as @e[type=minecraft:item,nbt={Fire:150s,Item:{components:{"minecraft:custom_data":{gz_data:{id:25b}}}}}] at @s if block ~ ~-1 ~ minecraft:lightning_rod as @p run function thepa:give/tesla_gun

execute as @e[type=minecraft:item,nbt={Fire:149s,Item:{components:{"minecraft:custom_data":{gz_data:{id:25b}}}}}] at @s if block ~ ~-1 ~ minecraft:lightning_rod run kill @s

#Laser Sight
execute if predicate {type:"minecraft:any_of",terms:[{type:"minecraft:entity_scores",entity:"this",scores:{gz_id:{min:40,max:42}}}]} as @a[nbt={SelectedItem:{components:{"minecraft:custom_data":{gz_data:{}}}}}] run tag @s add gunsight
execute if score GLOBAL legacyControls matches 1 as @a[nbt={equipment:{offhand:{components:{"minecraft:custom_data":{gz_data:{}}}}}}] if predicate {type:"minecraft:any_of",terms:[{type:"minecraft:entity_scores",entity:"this",scores:{gz_id:{min:40,max:42}}}]} run tag @s add gunsight
execute as @a unless items entity @s weapon.* *[minecraft:custom_data~{gz_data:{}}] run tag @s remove gunsight
execute as @a unless predicate {type:"minecraft:any_of",terms:[{type:"minecraft:entity_scores",entity:"this",scores:{gz_id:{min:40,max:42}}}]} run tag @s remove gunsight
execute as @a[tag=gunsight] run function thepa:utilities/lasersight



execute if entity @e[tag=teslazap,type=armor_stand] run function thepa:projectiles/hit/entity/laser

execute if score GLOBAL legacyControls matches 1 as @a[scores={gz_crossbow=1..},nbt={SelectedItem:{components:{"minecraft:custom_data":{gz_data:{}}}}}] at @s run function thepa:shoot/trigger
execute if score GLOBAL legacyControls matches 1 as @a[scores={gz_crossbow=1..},nbt={equipment:{offhand:{ components:{"minecraft:custom_data":{gz_data:{}}}}}}] at @s run function thepa:shoot/trigger

execute if entity @e[tag=turretT,type=armor_stand] run function thepa:turret/functionality

scoreboard players set @a minigunCharge 0
scoreboard players set @a gz_click 0
scoreboard players set @a gz_crossbow 0
scoreboard players set @a gz_sneak 0


#Untypeal Function
function thepa:turret/loop

execute as @e[tag=motion_added,nbt={OnGround:1b}] at @s run function thepa:projectiles/apply_y
execute as @e[tag=motion_added] at @s store result score @s SCOREBOARD1 run data get entity @s Motion[0] 150


execute as @e[tag=motion_projectile,tag=!motion_added] at @s rotated as @p run function thepa:projectiles/apply_motion
execute as @e[tag=motion_projectile] at @e[tag=motion_projectile] unless block ~ ~-0.5 ~ #thepa:air run tag @s remove motion_projectile

execute as @e[tag=motion_projectile2,tag=!motion_added2] at @s rotated as @p run function thepa:projectiles/apply_motion2
execute as @e[tag=motion_projectile2] at @e[tag=motion_projectile2] unless block ~ ~-0.5 ~ #thepa:air run data merge entity @e[tag=motion_projectile2,limit=1] {Fuse:0}

tag @a add recipeggiven

execute as @a[nbt={SelectedItem:{components:{"minecraft:custom_data":{gz_data:{id: 54b}}}}},scores={bfg_idle=1}] at @s run playsound guns:bfg_idle player @s ~ ~ ~ 10 1


execute as @a[nbt={equipment:{offhand:{components:{"minecraft:custom_data":{gz_data:{id: 54b}}}}}},scores={bfg_idle=1}] at @s run playsound guns:bfg_idle player @s ~ ~ ~ 10 1
kill @e[tag=targetScore,nbt={inGround:1b},type=arrow]
kill @e[tag=arrowRot,type=marker]

#BFG 
function thepa:projectiles/bfg/loop
function thepa:utilities/dynamic_scale

execute as @a[scores={deathCount=1..}] run attribute @s minecraft:scale base set 1
scoreboard players reset @a[scores={deathCount=1..}] deathCount


execute as @a[scores={gz_id=61,shotcounter=0}] if items entity @s weapon.* *[item_model="minecraft:guns/poweruprifle_hot"|item_model="minecraft:guns/poweruprifle_hot_sc"] if score GLOBAL legacyControls matches 0 run function thepa:utilities/single_ammo_model {id:61,path:'value "minecraft:guns/poweruprifle"'}
