from this import d
from urllib import request
from flask import Flask, request
from initialize_database import initialize
from flask_cors import CORS
import database as db
import json
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
        temp.update({"tumbnail_url":i[6]})
        temp.update({"title":i[1]})
        all_products.append(temp)
    return {"data":all_products}


@app.route("/login", methods = ['GET', 'POST'])
def login():
    var = request.data.decode("UTF-8")
    var = json.loads(var)
    mail = var["email"]
    password = var["password"]
    if(db.checkUser(mail,password)!=0):
        data = {}
        id,name,surname = db.checkUser(mail,password)
        data.update({"id":id})
        data.update({"name":name})
        data.update({"surname":surname})
        return {"data":data}
    else:
        return {"data":0}


@app.route("/showtable/pastorders", methods = ["GET", "POST"])
def pastorders():
    id = request.data.decode("UTF-8")
    id = json.loads(id)
    id = id["id"]
    temp  = db.totalPackageOfBought(id)#tarih, ürünıd, paket sayısı
    products = db.getNamesOfProducts() #{{"id":value, "name":value}}
    categories = []
    for i in temp:
        categories.append(i[0]) #dates
    categories = list(set(categories))    
    res = []    
    for i in products:
        d = {}
        datas = []
        for j in categories:
            datas.append(0)
        d.update({"name":i["name"],"data":datas})
        res.append(d)
    for i in res:
        for j in range(len(categories)):    
            for k in temp:
                if(i["name"] == db.getProductName(k[1])):
                    if(k[0] == categories[j]):
                        i["data"][j] = k[2]  
    return {"dates":categories, "pastOrders":res}            
                        
  

app.debug=False
app.run()

