from api import app
from api import database
from flask import jsonify
from flask import request


# @app.route('/companies', methods=['POST', 'GET'])
# def create_company():
#     """Create a new company"""
#     # Get the posted data
#     company = request.get_json()
#     # Insert new company into the DB
#     db = database()
#     db.update(company)
#     # Return the newly company as JSON
#     return jsonify(company), 201
