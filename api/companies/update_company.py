from api import app
from api import database
from flask import jsonify
from flask import request

@app.route('/companies/<string:company_id>', methods=['PUT'])
def update_company(company_id):
    """Update a company"""
    # Get the company details
    company = request.get_json()
    # Update the company with id = company_id
    db = database()
    db[company_id] = company
    # Return the updated company as JSON
    return jsonify({company_id: db[company_id]})


@app.route('/companies', methods=['POST'])
def create_company():
    """Create a new company"""
    # Get the posted data
    company = request.get_json()
    # Insert new company into the DB
    db = database()
    db.update(company)
    # Return the newly company as JSON
    return jsonify(company), 201
