class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if isinstance(self.props, dict):
            properties = self.props
        else:
            properties = eval(self.props.strip())

        return " " + " ".join([f'{key}="{value}"' for key, value in properties.items()])

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"