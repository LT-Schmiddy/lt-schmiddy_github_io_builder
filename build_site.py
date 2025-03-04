import pathlib, shutil
from pathlib import Path

from site_builder import MainBuilder

def main():
    proot = Path(__file__).parent
    template_root = proot.joinpath("./src/jinja2")
    markdown_root = proot.joinpath("./src/markdown")
    site_root = proot.joinpath("./LT-Schmiddy.github.io")
    rsrc_root = site_root.joinpath("rsrc")
    b = MainBuilder(proot, template_root, markdown_root, site_root, rsrc_root)
    
    
    b.add_style(proot.joinpath("./src/sass/main.scss"), "main.css");
    b.add_script(proot.joinpath("./src/ts/main.ts"), "bundle.js");
    
    b.add_page("index.html", "index.html", "Home", title="Home", desc="LT_Schmiddy's Stash")
    
    b.add_page("markdown_page.html", "z64r_eztr.html", "Zelda64Recompiled/EZTR",
        title="EZTR", desc="EZ Text Replacer for Zelda64Recompiled",
        jinja_args={
            "markdown_doc": "EZTR.md"
        }
    )
    
    b.build_all()
    
if __name__ == '__main__':
    main()