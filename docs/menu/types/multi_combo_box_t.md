## Getters
{{ define_function("multicombobox", "get", [
    ["index", "number", "Index of the item to get"]
], "boolean", True) }}
---
## Setters
{{ define_function("multicombobox", "set", [
    ["index", "number", "Index of the item to set"],
    ["enabled", "boolean", "Is the item enabled"]
], "", True) }}
---
{{ define_function("multicombobox", "set_items", [
    ["items", "string[]", "New multi combo box items"]
], "", True) }}