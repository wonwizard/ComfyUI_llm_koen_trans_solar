from .node_solar_koen import *
from .node_showtext import *
from .node_LLM_CLIPTextEncode import *

NODE_CLASS_MAPPINGS = {
    "LLMTrans": LLMTrans,
    "ShowText": ShowText,
    "LLM_CLIPTextEncode": LLM_CLIPTextEncode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LLMTrans": "LLM Translate(ko<->En) node",
    "ShowText": "Show Text",
    "LLM_CLIPTextEncode": "LLM CLIPTextEncode",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
