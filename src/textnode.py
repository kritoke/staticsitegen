from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = ""
    BOLD = "**"
    ITALIC = "_"
    CODE = "`"
    LINKS = ""
    IMAGE = "  "

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, otherText):
        if (self.text == otherText.text) & (self.text_type == otherText.text_type) & (self.url == otherText.url):
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def text_node_to_html_node(self):
        if self.text_type == TextType.TEXT or self.text_type == TextType.LINKS:
            return LeafNode(None, self.text)
        else:
            return f"{self.text_type.value}{self.text}{self.text_type.value}"
