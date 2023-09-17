## Getters
{{ define_function("colorpicker", "get", [], "color_t", True) }}
---
{{ element_getters("colorpicker") }}
---
## Setters
{{ define_function("colorpicker", "set", [
    ["value", "color_t", "New color the color picker will be set to"]
], "", True) }}
---
{{ element_setters("colorpicker") }}
