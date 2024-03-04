from .node_solar_koen import *
from .showtext_node import *

NODE_CLASS_MAPPINGS = {
    "LLMTrans": LLMTrans,
    "ShowText": ShowText,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LLMTrans": "LLM Translate(ko<->En) node",
    "ShowText": "Show Text",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
