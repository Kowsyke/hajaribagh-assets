# Royal Firearms Law Enforcement
# Strips guns, ammo, and munitions from unauthorized citizens

clear @s *[minecraft:custom_data~{gz_data:{}}]
playsound minecraft:block.anvil.land player @s ~ ~ ~ 1 0.7
title @s actionbar {"text":"[!] Royal Firearms Law: You do not possess a Firearms License.","color":"red","bold":true}
tellraw @s [{"text":"[Hajaribagh Law] ","color":"red","bold":true},{"text":"Firearms and military munitions are strictly restricted to Royal Cabinet Ministers. Your weapons have been confiscated.","color":"yellow"}]
