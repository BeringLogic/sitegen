import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_none(self):
        node = HTMLNode("p", "This is a paragraph")
        expected = ""
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

    def test_props_empty(self):
        node = HTMLNode("p", "This is a paragraph", None, {})
        expected = ""
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

    def test_props(self):
        node = HTMLNode("a", "This is a link", None, {"href": "https://google.com", "target": "_blank"})
        expected = ' href="https://google.com" target="_blank"'
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
