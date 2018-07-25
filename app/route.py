from flask import Flask, jsonify, abort, make_response, request, Markup

from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

Dashboard = [
    {
        "id": 1,
        "Date": "Tuesday",
        "Title": "My first Blog",
        "Body": "So I decided to pin down all my thoughts here...."
    },

    {
        "id": 2,
        "Date": "Wednesday",
        "Title": "My WCW",
        "Body": "Ain't she a beauty...."
    },

    {
        "id": 3,
        "Date": "Thursday",
        "Title": "Throw Back",
        "Body": "So when is it i decided to try programming again?...." 
    },

]

@app.route('/')
def home():
    html = Markup("<h1>Hello, welcome to your Diary</h1>")
    return html

"""
We defined the method as GET, here we get all the enrtries made
Content-type: application/json
"""
@app.route('/mydiary/api/v1/entries', methods=['GET'])
def get_entries():
    return jsonify({'Dashboard': Dashboard})

"""
Define the methos as GET, here we get a spefic entry with a given id
"""
@app.route('/mydiary/api/v1/entries/<int:entryId>', methods=['GET'])
def get_specificEntry(entryId):
    newDashboard = [Entry for Entry in Dashboard if Entry["id"] == entryId]
    if len(newDashboard) == 0:
        abort(404)
    return jsonify({'Dashboard': newDashboard})

"""
Define the method as POST
"""
@app.route('/mydiary/api/v1/entries', methods=['POST'])
def create_entries():
    if not request.json or not 'Title' in request.json:
        abort(404)

    entry = {
        "id": Dashboard[-1]["id"] + 1,
        "Date": request.json["Date"],
        "Title": request.json["Title"],
        "Body": request.json["Body"],    
    }
    Dashboard.append(entry)
    return jsonify({'Dashboard': Dashboard}), 201

"""
Define the method as PUT, here we update the existing resourse
"""
@app.route('/mydiary/api/v1/entries/<int:entryId>', methods=['PUT'])
def update_entry(entryId):
    updatedDashdoard = [updateEntry for updateEntry in Dashboard if updateEntry['id'] == entryId]
    
    updatedDashdoard[0]['Date'] = request.json.get("Date")
    updatedDashdoard[0]['Title'] = request.json.get('Title')
    updatedDashdoard[0]['Body'] = request.json.get('Body')
    
    return jsonify({'Dashboard': updatedDashdoard[0]})

"""
Define the method as DELETE, here we delete a resourse
"""
@app.route('/mydiary/api/v1/entries/<int:entryId>', methods=['DELETE'])
def delete_task(entryId):
    delDashboard = [delEntry for delEntry in Dashboard if delEntry['id'] == entryId]
    if len(delDashboard) == 0:
        abort(404)
    Dashboard.remove(delDashboard[0])
    return jsonify({'result': True})


@app.errorhandler(404)
def entriesNotFound(error):
    return make_response(jsonify({"error": "Resource not found"}), 404)

@app.errorhandler(405)
def methodsNotFound(error):
    return make_response(jsonify({"error": "Method not allowed"}), 405)
