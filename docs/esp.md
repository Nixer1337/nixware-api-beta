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
    ["callback", "function", "Function that receives " + format_lua_type("entity_t") + " in the argument, and should return a `number` in range of `[0-100]`"]
], "", True) }}

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
    ["bar_name",      "string",   "Name of the indicator"],
    ["preview_value", "string",   "Preview value of the indicator"],
    ["callback",      "function", "Function that receives " + format_lua_type("entity_t") + " in the argument, and should return a `string` value"]
], "", True) }}
??? example
    ``` lua linenums="1"
    local m_vecVelocity = engine.get_netvar_offset("DT_BasePlayer", "m_vecVelocity[0]")

    local function vec3_len(x, y, z)
        return math.sqrt(x * x + y * y + z * z)
    end

    esp.local_player.add_text("Velocity text", "250.00", function(entity)
        local x = ffi.cast("float*", entity[m_vecVelocity])[0]
        local y = ffi.cast("float*", entity[m_vecVelocity])[1]
        local z = ffi.cast("float*", entity[m_vecVelocity])[2]

        return string.format("%.2f", vec3_len(x, y, z))
    end)

    ```