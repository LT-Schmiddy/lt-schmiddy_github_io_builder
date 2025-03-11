from pathlib import Path

import markdown

class MarkdownHandler(markdown.Markdown):
    markdown_root: Path
    
    def __init__(self, p_markdown_root: Path, **kwargs):
        super().__init__(**kwargs)
        
        self.markdown_root = p_markdown_root
        
    def load_src(self, file_path: str):
        md_file: Path = self.markdown_root.joinpath(file_path)
        return self.convert(md_file.read_text())