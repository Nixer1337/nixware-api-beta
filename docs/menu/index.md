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
    With context you can add a context menu to your element, which will be shown if you right click on it.
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
??? example
    ``` lua linenums="1"
    local combobox =
        menu.add_combo_box("Extra", "Ragebot/Globals", {"DDoS on peek", "Crash all enemies"}, 0)
    ```

---
{{ define_function("menu", "add_multi_combo_box", [
    ["label",         "string",   "Label of the multi combo box"],
    ["location",      "string",   "Location of the multi combo box"],
    ["items",         "string[]", "Array of items for the multi combo box"],
    ["default_value", "number[]", "List of active by default indeces", true],
], "multi_combo_box_t") }}
??? example
    ``` lua linenums="1"
    local combobox =
        menu.add_combo_box("Extra", "Ragebot/Globals", {"DDoS on peek", "Crash all enemies", "Crash myself"}, {0, 1})
    ```
<!-- ---
??? example
    ``` lua linenums="1"
    local combobox =
        menu.add_combo_box("Extra", "Ragebot/Globals", {"DDoS on peek", "Crash all enemies"}, 0)
    ``` -->
---
{{ define_function("menu", "add_key_bind", [
    ["label",           "string",  "Label of the key bind"],
    ["location",        "string",  "Location of the key bind"],
    ["show_label",      "boolean", "Whether to show the label", true],
    ["key",             "number",  "The key for the key bind", true],
    ["type",            "number",  "The type for the key bind", true],
    ["display_in_list", "boolean", "Whether to display the key bind in the key bind list", true],
], "key_bind_t") }}
??? example
    This code will create a key bind attached to check box
    ``` lua linenums="1"
    local box = menu.add_check_box("best cheat", "Ragebot/Globals")
    local bind = menu.add_key_bind("best cheat", "Ragebot/Globals", false)
    ```
    This is how to create a standalone key bind
    ``` lua linenums="1"
    local bind = menu.add_key_bind("best cheat", "Ragebot/Globals")
    ```
---
{{ define_function("menu", "add_color_picker", [
    ["label",         "string",  "Label of the color picker"],
    ["location",      "string",  "Location of the color picker"],
    ["show_label",    "boolean", "Whether to show the label", true],
    ["show_alpha",    "boolean", "Whether to show the alpha channel", true],
    ["default_value", "color_t", "Default color for the color picker", true],
], "color_picker_t") }}
??? example
    This code will create a color picker attached to check box
    ``` lua linenums="1"
    local box = menu.add_check_box("test", "Ragebot/Globals")
    local color_picker = menu.add_color_picker("test", "Ragebot/Globals", false)
    ```
    This code will create a standalone color picker
    ``` lua linenums="1"
    local color_picker = menu.add_color_picker("test", "Ragebot/Globals")
    ```
---
{{ define_function("menu", "add_button", [
    ["label",    "string",  "Label of the button"],
    ["location", "string",  "Location of the button"],
    ["callback", "function", "Callback which will be executed when the button is pressed"],
], "button_t") }}
??? example
    ``` lua linenums="1"
    local my_button = menu.add_button("My button", "Misc/Misc", function()
        print("My button exec!")
    end)
    ```
---
## Functions to find elements
{{ define_function("menu", "find_check_box", [
    ["label",    "string", "Label of the check box"],
    ["location", "string", "Location of the check box"],
], "check_box_t") }}
??? example
    ``` lua linenums="1"
    local ragebot_enabled = menu.find_check_box("Enabled", "Ragebot/Globals")
    ```
---
{{ define_function("menu", "find_slider_int", [
    ["label",    "string", "Label of the slider"],
    ["location", "string", "Location of the slider"],
], "slider_int_t") }}
??? example
    ``` lua linenums="1"
    local ragebot_fov = menu.find_slider_int("FOV", "Ragebot/Globals")
    ```
---
{{ define_function("menu", "find_slider_float", [
    ["label",    "string", "Label of the slider"],
    ["location", "string", "Location of the slider"],
], "slider_float_t") }}
??? example
    ``` lua linenums="1"
    local viewmodel_fov = menu.find_slider_float("FOV", "Visuals/Viewmodel")
    ```
---
{{ define_function("menu", "find_combo_box", [
    ["label",    "string", "Label of the combo box"],
    ["location", "string", "Location of the combo box"],
], "combo_box_t") }}
---
{{ define_function("menu", "find_multi_combo_box", [
    ["label",    "string", "Label of the multi combo box"],
    ["location", "string", "Location of the multi combo box"],
], "multi_combo_box_t") }}
---
{{ define_function("menu", "find_key_bind", [
    ["label",    "string", "Label of the key bind"],
    ["location", "string", "Location of the key bind"],
], "key_bind_t") }}
---
{{ define_function("menu", "find_color_picker", [
    ["label",    "string", "Label of the color picker"],
    ["location", "string", "Location of the color picker"],
], "color_picker_t") }}
---
## Other functions
{{ define_function("menu", "get_menu_rect", [], "vec4_t")}}
??? example
    ``` lua linenums="1"
    register_callback("paint", function()
        if menu.is_visible() then
            local menu_rect = menu.get_menu_rect()

            render.rect_filled_fade(
                vec2_t.new(menu_rect.x - 5, menu_rect.y - 5),
                vec2_t.new(menu_rect.z + 5, menu_rect.w + 5),
                color_t.new(1, 0, 0, 0.3),
                color_t.new(0, 0, 1, 0),
                color_t.new(0, 0, 1, 0.3),
                color_t.new(1, 0, 0, 0)
            )
        end
    end)
    ```
---
{{ define_function("menu", "is_visible", [], "boolean")}}
---
{{ define_function("menu", "dump", []) }}
Prints all elements to console