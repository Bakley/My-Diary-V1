from flask import Flask, jsonify
# from flask_restful import Api, Resource

app = Flask(__name__)
# api = Api(app)

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

if __name__ == "__main__":
    app.run(debug=True)