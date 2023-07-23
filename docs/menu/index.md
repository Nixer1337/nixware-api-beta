# home
---
{{ define_function("menu", "add_check_box", [
    ["default_value",    "boolean", "Default value of the check box"],
    ["label",            "string",  "Label of the check box"],
    ["location",         "string",  "Location of the check box"],
    ["context_location", "string",  "Context location of the check box", true],
], "check_box_t") }}
---
{{ define_function("menu", "add_slider_int", [
    ["default_value", "number", "Default value of the slider"],
    ["min",           "number", "Minimum value of the slider"],
    ["max",           "number", "Maximum value of the slider"],
    ["label",         "string", "Label of the slider"],
    ["location",      "string", "Location of the slider"],
], "slider_int_t") }}
---
{{ define_function("menu", "add_slider_float", [
    ["default_value", "number", "Default value of the slider"],
    ["min",           "number", "Minimum value of the slider"],
    ["max",           "number", "Maximum value of the slider"],
    ["label",         "string", "Label of the slider"],
    ["location",      "string", "Location of the slider"],
], "slider_float_t") }}
---
{{ define_function("menu", "add_combo_box", [
    ["default_value", "number",   "Default value of the combo box"],
    ["items",         "string[]", "Array of items for the combo box"],
    ["label",         "string",   "Label of the combo box"],
    ["location",      "string",   "Location of the combo box"],
], "combo_box_t") }}
---
{{ define_function("menu", "add_multi_combo_box", [
    ["default_value", "number",   "Default value of the multi combo box"],
    ["items",         "string[]", "Array of items for the multi combo box"],
    ["label",         "string",   "Label of the multi combo box"],
    ["location",      "string",   "Location of the multi combo box"],
], "multi_combo_box_t") }}
---
{{ define_function("menu", "add_key_bind", [
    ["key",             "number",  "The key for the key bind"],
    ["type",            "number",  "The type for the key bind"],
    ["display_in_list", "boolean", "Whether to display the key bind in the key bind list"],
    ["label",           "string",  "Label of the key bind"],
    ["show_label",      "boolean", "Whether to show the label"],
    ["location",        "string",  "Location of the key bind"],
], "key_bind_t") }}
---
{{ define_function("menu", "add_color_picker", [
    ["default_value", "color_t", "Default color for the color picker"],
    ["label",         "string",  "Label of the color picker"],
    ["show_label",    "boolean", "Whether to show the label"],
    ["show_alpha",    "boolean", "Whether to show the alpha channel"],
    ["location",      "string",  "Location of the color picker"],
], "color_picker_t") }}