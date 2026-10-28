# Subterranean Citadel: The Sovereign Banquet and Gathering Hall
# Dimensions: X: 132..154, Z: -330..-306, Floor Y: 50, Ceiling Y: 62
fill 132 50 -330 154 62 -306 air

# Shell & Foundation
fill 131 49 -331 155 49 -305 polished_deepslate
fill 132 50 -330 154 50 -306 polished_blackstone_bricks
fill 131 50 -331 131 62 -305 polished_blackstone_bricks
fill 155 50 -331 155 62 -305 polished_blackstone_bricks
fill 131 50 -331 155 62 -331 polished_blackstone_bricks
fill 131 50 -305 155 62 -305 polished_blackstone_bricks
fill 131 63 -331 155 63 -305 deepslate_tiles

# Central Ceremonial Red & Gold Carpet Aisle
fill 142 50 -328 144 50 -308 red_carpet
fill 141 50 -328 141 50 -308 yellow_carpet
fill 145 50 -328 145 50 -308 yellow_carpet

# Long Banquet Feast Tables (West: X: 137..139, East: X: 147..149)
fill 138 50 -325 138 50 -310 dark_oak_planks
fill 138 51 -325 138 51 -310 dark_oak_slab[type=top]
fill 137 51 -325 137 51 -310 dark_oak_stairs[facing=east,half=bottom]
fill 139 51 -325 139 51 -310 dark_oak_stairs[facing=west,half=bottom]

fill 148 50 -325 148 50 -310 dark_oak_planks
fill 148 51 -325 148 51 -310 dark_oak_slab[type=top]
fill 147 51 -325 147 51 -310 dark_oak_stairs[facing=east,half=bottom]
fill 149 51 -325 149 51 -310 dark_oak_stairs[facing=west,half=bottom]

# Feast Tableware (Cakes, Candles, Steins, Decorated Pots)
setblock 138 52 -324 cake[bites=0]
setblock 138 52 -321 candle[lit=true,candles=3]
setblock 138 52 -318 decorated_pot[facing=north]
setblock 138 52 -315 candle[lit=true,candles=4]
setblock 138 52 -312 cake[bites=0]

setblock 148 52 -324 cake[bites=0]
setblock 148 52 -321 candle[lit=true,candles=3]
setblock 148 52 -318 decorated_pot[facing=north]
setblock 148 52 -315 candle[lit=true,candles=4]
setblock 148 52 -312 cake[bites=0]

# Sovereign High Table Dais (South End: Z: -308..-306)
fill 139 51 -308 147 51 -306 smooth_quartz
fill 140 52 -307 146 52 -306 dark_oak_slab[type=top]
setblock 143 52 -306 polished_deepslate_stairs[facing=north,half=bottom]
setblock 142 52 -306 dark_oak_stairs[facing=north,half=bottom]
setblock 144 52 -306 dark_oak_stairs[facing=north,half=bottom]

# Dual Roaring Hearths (East Wall: X: 154)
fill 153 50 -324 154 50 -322 netherrack
fill 153 51 -324 154 51 -322 fire
fill 153 52 -324 154 55 -322 bricks
setblock 152 51 -323 iron_bars

fill 153 50 -314 154 50 -312 netherrack
fill 153 51 -314 154 51 -312 fire
fill 153 52 -314 154 55 -312 bricks
setblock 152 51 -313 iron_bars

# Grand Triple Chandeliers
setblock 143 62 -324 iron_chain[axis=y]
setblock 143 61 -324 iron_chain[axis=y]
setblock 143 60 -324 copper_bulb[lit=true,powered=false]
setblock 143 59 -324 lantern[hanging=true]

setblock 143 62 -317 iron_chain[axis=y]
setblock 143 61 -317 iron_chain[axis=y]
setblock 143 60 -317 copper_bulb[lit=true,powered=false]
setblock 143 59 -317 lantern[hanging=true]

setblock 143 62 -310 iron_chain[axis=y]
setblock 143 61 -310 iron_chain[axis=y]
setblock 143 60 -310 copper_bulb[lit=true,powered=false]
setblock 143 59 -310 lantern[hanging=true]

# Doorway to Crossroads Corridor at X=131
fill 131 50 -307 131 54 -305 air
