# The Great Treasury Master Builder
# Executes all construction phases sequentially
function treasury:excavate
function treasury:shell
function treasury:alcoves
function treasury:royal_vault
function treasury:entrance
function treasury:decor

# Audio confirmation
playsound minecraft:ui.toast.challenge_complete player @a ~ ~ ~ 2 1
tellraw @a [{"text":"[The Great Treasury] ","color":"gold","bold":true},{"text":"Construction complete: The Great Treasury of King Abir is open.","color":"green"}]
