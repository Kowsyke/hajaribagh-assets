# Project Hajaribagh Royal Armory Arsenal
# Strictly restricted to Kowsyke, ahsane, and GothHunterJamal

function thepa:give/ak_47
function thepa:give/deagle
function thepa:give/combat_shotgun
function thepa:give/awp

# Ammunition supplies
give @s minecraft:clock[minecraft:item_model="minecraft:ammo/medium_ammo",minecraft:custom_data={"gz_data":{"bullet_type":6b}},minecraft:item_name={"translate":"thepa.item.name.bullet_6","color":"white","italic":false},minecraft:custom_name={"text":"Medium Rounds (AK-47)","color":"gold","italic":false}] 64
give @s minecraft:clock[minecraft:item_model="minecraft:ammo/medium_ammo",minecraft:custom_data={"gz_data":{"bullet_type":6b}},minecraft:item_name={"translate":"thepa.item.name.bullet_6","color":"white","italic":false},minecraft:custom_name={"text":"Medium Rounds (AK-47)","color":"gold","italic":false}] 64

give @s minecraft:clock[minecraft:item_model="minecraft:ammo/50_cal_ammo",minecraft:custom_data={"gz_data":{"bullet_type":26b}},minecraft:item_name={"translate":"thepa.item.name.bullet_26","color":"white","italic":false},minecraft:custom_name={"text":".50 Cal Ammo (Deagle)","color":"gold","italic":false}] 64

give @s minecraft:clock[minecraft:item_model="minecraft:ammo/shotgun_shells",minecraft:custom_data={"gz_data":{"bullet_type":2b}},minecraft:item_name={"translate":"thepa.item.name.bullet_2","color":"white","italic":false},minecraft:custom_name={"text":"Shells (Combat Shotgun)","color":"gold","italic":false}] 64

give @s minecraft:clock[minecraft:item_model="minecraft:ammo/sniper_ammo",minecraft:custom_data={"gz_data":{"bullet_type":11b}},minecraft:item_name={"translate":"thepa.item.name.bullet_11","color":"white","italic":false},minecraft:custom_name={"text":"Heavy Rounds (AWP Sniper)","color":"gold","italic":false}] 32

# Tactical Attachments and Grenades
function thepa:give/frag_grenade
function thepa:give/frag_grenade
function thepa:give/smoke_grenade
function thepa:give/smoke_grenade
function thepa:give/suppressor
function thepa:give/lasersight
function thepa:give/recipe_book
tag @s add inf_reload

# Visual and Audio Confirmation
playsound minecraft:item.armor.equip_netherite player @s ~ ~ ~ 1.5 1
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 1 1.2
title @s actionbar {"text":"✦ Royal Firearms Arsenal Issued ✦","color":"gold","bold":true}
tellraw @s [{"text":"[Royal Armory] ","color":"gold","bold":true},{"text":"Full combat arsenal equipped: AK-47, Deagle, Combat Shotgun, AWP Sniper, plus ammunition and tactical attachments. Right-click to shoot, Sneak to reload or aim. Drop gun and suppressor together to attach.","color":"yellow"}]
