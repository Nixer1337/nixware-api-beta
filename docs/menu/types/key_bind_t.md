{{ define_function("keybind", "is_active", [], "boolean", True) }}
{{ define_function("keybind", "get_key", [], "number", True) }}
{{ define_function("keybind", "get_type", [], "number", True) }}
{{ define_function("keybind", "set_type", [
    ["type", "number", "Type to set the key bind to"]
], "", True) }}
{{ define_function("keybind", "set_key", [
    ["key", "number", "Key which will be used to activate the key bind"]
], "", True) }}