#mc-build WASD content
#Enable/Disable recipes. 1 = Enabled/True. 0= Disabled/False.
#Enable/Disable Bosses.
scoreboard players set bosses w.bosses_setting 1
#Enable/Disable Types of Bosses
scoreboard players set fire w.bosses_setting 1
scoreboard players set water w.bosses_setting 1
scoreboard players set electric w.bosses_setting 1
scoreboard players set earth w.bosses_setting 1
scoreboard players set metal w.bosses_setting 1
scoreboard players set air w.bosses_setting 1
scoreboard players set chicken w.bosses_setting 1
#Spawn Chance of Bosses (% chance to turn enderman and witches into a boss) Must be between 1 and 100
scoreboard players set spawn_chance w.bosses_setting 100
scoreboard players set max_bosses w.bosses_setting 3