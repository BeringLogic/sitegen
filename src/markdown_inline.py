from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # we don't do nested nodes, like italic and bold text
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception(f'Error: invalid markdown: {node.text}')

        # no delimiter
        if len(parts) == 1 and parts[0] == node.text:
            new_nodes.append(node)
            continue

        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(parts[i], TextType.PLAIN))
            else:
                new_nodes.append(TextNode(parts[i], text_type))

    return new_nodes

def extract_markdown_images(markdown):
    matches = re.findall(r"!\[(.+?)\]\((.+?)\)", markdown)
    return matches

def extract_markdown_links(markdown):
    matches = re.findall(r"(?<!!)\[(.+?)\]\((.+?)\)", markdown)
    return matches

def split_nodes(old_nodes, regex, extract_markdown_func, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue

        match_text = ""
        matches = re.findall(regex, node.text)
        for match in matches:
            if match[0] != "":
                new_nodes.append(TextNode(match[0], TextType.PLAIN))

            items = extract_markdown_func(match[1])
            (alt, url) = items[0]
            new_nodes.append(TextNode(alt, text_type, url))

            match_text += match[0] + match[1]

        trailing_text = node.text.replace(match_text, "")
        if len(trailing_text) > 0:
            new_nodes.append(TextNode(trailing_text, TextType.PLAIN))

    return new_nodes

def split_nodes_image(old_nodes):
    return split_nodes(old_nodes, r"(.*?)(!\[.+?\]\(.+?\))", extract_markdown_images, TextType.IMAGE)

def split_nodes_link(old_nodes):
    return split_nodes(old_nodes, r"(.*?)(?<!!)(\[.+?\]\(.+?\))", extract_markdown_links, TextType.LINK)

def text_to_textnodes(markdown):
    nodes = [
        TextNode(markdown, TextType.PLAIN)
    ]
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    return nodes

