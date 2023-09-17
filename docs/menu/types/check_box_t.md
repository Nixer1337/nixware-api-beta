## Getters
{{ define_function("checkbox", "get", [], "boolean", True) }}
---
{{ element_getters("checkbox") }}
---
## Setters
{{ define_function("checkbox", "set", [
    ["value", "boolean", "Value to set the check box to"]
], "", True) }}
---
{{ element_setters("checkbox") }}
<!-- 
{{ define_function("checkbox", "set_label", [
    ["label", "string", "New check box label"]
], "", True) }} -->
