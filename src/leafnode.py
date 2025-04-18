from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag=tag, value=value, children = None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value cannot be None")
        elif self.tag is None:
            return f'{self.value}'

        if self.props is None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            props_string = self.props_to_html()
            return f'<{self.tag}{props_string}>{self.value}</{self.tag}>'
