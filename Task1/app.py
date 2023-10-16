from flask import Flask

#create a flask web application
app = Flask(__name__)

#Define a route for the home page
@app.route('/')

def home():
    return "<h1>Welcome to my simple flask app!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
