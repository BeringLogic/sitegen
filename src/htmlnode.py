

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        html = ""
        if self.tag:
            html += f"<{self.tag}"
            if self.props:
                html += self.props_to_html()
            html += ">"
        if self.value:
            html += self.value
        else:
            if self.children is not None:
                for child in self.children:
                    html += child.to_html()
        if self.tag:
            html += f"</{self.tag}>"
        return html

    def props_to_html(self):
        if self.props == None:
            return ""

        s = ""
        for prop in self.props:
            s += f' {prop}="{self.props[prop]}"'
        return s

    def __repr__(self):
        return f'HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})'

