## Getters
{{ define_function("colorpicker", "get", [], "color_t", True) }}
---
{{ define_function("colorpicker", "is_visible", [], "boolean", True) }}
---
## Setters
{{ define_function("colorpicker", "set", [
    ["value", "color_t", "New color the color picker will be set to"]
], "", True) }}
---
{{ define_function("colorpicker", "set_visible", [
    ["visibility", "boolean", "Will the element be visible"]
], "", True) }}