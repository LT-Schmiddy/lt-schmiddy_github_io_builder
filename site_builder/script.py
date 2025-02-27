import pathlib, shutil, subprocess
from pathlib import Path

class ScriptBuilder:
    proot: Path
    in_file: Path
    out_file: Path
    
    browserify_cmd: list[str]
    
    def __init__(self, proot: Path, in_file: Path, out_file: Path, browserify_cmd: list[str] = None):
        self.proot = proot
        self.in_file = in_file
        self.out_file = out_file
        
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
    
        
    