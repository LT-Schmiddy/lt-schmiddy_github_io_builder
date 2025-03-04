from pathlib import Path

import markdown

class MarkdownHandler:
    markdown_root: Path
    converter: markdown.Markdown
    
    def __init__(self, p_markdown_root: Path, **kwargs):
        self.markdown_root = p_markdown_root
        
        if 'extensions' not in kwargs:
            kwargs['extensions'] = [
                "extra"
            ]
        
        self.converter = markdown.Markdown(**kwargs)
        
    def load(self, file_path: str):
        md_file: Path = self.markdown_root.joinpath(file_path)
        return self.converter.convert(md_file.read_text())