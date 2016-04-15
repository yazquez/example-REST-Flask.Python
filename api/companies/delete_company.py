from api import app
from api import database
from flask import jsonify

@app.route('/companies/<string:company_id>', methods=['DELETE'])
def delete_company(company_id):
    """Delete a company"""
    db = database()
    # Save the company's details for the response.
    # Normally this would be handled via RETURNING
    # or a similar feature of the database.
    company = db[company_id]
    print(company)
    # Delete the company with id = company_id
    del db[company_id]
    # Return the company as JSON
    return jsonify({company_id: company})