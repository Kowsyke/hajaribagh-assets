$scoreboard players set GLOBAL bloom $(bloom_choice)
$scoreboard players set GLOBAL camera $(camera_choice)
$scoreboard players set GLOBAL recoil $(recoil_choice)
$scoreboard players set GLOBAL spray $(spray_choice)
$scoreboard players set GLOBAL breaksBlocks $(block_break)
$scoreboard players set GLOBAL mobWeaponFrequency $(mob_frequency)
$scoreboard players set GLOBAL legacyControls $(legacy_controls)
$tag @a $(add_or_remove) inf_reload
execute if score GLOBAL mobWeaponFrequency matches 0 run scoreboard players set GLOBAL mobWeapon 0
execute if score GLOBAL mobWeaponFrequency matches 1.. run scoreboard players set GLOBAL mobWeapon 1