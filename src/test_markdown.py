import unittest

from textnode import TextType, TextNode
from markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links


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

    def test_extract_markdown_images(self):
        markdown = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        actual = extract_markdown_images(markdown)
        self.assertListEqual(expected, actual)

    def test_extract_multiple_images_in_same_paragraph(self):
        markdown = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png). This is text with ![another image](https://i.imgur.com/stuff.png)"
        expected = [
            ("image", "https://i.imgur.com/zjjcJKZ.png"),
            ("another image", "https://i.imgur.com/stuff.png"),
        ]
        actual = extract_markdown_images(markdown)
        self.assertListEqual(expected, actual)

    def test_extract_markdown_links(self):
        markdown = "This is text with a [link](https://google.com)"
        expected = [("link", "https://google.com")]
        actual = extract_markdown_links(markdown)
        self.assertListEqual(expected, actual)

    def test_extract_multiple_links_in_same_paragraph(self):
        markdown = "This is text with a [link](https://google.com). This is text with [another link](https://boot.dev)"
        expected = [
            ("link", "https://google.com"),
            ("another link", "https://boot.dev"),
        ]
        actual = extract_markdown_links(markdown)
        self.assertListEqual(expected, actual)

    def test_extract_image_from_markdown_with_both_link_and_image(self):
        markdown = "This is text with a [link](https://google.com). This is text with an ![image](https://boot.dev/logo.png)"
        expected = [
            ("image", "https://boot.dev/logo.png"),
        ]
        actual = extract_markdown_images(markdown)
        self.assertListEqual(expected, actual)


    def test_extract_link_from_markdown_with_both_link_and_image(self):
        markdown = "This is text with a [link](https://google.com). This is text with an ![image](https://boot.dev/logo.png)"
        expected = [
            ("link", "https://google.com"),
        ]
        actual = extract_markdown_links(markdown)
        self.assertListEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
