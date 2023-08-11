# globals

{{ get_arguments_table([
    ["cur_time",                "number",           "Current server time in seconds"],
    ["real_time",               "number",           "Current local time in seconds"],
    ["frame_time",              "number",           "Time that was used to render a last game frame in seconds"],
    ["frame_count",             "number",           "Total rendered frames count"],
    ["absolute_frame_time",     "number",           "Time that was used to render a last game frame in seconds"],
    ["tick_count",              "number",           "Count of ticks that server has handled"],
    ["interval_per_tick",       "number",           "Duration of a tick in seconds"],
    ["max_clients",             "number",           "Maximum number of players allowed on the server"],
    ["choked_commands",         "number",           "Count of choked commands"],
    ["command_ack",             "number",           "Last command that server has been acknowledged of"],
    ["last_outgoing_command",   "number",           "Number of last command sequence number acknowledged by server"],
    ["delta_tick",              "number",           "Last valid received server tick"],
    ["is_connected",            "boolean",          "Is client connected to server or loading in game"],
    ["is_in_game",              "boolean",          "Is client loaded to server and in game"],
    ["camera_in_third_person",  "boolean",          "Is camera in third person"]
]) }}