from urllib import request
from flask import Flask, request
from initialize_database import initialize
from flask_cors import CORS
import database as db
app = Flask(__name__)
CORS(app)


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
@app.route("/login", methods = ['GET', 'POST'])
def login():
    var = request.form.dict()
    mail = var["mail"]
    password = var["password"]
    
    return mail,password


app.debug=False
app.run()

