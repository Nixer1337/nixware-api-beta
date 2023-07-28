## Getters

{{ define_function("event", "get_name", [], "string", True) }}
---
{{ define_function("event", "get_bool", [
    ["key_name", "string", "Key name"],
    ["default_value", "boolean", "Default value which will be returned if event value isn't available", true]
], "boolean", True) }}
---
{{ define_function("event", "get_int", [
    ["key_name", "string", "Key name"],
    ["default_value", "number", "Default value which will be returned if event value isn't available", true]
], "number", True) }}
---
{{ define_function("event", "get_uint64", [
    ["key_name", "string", "Key name"],
    ["default_value", "number", "Default value which will be returned if event value isn't available", true]
], "number", True) }}
---
{{ define_function("event", "get_float", [
    ["key_name", "string", "Key name"],
    ["default_value", "number", "Default value which will be returned if event value isn't available", true]
], "number", True) }}
---
{{ define_function("event", "get_string", [
    ["key_name", "string", "Key name"],
    ["default_value", "string", "Default value which will be returned if event value isn't available", true]
], "string", True) }}
---
{{ define_function("event", "get_wstring", [
    ["key_name", "string", "Key name"],
    ["default_value", "string", "Default value which will be returned if event value isn't available", true]
], "string", True) }}
---
## Setters

{{ define_function("event", "set_bool", [
    ["key_name", "string", "Key name"],
    ["value", "boolean", "New boolean value"]
], "", True) }}
---
{{ define_function("event", "set_int", [
    ["key_name", "string", "Key name"],
    ["value", "number", "New int value"]
], "", True) }}
---
{{ define_function("event", "set_uint64", [
    ["key_name", "string", "Key name"],
    ["value", "number", "New uint64 value"]
], "", True) }}
---
{{ define_function("event", "set_float", [
    ["key_name", "string", "Key name"],
    ["value", "number", "New float value"]
], "", True) }}
---
{{ define_function("event", "set_string", [
    ["key_name", "string", "Key name"],
    ["value", "string", "New string value"]
], "", True) }}
---
{{ define_function("event", "set_wstring", [
    ["key_name", "string", "Key name"],
    ["value", "string", "New wstring value"]
], "", True) }}