function salman_f_rahman:check_free_space
execute if score @s sfr_has_space matches 1 run function salman_f_rahman:give_ore
execute if score @s sfr_has_space matches 0 run function salman_f_rahman:start_warn_countdown
