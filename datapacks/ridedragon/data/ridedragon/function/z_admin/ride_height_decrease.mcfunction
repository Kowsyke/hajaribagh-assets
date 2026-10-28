#
# Description:	Adjust the ride height of the player
# Called by:	ridedragon:admin via chat link
# Entity @s:	player
#

execute store result score #rd_math rd_help run data get storage ridedragon:settings ride_height 100
# The ride_height is stored as a negative float value. Since math operations can 
# only be performed on scores, scores are integer and conversion to and from float
# can lead to truncation effects, do the math carefully.
# Multiply by 100, do operation with a bit of margin, divide and truncate to 10 and finally
# store back as a float, dividing out the last 10 as a scale operation.
scoreboard players add #rd_math rd_help 12
scoreboard players set #rd_math rd_math_extra1 10
scoreboard players operation #rd_math rd_help /= #rd_math rd_math_extra1
execute if score #rd_math rd_help matches ..-3 store result storage ridedragon:settings ride_height float 0.1 run scoreboard players get #rd_math rd_help
scoreboard players set #rd_math rd_math_extra1 0
scoreboard players operation #rd_math rd_math_extra1 -= #rd_math rd_help
execute if score #rd_math rd_help matches ..-3 store result storage ridedragon:settings rd_admin.ride_height_display float 0.1 run scoreboard players get #rd_math rd_math_extra1


function ridedragon:admin

