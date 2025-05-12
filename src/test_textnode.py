import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noeq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("THis is a text italics", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_nourl(self):
        node = TextNode("This is a test node", TextType.BOLD, None)
        node2 = TextNode("This is a test", TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(node, node2)

    def test_bothurldefined(self):
        node = TextNode("This is a test", TextType.BOLD, "https://www.google.com")
        node2 = TextNode("This is a test", TextType.BOLD, "https://www.google.com")
        self.assertEqual(node, node2)

    def test_bothurlundefined(self):
        node = TextNode("This is a test", TextType.BOLD, None)
        node2 = TextNode("This is a test", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text", TextType.BOLD)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node, "**This is a bold text**")

    def test_italic(self):
        node = TextNode("This is an italic text", TextType.ITALIC)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node, "_This is an italic text_")

    def test_code(self):
        node = TextNode("This is a code text", TextType.CODE)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node, "`This is a code text`")

    def test_links(self):
        node = TextNode("This is a link", TextType.LINKS, "https://example.com")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a link")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://example.com/image.jpg")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node, "  This is an image  ")

    def test_empty_text(self):
        node = TextNode("", TextType.TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "")

    def test_empty_bold(self):
        node = TextNode("", TextType.BOLD)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node, "****")

if __name__ == "__main__":
    unittest.main()
