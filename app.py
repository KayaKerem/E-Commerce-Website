from flask import Flask
from initialize_database import initialize
import database as db
app = Flask(__name__)


print(initialize())
@app.route("/showtable")
def show_table():
    dict = {}
    res = db.getProducts()
    for i in res:
        dict.update({i[1]:i})
    return dict
   

app.debug=False
app.run()

