from textnode import TextType, TextNode

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

