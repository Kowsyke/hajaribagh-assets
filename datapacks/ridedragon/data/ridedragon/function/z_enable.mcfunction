#
# Periodic reset of triggers on reload
#
scoreboard players enable @p rd_help
scoreboard players enable @p rd_summon
scoreboard players enable @p rd_vanish
scoreboard players enable @p rd_silence

# Repeat every 4 seconds
schedule function ridedragon:z_enable 83t
