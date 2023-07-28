## Getters
{{ define_function("keybind", "is_active", [], "boolean", True) }}
---
{{ define_function("keybind", "get_key", [], "number", True) }}
---
{{ define_function("keybind", "get_type", [], "number", True) }}
---
{{ define_function("keybind", "get_display_in_list", [], "boolean", True) }}
---
## Setters
{{ define_function("keybind", "set_type", [
    ["type", "number", "Type to set the key bind to"]
], "", True) }}
---
{{ define_function("keybind", "set_key", [
    ["key", "number", "Key which will be used to activate the key bind"]
], "", True) }}
---
{{ define_function("keybind", "set_display_in_list", [
    ["display_in_list", "boolean", "Display or hide the keybind in the active binds list"]
], "", True) }}