import pathlib, shutil, subprocess
from pathlib import Path

from .file_builder_base import FileBuilderBase

class ScriptBuilder(FileBuilderBase):
    proot: Path
    in_file: Path
    out_file: Path
    
    browserify_cmd: list[str]
    
    def __init__(self, proot: Path, site_root: Path, site_rsrc_root: Path, in_file: Path, out_file: Path, browserify_cmd: list[str] = None):
        super().__init__(proot, site_root, site_rsrc_root, in_file, out_file)
        
        if browserify_cmd is None:
            self.browserify_cmd = [shutil.which("npx"), "browserify"]
        else:
            self.browserify_cmd = browserify_cmd
    
    def run_build(self) -> subprocess.CompletedProcess:
        return subprocess.run(
            self.browserify_cmd
            + [
                str(self.in_file.absolute()),
                "-p",
                "[tsify]",
                "-o",
                str(self.out_file.absolute())
            ],
            cwd=self.proot
        )
    
        
    