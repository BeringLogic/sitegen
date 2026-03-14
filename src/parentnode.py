from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Error: ParentNode must have a tag")
        if self.children == None:
            raise ValueError("Error: ParentNode must have children")

        s = f'<{self.tag}>'
        for node in self.children:
            s += node.to_html()
        s += f'</{self.tag}>'
        return s

