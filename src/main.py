from textnode import TextType, TextNode

def main():
    print("Site Generator")
    print()

    node = TextNode("This is a link", TextType.LINK, "https://www.boot.dev/")
    print(node)

main()
