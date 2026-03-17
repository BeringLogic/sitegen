import unittest

from html import markdown_to_html_node, extract_title

class TestHTML(unittest.TestCase):

    def test_header1_block(self):
        markdown = "# This is a header 1"
        expected = "<div><h1>This is a header 1</h1></div>"
        node = markdown_to_html_node(markdown)
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_header6_block(self):
        markdown = "###### This is a header 6"
        expected = "<div><h6>This is a header 6</h6></div>"
        node = markdown_to_html_node(markdown)
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_header_block_with_inline_markdown(self):
        markdown = "# This is a **header 1** with bold text"
        expected = "<div><h1>This is a <b>header 1</b> with bold text</h1></div>"
        node = markdown_to_html_node(markdown)
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_code_block(self):
        markdown = """```
print("This is a code block")
```
"""
        expected = """<div><pre><code>
print("This is a code block")
</code></pre></div>"""
        node = markdown_to_html_node(markdown)
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_code_block_with_inline_markdown(self):
        markdown = """```
print("This is a **code** block")
```
"""
        expected = """<div><pre><code>
print("This is a **code** block")
</code></pre></div>"""
        node = markdown_to_html_node(markdown)
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_quote_block(self):
        markdown = "> This is a quote block"
        expected = "<div><blockquote>This is a quote block</blockquote></div>"
        node = markdown_to_html_node(markdown)
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_quote_block_with_multiple_lines(self):
        markdown = """> This is a quote block
>With multiple
>  lines
"""
        expected = """<div><blockquote>This is a quote block
With multiple
lines</blockquote></div>"""
        node = markdown_to_html_node(markdown)
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_quote_block_with_inline_markdown(self):
        markdown = "> This is a **quote** block"
        expected = "<div><blockquote>This is a <b>quote</b> block</blockquote></div>"
        node = markdown_to_html_node(markdown)
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_unordered_list(self):
        markdown = """- This is an **unordered list**
- with inline markdown _in it_
"""
        expected = "<div><ul><li>This is an <b>unordered list</b></li><li>with inline markdown <i>in it</i></li></ul></div>"
        node = markdown_to_html_node(markdown)
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_ordered_list(self):
        markdown = """1. This is an **ordered list**
2. with inline markdown _in it_
"""
        expected = "<div><ol><li>This is an <b>ordered list</b></li><li>with inline markdown <i>in it</i></li></ol></div>"
        node = markdown_to_html_node(markdown)
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_paragraph(self):
        markdown = "This is a **simple** paragraph with _inline markdown_"
        expected = "<div><p>This is a <b>simple</b> paragraph with <i>inline markdown</i></p></div>"
        node = markdown_to_html_node(markdown)
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_extract_title(self):
        markdown = "# This is a header 1"
        expected = "This is a header 1"
        actual = extract_title(markdown)
        self.assertEqual(expected, actual)

    def test_extract_title_no_title(self):
        markdown = "This is not a header"
        with self.assertRaises(Exception):
            extract_title(markdown)

