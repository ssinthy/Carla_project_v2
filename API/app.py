from flask import Flask, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Configure the MongoDB client
client = MongoClient('mongodb://localhost:27017/')
db = client.odd


@app.route('/')
def home():
    return "Hello, Flask and MongoDB!"

@app.route('/api/odd/<id>', methods=['GET'])
def get_data(id):
    try:
        # Retrieve data from the MongoDB collection
        data = db.odd_collection.find_one({'_id': ObjectId(id)})

        if data:
            data['_id'] = str(data['_id'])
            return jsonify(data), 200
        else:
            return jsonify({'error': 'Document not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/roadinfo/<key>', methods=['GET'])
def get_roadtype(key):
    try:
        key = int(key)
        # Retrieve data from the MongoDB collection
        query = { f"{key}.ROADTYPE": { "$exists": True } }
        projection = { f"{key}.ROADTYPE": 1, "_id": 0 }
        document = db.roadinfo.find_one(query, projection)

        if document and str(key) in document:
            roadtype_value = document[str(key)].get("ROADTYPE")
            return jsonify({"ROADTYPE": roadtype_value})
        else:
            return jsonify({"error": "Document not found or ROADTYPE not found"}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    

if __name__ == '__main__':
    app.run(debug=True)
