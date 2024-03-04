class ShowText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
                "string_field": ("STRING", {
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": ""
                }),    
            },
        }

    RETURN_TYPES = ("STRING",)
    
    FUNCTION = "run"
    CATEGORY = "LLM Translate"

    def run(self, text, string_field):
        
        return {"ui": {"string_field": text}, "result": (text,)}


NODE_CLASS_MAPPINGS = {
    "ShowText": ShowText,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ShowText": "Show Text",
}
