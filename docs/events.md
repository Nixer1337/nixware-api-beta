# events

{{ define_function("", "create_move", [
    ["cmd", "user_cmd_t", "User command"],
]) }}
---
{{ define_function("", "paint", []) }}
---
{{ define_function("", "override_view", [
    ["view_setup", "view_setup_t", "View setup"],
]) }}
---
{{ define_function("", "game_event", [
    ["event", "game_event_t", "Game event"],
]) }}
!!! note
    List of all game events can be found <a href="https://wiki.alliedmods.net/Counter-Strike:_Global_Offensive_Events" target="_blank">here</a>
---
{{ define_function("", "unload", []) }}