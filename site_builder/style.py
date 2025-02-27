import pathlib, shutil, subprocess
from pathlib import Path

class StyleBuilder:
    proot: Path
    in_file: Path
    out_file: Path
    
    sass_cmd: list[str]
    
    def __init__(self, proot: Path, in_file: Path, out_file: Path, sass_cmd: list[str] = None):
        self.proot = proot
        self.in_file = in_file
        self.out_file = out_file
        
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
    
        
    