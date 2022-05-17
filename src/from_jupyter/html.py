import pkgutil
from pathlib import Path

import markdown
from nbformat import NotebookNode

from from_jupyter.hash_header_processor import HashHeaderProcessor


def to_html(notebook: NotebookNode, parent_dir: Path, file: Path):
    image_output_folder = Path(parent_dir, file.stem)
    image_output_folder.mkdir(exist_ok=True)

    md = markdown.Markdown(extensions=["fenced_code"])
    # TODO: The HashHeaderProcessor is specifically made for Medium posts probably needs a better name.
    # TODO: Put the HashHeaderProcessor behind a flag
    md.parser.blockprocessors.register(HashHeaderProcessor(md.parser), "hprocessor", 175)

    template = pkgutil.get_data(__name__, "to_html.html").decode("utf-8")
    content = []
    for idx, cell in enumerate(notebook["cells"], 1):
        if cell["cell_type"] == "markdown":
            html = md.convert(cell["source"])
            content.append(html)
        # TODO: We need to add code blocks
    html = template.replace("{{CONTENT}}", "\n".join(content))
    with open(image_output_folder / "index.html", "w") as w:
        w.write(html)
