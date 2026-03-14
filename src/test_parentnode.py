import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):

    def test_to_html_with_child(self):
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

    def test_to_html_multiple_children(self):
        children = [
            LeafNode(None, "plain text"),
            LeafNode("b", "bold text"),
            LeafNode("i", "italics text"),
        ]
        parent_node = ParentNode("p", children)
        expected = "<p>plain text<b>bold text</b><i>italics text</i></p>"
        actual = parent_node.to_html()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
