#mc-build WASD content
tellraw @a {"bold":true,"color":"red","text":"Missing the Required Library!"}
tellraw @a {"text":" "}
tellraw @a [{"color":"dark_red","text":"Missing: "},{"clickEvent":{"action":"open_url","value":"https://wasdbuildteam.website/data-packs/wasd-libraries/"},"color":"#26DBFF","hoverEvent":{"action":"show_text","value":[{"text":"Click to Install"}]},"text":"Library"}]