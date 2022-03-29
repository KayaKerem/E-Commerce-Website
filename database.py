import sqlite3
from webbrowser import get

def addProduct(name,quantity,price,weightofpackages,details,image):#Product Ekler
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()

    add_command = '''INSERT INTO PRODUCTS(NAME,QUANTITY,PRICE,WEIGHTOFPACKAGES,DETAILS,IMAGE)VALUES{}'''
    data = (name,quantity,price,weightofpackages,details,image)
    cursor.execute(add_command.format(data))

    conn.commit()
    conn.close()
def addProductFirst(id,name,quantity,price,weightofpackages,details,image):#addProduct ile aynı olup ID yi spesifik bir sayıdan başlatmak için ilk eleman bununla eklenir
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()

    add_command = '''INSERT INTO PRODUCTS(ID,NAME,QUANTITY,PRICE,WEIGHTOFPACKAGES,DETAILS,IMAGE)VALUES{}'''
    data = (id,name,quantity,price,weightofpackages,details,image)
    cursor.execute(add_command.format(data))

    conn.commit()
    conn.close()    

def addUser(name,surname,mail,password,address):#Kullanıcı Ekler eğer mail adresi zaten kullanılıyor ise '0' döner
    conn = sqlite3.connect('Dunder.db')
    cursor=conn.cursor()
    flag = 0
    cursor.execute('''SELECT * FROM USERS''')
    mailsTuple = cursor.fetchall()
    for i in mailsTuple:
        if mail == i[3]:
            flag = 1
    if flag == 0:
        add_command = ''' INSERT INTO USERS(NAME,SURNAME,MAIL,PASSWORD,ADDRESS) VALUES {}'''
        data = (name,surname,mail,password,address)
        cursor.execute(add_command.format(data))
    else:
        # print('Girmiş Olduğunuz Mail Adresi Zaten Kullanılmaktadır')
        return 0

    conn.commit()
    conn.close()
def addUserFirst(id,name,surname,mail,password,address):#AddUser ile aynı olup ID yi spesifik sayıdan başlatmak için ilk eleman bununla eklenir
    conn = sqlite3.connect('Dunder.db')
    cursor=conn.cursor()
    flag = 0
    cursor.execute('''SELECT * FROM USERS''')
    mailsTuple = cursor.fetchall()
    for i in mailsTuple:
        if mail == i[3]:
            flag = 1
    if flag == 0:
        add_command = ''' INSERT INTO USERS(ID,NAME,SURNAME,MAIL,PASSWORD,ADDRESS) VALUES {}'''
        data = (id,name,surname,mail,password,address)
        cursor.execute(add_command.format(data))
    else:
        # print('Girmiş Olduğunuz Mail Adresi Zaten Kullanılmaktadır')
        return 0

    conn.commit()
    conn.close()    

def getProducts():#Product Table ındakileri Döndürür(Liste içinde Liste olarak)
    new_list = []
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM PRODUCTS''')
    productList = cursor.fetchall()
    for i in productList:
        new_list.append(list(i))
        
    return new_list

def addOrder(userId,ProductId,quantityOfPackage,pricePerProduct):#Sipariş Ekler
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()

    add_command = ''' INSERT INTO ORDERS(USER_ID,PRODUCT_ID,QUANTITYOFPACKAGE,PRICEPERPRODUCT)VALUES{}'''
    data = (userId,ProductId,quantityOfPackage,pricePerProduct)
    cursor.execute(add_command.format(data))

    conn.commit()
    conn.close()

def getOrders():#Order Table ındakileri Döndürür(Liste içinde Liste olarak)
    orderList = []
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM ORDERS''')
    orderTuple = cursor.fetchall()

    for i in orderTuple:
        orderList.append(list(i)) 

    return(orderList)

def checkUser(mail,password):#Kullanıcı giriş kontrolü yapılır.Doğru bilgiler girildiyse '1' aksi takdirde '0' döndürür.
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM USERS WHERE MAIL = ?''',(mail,))
    listofuser = cursor.fetchone()
    if listofuser is not None:
        if  listofuser[3] == mail :
            if listofuser[4] == password:
                id = listofuser[0]
                name =listofuser[1]
                surname = listofuser[2]
                return id,name,surname
                # print('Giriş Başarılı')
            else:
                return 0
                # print('Giriş Başarısız şifre yanlış')  
    else:
        return 0
        # print('Giriş Başarısız K.adı yanlış')     
        

    conn.commit()
    conn.close()

def updatePrice(newPrice,productId):#Ürünün Fiyatını yeniler
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor() 

    cursor.execute(''' UPDATE PRODUCTS SET PRICE = ? WHERE ID = ?''',(newPrice,productId,))

    conn.commit()
    conn.close()

def updateQuantity(newQuantity,productId):#Ürünün miktarını yeniler
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()

    cursor.execute(''' UPDATE PRODUCTS SET QUANTITY = ? WHERE ID = ?''',(newQuantity,productId))
    conn.commit()
    conn.close()



def buyProduct(userId,productId,amount):#ürün satın alır order tablosuna ekler
    conn =sqlite3.connect('Dunder.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM PRODUCTS WHERE ID = ?',(productId,))
    listProduct = list(cursor.fetchone())
    # print(listProduct)
    updateQuantity(listProduct[2]-amount,productId)
    addOrder(userId,productId,amount,listProduct[3])
    conn.commit()
    conn.close()

def getTradeOfUser(user_id):#Kullanıcının aldığı  ürünlerin toplam sayısını dict olarak {ürün:toplam alınan miktar} şeklinde döndürür
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT PRODUCT_ID,SUM(QUANTITYOFPACKAGE) FROM ORDERS WHERE USER_ID = ? GROUP BY PRODUCT_ID ''',(user_id,))
    x = cursor.fetchall()
    newList=[]
    dictOfData = {}
    for i in x:
        newList.append(list(i))

    for i in newList:
        dictOfData.update({i[0]:i[1]})

    # print(dictOfData)
    conn.commit()
    conn.close()
    return dictOfData
def getNamesOfProducts():
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT NAME FROM PRODUCTS''')
    tupleOfNames = cursor.fetchall()
    listOfNames = []

    for i in tupleOfNames:
        listOfNames.append(i[0])
    # print(listOfNames)
    conn.commit()
    conn.close()
    return listOfNames

def getProductName(product_id):#ID si verilen ürünün ismini döndürür.
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT NAME FROM PRODUCTS WHERE ID = ?''',(product_id,))
    nameTuple =cursor.fetchall()
    name = ''.join(nameTuple[0])
    conn.commit()
    conn.close()
    return name

#Kullanıcının belirli tarihlerde hangi üründen toplam harcadığı parayı liste içinde liste olarak döndürür[[tarih,ürün,para],[tarih,ürün,para]]
def totalSpentOfMoney(user_id):
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()    
    cursor.execute(''' SELECT DATE,PRODUCT_ID,SUM(PRICEPERPRODUCT*QUANTITYOFPACKAGE) FROM ORDERS WHERE USER_ID = ? GROUP BY DATE,PRODUCT_ID ORDER BY DATE''',(user_id,))
    x = cursor.fetchall()
    newList = []
    for i in x:
        newList.append(list(i))
    # print(newList)

    conn.commit()
    conn.close()
    return newList

#Kullanıcın belirli tarihlerde hangi üründen toplam kaç paket ürün aldığını liste içinde liste olarak döndürür[[tarih,ürün,paket sayısı],[tarih,ürün,paket sayısı]]
def totalPackageOfBought(user_id):
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()    
    cursor.execute(''' SELECT STRFTIME('%d-%m-%Y',DATE) as DATE,PRODUCT_ID,SUM(QUANTITYOFPACKAGE) FROM ORDERS WHERE USER_ID = ? GROUP BY DATE,PRODUCT_ID ORDER BY DATE''',(user_id,))
    x = cursor.fetchall()
    newList = []
    for i in x:
        newList.append(list(i))
    # print(newList)

    conn.commit()
    conn.close()
    return newList

#Aylara göre kullanıcının harcadığı toplam miktar liste içinde liste döndürür[[Ay,Harcanan Para],[Ay,Harcanan Para]]
def spentOfMoneyForMonths(user_id):
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()
    newList =[]
    cursor.execute('''SELECT STRFTIME('%m', DATE) as Month ,SUM(PRICEPERPRODUCT*QUANTITYOFPACKAGE) FROM ORDERS
    WHERE USER_ID = ? AND STRFTIME('%Y', DATE) = STRFTIME('%Y',CURRENT_TIMESTAMP) 
    GROUP BY DATE ORDER BY STRFTIME('%m', DATE)''',(user_id,))
    x = cursor.fetchall()
    for i in x:
        newList.append(list(i))
    # print(newList)
    conn.commit()
    conn.close()
    return newList

def getDetails(product_id):#Ürün detayını string olarak döndürür(text şeklinde)
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()
    detailList = []
    detail = ""
    cursor.execute(''' SELECT DETAILS FROM PRODUCTS WHERE ID = ? ''',(product_id,))
    detailList = cursor.fetchall()
    detail = "".join(detailList[0])
    # print(detail)
    conn.commit()
    conn.close()
    return detail

#Verilen user_id nin geçmiş siparişlerini en son verilen siparişten ilk verilen siparişe list içinde list olarak [[Ürünİsmi, Miktar, PaketFiyatı, Tarih],...] şeklinde döndürür
def getPastOrders(user_id):
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT PRODUCT_ID,QUANTITYOFPACKAGE,PRICEPERPRODUCT,DATE FROM ORDERS WHERE USER_ID = ? ORDER BY DATE DESC''',(user_id,))
    tupleOfOrders = cursor.fetchall()
    listOfOrders = []
    tuple2 =[]
    tmp =[]
    # print(tupleOfOrders)
    for i in tupleOfOrders:
        listOfOrders.append(list(i))
    # print(listOfOrders)
    for i in listOfOrders:
        cursor.execute('''SELECT NAME FROM PRODUCTS WHERE ID = ?''',(i[0],))
        tuple2 = cursor.fetchall()
        # print(tuple2)
        for j in tuple2:
            tmp.append(''.join(tuple2[0]))
    # print(tmp)
    k = 0
    for i in listOfOrders:
        i[0] =tmp[k]
        k+=1
    # print(listOfOrders)
    conn.commit()
    conn.close()
    return listOfOrders
def getIdsOfProducts():
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()

    cursor.execute(''' SELECT ID FROM PRODUCTS''')
    tupleOfIds = cursor.fetchall()
    listOfIds = []
    for i in tupleOfIds:
        listOfIds.append(i[0])
    # print(listOfIds)
    return listOfIds
