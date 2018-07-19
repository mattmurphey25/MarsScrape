from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"

mongo = PyMongo(app)

# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    # Find data
    mars_dict = mongo.db.collection.find()

    # return template and data
    return render_template("index.html", mars_dict=mars_dict)




@app.route("/scrape")
def scrape():

    mars_dict = mongo.db.collection
    # Run scraped functions
    mars = scrape_mars.scrape()

    mars_dict.update(
        {},
        mars,
        upsert=True
    )

    # Redirect back to home page
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)