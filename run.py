import os
from flask import Flask, render_template # Allows us to render an external html file - Flask functions


app = Flask(__name__)

"""
The below lines of code are the app routing of the html pages. 
First defining the page route name for the address bar
Then defining the function where the page is located on the server so the page can be rendered by the flask framework
"""

# Says if the app is running on the correct file path, then display the hello world string
@app.route("/") 
# Function that returns the index.html file on the root level due to the app.route('/' ) method
def index():
    return render_template("index.html") # Flask looks for the file in a folder called 'templates' at the same level as the python file
    # return "Hello World" Renders a basic string of text on the web page

@app.route("/about")
def about():
    return render_template("about.html")

#You can change the route name to what ever you want ie
# @app.route("/bananana") along with the contact_us function would return the same thing
@app.route("/contact")
def contact_us():
    return render_template("contact-us.html")

@app.route("/careers")
def careers():
    return render_template("careers.html")

"""
Running a basic server using the python/flask frameworks
"""

# Setting up the server for the application to run on
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "4000")),
        debug=True) # Never have this in a production application/when submitting a project for assessment. 
        # As its a security flaw. debug=False is allowed
        