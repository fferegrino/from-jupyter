import re
from xml.etree import ElementTree as etree

from markdown.blockprocessors import BlockProcessor, logger


class HashHeaderProcessor(BlockProcessor):
    """Process Hash Headers.
    https://github.com/Python-Markdown/markdown/blob/7334ecd4c747f9a36351a5073b55c2a606917ef9/markdown/blockprocessors.py#L444
    """

    # Detect a header at start of any line in block
    RE = re.compile(r"(?:^|\n)(?P<level>#{1,6})(?P<header>(?:\\.|[^\\])*?)#*(?:\n|$)")

    def test(self, parent, block):
        return bool(self.RE.search(block))

    def run(self, parent, blocks):
        block = blocks.pop(0)
        m = self.RE.search(block)
        if m:
            before = block[: m.start()]  # All lines before header
            after = block[m.end() :]  # All lines after header
            if before:
                # As the header was not the first line of the block and the
                # lines before the header must be parsed first,
                # recursively parse this lines as a block.
                self.parser.parseBlocks(parent, [before])
            # Create header using named groups from RE
            level = len(m.group("level"))
            if level < 3:
                h = etree.SubElement(parent, "h2")
            elif 3 <= level < 5:
                h = etree.SubElement(parent, "h4")
            else:
                h = etree.SubElement(parent, "strong")

            h.text = m.group("header").strip()
            if after:
                # Insert remaining lines as first block for future parsing.
                blocks.insert(0, after)
        else:  # pragma: no cover
            # This should never happen, but just in case...
            logger.warning("We've got a problem header: %r" % block)
