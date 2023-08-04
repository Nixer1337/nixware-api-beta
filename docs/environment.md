# environment

{{ define_function("", "register_callback", [
    ['name', 'string', "Event name. Look [here](/events/) for event list"],
    ["func", "function", "Callback function"],
]) }}
---
{{ define_function("", "print", [
    ["text", "string", "Text to print"],
    ["color", "color_t", "Text color", true],
]) }}
!!! info 
    You can put `\0` in the end of the text to prevent newline