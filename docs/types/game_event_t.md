## Getters

{{ define_function("event", "get_name", [], "string", True) }}
---
{{ define_function("event", "get_bool", [], "boolean", True) }}
---
{{ define_function("event", "get_int", [], "number", True) }}
---
{{ define_function("event", "get_uint64", [], "number", True) }}
---
{{ define_function("event", "get_float", [], "number", True) }}
---
{{ define_function("event", "get_string", [], "string", True) }}
---
{{ define_function("event", "get_wstring", [], "number", True) }}
---
## Setters

{{ define_function("event", "set_bool", [
    ["value", "boolean", "New boolean value"]
], "", True) }}
---
{{ define_function("event", "set_int", [
    ["value", "number", "New int value"]
], "", True) }}
---
{{ define_function("event", "set_uint64", [
    ["value", "number", "New uint64 value"]
], "", True) }}
---
{{ define_function("event", "set_float", [
    ["value", "number", "New float value"]
], "", True) }}
---
{{ define_function("event", "set_string", [
    ["value", "string", "New string value"]
], "", True) }}
---
{{ define_function("event", "set_wstring", [
    ["value", "string", "New wstring value"]
], "", True) }}