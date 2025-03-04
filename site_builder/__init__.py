import pathlib, shutil, jinja2
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from .style import StyleBuilder
from .script import ScriptBuilder
from .page import PageBuilder

from .utils import recursive_update_dict
    
class MainBuilder:
    proot: Path
    site_root: Path
    site_rsrc_root: Path
    _site_rcsc_root_rel: Path
    
    styles: list[StyleBuilder]
    scripts: list[ScriptBuilder]
    pages: list[PageBuilder]
    
    env: Environment
    
    
    def __init__(self, proot: Path, template_root: Path, site_root: Path, site_rsrc_root: Path):
        self.proot = proot
        self.template_root = template_root
        self.site_root = site_root
        self.site_rsrc_root = site_rsrc_root
        
        self._site_rcsc_root_rel = site_rsrc_root.relative_to(site_root)

        self.styles = []
        self.scripts = []
        self.pages = []

        self.env = Environment(
            loader=FileSystemLoader(self.template_root),
            trim_blocks = True,
            lstrip_blocks = True,
            extensions=[
                "jinja2.ext.do",
                "jinja2.ext.loopcontrols",
            ]            
        )
        
        self.env.make_globals({
            "get_rsrc": self.get_rsrc
        })
    
    def get_default_jinja_args(self):
        return {
            "title": "Base page template",
            "scripts": self.scripts,
            "styles": self.styles,
            "pages": self.pages,
            "meta": {
                "description": "Base template for LT-Schmiddy.Github.io",
                "author": "LT_Schmiddy",
                "og:title": "A Basic HTML5 Template",
                "og:type": "website",
                "og:url": "https://www.sitepoint.com/a-basic-html5-template/",
                "og:description": "Base template for LT-Schmiddy.Github.io",
                "og:image": "image.png"
            },
            "get_nav": self.get_nav_table
        }
    
    def get_nav_table(self) -> dict[str, str]:
        retVal = {}
        for i in self.pages:
            retVal[i.nav_str] = str(i.out_file.relative_to(self.site_root)).replace("\\", "/")
            
        return retVal
    
    def get_rsrc(self, rsrc: str)->str:
        return str(self._site_rcsc_root_rel.joinpath(rsrc)).replace("\\", "/")
    
    def add_style(self, in_file: Path, out_name: str, sass_cmd: list[str] = None):
        out_path = self.site_rsrc_root.joinpath(out_name)
        self.styles.append(StyleBuilder(self.proot, self.site_root, self.site_rsrc_root, in_file, out_path, sass_cmd))
    
    def add_script(self, in_file: Path, out_name: str, browserify_cmd: list[str] = None):
        out_path = self.site_rsrc_root.joinpath(out_name)
        self.scripts.append(ScriptBuilder(self.proot, self.site_root, self.site_rsrc_root, in_file, out_path, browserify_cmd))
    
    def add_page(self, template_name: Path, out_name: str, nav_str: str, *, title: str = None, desc: str = None, jinja_args: dict = None):
        out_path = self.site_root.joinpath(out_name)
        pass_args = self.get_default_jinja_args()
        
        if jinja_args is not None:
            recursive_update_dict(pass_args, jinja_args)
            
        if title is not None:
            pass_args["title"] = title
        
        if desc is not None:
            pass_args["meta"]["description"] = desc
            pass_args["meta"]["og:description"] = desc
        
        self.pages.append(PageBuilder(self.proot, self.site_root, self.site_rsrc_root, template_name, out_path, nav_str, self.env, pass_args))
    
    def build_all(self):
        self.build_styles()
        self.build_scripts()
        self.build_pages()
    
    def build_styles(self):
        print("Building Stylesheets:")
        for i in self.styles:
            print(f"\t-> {i.out_file.name}")
            i.run_build()
            
    def build_scripts(self):
        print("Building Scripts:")
        for i in self.scripts:
            print(f"\t-> {i.out_file.name}")
            i.run_build()
            
    def build_pages(self):
        print("Building Pages:")
        for i in self.pages:
            print(f"\t-> {i.out_file.name}")
            i.run_build()
            
