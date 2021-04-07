from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


#@app.route("/<string:name>")
##ef hello(name):
   # return f"<h1>Hello, {name}!</h1>"



#@app.route("/david")
#def david():
  #  return "Hello David!"

#@app.route("/maria")
#def david():
#    return "Hello DMaria!"


#@app.route('/<name>')

#def index(name):
 #   return '<h1>Hello {}!</h1>'.format(name)
