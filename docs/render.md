# render
---
## Functions
{{ define_function("render", "setup_font", [
    ["filename",    "string",   "Path to the font"],
    ["size",        "number",   "Font size"],
    ["flags",       "number",   "Font flags"],
], "font_t") }}
---
{{ define_function("render", "world_to_screen", [
    ["pos", "vec3_t", "World position"],
], "vec3_t") }}
---
{{ define_function("render", "calc_text_size", [
    ["text",    "string",   "Text size of which will be calculated"],
    ["font",    "font_t",   "Font object"],
    ["size",   "number",   "Font size", true],
], "vec2_t") }}
---
## Draw functions
{{ define_function("render", "text", [
    ["text",    "string",   "Text to render"],
    ["font",    "font_t",   "Font object"],
    ["pos",     "vec2_t",   "Position of where text will be rendered"],
    ["color",   "color_t",  "Text color"],
    ["size",    "number",   "Text size", true],
]) }}
---
{{ define_function("render", "line", [
    ["from",    "vec2_t",   "Start position of the line"],
    ["to",      "vec2_t",   "End position of the line"],
    ["color",   "color_t",  "Color of the line"],
]) }}
---
{{ define_function("render", "rect", [
    ["from",        "vec2_t",   "Start position of the rectangle"],
    ["to",          "vec2_t",   "End position of the rectangle"],
    ["color",       "color_t",  "Color of the rectangle"],
    ["rounding",    "number",   "Rounding of the rectangle", true],
]) }}
---
{{ define_function("render", "rect_filled", [
    ["from",        "vec2_t",   "Start position of a rectangle"],
    ["to",          "vec2_t",   "End position of the rectangle"],
    ["color",       "color_t",  "Color of the rectangle"],
    ["rounding",    "number",   "Rounding of the rectangle", true],
]) }}
---
{{ define_function("render", "rect_filled_fade", [
    ["from",            "vec2_t",   "Start position of a rectangle"],
    ["to",              "vec2_t",   "Font object"],
    ["col_upr_left",    "color_t",  "Color of the top left corner"],
    ["col_upr_right",   "color_t",  "Color of the top right corner"],
    ["col_bot_right",   "color_t",  "Color of the bottom right corner"],
    ["col_bot_left",    "color_t",  "Color of the bottom left corner"],
]) }}
<!-- ["rounding",    "number",   "Rounding of the rectangle", true], -->
---
{{ define_function("render", "circle", [
    ["pos",         "vec2_t",   "Position of the circle"],
    ["radius",      "number",   "Radius of the circle"],
    ["segments",    "number",   "Count of the circle segments"],
    ["filled",      "boolean",  "Is the circle filled"],
    ["color",       "color_t",  "Color of the circle"],
]) }}
---
{{ define_function("render", "circle_fade", [
    ["pos",         "vec2_t",   "Position of the circle"],
    ["radius",      "number",   "Radius of the circle"],
    ["color_in",    "color_t",  "Color of the center of the circle"],
    ["color_out",   "color_t",  "Color of the edge of the circle"],
]) }}
---
{{ define_function("render", "filled_polygon", [
    ["points",  "vec2_t[]", "Array of screen positions"],
    ["color",   "color_t",  "Color of the polygon"],
]) }}
---
{{ define_function("render", "poly_line", [
    ["points",  "vec2_t[]", "Array of screen positions"],
    ["color",   "color_t",  "Color of the polyline"],
]) }}
---
{{ define_function("render", "push_clip_rect", [
    ["from",                                "vec2_t",   "Start position of the clip rect"],
    ["to",                                  "vec2_t",   "End position of the clip rect"],
    ["intersect_with_current_clip_rect",    "boolean",  "Allow intersections with other clips", true],
]) }}
---
{{ define_function("render", "pop_clip_rect", []) }}





<!-- ``` lua linenums="1"
for i = 10, 60 do
    renderer.setup_font("C:/windows/fonts/tahomabd.ttf", i, 0)
end
register_callback("paint", function()
    renderer.rect_filled(vec2_t.new(100, 100), vec2_t.new(200, 200), color_t.new(1, 1, 1, 1))
end)
``` -->

