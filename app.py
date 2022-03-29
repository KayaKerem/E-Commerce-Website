from flask import Flask
from initialize_database import initialize
import database as db
app = Flask(__name__)



@app.route("/showtable")
def show_table():
    dict = {}
    res = db.getProducts()
    for i in res:
        dict.update({i[1]:i})
    return dict
   
@app.route("/products", methods = ['GET'])
def products():
    res = db.getProducts()
    print(res)
    all_products = []
    for i in res:
        temp = {}
        temp.update({"description":i[5]})
        temp.update({"id":i[0]})
        temp.update({"price":i[3]})
        temp.update({"quantity":i[2]})
        temp.update({"tumbnail_url":5})
        temp.update({"title":i[1]})
        all_products.append(temp)
    return {"data":all_products}


app.debug=False
app.run()

