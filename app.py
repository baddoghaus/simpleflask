# from the package flask install the class Flask
from flask import Flask

# python variable that gives each file a unique name in a flask application
app = Flask(__name__)


# the home page of the application
@app.route('/')
def home():
    return "Hello, world!"
