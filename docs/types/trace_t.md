## trace_t
{{ get_arguments_table([
    ["start_pos",           "vec3_t",                    "Start position"],
    ["end_pos",             "vec3_t",                    "Final position"],
    ["plane",               "[`plane_t`](#plane_t)",     "Surface normal at impact."],
    ["fraction",            "number",                    "Percentage in the range [0.0, 1.0]. How far the trace went before hitting something. `1.0` - didn't hit anything"],
    ["contents",            "number",                    "Contents on other side of surface hit"],
    ["disp_flags",          "number",                    "Displacement flags for marking surfaces with data"],
    ["all_solid",           "boolean",                   "Returns `true` if the plane is invalid"],
    ["start_solid",         "boolean",                   "Returns `true` if the initial point was in a solid area"],
    ["surface",             "[`surface_t`](#surface_t)", "Surface hit (impact surface). "],
    ["hitgroup",            "number",                    "`0` - generic, non-zero is specific body part"],
    ["physics_bone",        "number",                    "Physics bone that was hit by the trace"],
    ["world_surface_index", "number",                    "Index of the `msurface2_t`, if applicable"],
    ["entity",              "entity_t",                  "Entity that was hit by the trace"],
    ["hitbox",              "number",                    "Hitbox that was hit by the trace"],
    ["did_hit",             "function",                  "Returns `true` if there was any kind of impact at all"],
    ["did_hit_world",       "function",                  "Returns `true` if the entity points at the world entity"],
    ["did_hit_non_world",   "function",                  "Returns `true` if the trace hit something and it wasn't the world"],
    ["is_visible",          "function",                  "Returns `true` if the final position is visible"]
]) }}

---
## surface_t

{{ get_arguments_table([
    ["name",  "string"],
    ["props", "number"],
    ["flags", "number"],
]) }}

---
## plane_t

{{ get_arguments_table([
    ["normal",   "vec3_t"],
    ["dist",     "number"],
    ["type",     "number"],
    ["signbits", "number"],
]) }}