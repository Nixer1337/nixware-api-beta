## Getters
{{ define_function("combobox", "get", [], "number", True) }}
---
{{ define_function("combobox", "is_visible", [], "boolean", True) }}
---
## Setters
{{ define_function("combobox", "set", [
    ["value", "number", "New combo box value (corresponds to the index of the item)"]
], "", True) }}
---
{{ define_function("combobox", "set_items", [
    ["items", "string[]", "New combo box items"]
], "", True) }}
---
{{ define_function("combobox", "set_visible", [
    ["visibility", "boolean", "Will the element be visible"]
], "", True) }}