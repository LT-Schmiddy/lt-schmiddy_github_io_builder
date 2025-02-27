import pathlib, shutil
from pathlib import Path

from .style import StyleBuilder
from .script import ScriptBuilder
from .page import PageBuilder

class MainBuilder:
    proot: Path
    
    styles: list[StyleBuilder]
    scripts: list[ScriptBuilder]
    # pages: list[PageBuilder]
    
    def __init__(self, proot: Path):
        self.proot = proot
        
        self.styles = []
        self.scripts = []
        # self.pages = []
    
    
    def add_style(self, in_file: Path, out_file: Path, sass_cmd: list[str] = None):
        self.styles.append(StyleBuilder(self.proot, in_file, out_file, sass_cmd))
    
    def add_script(self, in_file: Path, out_file: Path, browserify_cmd: list[str] = None):
        self.scripts.append(ScriptBuilder(self.proot, in_file, out_file, browserify_cmd))
        
    def build_all(self):
        self.build_styles()
        self.build_scripts()
    
    def build_styles(self):
        for i in self.styles:
            i.run_build()
            
    def build_scripts(self):
        for i in self.scripts:
            i.run_build()
        
    