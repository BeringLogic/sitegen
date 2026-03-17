from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH="paragraph"
    HEADER="header"
    CODE="code"
    QUOTE="quote"
    UNORDERED_LIST="unordered_list"
    ORDERED_LIST="ordered_list"

def markdown_to_blocks(markdown):
    new_blocks = []

    blocks = markdown.split("\n\n")
    for block in blocks:
        if block == "" or block == "\n":
            continue

        new_blocks.append(block.strip())

    return new_blocks

def block_to_block_type(markdown):
    if re.findall(r"^#{1,6} ", markdown):
        return BlockType.HEADER
    if re.findall(r"^```\n", markdown):
        return BlockType.CODE
    if re.findall(r"^\>", markdown):
        return BlockType.QUOTE
    if re.findall(r"^\s*-", markdown):
        return BlockType.UNORDERED_LIST
    if re.findall(r"^\s*\d+\.", markdown):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


