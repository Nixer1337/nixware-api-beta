# environment

!!! info
    This page describes only overridden and custom functions.  
    Other functions of the standard Lua environment haven't been changed in any aspect

{{ define_function("", "register_callback", [
    ['name', 'string', "Event name. Look [here](/events/) for event list"],
    ["func", "function", "Callback function"],
]) }}
---
{{ define_function("", "find_pattern", [
    ["module", 'string', "Module name to search the pattern in"],
    ["pattern", "string", "Pattern to search for"],
    ["offset", "number", "Byte offset", true],
], "void*") }}
---
{{ define_function("", "print", [
    ["text", "string", "Text to print"],
    ["color", "color_t", "Text color", true],
]) }}
!!! info 
    You can put `\0` in the end of the text to prevent newline