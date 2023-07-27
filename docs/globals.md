# globals

{{ define_function("", "register_callback", [
    ['name', 'string', "Event name. Look [here](/events/) for event list"],
    ["func", "function", "Callback function"],
]) }}
---
{{ define_function("", "print", [
    ["text", "string", "Text to print"],
    ["color", "color_t", "Text color", true],
]) }}