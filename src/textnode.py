from enum import Enum
from htmlnode import HTMLNode

class TextType(Enum):
    PLAIN = "text (plain)"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return other.text == self.text and other.text_type == self.text_type and other.url == self.url

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'

def text_node_to_html_node(text_node):
    text_node.text = text_node.text.replace("\n", "<br />")
    match(text_node.text_type):
        case TextType.PLAIN:
            return HTMLNode(None, text_node.text)
        case TextType.BOLD:
            return HTMLNode("b", text_node.text)
        case TextType.ITALIC:
            return HTMLNode("i", text_node.text)
        case TextType.CODE:
            return HTMLNode("code", text_node.text)
        case TextType.LINK:
            if text_node.url == None:
                raise Exception("Error: a link must have a url")
            return HTMLNode("a", text_node.text, None, {"href": text_node.url})
        case TextType.IMAGE:
            if text_node.url == None:
                raise Exception("Error: an image must have a url")
            return HTMLNode("img", None, None, {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Error: invalid text_type")
