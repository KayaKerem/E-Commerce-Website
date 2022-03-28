from mimetypes import init
import sqlite3
import database as db

def initialize():
    conn = sqlite3.connect('Dunder.db')
    print('Bağlantı Gerçekleşti')

    cursor=conn.cursor()
    print("Cursor Oluşturuldu")
    
    cursor.execute(''' CREATE TABLE PRODUCTS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NAME TEXT NOT NULL,
        QUANTITY INTEGER NOT NULL,
        PRICE INTEGER NOT NULL,
        WEIGHTOFPACKAGES INTEGER NOT NULL,
        DETAILS TEXT NOT NULL
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
        DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    )''')
    conn.commit()
    db.addProductFirst(1000,'Mukavva',7000,250,175,'En temelde kağıt grubunda yer alan bir endüstriyel üründür. Özellikle kutu üretiminde ve taşıma sektöründe oldukça pay sahibi olması nedeni ile ön plana çıkar. Mukavva karton 3,20 mm – 1,00 mm arası kalınlıkta ve 70*100 ebadında bulunmaktadır.')
    db.addProduct('Hamur',6500,150,200,'Genellikle antetli kağıt, kitap, broşür gibi çalışmaların baskısında kullanılır. Bileşimindeki selüloz miktarı çok, odun miktarı azdır. Hamur kağıt 2,90 mm – 1,30 mm arası kalınlıkta ve 65*110 ebadında bulunmaktadır.')
    db.addProduct('Kuşe',7000,200,150,'Tasarımcılar tarafından hazırlanan afiş, broşür ve el ilanlarında en çok verim sağlayan kuşe kağıt kullanılır. Kuşe kağıt 2,20 mm – 0,90 mm arası kalınlıkta ve 60*90 ebadında bulunmaktadır.')
    db.addProduct('Pelur',8000,125,100,'İnce ve hafif bir yapısı olduğundan dolayı ürün ambalajında kullanılır. Ayakkabı mağazaları, bujiteriler, çanta üreticileri, kuyumcular vs. tarafından kullanılmaktadır. Pelur kağıt 3,00 mm – 1,10 mm arası kalınlıkta ve 40*120 ebadında bulunmaktadır.')
    db.addProduct('Kroma Karton',7700,175,220,'Genelde ambalaj sektöründe kullanılan bir yüzeyi parlak diğer yüzeyi mat bir kağıttır. Kroma karton 2,40 mm – 1,00 mm arası kalınlıkta ve 50*100 ebadında bulunmaktadır.')

    db.addUserFirst(2000,'Kutay','Sarı','kutaysari@gmail.com','kutaysari')
    db.addUser('Kerem','Kaya','keremkaya@gmail.com','keremkaya')
    db.addUser('Sena','Eser','senaeser@gmail.com','senaeser')
    db.addUser('Berkay','Gündüz','berkaygunduz@gmail.com','berkaygunduz')
    db.addUser('İrem','Avcı','iremavci@gmail.com','iremavci')


    conn.commit()
    conn.close()

initialize()