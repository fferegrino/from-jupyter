from pathlib import Path

from from_jupyter.gist_client import GistClient
from from_jupyter.utils import hash_string


class CodeProcessor:
    def process_cell(self, cell, metadata, file):
        pass


class FileProcessor:
    def __init__(self, output_directory: Path, endl='\n'):
        self.output_directory = output_directory
        self.endl = endl

    def process_cell(self, cell, metadata, file):

        gist = metadata.get("gist")
        code_output = self.output_directory / file.stem / gist
        code_output.parent.mkdir(parents=True, exist_ok=True)

        with open(code_output, "w") as w:
            w.write(cell["source"].rstrip() + self.endl)


class GistProcessor(CodeProcessor):
    def __init__(self, personal_token: str):
        self.gist_client = GistClient(personal_token)

    def process_cell(self, cell, metadata, file):
        gist_id = metadata.get("gist_id")
        gist = metadata.get("gist")
        name, _, extension = gist.partition(".")
        file_hash = hash_string(file.name)
        new_file_name = f"{name}-{file_hash}.{extension}"
        description = f"File {gist} for the file {file.name}"
        if gist_id:
            gist_id = self.gist_client.update_gist(gist_id, description, new_file_name, cell["source"])
        elif gist:
            gist_id = self.gist_client.gist_client.publish_gist(description, new_file_name, cell["source"])
        metadata["gist_id"] = gist_id
