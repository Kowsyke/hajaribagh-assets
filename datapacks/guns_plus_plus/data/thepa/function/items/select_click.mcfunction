
function thepa:utilities/select_hand_reload

execute if entity @s[tag=gz_mainhand] run function thepa:items/mainhand
execute if entity @s[tag=gz_offhand] run function thepa:items/offhand

