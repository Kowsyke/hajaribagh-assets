scoreboard objectives add smoke trigger "Smoke Cannabis"
scoreboard objectives add use_joint minecraft.used:minecraft.warped_fungus_on_a_stick "Use Joint"
scoreboard objectives add smoke_timer dummy "Smoke Timer"
scoreboard players enable @a smoke
tellraw @a {"text":"[Cannabis & Smoking] Loaded! Type /trigger smoke or right-click a Cannabis Joint to smoke.","color":"green"}
