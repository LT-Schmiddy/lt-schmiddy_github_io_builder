import pathlib, shutil, subprocess
from pathlib import Path

from jinja2 import Environment

from .file_builder_base import FileBuilderBase
# from .page_def import PageDef

class PageBuilder(FileBuilderBase):
    template_name: str
    nav_str: str
    
    jinja_env: Environment
    jinja_args: dict
    
    def __init__(self, proot: Path, site_root: Path, site_rsrc_root: Path, template_name: Path, out_file: Path, 
                nav_str: str, jinja_env: Environment, jinja_args: dict = None):
        super().__init__(proot, site_root, site_rsrc_root, None, out_file)
        
        self.template_name = template_name
        self.nav_str = nav_str
        self.jinja_env = jinja_env
        
        if jinja_args is None:
            self.jinja_args = {}
        else:
            self.jinja_args = jinja_args

    def update_args(self, new_args: dict):
        self.jinja_args.update(new_args)
    
    def run_build(self) -> None:
        template = self.jinja_env.get_template(self.template_name)
        
        page_out: str = template.render(**self.jinja_args);
        
        out_file = self.site_root.joinpath(self.out_file)
        out_file.write_text(page_out)
    
        
    