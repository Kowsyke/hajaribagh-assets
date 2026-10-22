scoreboard players add #rainbow sfr_rainbow 1
execute if score #rainbow sfr_rainbow matches 28.. run scoreboard players set #rainbow sfr_rainbow 0

execute if score #rainbow sfr_rainbow matches 0..3 run team modify sfr_tycoon color red
execute if score #rainbow sfr_rainbow matches 4..7 run team modify sfr_tycoon color gold
execute if score #rainbow sfr_rainbow matches 8..11 run team modify sfr_tycoon color yellow
execute if score #rainbow sfr_rainbow matches 12..15 run team modify sfr_tycoon color green
execute if score #rainbow sfr_rainbow matches 16..19 run team modify sfr_tycoon color aqua
execute if score #rainbow sfr_rainbow matches 20..23 run team modify sfr_tycoon color blue
execute if score #rainbow sfr_rainbow matches 24..27 run team modify sfr_tycoon color light_purple
