from flask import Flask

# application object
app = Flask(__name__)

@app.route("/")
@app.route("/hello")

# dynamic route
@app.route("/test/<search_query>")

def search (search_query):
    return search_query

def hello_world():
    return "Hello, World!"

# start development server
if __name__ == "__main__":
    app.run()
