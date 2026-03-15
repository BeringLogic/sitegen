import unittest

from textnode import TextType, TextNode
from markdown import split_nodes_delimiter


class TestMarkdown(unittest.TestCase):

    def test_italic_part_in_middle(self):
        node = TextNode("some plain text _with italic in the middle_ some more plain text", TextType.PLAIN)
        expected = [
            TextNode("some plain text ", TextType.PLAIN), 
            TextNode("with italic in the middle", TextType.ITALIC), 
            TextNode(" some more plain text", TextType.PLAIN), 
        ]
        actual = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(expected, actual)

    def test_only_italic(self):
        node = TextNode("_italic text_", TextType.PLAIN)
        expected = [
            TextNode("italic text", TextType.ITALIC), 
        ]
        actual = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(expected, actual)

    def test_just_plain(self):
        node = TextNode("this is just plain text", TextType.PLAIN)
        expected = [
            TextNode("this is just plain text", TextType.PLAIN)
        ]
        actual = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(expected, actual)

    def test_bold(self):
        node = TextNode("**bold**", TextType.PLAIN)
        expected = [
            TextNode("bold", TextType.BOLD),
        ]
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(expected, actual)

    def test_code(self):
        node = TextNode("```print('hello, world')```", TextType.PLAIN)
        expected = [
            TextNode("print('hello, world')", TextType.CODE),
        ]
        actual = split_nodes_delimiter([node], "```", TextType.CODE)
        self.assertEqual(expected, actual)

    def test_2_different_delimiters(self):
        node = TextNode("some **bold** and some _italic_ text", TextType.PLAIN)
        expected = [
            TextNode("some ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" and some ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.PLAIN),
        ]
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        actual = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertEqual(expected, actual)

    def test_invalid_markdown(self):
        node = TextNode("_hello, world", TextType.PLAIN)
        with self.assertRaises(Exception):
            actual = split_nodes_delimiter([node], "_", TextType.ITALIC),

if __name__ == "__main__":
    unittest.main()
