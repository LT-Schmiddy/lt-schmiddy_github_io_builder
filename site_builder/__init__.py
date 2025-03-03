import pathlib, shutil, jinja2
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


from .style import StyleBuilder
from .script import ScriptBuilder

class PageDef:
    title: str
    template: str
    out_file: Path
    
    def __init__(self, title: str, template: str, out_file: Path):
        self.title = title;
        self.template = template
        self.out_file = out_file
        
    
class MainBuilder:
    proot: Path
    site_root: Path
    site_rsrc_root: Path
    _site_rcsc_root_rel: Path
    
    styles: list[StyleBuilder]
    scripts: list[ScriptBuilder]
    
    env: Environment
    
    
    def __init__(self, proot: Path, template_root: Path, site_root: Path, site_rsrc_root: Path):
        self.proot = proot
        self.template_root = template_root
        self.site_root = site_root
        self.site_rsrc_root = site_rsrc_root
        
        self._site_rcsc_root_rel = site_rsrc_root.relative_to(site_root)

        self.styles = []
        self.scripts = []

        self.env = Environment(
            loader=FileSystemLoader(self.template_root),
            extensions=[
                "jinja2.ext.do",
                "jinja2.ext.loopcontrols",
            ]            
        )
        
        self.env.make_globals({
            "get_rsrc": self.get_rsrc
        })
    
    def get_rsrc(self, rsrc: str)->str:
        return str(self._site_rcsc_root_rel.joinpath(rsrc)).replace("\\", "/")
    
    def add_style(self, in_file: Path, out_file: str, sass_cmd: list[str] = None):
        out_path = self.site_rsrc_root.joinpath(out_file)
        self.styles.append(StyleBuilder(self.proot, self.site_root, self.site_rsrc_root, in_file, out_path, sass_cmd))
    
    def add_script(self, in_file: Path, out_file: str, browserify_cmd: list[str] = None):
        out_path = self.site_rsrc_root.joinpath(out_file)
        self.scripts.append(ScriptBuilder(self.proot, self.site_root, self.site_rsrc_root, in_file, out_path, browserify_cmd))
        
    def build_all(self):
        self.build_styles()
        self.build_scripts()
    
    def build_styles(self):
        for i in self.styles:
            i.run_build()
            
    def build_scripts(self):
        for i in self.scripts:
            i.run_build()
            
    def build_page(self, page: PageDef, **kwargs):
        template = self.env.get_template(page.template)
        
        # page_out: str = template.render(**kwargs);
        page_out: str = template.render(styles=self.styles, scripts=self.scripts);
        
        out_file = self.site_root.joinpath(page.out_file)
        out_file.write_text(page_out)
        
    