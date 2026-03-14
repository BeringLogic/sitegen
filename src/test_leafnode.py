import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_p(self):
        node = LeafNode("p", "This is a paragraph")
        expected = "<p>This is a paragraph</p>"
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_a(self):
        node = LeafNode("a", "This is a link", {"href":"https://google.com"})
        expected = '<a href="https://google.com">This is a link</a>'
        actual = node.to_html()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
