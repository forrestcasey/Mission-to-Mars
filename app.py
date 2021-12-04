#10.5.1
# import dependencies

from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# set up flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


#define the route for the HTML page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

#set up scraping route for "button" of the web application,will scrape updated data when we tell it to
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

#update the database
mars.update({}, mars_data, upsert=True)

#add a redirect after successfully scraping the data
#This will navigate our page back to / where we can see the updated content
return redirect('/', code=302)

#tell it to run
if __name__ == "__main__":
   app.run()











