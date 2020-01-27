from flask import Flask

# application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    return "Hello, World!?!?!?"

# dynamic routes
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return "correct"

@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "correct"

# dynamic route with explicit status codes
@app.route("/name/<name>")
def index(name):
    if name.lower() == "chris":
        return "Hello, {}".format(name)
    else:
        return "Not Found", 404
# start development server
if __name__ == "__main__":
    app.run()
