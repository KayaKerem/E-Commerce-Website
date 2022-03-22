import sqlite3
import database as db

def initialize():
    conn = sqlite3.connect('Database.db')
    print('Bağlantı Gerçekleşti')

    cursor=conn.cursor()
    print("Cursor Oluşturuldu")
    
    cursor.execute(''' CREATE TABLE PRODUCTS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NAME TEXT NOT NULL,
        QUANTITY INTEGER NOT NULL,
        PRICE INTEGER NOT NULL,
        WEIGHTOFPACKAGES INTEGER NOT NULL
    )''')
    conn.commit()
    cursor.execute(''' CREATE TABLE USERS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NAME TEXT NOT NULL,
        SURNAME TEXT NOT NULL,
        MAIL TEXT NOT NULL,
        PASSWORD TEXT NOT NULL
    )''')
    conn.commit()
    cursor.execute('''CREATE TABLE ORDERS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        USER_ID INTEGER NOT NULL,
        PRODUCT_ID INTEGER NOT NULL,
        QUANTITYOFPACKAGE INTEGER NOT NULL,
        PRICEPERPRODUCT INTEGER NOT NULL,
        DATE DATE NOT NULL
    )''')
    conn.commit()
    db.addProduct('Mukavva',7000,250,175)
    db.addProduct('Hamur',6500,150,200)
    db.addProduct('Kuşe',7000,200,150)
    db.addProduct('Pelur',8000,125,100)
    db.addProduct('Kroma Karton',7700,175,220)

    db.addUser('Kutay','Sarı','kutaysari@gmail.com','kutaysari')
    db.addUser('Kerem','Kaya','keremkaya@gmail.com','keremkaya')
    db.addUser('Sena','Eser','senaeser@gmail.com','senaeser')
    db.addUser('Berkay','Gündüz','berkaygunduz@gmail.com','berkaygunduz')
    db.addUser('İrem','Avcı','iremavci@gmail.com','iremavci')


    conn.commit()
    conn.close()
    return 1

