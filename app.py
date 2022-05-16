from this import d
from urllib import request
from flask import Flask, request
from initialize_database import initialize
from flask_cors import CORS
import database as db
import json


app = Flask(__name__)
CORS(app)
        

# @app.route("/showtable")
# def show_table():
#     dict = {}
#     res = db.getProducts()
#     for i in res:
#         dict.update({i[1]:i})
#     return dict
   
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
        temp.update({"thumbnail_url":i[6]})
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

def getUserID():
    id = request.data.decode("UTF-8")
    id = json.loads(id)
    id = id["id"]
    return id

def getProductID():
    id = request.data.decode("UTF-8")
    id = json.loads(id)
    id = id["product_id"]
    return id

def getAmount():
    amount = request.data.decode("UTF-8")
    amount = json.loads(amount)
    amount = amount["amount"]
    return amount

@app.route("/showtable/pastorders", methods = ["GET", "POST"])
def pastorders():
    id = getUserID()
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


@app.route("/showtable/pastorders_money", methods = ["GET", "POST"])                  
def pastordersMoney():
    id = getUserID()
    temp = db.totalSpentOfMoney(id)#tarih, ürünıd, paket sayısı
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


@app.route("/showtable/packageoftotalbought",methods = ["GET", "POST"])
def packageOfTotalBought():
    id = getUserID()
    temp = db.getPastOrders(id)#ürünıd, miktar
    pck = db.getNamesOfProducts()
    labels = []
    series = []
    for i in pck:
        labels.append(i["name"])
    for i in pck:
        series.append(0)
    a = 0
    for i in pck:
        for j in temp:
            if(i["name"]==j[0]):
                series[a] +=j[1]
        a+=1
    return {"labels":labels, "series":series}
    
@app.route("/showtable/spentmoneyformonths",methods = ["GET", "POST"])
def spentmoneyformonths():
    id = getUserID()
    temp = db.spentOfMoneyForMonths(id) #ay, harcanan para
    months = [["01","Ocak"],["02","Şubat"],["03","Mart"],["04","Nisan"],["05","Mayıs"],["06","Haziran"],["07","Temmuz"],["08","Ağustos"],["09","Eylül"],["10","Ekim"],["11","Kasım"],["12","Aralık"]]
    series = []
    labels = []
    for i in months:
        labels.append(i[1])
        series.append(0)
    for i in temp:
        for j in range(len(months)):
            if(i[0]==months[j][0]):
                series[j]+=i[1]
                
    return {"labels":labels, "series":series}

@app.route("/buyProduct",methods = ["GET", "POST"])
def buyProduct():
    user_id = getUserID()
    product_id = getProductID()
    amount = getAmount()
    res = db.buyProduct(user_id, product_id, amount)
    return res

app.debug=False
app.run()