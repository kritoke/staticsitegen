from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():
    new_text = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(new_text)

    new_html = HTMLNode(None, None, None, '{ "href": "https://www.google.com", "target": "_blank", }')
    print(new_html.props_to_html())

    new_plain_leaf = LeafNode("p", "This is a paragraph of text.").to_html()
    print(new_plain_leaf)

    new_leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
    print(new_leaf)

    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())

main()