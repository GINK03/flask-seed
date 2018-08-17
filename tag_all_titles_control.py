from flask import Flask
from jinja2 import Template
import json
from collections import namedtuple
def tag_all_titles(tag=None):
  print(tag) 
  tag_hashs = json.load(open('files/tag_hashs.json'))
  h2_hash   = json.load(open('files/h2_hash.json'))
  hash_imgs = json.load(open('files/hash_imgs.json'))
  hash_h2   = { hash:h2 for h2, hash in h2_hash.items() }

  Item = namedtuple('Item', ('h2', 'hash', 'ref', 'img')) 
  hashs = tag_hashs[tag]

  items = []
  for hash in hashs:
    img = sorted(hash_imgs[hash])[0]
    h2 = hash_h2[hash]
    ref = f'http://192.168.20.32:8080/view?hash={hash}'
    item = Item(h2, hash, ref, img)
    items.append( item )
    
  fp = open('htmls/tag_all_titles.html')
  base_html = fp.read()
  template = Template(base_html)
  return template.render(name="hoge", items=items)
  
