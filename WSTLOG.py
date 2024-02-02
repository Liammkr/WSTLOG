import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Read the configuration file
with open('config.json') as config_file:
    config = json.load(config_file)

# Initialize Firebase with the service account key
cred = credentials.Certificate(config['service_account_key_path'])
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://logtestwst-default-rtdb.firebaseio.com/'
})
ref = db.reference('/')

# Define the data you want to write
data = {
    'users': {
        'user1': {
            'name': 'John',
            'age': 30
        },
        'user2': {
            'name': 'Alice',
            'age': 25
        }
    }
}

# Push the data to the database
ref.update(data)

print("Data written successfully.")