"""Module to handle the routes.

Author: Nick Machairas, 2022
"""
from flask import render_template
from app import app
from app.forms import SearchForm
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl import connections
from elasticsearch.helpers import bulk
import json
import pymongo

from pymongo import MongoClient
client = MongoClient('localhost',27017) 
db = client.newapp


path = '/Users/zhenyucheng/Desktop/apan_flask_apps/app/'


@app.route("/", methods=["GET", "POST"])
def home():
    """Render the home page."""
    form = SearchForm()
    search_results = None
    search_results_rest = None
    search_results_theater = None
    if form.validate_on_submit():
        address = form.location.data
        preference = form.preference.data
        if preference == 'milktea':
            query = {
            "ADDRESS":{"$regex":address,
                    "$options" :'i' }
            }
            search_results = db.milktea.find(query)
            return render_template("home.html", form=form, search_results=search_results)
        elif preference == 'bar':
            query = {
            "ADDRESS":{"$regex":address,
                    "$options" :'i' }
            }
            search_results = db.bar.find(query)
            return render_template("home.html", form=form, search_results=search_results)
        elif preference == 'museum':
            query = {
            "ADDRESS":{"$regex":address,
                        "$options" :'i' }
            }   
            search_results = db.museum.find(query)
            return render_template("home.html", form=form, search_results=search_results)
        elif preference == 'restaurant':
            query = {
            'location.display_address':{"$regex":address,
                                        "$options" :'i'}
            }
            search_results_rest = db.restaurant.find(query)  
            return render_template("home.html", form=form, search_results_rest=search_results_rest)
        elif preference == 'theater':
            query = {
                "$or": [
                {"ADDRESS1": {"$regex": address}},
                 {"ZIP": {"$regex": address}}
                    ]
                    }
            search_results_theater = db.theater.find(query)
            return render_template("home.html", form=form, search_results_theater=search_results_theater)

    


