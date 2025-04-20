from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag cannot be None")
        elif self.children is None:
            raise ValueError("Children cannot be None")
        elif len(self.children) == 0:
            html_children = ""
        else:
            html_children = "".join([child.to_html() for child in self.children])
        return f'<{self.tag}>{html_children}</{self.tag}>'