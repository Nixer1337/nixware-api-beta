# entitylist

{{ define_function("entitylist", "get", [
    ["idx_or_user_id", "number", "Index or User ID of the player"],
    ["is_user_id", "boolean", "Is value a User ID"]
], "entity_t") }}
---
{{ define_function("entitylist", "get_local_player", [], "entity_t") }}
---
### **get_entities**
=== "Return style"
    {{ get_function_table_and_definition("entitylist", "get_entities", [
        ["class_name_or_id", "string|number|nil", "Name or ID of the class. `nil` to get all entities"],
        ["include_dormant", "boolean", "Whether to include dormant entities or not"]
    ], "entity_t[]") }}

=== "Callback style"
    {{ get_function_table_and_definition("entitylist", "get_entities", [
        ["class_name_or_id", "string|number|nil", "Name or ID of the class. `nil` to get all entities"],
        ["include_dormant", "boolean", "Whether to include dormant entities or not"],
        ["callback", "function", "Callback function, that receives " + format_lua_type("entity_t") + " as an argument"]
    ]) }}
    ```lua linenums="1"
    entitylist.get_entities("CCSPlayer", false, function(entity)
        render.circle_fade_3d(entity:get_origin(), 50, color_t.new(1, 0, 0, 0.5), color_t.new(1, 0, 0, 0))
    end)
    ```