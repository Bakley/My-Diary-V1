from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

Dashboard = [
    {
        "Date" : "Tuesday",
        "Title" : "My first Blog",
        "Body" : "So I decided to pin down all my thoughts here...."
    },

    {
        "Date" : "Wednesday",
        "Title" : "My WCW",
        "Body" : "Ain't she a beauty...."
    },

    {
        "Date" : "Thursday",
        "Title" : "Throw Back",
        "Body" : "So when is it i decided to try programming again?...." 
    }
]