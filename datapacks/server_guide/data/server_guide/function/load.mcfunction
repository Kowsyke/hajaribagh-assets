scoreboard objectives add gta_deaths deathCount

scoreboard objectives add tp_base trigger
scoreboard objectives add tp_spawn trigger
scoreboard objectives add gtp trigger
scoreboard objectives add minimap trigger
scoreboard objectives add gtp_timer dummy
scoreboard objectives add has_starter_kit dummy
scoreboard objectives add guide trigger
scoreboard objectives add guide_version dummy
team add pm "Prime Minister"
team modify pm prefix [{"text":"[Prime Minister] ","color":"gold","bold":true}]
team modify pm color gold
team join pm Kowsyke
team add president "President"
team modify president prefix [{"text":"[President] ","color":"aqua","bold":true}]
team modify president color aqua
team join president ahsane
team add communication "Minister of Communication"
team modify communication prefix [{"text":"[Minister Dip] ","color":"green","bold":true}]
team modify communication color green
team join communication Dip
team add tourism "Minister of Tourism"
team modify tourism prefix [{"text":"[Tourism Minister] ","color":"red","bold":true}]
team modify tourism color red
team join tourism GothHunterJamal
team add agriculture "Minister of Agriculture"
team modify agriculture prefix [{"text":"[Agriculture Minister] ","color":"yellow","bold":true}]
team modify agriculture color yellow
team join agriculture GREAT-RED-DRAGO
team add public_works "Minister of Public Works"
team modify public_works prefix [{"text":"[Works Minister] ","color":"blue","bold":true}]
team modify public_works color blue
team join public_works exacyyv
team join public_works Exacyyv
team add first_lady "First Lady"
team modify first_lady prefix [{"text":"[First Lady] ","color":"light_purple","bold":true}]
team modify first_lady color light_purple
team add citizen "Citizen"
team modify citizen prefix [{"text":"[Citizen] ","color":"gray"}]
team modify citizen color gray

# TNT Arrow Objectives
scoreboard objectives add tnt_arrow trigger
scoreboard objectives add tnt_mode dummy
scoreboard objectives add used_bow minecraft.used:minecraft.bow
scoreboard objectives add used_cbow minecraft.used:minecraft.crossbow

scoreboard objectives add kit_platinum trigger
scoreboard objectives add kit_dev trigger
scoreboard objectives add kit_shears trigger
scoreboard objectives add kit_shield trigger
scoreboard objectives add kit_boots trigger
scoreboard objectives add kit_guns trigger

# Firearms Safety Rules
scoreboard players set GLOBAL mobWeapon 0
scoreboard players set GLOBAL breaksBlocks 0

# Disable phantom mob spawning
gamerule spawn_phantoms false

