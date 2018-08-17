from flask import Flask
from jinja2 import Template
import json
from collections import namedtuple
def hash_control(hash=None):
  print(hash) 
  tag_hashs = json.load(open('files/tag_hashs.json'))
  h2_hash = json.load(open('files/h2_hash.json'))
  hash_h2 = { hash:h2 for h2, hash in h2_hash.items() }
  hash_imgs = json.load(open('files/hash_imgs.json'))

  Item = namedtuple('Item', ('h2', 'hash', 'imgs')) 
  
  h2   = hash_h2[hash]
  imgs = sorted( hash_imgs[hash] )
  item = Item(h2, hash, imgs)

    
  fp = open('htmls/view.html')
  base_html = fp.read()
  template = Template(base_html)
  return template.render(name="hoge", item=item)
  
