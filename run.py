import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"): # Checking if the env.py path exists then import it.
    import env

"""
Flask - Allows u to use python to build the front end of a website using the python language.
By using other parts and frameworks alongside we are able to build complex websites. Also allowing us to build a 
simple server for testing purposes

render_template = Allows us to render entire pages by using templates. Allowing us to write minimal repeated
code. And search for and retrieve data from other files to populate the web page

request - Handles all requests made by the user and the application. Such as sending contact from emails. Posting 
data to a database etc...

flash - flashes a message or a piece of data to the user. It is a non permanent message that can be shown to the user

"""

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

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
    data = []
    with open("data/company.json", "r") as json_data: # Opening the company file in read only mode
        data = json.load(json_data) # assigning the data in the document to data    
    return render_template(
        "about.html", page_title="About", company=data) # passing the data variable to the page
    # By adding extra arguments/variables to the render_template function we can input more logic into the html 
    # directly from the server side of the application. Again reducing repeated code though out the application

@app.route("/about/<member_name>") # Creates a new page for the member that has been selected by the user
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data: # Opening the Json in read only to read the specific data requested by the user
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name: # checks if the members name and url match. The displays the appropriate information
                member = obj
    return render_template("member.html", member=member) 

#You can change the route name to what ever you want ie
# @app.route("/bananana") along with the contact_us function would return the same thing
@app.route("/contact", methods =["GET", "POST"])
def contact_us():
    if request.method == "POST":
        #print("Hello, is anyone there? Can you hear me?")  - Ensuring the post method is working by logging to the console.
        print(request.form.get("name"))
        print(request.form["email"]) 
        flash("Thanks {}, we have received your message!".format( # Flashes a message that is defined to the user on the page
            request.form.get("name"))) # getting the name key to populate the flash
        # Works the same both ways. But target different ways of retrieving the data.
    return render_template(
        "contact-us.html", page_title="Contact Us", list_of_numbers=[1, 2, 3])

@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")
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
        