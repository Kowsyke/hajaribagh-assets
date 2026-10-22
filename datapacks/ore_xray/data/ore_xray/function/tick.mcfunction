scoreboard players enable @a[name=Kowsyke] xray
execute as @a[name=Kowsyke,scores={xray=1..}] at @s run function ore_xray:toggle
execute as @a[name=!Kowsyke,scores={xray=1..}] run scoreboard players set @s xray 0
