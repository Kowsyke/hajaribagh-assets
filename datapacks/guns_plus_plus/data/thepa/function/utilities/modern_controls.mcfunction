

scoreboard players set @s[scores={gz_crossbow=1..,gz_sneak=0}] scope_timer 11
execute if entity @s[scores={gz_crossbow=1..,gz_sneak=1..}] run function thepa:shoot/trigger
scoreboard players remove @s[scores={scope_timer=1..}] scope_timer 1

function thepa:utilities/calculate_delay {"slot":"SelectedItem"}
execute if entity @s[scores={scope_timer=0..}] unless entity @s[scores={scope_timer=2..9}] run function thepa:utilities/modify_mainhand with entity @s SelectedItem.components."minecraft:custom_data"."gz_data"
execute if entity @s[scores={scope_timer=1..,gz_id=62}] run function thepa:shoot/minigun/model_swap {debuff:-0.92}