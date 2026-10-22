scoreboard players enable @a smoke
execute as @a[scores={smoke=1..}] at @s run function cannabis:smoke
execute as @a[scores={use_joint=1..}] at @s run function cannabis:smoke
execute as @a[scores={smoke_timer=1..}] at @s run function cannabis:puff_particles
