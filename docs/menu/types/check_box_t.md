## Getters
{{ define_function("checkbox", "get", [], "boolean", True) }}
---
{{ define_function("checkbox", "is_visible", [], "boolean", True) }}
---
## Setters
{{ define_function("checkbox", "set", [
    ["value", "boolean", "Value to set the check box to"]
], "", True) }}
---
{{ define_function("checkbox", "set_visible", [
    ["visibility", "boolean", "Will the element be visible"]
], "", True) }}
---
<!-- 
{{ define_function("checkbox", "set_label", [
    ["label", "string", "New check box label"]
], "", True) }} -->
