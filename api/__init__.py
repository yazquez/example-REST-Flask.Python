"""Create and configure the Flask server"""
from flask import Flask
app = Flask(__name__)
# Fake database
def database():
    return {
        "acme": {
            "name": "ACME & Associates",
            "city": "New York"
        },
        "pragma": {
            "name": "Lost and Lost. Inc",
            "city": "Nowhere"
        }
    }


# Routes
from api.companies import read_company
from api.companies import read_companies
from api.companies import create_company
from api.companies import update_company
from api.companies import delete_company