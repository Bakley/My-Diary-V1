from flask import Flask, jsonify, abort, make_response, request, Markup

app = Flask(__name__)

Dashboard = [
    {
        "id":1,
        "Date":"Tuesday",
        "Title":"My first Blog",
        "Body":"So I decided to pin down all my thoughts here...."
    },

    {
        "id":2,
        "Date":"Wednesday",
        "Title":"My WCW",
        "Body":"Ain't she a beauty...."
    },

    {
        "id":3,
        "Date":"Thursday",
        "Title":"Throw Back",
        "Body":"So when is it i decided to try programming again?...." 
    },

]

@app.route('/')
def home():
    html = Markup("<h1>Hello, welcome to your Diary</h1>")
    return html

@app.route('/mydiary/api/v1/entries', methods=['GET'])
def get_entries():
    return jsonify({'Dashboard': Dashboard})

@app.route('/mydiary/api/v1/entries/<int:entryId>', methods=['GET'])
def get_specificEntry(entryId):
    newDashboard = [Dashboard for Dashboard in Dashboard if Dashboard["id"] == entryId]
    if len(newDashboard) == 0:
        abort(404)
    return jsonify({'Dashboard': newDashboard})


@app.route('/mydiary/api/v1/entries', methods=['POST'])
def create_entries():
    if not request.json or not 'Title' in request.json:
        abort(404)

    entry = {
        "id" :Dashboard[-1]["id"] + 1,
        "Date" :request.json["Date"],
        "Title" :request.json["Title"],
        "Body" :request.json["Body"],    
    }
    Dashboard.append(entry)
    return jsonify({'Dashboard': Dashboard}), 201

@app.route('/mydiary/api/v1/entries/<int:entryId>', methods=['PUT'])
def updateEntry(entryId):
    updatedDashdoard = [Dashboard for Dashboard in Dashboard if Dashboard['id'] == entryId]
    updatedDashdoard[0]['Date'] = request.json('Date', updatedDashdoard[0]['Date'])
    updatedDashdoard[0]['Title'] = request.json('Title', updatedDashdoard[0]['Title'])
    updatedDashdoard[0]['Body'] = request.json('Body',
        updatedDashdoard[0]['Body'])
    return jsonify({'Dashboard': updatedDashdoard[0]})

@app.route('/mydiary/api/v1/entries/<int:entryId>', methods=['DELETE'])
def delete_task(entryId):
    delDashboard = [Dashboard for Dashboard in Dashboard if Dashboard['id'] == entryId]
    if len(delDashboard) == 0:
        abort(404)
    Dashboard.remove(delDashboard[0])
    return jsonify({'result': True})


@app.errorhandler(404)
def entriesNotFound(error):
    return make_response(jsonify({"error": "Resource not found"}), 404)


if __name__ == "__main__":
    app.run(debug=False)