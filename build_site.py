import pathlib, shutil, json
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
    
    b.add_page("markdown_page.html", "n64r_repy.html", "N64Recompiled/REPY",
        title="EZTR", desc="RecompExternalPython for N64Recompiled",
        jinja_args={
            "markdown_doc": "REPY.md"
        }
    )
    
    b.add_page("markdown_page.html", "z64r_eztr.html", "Zelda64Recompiled/EZTR",
        title="EZTR", desc="EZ Text Replacer for Zelda64Recompiled",
        jinja_args={
            "markdown_doc": "EZTR.md"
        }
    )
    
    b.add_page("recomp_mods_page.html", "recomp_mods.html", "Zelda64Recompiled/Mods",
        title="EZTR", desc="Mods for Zelda64Recompiled",
        jinja_args={
            "mods": json.loads(proot.joinpath("./src/data/z64r_mods.json").read_text())["mods"]
        }
    )
    
    b.build_all()
    
if __name__ == '__main__':
    main()