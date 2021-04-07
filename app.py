from flask import Flask

app= Flask(__name__)

@app.route("/")
def index():
    return "Hello WOrld!"
@app.route("/<string:name>")
def hello(name):
    return f"Hello, {name}!"
#@app.route("/david")
#def david():
  #  return "Hello David!"

#@app.route("/maria")
#def david():
#    return "Hello DMaria!"


#@app.route('/<name>')

#def index(name):
 #   return '<h1>Hello {}!</h1>'.format(name)
