tag @s remove is_sfr
team leave @s

execute if entity @s[name=Kowsyke] run team join pm @s
execute if entity @s[name=ahsane] run team join president @s
execute if entity @s[name=Dip] run team join communication @s
execute if entity @s[name=GothHunterJamal] run team join tourism @s
execute if entity @s[name=GREAT-RED-DRAGO] run team join agriculture @s
execute if entity @s[name=Exacyyv] run team join public_works @s
execute if entity @s[name=exacyyv] run team join public_works @s
execute unless entity @s[team=pm] unless entity @s[team=president] unless entity @s[team=communication] unless entity @s[team=tourism] unless entity @s[team=agriculture] unless entity @s[team=public_works] run team join citizen @s

tellraw @a [{"text":"[Salman F Rahman] ","color":"gold","bold":true},{"selector":"@s","color":"yellow"},{"text":" has been dethroned from the Salman F Rahman Tycoon status!","color":"gray"}]
