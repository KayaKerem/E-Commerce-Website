import sqlite3

def addProduct(name,quantity,price,weightofpackages):
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()

    add_command = '''INSERT INTO PRODUCTS(NAME,QUANTITY,PRICE,WEIGHTOFPACKAGES)VALUES{}'''
    data = (name,quantity,price,weightofpackages)
    cursor.execute(add_command.format(data))

    conn.commit()
    conn.close()

def addUser(name,surname,mail,password):#Kullanıcı Ekleme Fonksiyonu
    conn = sqlite3.connect('Dunder.db')
    cursor=conn.cursor()
    add_command = ''' INSERT INTO USERS(NAME,SURNAME,MAIL,PASSWORD) VALUES {}'''
    data = (name,surname,mail,password)
    cursor.execute(add_command.format(data))
    conn.commit()
    conn.close()

def getProducts():
    new_list = []
    conn = sqlite3.connect('Dunder.db')
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM PRODUCTS''')
    productList = cursor.fetchall()
    for i in productList:
        new_list.append(list(i))
        
    return new_list