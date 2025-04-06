from enum import Enum

class TextType(Enum):
    NORMAL = ""
    BOLD = "**"
    ITALIC = "_"
    CODE = "`"
    LINKS = ""
    Images = "  "

class TextNode():
    def __init__(self, text, text_type, url):
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
    