# LLM Solar Translate ko<->en 
# made by : won.wizard
# 
# reauirement : pip install openai==1.2.0
# api_key : input user's api key
#

from openai import OpenAI # openai==1.2.0

class LLMTrans:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_field": ("STRING", {
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "아름다운 풍경 자연 유리 병 풍경, 보라색 은하 병,"
                }),
                "trans_type": (["Solar Ko2En","Solar En2Ko"],)
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Transed_String",)

    FUNCTION = "run"

    CATEGORY = "LLM Translate"

    def run(self, input_field, trans_type):

        client = OpenAI(
        api_key="HMG6GMDhUHXuiXjhSB4UpHS8SPI8w153",    #Beta access token
        base_url="https://api.upstage.ai/v1/solar"
        )

        #lnw add, 입력 받기
        #print ("Input strings:")
        input_str = input_field

        if trans_type == "Solar Ko2En":
            model_type="solar-1-mini-translate-koen"
        elif trans_type == "Solar En2Ko" :
            model_type="solar-1-mini-translate-enko"

        stream = client.chat.completions.create(
        model=model_type,
        messages=[
            {
            "role": "user",
            "content": "아버지가방에들어가셨다"
            },
            {
            "role": "assistant",
            "content": "Father went into his room"
            },
            {
            "role": "user",
            "content": input_str     #lnw change "엄마도들어가셨다" -> input_str
            }
        ],
        stream=True,
        )

        out_str = ""
        for chunk in stream:
          if chunk.choices[0].delta.content is not None:
            #print(chunk.choices[0].delta.content, end="")
            tmp_str = chunk.choices[0].delta.content
            out_str += tmp_str

        print(out_str)  

        # Use with stream=False
        # print(stream.choices[0].message.content)
        
        # Return 
        return (out_str,)
    
NODE_CLASS_MAPPINGS = {
    "LLMTrans": LLMTrans
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LLMTrans": "LLM Translate(ko<->En) node"
}

