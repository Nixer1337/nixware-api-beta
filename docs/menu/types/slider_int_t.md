## Getters
{{ define_function("slider", "get", [], "number", True) }}
---
{{ element_getters("slider") }}
---
## Setters
{{ define_function("slider", "set", [
    ["value", "number", "New slider value"]
], "", True) }}
---
{{ element_setters("slider") }}