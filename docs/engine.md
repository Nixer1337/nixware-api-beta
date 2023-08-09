# engine

### trace_line
=== "Skip single entity"
    {{ get_function_table_and_definition("engine", "trace_line", [
        ["from", "vec3_t", "Position to start tracing from"],
        ["to",   "vec3_t", "Position where the trace ends"],
        ["skip", "entity_t", "Entity to skip", true],
        ["mask", "number", "Trace mask", true],
        ["type", "number", "Trace type [0-3]<br/>`0`: Everything `Default`<br/>`1`: World only<br/>`2`: Entities only<br/>`3`: Everything filter props", true]
    ], "trace_t") }}
=== "Skip multiple entities"
    {{ get_function_table_and_definition("engine", "trace_line", [
        ["from", "vec3_t", "Position to start tracing from"],
        ["to",   "vec3_t", "Position where the trace ends"],
        ["skip", "entity_t[]", "Table of entities to skip", true],
        ["mask", "number", "Trace mask", true],
        ["type", "number", "Trace type [0-3]<br/>`0`: Everything `Default`<br/>`1`: World only<br/>`2`: Entities only<br/>`3`: Everything filter props", true]
    ], "trace_t") }}
=== "Filter entities"
    {{ get_function_table_and_definition("engine", "trace_line", [
        ["from", "vec3_t", "Position to start tracing from"],
        ["to",   "vec3_t", "Position where the trace ends"],
        ["skip", "function", "Function, that receives " + format_lua_type("entity_t") + " and `contents_mask` in its arguments, and skips an entity if function returns `true`", true],
        ["mask", "number", "Trace mask", true],
        ["type", "number", "Trace type [0-3]<br/>`0`: Everything `Default`<br/>`1`: World only<br/>`2`: Entities only<br/>`3`: Everything filter props", true]
    ], "trace_t") }}
    
---

### trace_hull
=== "Skip single entity"
    {{ get_function_table_and_definition("engine", "trace_hull", [
        ["from", "vec3_t", "Position to start tracing from"],
        ["to",   "vec3_t", "Position where the trace ends"],
        ["mins", "vec3_t", "Mins of the hull"],
        ["maxs", "vec3_t", "Maxs of the hull"],
        ["skip", "entity_t", "Entity to skip", true],
        ["mask", "number", "Trace mask", true],
        ["type", "number", "Trace type [0-3]<br/>`0`: Everything `Default`<br/>`1`: World only<br/>`2`: Entities only<br/>`3`: Everything filter props", true]
    ], "trace_t") }}
=== "Skip multiple entities"
    {{ get_function_table_and_definition("engine", "trace_hull", [
        ["from", "vec3_t", "Position to start tracing from"],
        ["to",   "vec3_t", "Position where the trace ends"],
        ["mins", "vec3_t", "Mins of the hull"],
        ["maxs", "vec3_t", "Maxs of the hull"],
        ["skip", "entity_t[]", "Table of entities to skip", true],
        ["mask", "number", "Trace mask", true],
        ["type", "number", "Trace type [0-3]<br/>`0`: Everything `Default`<br/>`1`: World only<br/>`2`: Entities only<br/>`3`: Everything filter props", true]
    ], "trace_t") }}
=== "Filter entities"
    {{ get_function_table_and_definition("engine", "trace_hull", [
        ["from", "vec3_t", "Position to start tracing from"],
        ["to",   "vec3_t", "Position where the trace ends"],
        ["mins", "vec3_t", "Mins of the hull"],
        ["maxs", "vec3_t", "Maxs of the hull"],
        ["skip", "function", "Function, that receives " + format_lua_type("entity_t") + " and `contents_mask` in its arguments, and skips an entity if function returns `true`", true],
        ["mask", "number", "Trace mask", true],
        ["type", "number", "Trace type [0-3]<br/>`0`: Everything `Default`<br/>`1`: World only<br/>`2`: Entities only<br/>`3`: Everything filter props", true]
    ], "trace_t") }}

---
{{ define_function("engine", "get_netvar_offset", [
    ["table_name", "string", "Name of the table"],
    ["prop_name", "string", "Name of the property"]
], "number") }}
---
{{ define_function("engine", "get_view_angles", [], "angle_t") }}
---
{{ define_function("engine", "set_view_angles", [
    ["angles", "angle_t", "New view angles"]
]) }}
