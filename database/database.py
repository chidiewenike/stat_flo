import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time 

cred = credentials.Certificate('stat-flo.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def store_data(data, node):
    doc_ref = db.collection(u'' + node).document(u'' + time.strftime("%b%d%Y%H%M%S"))
    print(doc_ref.get())
    doc_ref.set({
            u'data': u'' + data
        })

if __name__ == "__main__":
    store_data("2.421", "node_04")
