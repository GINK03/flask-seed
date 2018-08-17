from flask import Flask
from jinja2 import Template
import json
from collections import namedtuple

def tag_control(query=None):
  Item = namedtuple('Item', ('tag_size', 'ref'))  
  tag_hashs = json.load(open('files/tag_hashs.json'))

  items = []
  for tag, hashs in sorted(tag_hashs.items(), key=lambda x:len(x[1])*-1):
    tag_size = f'{tag}, size={len(hashs)}'
    ref      = f'http://192.168.20.32:8080/tag_all_titles?tag={tag}'
    item = Item(tag_size, ref)
    items.append( item )
  fp = open('htmls/tag.html')
  base_html = fp.read()
  template = Template(base_html)
  return template.render(namel="hoge", items=items)
  
