# esp

## ESP types
| Name           |
| -------------- |
| `enemy`        |
| `local_player` |
| `team`         |

## Functions

{{ define_function("esp.local_player", "add_bar", [
    ["bar_name", "string", "Name of the bar"],
    ["callback", "function", "Function that receives " + format_lua_type("entity_t") + " in the argument, and should return a `number` in range of `[0-100]`. If returns `nil` then bar will not be drawn"]
], "") }}

??? example
    ``` lua linenums="1"
    local m_vecVelocity = engine.get_netvar_offset("DT_BasePlayer", "m_vecVelocity[0]")

    local function vec3_len(x, y, z)
        return math.sqrt(x * x + y * y + z * z)
    end

    esp.local_player.add_bar("Velocity", function(entity)
        local x = ffi.cast("float*", entity[m_vecVelocity])[0]
        local y = ffi.cast("float*", entity[m_vecVelocity])[1]
        local z = ffi.cast("float*", entity[m_vecVelocity])[2]

        return vec3_len(x, y, z) / 250 * 100
    end)

    ```

{{ define_function("esp.enemy", "add_text", [
    ["text_name",     "string",   "Name of the indicator"],
    ["preview_value", "string",   "Preview value of the indicator"],
    ["callback",      "function", "Function that receives " + format_lua_type("entity_t") + " in the argument, and should return a `string` value. If returns `nil` then indicator will not be drawn"]
], "") }}
??? example
    ``` lua linenums="1"
    local m_bIsScoped = engine.get_netvar_offset("DT_CSPlayer", "m_bIsScoped")

    esp.enemy.add_text("Scoped", "Scoped", function(entity)
        if not entity:is_dormant() and ffi.cast("bool*", entity[m_bIsScoped])[0] then
            return "Scoped"
        end
    end)
    ```