## Getters
{{ define_function("slider", "get", [], "number", True) }}
---
{{ define_function("slider", "is_visible", [], "boolean", True) }}
---
## Setters
{{ define_function("slider", "set", [
    ["value", "number", "New slider value"]
], "", True) }}
---
{{ define_function("slider", "set_visible", [
    ["visibility", "boolean", "Will the element be visible"]
], "", True) }}