from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)


Dashboard = [
    {
        "id" : 1,
        "Date" : "Tuesday",
        "Title" : "My first Blog",
        "Body" : "So I decided to pin down all my thoughts here...."
    },

    {
        "id" : 2,
        "Date" : "Wednesday",
        "Title" : "My WCW",
        "Body" : "Ain't she a beauty...."
    },

    {
        "id" : 3,
        "Date" : "Thursday",
        "Title" : "Throw Back",
        "Body" : "So when is it i decided to try programming again?...." 
    }
]

@app.route('/mydiary/api/v1/entries', methods=['GET'])
def get_entries():
    return jsonify({'Dashboard': Dashboard})

@app.route('/mydiary/api/v1/entries/<int:entryId>', methods=['GET'])
def get_specificEntry(entryId):
    newDashboard = [Dashboard for Dashboard in Dashboard if Dashboard["id"] == entryId]
    if len(newDashboard) == 0:
        abort(404)
    return jsonify({'Dashboard': newDashboard})

@app.errorhandler(404)
def entriesNotFound(error):
    return make_response(jsonify({"error": "Resource not found"}, 404))


if __name__ == "__main__":
    app.run(debug=True)