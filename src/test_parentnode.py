import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_empty_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("span", "first")
        child2 = LeafNode("p", "second")
        child3 = LeafNode("a", "third")
        parent_node = ParentNode("div", [child1, child2, child3])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>first</span><p>second</p><a>third</a></div>"
        )

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container", "id": "main"})
        # Note: This test might fail if ParentNode doesn't handle props correctly
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container" id="main"><span>child</span></div>'
        )

    def test_none_tag_raises_error(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_none_children_raises_error(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
