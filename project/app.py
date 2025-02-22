from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Update with your MongoDB connection string
db = client['vm_managerDB']  # Replace with your database name
collection1 = db['templates']  # Replace with your collection name
collection2 = db['VMS']
@app.route('/')
def home():
    vms = list(collection1.find())
    return render_template('index.html', vms=vms)
@app.route('/vms')
def vms_list():
    user_vms = list(collection2.find())
    return render_template('vms_list.html', user_vms=user_vms)

if __name__ == '__main__':
    app.run(debug=True)
