{{ get_arguments_table([
    ["send_packet",     "boolean",  "Is packet will be sent to the server (fake lag)"],
    ["command_number",  "number",   "Current command number"],
    ["tick_count",      "number",   "Current tick count"],
    ["viewangles",      "angle_t",  "Crosshair angle"],
    ["forwardmove",     "number",   "Forward/backward speed"],
    ["sidemove",        "number",   "Left/right speed"],
    ["upmove",          "number",   "Up/down speed"],
    ["buttons",         "number",   "Buttons bit field"],
    ["random_seed",     "number",   "Random seed for shared random functions"],
    ["mousedx",         "number",   "Mouse X movement delta"],
    ["mousedy",         "number",   "Mouse Y movement delta"]
]) }}