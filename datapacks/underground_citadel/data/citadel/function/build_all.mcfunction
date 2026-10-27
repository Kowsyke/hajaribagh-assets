# Subterranean Citadel: Master Build Orchestrator
# Executes all sectors sequentially to construct the underground fortress

function citadel:stairs_descent
function citadel:atrium_excavate
function citadel:atrium_shell
function citadel:atrium_decor
function citadel:forge_excavate
function citadel:forge_build
function citadel:hydroponics_excavate
function citadel:hydroponics_build
function citadel:bunker_excavate
function citadel:bunker_build
function citadel:suites_build
function citadel:conduits_build

tellraw @a [{"text":"[Architect] ","color":"gold","bold":true},{"text":"The Subterranean Citadel Mega Fortress has been completed! All sectors operational.","color":"green"}]
