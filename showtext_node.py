class ShowText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
            },
        }


    RETURN_TYPES = ("STRING",)

    FUNCTION = "run"

    CATEGORY = "LLM Translate"

    def run(self, text):
        return {"ui": {"text": text}, "result": (text,)}


NODE_CLASS_MAPPINGS = {
    "ShowText": ShowText,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ShowText": "Show Text",
}
