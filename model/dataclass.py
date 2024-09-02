from dataclasses import *


@dataclass
class Persona:
    name: str|None =None
    desc: str|None =None
    folder_id:list|None =None # This is the id of the folder
    moods:list|None = None # This is the list of moods (not expression)
    expressions:list|None = None # This is the list of possible expressions
    background:list|None = None # List of Background Images/Frames
    outfit:list|None = None # Outfit, might be too complex, just make another persona for different outfit

@dataclass
class Setting:
    globals:str|None=None # I'm also not sure, but might be useful to have this around