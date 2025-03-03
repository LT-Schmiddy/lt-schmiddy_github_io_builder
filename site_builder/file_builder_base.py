import pathlib, shutil, subprocess
from pathlib import Path

class FileBuilderBase:
    proot: Path
    site_root: Path
    site_rsrc_root: Path
    
    in_file: Path
    out_file: Path
    
    sass_cmd: list[str]
    
    def __init__(self, proot: Path, site_root: Path, site_rsrc_root: Path, in_file: Path, out_file: Path):
        self.proot = proot
        self.site_root = site_root
        self.site_rsrc_root = site_rsrc_root
        self.in_file = in_file
        self.out_file = out_file
    
    def get_rsrc_path(self):
        return str(self.out_file.relative_to(self.site_root)).replace("\\", "/")
    
    def run_build(self) -> subprocess.CompletedProcess:
        raise NotImplementedError(f"Method 'run_build' not implemented for {type(self)}")
        
    
    
        
    