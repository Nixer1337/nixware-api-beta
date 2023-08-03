## Getters

{{ define_function("convar", "get_name", [], "string", True) }}
---
{{ define_function("convar", "get_bool", [], "boolean", True) }}
---
{{ define_function("convar", "get_int", [], "number", True) }}
---
{{ define_function("convar", "get_float", [], "number", True) }}
---
{{ define_function("convar", "get_string", [], "string", True) }}
---

## Setters

{{ define_function("convar", "set_bool", [
    ["value", "boolean", "New boolean value"],
], "", True) }}
---
{{ define_function("convar", "set_int", [
    ["value", "number", "New int value"],
], "", True) }}
---
{{ define_function("convar", "set_float", [
    ["value", "number", "New float value"],
], "", True) }}
---
{{ define_function("convar", "set_string", [
    ["value", "string", "New string value"],
], "", True) }}
---