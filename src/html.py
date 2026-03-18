from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type
from markdown_inline import text_to_textnodes
from textnode import text_node_to_html_node
from htmlnode import HTMLNode
import re

def markdown_to_html_node(markdown):
    children = []

    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        children.append(block_to_html_node(block, block_type))

    root = HTMLNode("div", None, children)
    return root

def block_to_html_node(markdown, block_type):

    match(block_type):

        case BlockType.HEADER:
            matches = re.findall(r"^(#{1,6}) (.+)", markdown)
            level = len(matches[0][0])

            header_nodes = []
            text_nodes = text_to_textnodes(matches[0][1])
            for text_node in text_nodes:
                header_nodes.append(text_node_to_html_node(text_node))

            return HTMLNode("h"+str(level), None, header_nodes)

        case BlockType.CODE:
            code = markdown.replace("```\n", "").replace("```", "")
            node = HTMLNode("code", code)
            return HTMLNode("pre", None, [node])

        case BlockType.QUOTE:
            quote = re.sub(r"^\>\s*", "", markdown, flags=re.MULTILINE)
            nodes = []
            text_nodes = text_to_textnodes(quote)
            for text_node in text_nodes:
                nodes.append(text_node_to_html_node(text_node))
            return HTMLNode("blockquote", None, nodes)

        case BlockType.UNORDERED_LIST:
            list_nodes = []
            matches = re.findall(r"^\s*-\s*(.+)", markdown, flags=re.MULTILINE)
            for line in matches:
                line_nodes = []
                text_nodes = text_to_textnodes(line)
                for text_node in text_nodes:
                    line_nodes.append(text_node_to_html_node(text_node))
                list_nodes.append(HTMLNode("li", None, line_nodes))
            return HTMLNode("ul", None, list_nodes)

        case BlockType.ORDERED_LIST:
            list_nodes = []
            matches = re.findall(r"^\d+\.\s*(.+)", markdown, flags=re.MULTILINE)
            for line in matches:
                line_nodes = []
                text_nodes = text_to_textnodes(line)
                for text_node in text_nodes:
                    line_nodes.append(text_node_to_html_node(text_node))
                list_nodes.append(HTMLNode("li", None, line_nodes))
            return HTMLNode("ol", None, list_nodes)

        case BlockType.PARAGRAPH:
            nodes = []
            text_nodes = text_to_textnodes(markdown)
            for text_node in text_nodes:
                nodes.append(text_node_to_html_node(text_node))
            return HTMLNode("p", None, nodes)

def extract_title(markdown):
    matches = re.findall(r"^# (.+)", markdown)
    if len(matches) != 1:
        raise Exception("page has no header")
    return matches[0]

def generate_page(markdown_file, template_file, html_file):
    with open(markdown_file, "r") as f:
        markdown = f.read()
    with open(template_file, "r") as f:
        template = f.read()

    title = extract_title(markdown)
    html_node = markdown_to_html_node(markdown)

    html = template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", html_node.to_html())

    with open(html_file, "w") as f:
        f.write(html)

