class ExtraPicker:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "extra_type": (["Zombies", "Robots", "Aliens"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("extra_prompt",)

    FUNCTION = "generate_extra_prompt"

    CATEGORY = "Chess"

    def generate_extra_prompt(self, extra_type):
        extra_prompt_map = {
            "Zombies": "(solo) piece (zombie-like:1.5), (decaying:1.3), (undead:1.4), (tattered clothing:1.2), (horrifying:1.2), (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Robots": "(solo) piece (robotic:1.5), (mechanical:1.3), (metallic:1.4), (futuristic:1.2), (high-tech:1.2), (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Aliens": "(solo) piece (alien-like:1.5), (otherworldly:1.3), (extraterrestrial:1.4), (bizarre:1.2), (unearthly:1.2), (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)"
        }
        return (extra_prompt_map[extra_type],)

NODE_CLASS_MAPPINGS = {
    "ExtraPicker": ExtraPicker
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ExtraPicker": "Extra Picker"
}