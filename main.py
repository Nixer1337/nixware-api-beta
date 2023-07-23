from markdown_table_generator import generate_markdown, table_from_string_list, Alignment
import glob
from pathlib import Path

# parse types folder to get all types
types_paths = ["docs/types/*.md", "docs/menu/types/*.md"]
lua_types = {}
for path in types_paths:
    for file in glob.glob(path):
        #type name = file name without extension
        type_name = Path(file).stem
        p = Path(file)
        type_path = p.relative_to(*p.parts[:1]).with_suffix('')
        lua_types[type_name] = type_path

def define_env(env):
    "Hook function"

    class argument():
        name: str
        type: str
        description: str
        is_optional: bool
        def __init__(self, table):
            self.name = table[0]
            self.type = table[1]
            self.description = table[2]
            if len(table) == 4:
                self.is_optional = table[3]
            else:
                self.is_optional = False

    def get_type_link(type_name) -> str:
        #if first characters of type_name matches a type, return that type
        lua_types_keys = list(lua_types.keys())
        for key in lua_types_keys:
            if type_name.startswith(key):
                return f"../{lua_types[key]}"
        return ""
    
    def format_lua_type(type_name) -> str:
        type_link = get_type_link(type_name)
        if type_link != "":
            return f"[`{type_name}`]({type_link})"
        return f"`{type_name}`"

    @env.macro
    def define_function(table_name: str, func_name: str, temp_args: list[list], return_type: str = ""):
        args: list[argument] = []
        for arg in temp_args:
            args.append(argument(arg))
        argument_list: list[str] = []
        markdown_arguments_list: list[list[str | None]] = [["Name", "Type", "Description"]]
        for arg in args:
            if arg.is_optional:
                arg.description = f"Optional. {arg.description}"
            markdown_arguments_list.append([f"**{arg.name}**", format_lua_type(arg.type), arg.description])
            if arg.is_optional:
                arg.name = f"{arg.name}?"
            argument_list.append(f"{arg.name}: {arg.type}")
        colon = ""
        if return_type != "":
            colon = ":"
            return_type = " " + format_lua_type(return_type)
        markdown_table = ""
        if len(markdown_arguments_list) > 1:
            markdown_table = generate_markdown(table_from_string_list(rows=markdown_arguments_list))
        return f"""
### **{func_name}**
<font size=5>`:::typescript {table_name}.{func_name}({", ".join(argument_list)}){colon}`{return_type}</font>

{ markdown_table }

"""