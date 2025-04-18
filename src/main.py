from textnode import TextNode
from htmlnode import HTMLNode

def main():
    new_text = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(new_text)

    new_html = HTMLNode(None, None, None, '{ "href": "https://www.google.com", "target": "_blank", }')
    print(new_html.props_to_html())

main()