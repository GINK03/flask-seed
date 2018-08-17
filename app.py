from flask import Flask
from jinja2 import Template
from flask import request

import tag_control
import tag_all_titles_control
import hash_control
app = Flask(__name__, static_folder='static_folder')


@app.route('/')
def hello():
  fp = open('htmls/00-index.html')
  base_html = fp.read()
  template = Template(base_html)
  return template.render(name='John Doe')

@app.route('/tag')
def tag():
  return tag_control.tag_control()

@app.route('/tag_all_titles',  methods=['GET'])
def tag_all_titles():
  tag = request.args.get('tag')
  return tag_all_titles_control.tag_all_titles(tag=tag)

@app.route('/view',  methods=['GET'])
def view():
  hash = request.args.get('hash')
  return hash_control.hash_control(hash=hash)

@app.route('/chartjs')
def chartjs():
  fp = open('htmls/chartjs-challenge.html')
  base_html = fp.read()
  template = Template(base_html)
  return template.render()


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
