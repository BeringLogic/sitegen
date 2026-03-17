import unittest

from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type


class TestMarkdownBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        markdown = """

This is **bolded** paragraph prefixed by an empty line 

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items

This is the last paragraph, and it has an extra line at the end

"""
        expected = [
            "This is **bolded** paragraph prefixed by an empty line",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
            "This is the last paragraph, and it has an extra line at the end"
        ]
        actual = markdown_to_blocks(markdown)
        self.assertEqual(expected, actual)

    def test_markdown_to_blocks_multiple_extra_lines(self):
        markdown = """
This is a paragraph




"""
        expected = [
            "This is a paragraph"
        ]
        actual = markdown_to_blocks(markdown)
        self.assertEqual(expected, actual)

    def test_block_type_heading(self):
        markdown = "###### This is a header"
        expected = BlockType.HEADER
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_block_type_code(self):
        markdown = """```
print("This is a block of code")
```
"""
        expected = BlockType.CODE
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_block_type_quote(self):
        markdown = "> This is a quote"
        expected = BlockType.QUOTE
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_block_type_unordered_list(self):
        markdown = """- these
- are
- bullets,
    - aka
    - unordered list
"""
        expected = BlockType.UNORDERED_LIST
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_block_type_ordered_list(self):
        markdown = """1. these
2. are
8. a
3. ordered list
"""
        expected = BlockType.ORDERED_LIST
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
