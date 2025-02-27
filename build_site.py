import pathlib, shutil
from pathlib import Path

from site_builder import MainBuilder

def main():
    proot = Path(__file__).parent
    site_root = proot.joinpath("./LT-Schmiddy.github.io")
    b = MainBuilder(proot)
    
    b.add_style(proot.joinpath("./src/sass/main.scss"), site_root.joinpath("main.css"));
    b.add_script(proot.joinpath("./src/ts/main.ts"), site_root.joinpath("bundle.js"));
    
    b.build_all()
    
if __name__ == '__main__':
    main()