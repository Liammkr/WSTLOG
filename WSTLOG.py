##                          .                .,                                ., G:        
##                         ;W               ,Wt j.                            ,Wt E#,    :
##            ;           f#E GEEEEEEEL    i#D. EW,                   ..     i#D. E#t  .GE
##          .DL         .E#f  ,;;L#K;;.   f#f   E##j                 ;W,    f#f   E#t j#K;
##  f.     :K#L     LWLiWW;      t#E    .D#i    E###D.              j##,  .D#i    E#GK#f  
##  EW:   ;W##L   .E#fL##Lffi    t#E   :KW,     E#jG#W;            G###, :KW,     E##D.   
##  E#t  t#KE#L  ,W#;tLLG##L     t#E   t#f      E#t t##f         :E####, t#f      E##Wi   
##  E#t f#D.L#L t#K:   ,W#i      t#E    ;#G     E#t  :K#E:      ;W#DG##,  ;#G     E#jL#D: 
##  E#jG#f  L#LL#G    j#E.       t#E     :KE.   E#KDDDD###i    j###DW##,   :KE.   E#t ,K#j
##  E###;   L###j   .D#j         t#E      .DW:  E#f,t#Wi,,,   G##i,,G##,    .DW:  E#t   jD
##  E#K:    L#W;   ,WK,          t#E        L#, E#t  ;#W:   :K#K:   L##,      L#, j#t     
##  EG      LE.    EG.            fE         jt DWi   ,KK: ;##D.    L##,       jt  ,;     
##  ;       ;@     ,               :                       ,,,      .,,                   
##                           
##                                                                              liamm --
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase with your service account credentials
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project-id.firebaseio.com/'
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
