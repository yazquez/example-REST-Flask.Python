from api import app
from api import database
from flask import jsonify


@app.route('/companies', methods=['GET'])
def read_companies():
    """Read all companies"""
    # Read all companies from DB
    db = database()
    companies_list = []
    for key, value in db.items():
        companies_list.append({key: value})
    # Return company as JSON
    return jsonify(companies=companies_list)
