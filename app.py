from flask import Flask
from jinja2 import Template
app = Flask(__name__, static_folder='static_folder')


@app.route('/')
def hello():
  fp = open('htmls/00-index.html')
  base_html = fp.read()
  template = Template(base_html)
  return template.render(name='John Doe')

@app.route('/tag')
def tag():
  fp = open('htmls/01-tags.html')
  base_html = fp.read()
  template = Template(base_html)
  return template.render()


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
