import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase with your service account credentials
cred = credentials.Certificate("testcreds.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://logtestwst-default-rtdb.firebaseio.com'
})

# Get a reference to the Firebase Realtime Database
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
