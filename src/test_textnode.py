import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.LINK, "https://example.com/")
        self.assertEqual(node.url, "https://example.com/")

    def test_text_is_different(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        node2 = TextNode("This is also a text node", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_type_is_different(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
