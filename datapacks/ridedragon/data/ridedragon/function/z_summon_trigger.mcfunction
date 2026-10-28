# Need to clear the rd_help scoreboard first as no-match in an execute statement is 
# not considered a failure (see https://bugs.mojang.com/browse/MC-125058)
scoreboard players set #rd_success rd_help 0

# Test for the conditions allowing summoning: 
#  - creative player, 
#  - non-creative player summoning and allowing bare triggers
#  - non-creative player holding the Book of Dragons
execute store success score #rd_success rd_help if entity @s[gamemode=creative] run function ridedragon:summon_dragon
execute store success score #rd_success rd_help unless score #rd_success rd_help matches 1 if data storage ridedragon:settings rd_admin{can_summon:"Enabled"} if data storage ridedragon:settings rd_admin{summon_without_book:"Enabled"} run function ridedragon:summon_dragon
execute unless score #rd_success rd_help matches 1 if data storage ridedragon:settings rd_admin{can_summon:"Enabled"} if items entity @s container.* minecraft:written_book[minecraft:custom_data~{DragonBook:"1"}] run function ridedragon:summon_dragon

execute unless entity @s[gamemode=creative] unless data storage ridedragon:settings rd_admin{can_summon:"Enabled"} run tellraw @s [{"text":"Dragon","color":"light_purple"},{"text":" summoning is globally disabled","color":"aqua"}]

#
# Reset player's trigger score and re-enable
#
scoreboard players set @s rd_summon 0
scoreboard players enable @s rd_summon

