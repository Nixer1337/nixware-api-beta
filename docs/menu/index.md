# home
---
## Functions to add elements

!!! info
    You can add elements in every location you want  
    For example: `Ragebot/Globals` or `Visuals/Other`

{{ define_function("menu", "add_check_box", [
    ["label",            "string",  "Label of the check box"],
    ["location",         "string",  "Location of the check box"],
    ["default_value",    "boolean", "Default value of the check box", true],
    ["context_location", "string",  "Location of the context menu", true],
], "check_box_t") }}
??? example
    ``` lua linenums="1"
    local my_checkbox = menu.add_check_box("My Checkbox!", "Misc/Misc")
    ```
??? question "What is "context"?"
    ``` lua linenums="1"
    local my_checkbox = menu.add_check_box("My Checkbox!", "Misc/Misc", false, "Misc/Misc/Test")
    --"Misc/Misc/Test" is the context location
    --all elements with this context location will be shown in the context menu
    local context_checkbox = menu.add_check_box("Context Checkbox", "Misc/Misc/Test", true)
    local context_slider = menu.add_slider_int("Context Slider", "Misc/Misc/Test", 0, 100, 50)
    ```
    If you right click on "My Checkbox!", it will show you the context menu with "Context Checkbox" and "Context Slider".

---
{{ define_function("menu", "add_slider_int", [
    ["label",         "string", "Label of the slider"],
    ["location",      "string", "Location of the slider"],
    ["min",           "number", "Minimum value of the slider"],
    ["max",           "number", "Maximum value of the slider"],
    ["default_value", "number", "Default value of the slider", true],
], "slider_int_t") }}
??? example
    ``` lua linenums="1"
    local my_slider = menu.add_slider_int("My Slider :)", "Misc/Misc", 0, 255)
    ```

---
{{ define_function("menu", "add_slider_float", [
    ["label",         "string", "Label of the slider"],
    ["location",      "string", "Location of the slider"],
    ["min",           "number", "Minimum value of the slider"],
    ["max",           "number", "Maximum value of the slider"],
    ["default_value", "number", "Default value of the slider", true],
], "slider_float_t") }}
??? example
    ``` lua linenums="1"
    local my_slider = menu.add_slider_float("My Slider :)", "Misc/Misc", 0, 255)
    ```

---
{{ define_function("menu", "add_combo_box", [
    ["label",         "string",   "Label of the combo box"],
    ["location",      "string",   "Location of the combo box"],
    ["items",         "string[]", "Array of items for the combo box"],
    ["default_value", "number",   "Default value of the combo box", true],
], "combo_box_t") }}
---
{{ define_function("menu", "add_multi_combo_box", [
    ["label",         "string",   "Label of the multi combo box"],
    ["location",      "string",   "Location of the multi combo box"],
    ["items",         "string[]", "Array of items for the multi combo box"],
    ["default_value", "number",   "Default value of the multi combo box", true],
], "multi_combo_box_t") }}
---
{{ define_function("menu", "add_key_bind", [
    ["label",           "string",  "Label of the key bind"],
    ["location",        "string",  "Location of the key bind"],
    ["show_label",      "boolean", "Whether to show the label", true],
    ["key",             "number",  "The key for the key bind", true],
    ["type",            "number",  "The type for the key bind", true],
    ["display_in_list", "boolean", "Whether to display the key bind in the key bind list", true],
], "key_bind_t") }}
---
{{ define_function("menu", "add_color_picker", [
    ["label",         "string",  "Label of the color picker"],
    ["location",      "string",  "Location of the color picker"],
    ["show_label",    "boolean", "Whether to show the label", true],
    ["show_alpha",    "boolean", "Whether to show the alpha channel", true],
    ["default_value", "color_t", "Default color for the color picker", true],
], "color_picker_t") }}
---
## Functions to find elements
{{ define_function("menu", "find_check_box", [
    ["location", "string", "Location of the check box"],
    ["label",    "string", "Label of the check box"],
], "check_box_t") }}
---
{{ define_function("menu", "find_slider_int", [
    ["location", "string", "Location of the slider"],
    ["label",    "string", "Label of the slider"],
], "slider_int_t") }}
---
{{ define_function("menu", "find_slider_float", [
    ["location", "string", "Location of the slider"],
    ["label",    "string", "Label of the slider"],
], "slider_float_t") }}
---
{{ define_function("menu", "find_combo_box", [
    ["location", "string", "Location of the combo box"],
    ["label",    "string", "Label of the combo box"],
], "combo_box_t") }}
---
{{ define_function("menu", "find_multi_combo_box", [
    ["location", "string", "Location of the multi combo box"],
    ["label",    "string", "Label of the multi combo box"],
], "multi_combo_box_t") }}
---
{{ define_function("menu", "find_key_bind", [
    ["location", "string", "Location of the key bind"],
    ["label",    "string", "Label of the key bind"],
], "key_bind_t") }}
---
{{ define_function("menu", "find_color_picker", [
    ["location", "string", "Location of the color picker"],
    ["label",    "string", "Label of the color picker"],
], "color_picker_t") }}