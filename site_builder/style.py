import pathlib, shutil, subprocess
from pathlib import Path

from .file_builder_base import FileBuilderBase

class StyleBuilder(FileBuilderBase):
    sass_cmd: list[str]
    
    def __init__(self, proot: Path, site_root: Path, site_rsrc_root: Path, in_file: Path, out_file: Path, sass_cmd: list[str] = None):
        super().__init__(proot, site_root, site_rsrc_root, in_file, out_file)
        
        if sass_cmd is None:
            self.sass_cmd = [shutil.which("npx"), "sass"]
        else:
            self.sass_cmd = sass_cmd
    
    def run_build(self) -> subprocess.CompletedProcess:
        return subprocess.run(
            self.sass_cmd
            + [
                str(self.in_file.absolute()),
                str(self.out_file.absolute())
            ],
            cwd=self.proot
        )
        
    
    
        
    