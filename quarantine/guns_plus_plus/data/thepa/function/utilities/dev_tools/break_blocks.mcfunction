execute if score GLOBAL breaksBlocks matches 1 run tellraw @s {"text": "\n\nGuns will no longer break blocks\n\n"}
execute if score GLOBAL breaksBlocks matches 1 run return run scoreboard players set GLOBAL breaksBlocks 0

execute if score GLOBAL breaksBlocks matches 0 run tellraw @s {"text": "\n\nGuns will now break blocks\n\n"}
execute if score GLOBAL breaksBlocks matches 0 run return run scoreboard players set GLOBAL breaksBlocks 1