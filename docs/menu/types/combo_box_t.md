## Getters
{{ define_function("combobox", "get", [], "number", True) }}
---
## Setters
{{ define_function("combobox", "set", [
    ["value", "number", "New combo box value (corresponds to the index of the item)"]
], "", True) }}
---
{{ define_function("combobox", "set_items", [
    ["items", "string[]", "New combo box items"]
], "", True) }}