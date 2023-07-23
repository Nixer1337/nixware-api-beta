# render
### text
`render.text(text: string, font: font_t, pos: vec2_t, color: color_t, size?: number)`
### setup_font
`render.setup_font(filename: string, size: number, flags: number): font_t`
### line
`render.line(from: vec2_t, to: vec2_t, color: color_t)`
### rect
`render.rect(from: vec2_t, to: vec2_t, color: color_t, rounding: number)`
### rect_filled
`render.rect_filled(from: vec2_t, to: vec2_t, color: color_t, rounding: number)`
### rect_filled_fade
`render.rect_filled_fade(from: vec2_t, to: vec2_t, col_upr_left: color_t, col_upr_right: color_t, col_bot_right: color_t, col_bot_left: color_t)`
### circle_fade
`render.circle_fade(pos: vec2_t, radius: number, color_in: color_t, color_out: color_t)`
### circle
`render.circle(pos: vec2_t, radius: number, segments: number, filled: boolean, color: color_t)`
### filled_polygon
`render.filled_polygon(points: vec2_t[], color: color_t)`
### poly_line
`render.poly_line(points: vec2_t[], color: color_t)`
### push_clip_rect
`render.push_clip_rect(from: vec2_t, to: vec2_t, intersect_with_current_clip_rect?: boolean)`
### pop_clip_rect
`render.pop_clip_rect()`
### world_to_screen
`render.world_to_screen(pos: vec3_t): vec2_t|nil`
### calc_text_size
`render.calc_text_size(text: string, font: font_t, size?: number): vec2_t`