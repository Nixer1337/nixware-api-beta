# cvars

## Getting convars
You can do this by `cvars.CONVAR_NAME`
``` lua linenums="1"
local MAX_RATE = 786432

if cvars.rate:get_int() ~= MAX_RATE then
    print("Bad config!", color_t.new(1, 0, 0, 1))
    cvars.rate:set_int(MAX_RATE)
end
```
Return type is {{ format_lua_type("convar_t") }}