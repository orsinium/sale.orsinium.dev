from __future__ import annotations
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader
from jinja_markdown2 import MarkdownExtension


env = Environment(loader=FileSystemLoader('templates'))
env.add_extension(MarkdownExtension)
public_dir = Path('public')
public_dir.mkdir(exist_ok=True)
template = env.get_template('index.html.j2')
data = yaml.safe_load(Path('data.yml').read_text())
items = [{**item, "slug": slug} for slug, item in data.items()]
items.sort(key=lambda item: (-(item['price'] or -1), item['name']))
content = template.render({'items': items, 'None': None})
Path('public', 'index.html').write_text(content)
