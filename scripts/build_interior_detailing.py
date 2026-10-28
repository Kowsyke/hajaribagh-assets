#!/usr/bin/env python3
"""Build interior detailing and furnishings for King Abir Hivemind Bunker.

Populates all 8 bunker rooms with functional redstone, furnishings,
armor stands, weapon displays, and decorative details.
Strictly respects object logic, parity, nonflammable fireplaces,
paired double chests, and facing constraints.
"""

import os
import subprocess
import sys

DEFAULT_HOST = os.environ.get("HZ_HOST", "132.226.135.26")
DEFAULT_USER = os.environ.get("HZ_USER", "ubuntu")
DEFAULT_KEY = os.environ.get("HZ_KEY", os.path.expanduser("~/.ssh/id_ed25519"))

LOCAL_FUNCTION_DIR = "datapacks/underground_citadel/data/citadel/function"
REMOTE_SERVER_PATH = "/home/ubuntu/minecraft-server"
REMOTE_FUNCTION_DIR = f"{REMOTE_SERVER_PATH}/world/datapacks/underground_citadel/data/citadel/function"


def build_decor_commands():
    """Generates the full list of Minecraft commands for bunker detailing."""
    cmds = []

    # Cleanup any previously summoned decor entities to ensure idempotency
    cmds.append("# Cleanup prior decorative entities")
    cmds.append("kill @e[tag=citadel_decor]")

    # =========================================================================
    # Sector 0: Central Command Rotunda (X: 111..123, Z: -307..-295, Y: 46..53)
    # =========================================================================
    cmds.append("# Sector 0: Central Command Rotunda Detailing")
    # Tactical holo compass table surrounding the central beacon well
    cmds.append("setblock 117 47 -300 dark_oak_stairs[facing=south,half=bottom]")
    cmds.append("setblock 117 47 -302 dark_oak_stairs[facing=north,half=bottom]")
    cmds.append("setblock 116 47 -301 dark_oak_stairs[facing=west,half=bottom]")
    cmds.append("setblock 118 47 -301 dark_oak_stairs[facing=east,half=bottom]")
    cmds.append("setblock 117 47 -301 copper_grate")
    cmds.append(
        "summon glow_item_frame 117.5 48.0 -300.97 "
        '{Tags:["citadel_decor","rotunda_compass"],Facing:2b,Item:{id:"minecraft:recovery_compass",count:1}}'
    )
    # Redstone sensor terminals on rotunda walls
    cmds.append("setblock 112 47 -301 chiseled_polished_blackstone")
    cmds.append("setblock 112 48 -301 calibrated_sculk_sensor")
    cmds.append("setblock 122 47 -301 chiseled_polished_blackstone")
    cmds.append("setblock 122 48 -301 comparator[facing=west]")
    # Citadel royal standards on corner pilasters
    cmds.append("setblock 111 49 -306 red_wall_banner[facing=south]")
    cmds.append("setblock 123 49 -306 red_wall_banner[facing=south]")
    cmds.append("setblock 111 49 -296 red_wall_banner[facing=north]")
    cmds.append("setblock 123 49 -296 red_wall_banner[facing=north]")
    # Potted greenery in rotunda alcoves
    cmds.append("setblock 112 47 -305 potted_flowering_azalea_bush replace")
    cmds.append("setblock 122 47 -305 potted_flowering_azalea_bush replace")

    # =========================================================================
    # Sector 1: Tool & Equipment Armory (X: 74..94, Z: -307..-295, Y: 46..53)
    # =========================================================================
    cmds.append("# Sector 1: Tool & Equipment Armory Detailing")
    # Six armor display pedestals along the West wall at X: 75
    # Pedestal Z positions: -306, -304, -302, -300, -298, -296
    pedestal_zs = [-306, -304, -302, -300, -298, -296]
    for z in pedestal_zs:
        cmds.append(f"setblock 75 47 {z} smooth_stone_slab[type=bottom]")
        cmds.append(f"setblock 75 48 {z} air")
        cmds.append(f"setblock 75 49 {z} air")
        cmds.append(f"setblock 75 50 {z} iron_trapdoor[half=bottom]")
        cmds.append(f"setblock 75 51 {z} sea_lantern")

    # Armor Stand 1: Netherite Vanguard at Z: -306
    cmds.append(
        "summon armor_stand 75.5 47.0 -305.5 "
        '{Tags:["citadel_decor","armory_stand_1"],ShowArms:1b,NoBasePlate:1b,Rotation:[270.0f,0.0f]}'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_1,limit=1] armor.head with '
        'netherite_helmet[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_1,limit=1] armor.chest with '
        'netherite_chestplate[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_1,limit=1] armor.legs with '
        'netherite_leggings[enchantments={"minecraft:protection":4,"minecraft:unbreaking":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_1,limit=1] armor.feet with '
        'netherite_boots[enchantments={"minecraft:protection":4,"minecraft:feather_falling":4}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_1,limit=1] weapon.mainhand with '
        'netherite_sword[enchantments={"minecraft:sharpness":5,"minecraft:unbreaking":3}]'
    )
    cmds.append('item replace entity @e[tag=armory_stand_1,limit=1] weapon.offhand with shield')

    # Armor Stand 2: Diamond Champion at Z: -304
    cmds.append(
        "summon armor_stand 75.5 47.0 -303.5 "
        '{Tags:["citadel_decor","armory_stand_2"],ShowArms:1b,NoBasePlate:1b,Rotation:[270.0f,0.0f]}'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_2,limit=1] armor.head with '
        'diamond_helmet[enchantments={"minecraft:protection":4}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_2,limit=1] armor.chest with '
        'diamond_chestplate[enchantments={"minecraft:protection":4}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_2,limit=1] armor.legs with '
        'diamond_leggings[enchantments={"minecraft:protection":4}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_2,limit=1] armor.feet with '
        'diamond_boots[enchantments={"minecraft:protection":4}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_2,limit=1] weapon.mainhand with '
        'diamond_axe[enchantments={"minecraft:efficiency":5}]'
    )
    cmds.append('item replace entity @e[tag=armory_stand_2,limit=1] weapon.offhand with shield')

    # Armor Stand 3: Royal Gold Paladin at Z: -302
    cmds.append(
        "summon armor_stand 75.5 47.0 -301.5 "
        '{Tags:["citadel_decor","armory_stand_3"],ShowArms:1b,NoBasePlate:1b,Rotation:[270.0f,0.0f]}'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_3,limit=1] armor.head with '
        'golden_helmet[enchantments={"minecraft:protection":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_3,limit=1] armor.chest with '
        'golden_chestplate[enchantments={"minecraft:protection":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_3,limit=1] armor.legs with '
        'golden_leggings[enchantments={"minecraft:protection":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_3,limit=1] armor.feet with '
        'golden_boots[enchantments={"minecraft:protection":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_3,limit=1] weapon.mainhand with '
        'trident[enchantments={"minecraft:loyalty":3}]'
    )
    cmds.append('item replace entity @e[tag=armory_stand_3,limit=1] weapon.offhand with totem_of_undying')

    # Armor Stand 4: Veteran Iron Infantry at Z: -300
    cmds.append(
        "summon armor_stand 75.5 47.0 -299.5 "
        '{Tags:["citadel_decor","armory_stand_4"],ShowArms:1b,NoBasePlate:1b,Rotation:[270.0f,0.0f]}'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_4,limit=1] armor.head with '
        'iron_helmet[enchantments={"minecraft:protection":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_4,limit=1] armor.chest with '
        'iron_chestplate[enchantments={"minecraft:protection":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_4,limit=1] armor.legs with '
        'iron_leggings[enchantments={"minecraft:protection":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_4,limit=1] armor.feet with '
        'iron_boots[enchantments={"minecraft:protection":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_4,limit=1] weapon.mainhand with '
        'crossbow[enchantments={"minecraft:quick_charge":3}]'
    )
    cmds.append('item replace entity @e[tag=armory_stand_4,limit=1] weapon.offhand with shield')

    # Armor Stand 5: Heavy Breaker at Z: -298
    cmds.append(
        "summon armor_stand 75.5 47.0 -297.5 "
        '{Tags:["citadel_decor","armory_stand_5"],ShowArms:1b,NoBasePlate:1b,Rotation:[270.0f,0.0f]}'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_5,limit=1] armor.head with '
        'netherite_helmet[enchantments={"minecraft:blast_protection":4}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_5,limit=1] armor.chest with '
        'netherite_chestplate[enchantments={"minecraft:blast_protection":4}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_5,limit=1] armor.legs with '
        'netherite_leggings[enchantments={"minecraft:blast_protection":4}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_5,limit=1] armor.feet with '
        'netherite_boots[enchantments={"minecraft:feather_falling":4}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_5,limit=1] weapon.mainhand with '
        'mace[enchantments={"minecraft:density":5}]'
    )
    cmds.append('item replace entity @e[tag=armory_stand_5,limit=1] weapon.offhand with shield')

    # Armor Stand 6: Diamond Marksman at Z: -296
    cmds.append(
        "summon armor_stand 75.5 47.0 -295.5 "
        '{Tags:["citadel_decor","armory_stand_6"],ShowArms:1b,NoBasePlate:1b,Rotation:[270.0f,0.0f]}'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_6,limit=1] armor.head with '
        'diamond_helmet[enchantments={"minecraft:projectile_protection":4}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_6,limit=1] armor.chest with '
        'diamond_chestplate[enchantments={"minecraft:projectile_protection":4}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_6,limit=1] armor.legs with '
        'diamond_leggings[enchantments={"minecraft:protection":4}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_6,limit=1] armor.feet with '
        'diamond_boots[enchantments={"minecraft:depth_strider":3}]'
    )
    cmds.append(
        'item replace entity @e[tag=armory_stand_6,limit=1] weapon.mainhand with '
        'bow[enchantments={"minecraft:power":5,"minecraft:flame":1}]'
    )
    cmds.append('item replace entity @e[tag=armory_stand_6,limit=1] weapon.offhand with spectral_arrow')

    # Paired double chest lockers: 3 paired sets on lower row, 3 paired sets on upper row
    # X=86 right, X=87 left; X=88 right, X=89 left; X=90 right, X=91 left
    for y in [47, 48]:
        cmds.append(f"setblock 86 {y} -306 chest[facing=south,type=right] replace")
        cmds.append(f"setblock 87 {y} -306 chest[facing=south,type=left] replace")
        cmds.append(f"setblock 88 {y} -306 chest[facing=south,type=right] replace")
        cmds.append(f"setblock 89 {y} -306 chest[facing=south,type=left] replace")
        cmds.append(f"setblock 90 {y} -306 chest[facing=south,type=right] replace")
        cmds.append(f"setblock 91 {y} -306 chest[facing=south,type=left] replace")
        cmds.append(f"setblock 92 {y} -306 deepslate_brick_wall replace")

    # Item frames displaying weapons and tools mounted directly on the chest lockers
    upper_weapons = [
        (86, "netherite_pickaxe"),
        (87, "netherite_axe"),
        (88, "netherite_shovel"),
        (89, "diamond_sword"),
        (90, "trident"),
        (91, "mace"),
    ]
    for x, item in upper_weapons:
        cmds.append(
            f"summon item_frame {x} 48 -305 "
            f'{{Tags:["citadel_decor","armory_frame"],Facing:3b,Item:{{id:"minecraft:{item}",count:1}}}}'
        )

    lower_weapons = [
        (86, "bow"),
        (87, "crossbow"),
        (88, "shield"),
        (89, "elytra"),
        (90, "spyglass"),
        (91, "clock"),
    ]
    for x, item in lower_weapons:
        cmds.append(
            f"summon item_frame {x} 47 -305 "
            f'{{Tags:["citadel_decor","armory_frame"],Facing:3b,Item:{{id:"minecraft:{item}",count:1}}}}'
        )

    # Tool smithing bench component displays
    bench_displays = [
        (80, "netherite_upgrade_smithing_template"),
        (81, "netherite_ingot"),
        (82, "diamond"),
        (83, "iron_ingot"),
        (84, "ender_eye"),
    ]
    for x, item in bench_displays:
        cmds.append(
            f"summon item_frame {x} 48 -305 "
            f'{{Tags:["citadel_decor","armory_bench_frame"],Facing:3b,Item:{{id:"minecraft:{item}",count:1}}}}'
        )

    # =========================================================================
    # Sector 2: Blacksmith & Smelting Workshop (X: 74..94, Z: -291..-275)
    # =========================================================================
    cmds.append("# Sector 2: Blacksmith & Smelting Workshop Detailing")
    # Water steam smoke particles via campfires installed below quenching cauldrons
    cmds.append("setblock 89 46 -283 campfire[lit=true] replace")
    cmds.append("setblock 89 47 -283 water_cauldron[level=3] replace")
    cmds.append("setblock 89 46 -281 campfire[lit=true] replace")
    cmds.append("setblock 89 47 -281 water_cauldron[level=3] replace")

    # Molten lava crucible with full spark protection cage
    cmds.append("fill 82 46 -285 86 46 -281 chiseled_polished_blackstone")
    cmds.append("setblock 84 46 -283 lava")
    cmds.append("setblock 84 47 -283 lava")
    cmds.append("setblock 84 48 -283 lava")
    cmds.append("fill 83 47 -284 85 48 -282 tinted_glass")
    # Outer iron bar spark deflector cage
    cmds.append("fill 82 47 -285 86 48 -285 iron_bars")
    cmds.append("fill 82 47 -281 86 48 -281 iron_bars")
    cmds.append("fill 82 47 -285 82 48 -281 iron_bars")
    cmds.append("fill 86 47 -285 86 48 -281 iron_bars")
    cmds.append("fill 83 49 -284 85 49 -282 iron_bars")

    # Ingot and raw metal storage rack displays
    cmds.append("setblock 92 47 -288 raw_iron_block replace")
    cmds.append("setblock 92 48 -288 raw_iron_block replace")
    cmds.append("setblock 92 47 -287 iron_block replace")
    cmds.append("setblock 92 47 -286 raw_gold_block replace")
    cmds.append("setblock 92 47 -285 gold_block replace")
    cmds.append("setblock 92 47 -284 raw_copper_block replace")

    ingot_frames = [
        (91, 48, -288, "iron_ingot"),
        (91, 47, -288, "raw_iron"),
        (91, 47, -287, "iron_block"),
        (91, 47, -286, "raw_gold"),
        (91, 47, -285, "gold_ingot"),
        (91, 47, -284, "copper_ingot"),
    ]
    for x, y, z, item in ingot_frames:
        cmds.append(
            f"summon glow_item_frame {x} {y} {z} "
            f'{{Tags:["citadel_decor","blacksmith_frame"],Facing:4b,Item:{{id:"minecraft:{item}",count:1}}}}'
        )

    # Master smithing tools displayed on wall
    cmds.append(
        'summon glow_item_frame 90 48 -289 '
        '{Tags:["citadel_decor","blacksmith_frame"],Facing:4b,Item:{id:"minecraft:netherite_ingot",count:1}}'
    )
    cmds.append(
        'summon glow_item_frame 90 48 -287 '
        '{Tags:["citadel_decor","blacksmith_frame"],Facing:4b,Item:{id:"minecraft:heavy_core",count:1}}'
    )

    # =========================================================================
    # Sector 3: Grand Arcane Library (X: 140..160, Z: -307..-295, Y: 46..53)
    # =========================================================================
    cmds.append("# Sector 3: Grand Arcane Library Detailing")
    # Floating lecterns on glowing end rods with written tomes
    floating_lecterns = [
        (144, -304, "east", "Hivemind Citadel Genesis"),
        (144, -298, "east", "Citadel Vault Protocols"),
        (156, -304, "west", "Redstone Engineering Lexicon"),
        (156, -298, "west", "Ancient Glyphs & Arcane Enigmas"),
    ]
    for x, z, facing, title in floating_lecterns:
        cmds.append(f"setblock {x} 47 {z} end_rod[facing=up] replace")
        cmds.append(f"setblock {x} 48 {z} lectern[facing={facing},has_book=true] replace")
        book_nbt = (
            '{id:"minecraft:written_book",count:1,components:'
            '{"minecraft:written_book_content":{author:"King Abir",'
            'title:"' + title + '",pages:["Registered in the royal archives of the Citadel."]}}}'
        )
        cmds.append(f"data modify block {x} 48 {z} Book set value {book_nbt}")

    # Study reading desks and chairs with strict chair facing logic
    cmds.append("setblock 144 47 -301 dark_oak_stairs[facing=east,half=bottom] replace")
    cmds.append("setblock 145 47 -301 dark_oak_slab[type=bottom] replace")
    cmds.append("setblock 156 47 -301 dark_oak_stairs[facing=west,half=bottom] replace")
    cmds.append("setblock 155 47 -301 dark_oak_slab[type=bottom] replace")

    # Lit candles on reading desks and study nooks
    cmds.append("setblock 145 48 -301 candle[candles=3,lit=true] replace")
    cmds.append("setblock 155 48 -301 purple_candle[candles=3,lit=true] replace")
    cmds.append("setblock 142 48 -305 candle[candles=4,lit=true] replace")
    cmds.append("setblock 158 48 -305 purple_candle[candles=4,lit=true] replace")
    cmds.append("setblock 142 48 -297 candle[candles=4,lit=true] replace")
    cmds.append("setblock 158 48 -297 purple_candle[candles=4,lit=true] replace")

    # Enchanted tome displays mounted on altar pillars
    tome_displays = [
        (147, 48, -301, 5, "mending"),
        (153, 48, -301, 4, "unbreaking"),
        (150, 48, -304, 3, "fortune"),
        (150, 48, -298, 2, "silk_touch"),
        (144, 48, -300, 5, "efficiency"),
        (156, 48, -300, 4, "infinity"),
    ]
    for x, y, z, facing_code, enchant in tome_displays:
        cmds.append(
            f"summon glow_item_frame {x} {y} {z} "
            f'{{Tags:["citadel_decor","library_frame"],Facing:{facing_code}b,'
            f'Item:{{id:"minecraft:enchanted_book",count:1,'
            f'components:{{"minecraft:stored_enchantments":{{"minecraft:{enchant}":1}}}}}}}}'
        )

    # =========================================================================
    # Sector 4: Brewing & Alchemy Laboratory (X: 140..160, Z: -291..-275)
    # =========================================================================
    cmds.append("# Sector 4: Brewing & Alchemy Laboratory Detailing")
    cmds.append("setblock 159 47 -283 water_cauldron[level=3] replace")
    cmds.append("setblock 158 47 -283 water_cauldron[level=3] replace")
    cmds.append("setblock 159 48 -285 brewing_stand replace")
    cmds.append("setblock 159 48 -284 brewing_stand replace")
    cmds.append("setblock 159 48 -282 brewing_stand replace")
    cmds.append("setblock 159 48 -281 brewing_stand replace")

    # Alchemical reagent display frames on the East wall
    reagents = [
        (159, 49, -285, "nether_wart"),
        (159, 49, -284, "blaze_powder"),
        (159, 49, -283, "ghast_tear"),
        (159, 49, -282, "glistering_melon_slice"),
        (159, 49, -281, "fermented_spider_eye"),
    ]
    for x, y, z, item in reagents:
        cmds.append(
            f"summon glow_item_frame {x} {y} {z} "
            f'{{Tags:["citadel_decor","brewing_frame"],Facing:4b,Item:{{id:"minecraft:{item}",count:1}}}}'
        )

    # =========================================================================
    # Sector 5: Underground Farm & Botany Pod (X: 96..114, Z: -291..-265)
    # =========================================================================
    cmds.append("# Sector 5: Underground Farm & Botany Pod Detailing")
    # Subterranean apiary calm fire under bee nests
    cmds.append("setblock 99 46 -273 campfire[lit=true] replace")
    cmds.append("setblock 99 48 -273 bee_nest[facing=east,honey_level=5] replace")
    cmds.append("setblock 103 46 -273 campfire[lit=true] replace")
    cmds.append("setblock 103 48 -273 bee_nest[facing=west,honey_level=5] replace")
    # Paired double chest for botanical harvest
    cmds.append("setblock 112 47 -268 chest[facing=west,type=right] replace")
    cmds.append("setblock 112 47 -267 chest[facing=west,type=left] replace")
    cmds.append(
        'summon item_frame 111 47 -268 '
        '{Tags:["citadel_decor","farm_frame"],Facing:4b,Item:{id:"minecraft:golden_carrot",count:1}}'
    )
    cmds.append(
        'summon item_frame 111 47 -267 '
        '{Tags:["citadel_decor","farm_frame"],Facing:4b,Item:{id:"minecraft:wheat",count:1}}'
    )
    # Agricultural tool display
    cmds.append(
        'summon item_frame 111 48 -267 '
        '{Tags:["citadel_decor","farm_frame"],Facing:4b,Item:{id:"minecraft:diamond_hoe",count:1}}'
    )

    # =========================================================================
    # Sector 6: Modern Subterranean Housing (X: 120..138, Z: -291..-265)
    # =========================================================================
    cmds.append("# Sector 6: Modern Subterranean Housing Detailing")
    # Master suite double bed with strict head and foot parity
    cmds.append("setblock 136 47 -289 red_bed[facing=north,part=head] replace")
    cmds.append("setblock 136 47 -288 red_bed[facing=north,part=foot] replace")
    cmds.append("setblock 135 47 -289 red_bed[facing=north,part=head] replace")
    cmds.append("setblock 135 47 -288 red_bed[facing=north,part=foot] replace")

    # Nightstands with potted greenery
    cmds.append("setblock 134 47 -289 stripped_spruce_log replace")
    cmds.append("setblock 134 48 -289 potted_fern replace")
    cmds.append("setblock 137 47 -289 stripped_spruce_log replace")
    cmds.append("setblock 137 48 -289 potted_flowering_azalea_bush replace")

    # Royal master wardrobe with embedded armor stands
    cmds.append("setblock 131 46 -290 smooth_quartz replace")
    cmds.append("setblock 132 46 -290 smooth_quartz replace")
    cmds.append("setblock 133 46 -290 smooth_quartz replace")
    cmds.append("setblock 131 47 -290 smooth_quartz replace")
    cmds.append("setblock 132 47 -290 barrel[facing=south] replace")
    cmds.append("setblock 133 47 -290 smooth_quartz replace")
    cmds.append("setblock 131 48 -290 air replace")
    cmds.append("setblock 132 48 -290 barrel[facing=south] replace")
    cmds.append("setblock 133 48 -290 air replace")
    cmds.append("setblock 131 49 -290 smooth_quartz_slab[type=bottom] replace")
    cmds.append("setblock 132 49 -290 smooth_quartz_slab[type=bottom] replace")
    cmds.append("setblock 133 49 -290 smooth_quartz_slab[type=bottom] replace")
    cmds.append("setblock 131 47 -289 spruce_trapdoor[facing=south,half=bottom,open=true] replace")
    cmds.append("setblock 133 47 -289 spruce_trapdoor[facing=south,half=bottom,open=true] replace")

    # Wardrobe Armor Stand 1: King Abir Royal Ceremonial Regalia
    cmds.append(
        "summon armor_stand 131.5 48.0 -289.8 "
        '{Tags:["citadel_decor","housing_wardrobe_1"],ShowArms:1b,NoBasePlate:1b,Rotation:[0.0f,0.0f]}'
    )
    cmds.append('item replace entity @e[tag=housing_wardrobe_1,limit=1] armor.head with golden_helmet')
    cmds.append('item replace entity @e[tag=housing_wardrobe_1,limit=1] armor.chest with diamond_chestplate')
    cmds.append('item replace entity @e[tag=housing_wardrobe_1,limit=1] armor.legs with golden_leggings')
    cmds.append('item replace entity @e[tag=housing_wardrobe_1,limit=1] armor.feet with netherite_boots')

    # Wardrobe Armor Stand 2: Formal Subterranean Field Robes
    cmds.append(
        "summon armor_stand 133.5 48.0 -289.8 "
        '{Tags:["citadel_decor","housing_wardrobe_2"],ShowArms:1b,NoBasePlate:1b,Rotation:[0.0f,0.0f]}'
    )
    cmds.append('item replace entity @e[tag=housing_wardrobe_2,limit=1] armor.head with turtle_helmet')
    cmds.append('item replace entity @e[tag=housing_wardrobe_2,limit=1] armor.chest with netherite_chestplate')
    cmds.append('item replace entity @e[tag=housing_wardrobe_2,limit=1] armor.legs with diamond_leggings')
    cmds.append('item replace entity @e[tag=housing_wardrobe_2,limit=1] armor.feet with diamond_boots')

    # Nonflammable brick fireplace with iron bar spark shield and vertical flue
    cmds.append("fill 135 47 -274 137 49 -274 bricks replace")
    cmds.append("setblock 136 47 -274 netherrack replace")
    cmds.append("setblock 136 48 -274 fire replace")
    cmds.append("fill 135 48 -273 137 48 -273 iron_bars replace")
    cmds.append("fill 136 49 -274 136 53 -274 bricks replace")

    # Modern sofa facing East towards coffee table at X: 133
    cmds.append("fill 131 47 -275 131 47 -271 smooth_quartz_stairs[facing=east,half=bottom] replace")
    cmds.append("setblock 131 47 -276 smooth_quartz_stairs[facing=south,half=bottom] replace")
    cmds.append("setblock 131 47 -270 smooth_quartz_stairs[facing=north,half=bottom] replace")
    # Coffee table with potted fern and candle
    cmds.append("setblock 133 47 -273 smooth_stone_slab[type=bottom] replace")
    cmds.append("setblock 133 47 -272 smooth_stone_slab[type=bottom] replace")
    cmds.append("setblock 133 48 -273 potted_fern replace")
    cmds.append("setblock 133 48 -272 candle[candles=2,lit=true] replace")

    # Contemporary lounge paintings
    cmds.append(
        'summon painting 125 48 -281 '
        '{Tags:["citadel_decor","housing_art"],facing:3b,variant:"minecraft:plant"}'
    )
    cmds.append(
        'summon painting 137 48 -277 '
        '{Tags:["citadel_decor","housing_art"],facing:4b,variant:"minecraft:wasteland"}'
    )

    # Modern kitchen details
    # Smoker with vertical ventilation chimney flue rising to ceiling
    cmds.append("setblock 121 47 -275 smoker[facing=east] replace")
    cmds.append("setblock 121 48 -275 hopper[facing=down] replace")
    cmds.append("fill 121 49 -275 121 52 -275 polished_deepslate_wall replace")
    cmds.append("setblock 121 53 -275 deepslate_tiles replace")

    # Brewing tap water cauldron with chrome hook faucet
    cmds.append("setblock 121 47 -274 water_cauldron[level=3] replace")
    cmds.append("setblock 121 48 -274 tripwire_hook[facing=east] replace")
    cmds.append("setblock 121 47 -273 barrel[facing=east] replace")
    cmds.append("setblock 121 47 -272 barrel[facing=east] replace")
    cmds.append("setblock 121 47 -271 brewing_stand replace")

    # Kitchen island breakfast bar and quartz bar stools facing West towards island
    cmds.append("fill 123 47 -274 123 47 -270 smooth_quartz replace")
    cmds.append("setblock 123 48 -274 heavy_weighted_pressure_plate replace")
    cmds.append("setblock 123 48 -273 flower_pot replace")
    cmds.append("setblock 123 48 -272 cake[bites=0] replace")
    cmds.append("setblock 123 48 -271 flower_pot replace")
    cmds.append("setblock 123 48 -270 heavy_weighted_pressure_plate replace")

    # Quartz bar stools facing West directly towards the counter
    cmds.append("setblock 125 47 -274 smooth_quartz_stairs[facing=west,half=bottom] replace")
    cmds.append("setblock 125 47 -272 smooth_quartz_stairs[facing=west,half=bottom] replace")
    cmds.append("setblock 125 47 -270 smooth_quartz_stairs[facing=west,half=bottom] replace")

    # Guest quarters beds and furnishings
    cmds.append("setblock 122 47 -289 cyan_bed[facing=north,part=head] replace")
    cmds.append("setblock 122 47 -288 cyan_bed[facing=north,part=foot] replace")
    cmds.append("setblock 124 47 -289 purple_bed[facing=north,part=head] replace")
    cmds.append("setblock 124 47 -288 purple_bed[facing=north,part=foot] replace")
    cmds.append("setblock 123 47 -289 stripped_spruce_log replace")
    cmds.append("setblock 123 48 -289 potted_fern replace")

    # =========================================================================
    # Sector 7: King's Council & Parliament (X: 105..129, Z: -261..-235)
    # =========================================================================
    cmds.append("# Sector 7: King's Council & High Parliament Detailing")
    # West member benches facing East towards desks at X: 113
    bench_zs = [-256, -254, -252, -250, -248, -246]
    for z in bench_zs:
        cmds.append(f"setblock 112 47 {z} dark_oak_stairs[facing=east,half=bottom] replace")
        cmds.append(f"setblock 111 48 {z} dark_oak_stairs[facing=east,half=bottom] replace")

    # West member desks and voting buttons
    cmds.append("fill 113 47 -256 113 47 -246 dark_oak_slab[type=top] replace")
    for z in bench_zs:
        cmds.append(f"setblock 113 48 {z} polished_blackstone_button[face=floor] replace")

    # East member benches facing West towards desks at X: 121
    for z in bench_zs:
        cmds.append(f"setblock 122 47 {z} dark_oak_stairs[facing=west,half=bottom] replace")
        cmds.append(f"setblock 123 48 {z} dark_oak_stairs[facing=west,half=bottom] replace")

    # East member desks and voting buttons
    cmds.append("fill 121 47 -256 121 47 -246 dark_oak_slab[type=top] replace")
    for z in bench_zs:
        cmds.append(f"setblock 121 48 {z} polished_blackstone_button[face=floor] replace")

    # Speaker table, lectern, and Dispatch Boxes
    cmds.append("fill 116 47 -243 118 47 -243 dark_oak_slab[type=top] replace")
    cmds.append("setblock 117 47 -242 lectern[facing=north,has_book=true] replace")
    parliament_book = (
        '{id:"minecraft:written_book",count:1,components:'
        '{"minecraft:written_book_content":{author:"King Abir",'
        'title:"Parliament Standing Orders",'
        'pages:[\"Decrees and rules of debate for the High Parliament.\"]}}}'
    )
    cmds.append(f"data modify block 117 47 -242 Book set value {parliament_book}")

    # Paired single chests representing Government and Opposition Dispatch Boxes
    cmds.append("setblock 116 48 -243 chest[facing=north] replace")
    cmds.append(
        'data modify block 116 48 -243 custom_name set value '
        '\'{"text":"Government Dispatch Box","color":"gold"}\''
    )
    cmds.append("setblock 118 48 -243 chest[facing=north] replace")
    cmds.append(
        'data modify block 118 48 -243 custom_name set value '
        '\'{"text":"Opposition Dispatch Box","color":"gold"}\''
    )

    # Ceremonial armor guards in four corner alcoves
    guard_alcoves = [
        (107.5, 47.0, -259.5, 135.0, "parliament_guard_nw"),
        (126.5, 47.0, -259.5, 225.0, "parliament_guard_ne"),
        (107.5, 47.0, -238.5, 45.0, "parliament_guard_sw"),
        (126.5, 47.0, -238.5, 315.0, "parliament_guard_se"),
    ]
    for x, y, z, yaw, tag in guard_alcoves:
        cmds.append(f"setblock {int(x)} 46 {int(z)} gilded_blackstone replace")
        cmds.append(
            f"summon armor_stand {x} {y} {z} "
            f'{{Tags:["citadel_decor","{tag}"],ShowArms:1b,NoBasePlate:1b,Rotation:[{yaw}f,0.0f]}}'
        )
        cmds.append(
            f'item replace entity @e[tag={tag},limit=1] armor.head with '
            'netherite_helmet[enchantments={"minecraft:protection":4}]'
        )
        cmds.append(
            f'item replace entity @e[tag={tag},limit=1] armor.chest with '
            'netherite_chestplate[enchantments={"minecraft:protection":4}]'
        )
        cmds.append(
            f'item replace entity @e[tag={tag},limit=1] armor.legs with '
            'netherite_leggings[enchantments={"minecraft:protection":4}]'
        )
        cmds.append(
            f'item replace entity @e[tag={tag},limit=1] armor.feet with '
            'netherite_boots[enchantments={"minecraft:protection":4}]'
        )
        cmds.append(
            f'item replace entity @e[tag={tag},limit=1] weapon.mainhand with '
            'trident[enchantments={"minecraft:loyalty":3}]'
        )
        cmds.append(f'item replace entity @e[tag={tag},limit=1] weapon.offhand with shield')

    # Banner valances encircling the high perimeter walls
    cmds.append("fill 108 51 -260 115 51 -260 red_wall_banner[facing=south] replace")
    cmds.append("fill 119 51 -260 126 51 -260 red_wall_banner[facing=south] replace")
    cmds.append("fill 108 51 -236 126 51 -236 red_wall_banner[facing=north] replace")
    cmds.append("fill 106 51 -258 106 51 -238 red_wall_banner[facing=east] replace")
    cmds.append("fill 128 51 -258 128 51 -238 red_wall_banner[facing=west] replace")

    return cmds


def write_local_mcfunction(cmds):
    """Writes the decor mcfunction file locally."""
    os.makedirs(LOCAL_FUNCTION_DIR, exist_ok=True)
    filepath = os.path.join(LOCAL_FUNCTION_DIR, "bunker_decor.mcfunction")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(cmds) + "\n")
    print(f"Generated local file: {filepath} ({len(cmds)} commands)")
    return filepath


def sync_mcfunction_to_remote(local_path, host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Copies the mcfunction file to the remote Minecraft server datapack directory."""
    remote_target = f"{REMOTE_FUNCTION_DIR}/bunker_decor.mcfunction"
    scp_cmd = [
        "scp",
        "-o", "StrictHostKeyChecking=no",
        "-i", key,
        local_path,
        f"{user}@{host}:{remote_target}",
    ]
    res = subprocess.run(scp_cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"SCP error: {res.stderr.strip()}", file=sys.stderr)
        sys.exit(res.returncode)
    print(f"Synced mcfunction to remote: {remote_target}")


def execute_via_rcon(cmds, host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Executes reload and triggers the function, with direct batch socket fallback."""
    # Build remote python script to reload, invoke function, and run entity commands
    py_code = """
import socket, struct

with open('/home/ubuntu/minecraft-server/server.properties') as f:
    props = dict(line.strip().split('=', 1) for line in f if '=' in line and not line.startswith('#'))

rcon_port = int(props.get('rcon.port', 25575))
rcon_pass = props.get('rcon.password', '')

s = socket.create_connection(('127.0.0.1', rcon_port), timeout=15)
s.sendall(struct.pack('<iii', len(rcon_pass) + 10, 1, 3) + rcon_pass.encode('utf-8') + b'\\x00\\x00')
s.recv(4096)

def run_cmd(c):
    s.sendall(struct.pack('<iii', len(c) + 10, 10, 2) + c.encode('utf-8') + b'\\x00\\x00')
    resp = s.recv(4096)
    if len(resp) >= 12:
        return resp[12:-2].decode('utf-8', errors='ignore')
    return ''

print('Reloading datapacks...')
print('Reload:', run_cmd('reload'))
print('Executing function citadel:bunker_decor...')
print('Function execution:', run_cmd('function citadel:bunker_decor'))

s.close()
"""
    ssh_cmd = [
        "ssh",
        "-o", "StrictHostKeyChecking=no",
        "-i", key,
        f"{user}@{host}",
        "python3 -c " + subprocess.list2cmdline([py_code]),
    ]
    res = subprocess.run(ssh_cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"RCON execution error: {res.stderr.strip()}", file=sys.stderr)
        sys.exit(res.returncode)
    print(res.stdout.strip())


def verify_live_blockstates(host=DEFAULT_HOST, user=DEFAULT_USER, key=DEFAULT_KEY):
    """Queries live blockstates and entity counts via RCON to verify construction."""
    py_verify = """
import socket, struct

with open('/home/ubuntu/minecraft-server/server.properties') as f:
    props = dict(line.strip().split('=', 1) for line in f if '=' in line and not line.startswith('#'))

rcon_port = int(props.get('rcon.port', 25575))
rcon_pass = props.get('rcon.password', '')

s = socket.create_connection(('127.0.0.1', rcon_port), timeout=15)
s.sendall(struct.pack('<iii', len(rcon_pass) + 10, 1, 3) + rcon_pass.encode('utf-8') + b'\\x00\\x00')
s.recv(4096)

def test_query(label, condition_cmd):
    s.sendall(struct.pack('<iii', len(condition_cmd) + 10, 10, 2) + condition_cmd.encode('utf-8') + b'\\x00\\x00')
    resp = s.recv(4096)
    msg = resp[12:-2].decode('utf-8', errors='ignore') if len(resp) >= 12 else ''
    passed = 'Test passed' in msg or 'has the following' in msg or 'Replaced' in msg or 'Modified' in msg
    status = '[PASS]' if passed else '[FAIL]'
    print(f'{status} {label}: {msg.strip()}')
    return passed

print('=== Live RCON Verification Audit ===')
# Tool Armory Checks
test_query('Armory Chest 86 (type=right)', 'execute if block 86 47 -306 chest[facing=south,type=right]')
test_query('Armory Chest 87 (type=left)', 'execute if block 87 47 -306 chest[facing=south,type=left]')
test_query('Armory Armor Stand 1 (Netherite)', 'execute if entity @e[tag=armory_stand_1]')
test_query('Armory Armor Stand 6 (Diamond)', 'execute if entity @e[tag=armory_stand_6]')

# Blacksmith Checks
test_query('Blacksmith Quenching Cauldron (water_cauldron[level=3])', 'execute if block 89 47 -283 water_cauldron[level=3]')
test_query('Blacksmith Steam Campfire', 'execute if block 89 46 -283 campfire[lit=true]')
test_query('Blacksmith Lava Crucible Protection', 'execute if block 82 47 -285 iron_bars')

# Library Checks
test_query('Library Floating Lectern NW', 'execute if block 144 48 -304 lectern[has_book=true]')
test_query('Library Floating End Rod NW', 'execute if block 144 47 -304 end_rod[facing=up]')
test_query('Library Desk Chair East Facing', 'execute if block 144 47 -301 dark_oak_stairs[facing=east]')
test_query('Library Candles Lit', 'execute if block 145 48 -301 candle[lit=true]')

# Modern Housing Checks
test_query('Housing Master Bed Head Parity', 'execute if block 136 47 -289 red_bed[facing=north,part=head]')
test_query('Housing Master Bed Foot Parity', 'execute if block 136 47 -288 red_bed[facing=north,part=foot]')
test_query('Housing Kitchen Flue Hopper', 'execute if block 121 48 -275 hopper[facing=down]')
test_query('Housing Brewing Tap Cauldron', 'execute if block 121 47 -274 water_cauldron[level=3]')
test_query('Housing Quartz Bar Stool West Facing', 'execute if block 125 47 -274 smooth_quartz_stairs[facing=west]')
test_query('Housing Wardrobe Armor Stand 1', 'execute if entity @e[tag=housing_wardrobe_1]')
test_query('Housing Nonflammable Fireplace Netherrack', 'execute if block 136 47 -274 netherrack')
test_query('Housing Fireplace Iron Shield', 'execute if block 136 48 -273 iron_bars')

# Parliament Hall Checks
test_query('Parliament Member Desk Top Slab', 'execute if block 113 47 -256 dark_oak_slab[type=top]')
test_query('Parliament Voting Button', 'execute if block 113 48 -256 polished_blackstone_button[face=floor]')
test_query('Parliament Member Chair East Facing', 'execute if block 112 47 -256 dark_oak_stairs[facing=east]')
test_query('Parliament Speaker Lectern Book', 'execute if block 117 47 -242 lectern[has_book=true]')
test_query('Parliament Ceremonial Guard NW', 'execute if entity @e[tag=parliament_guard_nw]')
test_query('Parliament Valance Banner', 'execute if block 115 51 -260 red_wall_banner[facing=south]')

# Rotunda, Farm & Brewing Checks
test_query('Rotunda Center Tactical Grate', 'execute if block 117 47 -301 copper_grate')
test_query('Brewing Lab Cauldron', 'execute if block 159 47 -283 water_cauldron[level=3]')
test_query('Farm Apiary Calm Campfire', 'execute if block 99 46 -273 campfire[lit=true]')
test_query('Farm Paired Double Chest Right', 'execute if block 112 47 -268 chest[facing=west,type=right]')
test_query('Farm Paired Double Chest Left', 'execute if block 112 47 -267 chest[facing=west,type=left]')

s.close()
"""
    ssh_cmd = [
        "ssh",
        "-o", "StrictHostKeyChecking=no",
        "-i", key,
        f"{user}@{host}",
        "python3 -c " + subprocess.list2cmdline([py_verify]),
    ]
    res = subprocess.run(ssh_cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Verification error: {res.stderr.strip()}", file=sys.stderr)
        sys.exit(res.returncode)
    print(res.stdout.strip())


def main():
    print("Designing interior detailing and redstone furnishings...")
    cmds = build_decor_commands()
    local_path = write_local_mcfunction(cmds)
    sync_mcfunction_to_remote(local_path)
    execute_via_rcon(cmds)
    verify_live_blockstates()
    print("Interior detailing and verification complete.")


if __name__ == "__main__":
    main()
