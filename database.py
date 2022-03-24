import sqlite3

def addProduct(name,quantity,price,weightofpackages):#Product Ekler
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()

    add_command = '''INSERT INTO PRODUCTS(NAME,QUANTITY,PRICE,WEIGHTOFPACKAGES)VALUES{}'''
    data = (name,quantity,price,weightofpackages)
    cursor.execute(add_command.format(data))

    conn.commit()
    conn.close()
def addProductFirst(id,name,quantity,price,weightofpackages):#addProduct ile aynı olup ID yi spesifik bir sayıdan başlatmak için ilk eleman bununla eklenir
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()

    add_command = '''INSERT INTO PRODUCTS(ID,NAME,QUANTITY,PRICE,WEIGHTOFPACKAGES)VALUES{}'''
    data = (id,name,quantity,price,weightofpackages)
    cursor.execute(add_command.format(data))

    conn.commit()
    conn.close()    

def addUser(name,surname,mail,password):#Kullanıcı Ekler eğer mail adresi zaten kullanılıyor ise '0' döner
    conn = sqlite3.connect('Dunder.db')
    cursor=conn.cursor()
    flag = 0
    cursor.execute('''SELECT * FROM USERS''')
    mailsTuple = cursor.fetchall()
    for i in mailsTuple:
        if mail == i[3]:
            flag = 1
    if flag == 0:
        add_command = ''' INSERT INTO USERS(NAME,SURNAME,MAIL,PASSWORD) VALUES {}'''
        data = (name,surname,mail,password)
        cursor.execute(add_command.format(data))
    else:
        # print('Girmiş Olduğunuz Mail Adresi Zaten Kullanılmaktadır')
        return 0

    conn.commit()
    conn.close()
def addUserFirst(id,name,surname,mail,password):#AddUser ile aynı olup ID yi spesifik sayıdan başlatmak için ilk eleman bununla eklenir
    conn = sqlite3.connect('Dunder.db')
    cursor=conn.cursor()
    flag = 0
    cursor.execute('''SELECT * FROM USERS''')
    mailsTuple = cursor.fetchall()
    for i in mailsTuple:
        if mail == i[3]:
            flag = 1
    if flag == 0:
        add_command = ''' INSERT INTO USERS(ID,NAME,SURNAME,MAIL,PASSWORD) VALUES {}'''
        data = (id,name,surname,mail,password)
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
                return 1
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

def getTradeOfUser(user_id):#Kullanıcının aldığı aldığı ürünlerin toplam sayısını dict olarak {ürün:toplam alınan miktar} şeklinde döndürür
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

    print(dictOfData)
    conn.commit()
    conn.close()
    return dictOfData