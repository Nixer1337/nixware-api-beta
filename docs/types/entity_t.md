## Entity functions

{{ define_function("entity", "is_player", [], "boolean", True) }}
---
{{ define_function("entity", "is_weapon", [], "boolean", True) }}
---
{{ define_function("entity", "is_dormant", [], "boolean", True) }}
---
{{ define_function("entity", "get_index", [], "number", True) }}
---
{{ define_function("entity", "get_origin", [], "vec3_t", True) }}
Returns abs origin of the entity

---
{{ define_function("entity", "get_class_id", [], "number", True) }}
---
{{ define_function("entity", "get_class_name", [], "string", True) }}
---
## Getting FFI pointer
To get entity pointer you can use `entity[0]`  
Also you can use `entity[ADDRESS]` to get address pointing to any offset of the entity
Hexadecimal and decimal number are both supported
!!! example
    This example will print money of all players
    ```lua linenums="1"
    entitylist.get_entities("CCSPlayer", false, function(entity)
        local origin = entity:get_origin()
        local origin2 = render.world_to_screen(origin)
        local money = ffi.cast("int*", entity[0x117B8])[0] --m_iAccount: 0x117B8

        if origin2 ~= nil then
            render.text(tostring(money), 0, origin2)
        end
    end)
    ```
