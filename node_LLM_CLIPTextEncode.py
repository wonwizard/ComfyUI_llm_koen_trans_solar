class LLM_CLIPTextEncode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": 
                {"intext": ("STRING", {"forceInput": True}), 
                 "text": ("STRING", {"multiline": True}), 
                 "clip": ("CLIP", )}
                 }
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"

    CATEGORY = "LLM Translate"

    def encode(self, intext, clip, text):
        text = intext + text
        tokens = clip.tokenize(text)
        cond, pooled = clip.encode_from_tokens(tokens, return_pooled=True)
        #return ([[cond, {"pooled_output": pooled}]], )
        return {"ui": {"text": text}, "result": ([[cond, {"pooled_output": pooled}]], )}

NODE_CLASS_MAPPINGS = {
    "LLM_CLIPTextEncode": LLM_CLIPTextEncode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LLM_CLIPTextEncode": "LLM CLIPTextEncode",
}
