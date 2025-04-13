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

if __name__ == "__main__":
    unittest.main()