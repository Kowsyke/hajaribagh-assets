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

# Central Ceremonial Red Carpet Aisle
fill 142 50 -328 144 50 -308 red_carpet
fill 141 50 -328 141 50 -308 yellow_carpet
fill 145 50 -328 145 50 -308 yellow_carpet

# Long Banquet Feast Tables (West: X: 137..139, East: X: 147..149)
fill 138 50 -325 138 50 -310 dark_oak_planks
fill 138 51 -325 138 51 -310 dark_oak_slab[type=top]
fill 137 51 -325 137 51 -310 dark_oak_stairs[facing=east]
fill 139 51 -325 139 51 -310 dark_oak_stairs[facing=west]

fill 148 50 -325 148 50 -310 dark_oak_planks
fill 148 51 -325 148 51 -310 dark_oak_slab[type=top]
fill 147 51 -325 147 51 -310 dark_oak_stairs[facing=east]
fill 149 51 -325 149 51 -310 dark_oak_stairs[facing=west]

# Feast Tableware (Cakes, Candles, Pots, Chalices)
setblock 138 52 -323 cake[bites=0]
setblock 138 52 -320 candle[lit=true,candles=3]
setblock 138 52 -317 decorated_pot[facing=north]
setblock 138 52 -314 candle[lit=true,candles=4]
setblock 138 52 -311 cake[bites=0]

setblock 148 52 -323 cake[bites=0]
setblock 148 52 -320 candle[lit=true,candles=3]
setblock 148 52 -317 decorated_pot[facing=north]
setblock 148 52 -314 candle[lit=true,candles=4]
setblock 148 52 -311 cake[bites=0]

# High Table Dais (North End: Z: -328..-326)
fill 136 51 -328 150 51 -326 smooth_quartz
fill 140 52 -327 146 52 -327 dark_oak_slab[type=top]
setblock 143 52 -328 dark_oak_stairs[facing=south]
setblock 142 52 -328 dark_oak_stairs[facing=south]
setblock 144 52 -328 dark_oak_stairs[facing=south]

# Dual Roaring Stone Fireplaces (East Wall X: 154, West Wall X: 132)
# West Fireplace
fill 132 50 -319 133 50 -317 netherrack
fill 132 51 -319 133 51 -317 campfire[lit=true]
fill 134 51 -319 134 53 -317 iron_bars
fill 132 52 -320 134 55 -316 polished_blackstone_bricks

# East Fireplace
fill 153 50 -319 154 50 -317 netherrack
fill 153 51 -319 154 51 -317 campfire[lit=true]
fill 152 51 -319 152 53 -317 iron_bars
fill 152 52 -320 154 55 -316 polished_blackstone_bricks

# Suspended Copper & Brass Chandeliers
setblock 143 62 -322 iron_chain[axis=y]
setblock 143 61 -322 iron_chain[axis=y]
setblock 143 60 -322 copper_bulb[lit=true]
setblock 143 59 -322 soul_lantern[hanging=true]

setblock 143 62 -314 iron_chain[axis=y]
setblock 143 61 -314 iron_chain[axis=y]
setblock 143 60 -314 copper_bulb[lit=true]
setblock 143 59 -314 soul_lantern[hanging=true]
