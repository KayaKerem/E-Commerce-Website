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
        DETAILS TEXT NOT NULL,
        IMAGE TEXT,
        THICKNESS TEXT NOT NULL,
        DIMENSION TEXT NOT NULL
    )''')
    conn.commit()
    cursor.execute(''' CREATE TABLE USERS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NAME TEXT NOT NULL,
        SURNAME TEXT NOT NULL,
        MAIL TEXT NOT NULL,
        PASSWORD TEXT NOT NULL,
        ADDRESS TEXT NOT NULL
    )''')
    conn.commit()
    cursor.execute('''CREATE TABLE ORDERS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        USER_ID INTEGER NOT NULL,
        PRODUCT_ID INTEGER NOT NULL,
        QUANTITYOFPACKAGE INTEGER NOT NULL,
        PRICEPERPRODUCT INTEGER NOT NULL,
        DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        ORDERNUMBER INTEGER NOT NULL
    )''')
   
    conn.commit()
    db.addProductFirst(1000,'Mukavva',7000,250,175,'En temelde kağıt grubunda yer alan bir endüstriyel üründür. Özellikle kutu üretiminde ve taşıma sektöründe oldukça pay sahibi olması nedeni ile ön plana çıkar.','https://www.elegansgrup.com/wp-content/uploads/2021/06/Mukavva-550x550-1.jpg','3,20 mm – 1,00 mm','70*100')
    db.addProduct('Hamur',6500,150,200,'Genellikle antetli kağıt, kitap, broşür gibi çalışmaların baskısında kullanılır. Bileşimindeki selüloz miktarı çok, odun miktarı azdır.','https://www.bordoambalaj.com/wp-content/uploads/2020/07/1.hamur-banner.jpg','2,90 mm – 1,30 mm','65*110')
    db.addProduct('Kuşe',7000,200,150,'Tasarımcılar tarafından hazırlanan afiş, broşür ve el ilanlarında en çok verim sağlayan kuşe kağıt kullanılır.','https://cdn03.ciceksepeti.com/cicek/kcm47418413-1/XL/100-adet-parlak-kuse-kagit-kalin-300-gr-a4-kuse-kcm47418413-1-0969d6e8487e470a8036ff4edfedc7e3.jpg','2,20 mm – 0,90 mm','60*90')
    db.addProduct('Pelur',8000,125,100,'İnce ve hafif bir yapısı olduğundan dolayı ürün ambalajında kullanılır. Ayakkabı mağazaları, bujiteriler, çanta üreticileri, kuyumcular vs. tarafından kullanılmaktadır.','https://www.polasambalaj.com/upload/b/pelur-kagitlari_4650384784.jpg','3,00 mm – 1,10 mm','40*120')
    db.addProduct('Kroma Karton',7700,175,220,'Genelde ambalaj sektöründe kullanılan bir yüzeyi parlak diğer yüzeyi mat bir kağıttır.','http://turkoglumukavva.com/wp-content/uploads/2019/07/kromekarton2.jpg','2,40 mm – 1,00 mm','50*100')

    db.addUserFirst(2000,'Kutay','Sarı','kutaysari@gmail.com','kutaysari','Yıldız Teknik Üniversitesi')
    db.addUser('Kerem','Kaya','keremkaya@gmail.com','keremkaya','Yıldız Teknik Üniversitesi')
    db.addUser('Sena','Eser','senaeser@gmail.com','senaeser','Yıldız Teknik Üniversitesi')
    db.addUser('Berkay','Gündüz','berkaygunduz@gmail.com','berkaygunduz','Yıldız Teknik Üniversitesi')
    db.addUser('İrem','Avcı','iremavci@gmail.com','iremavci','Yıldız Teknik Üniversitesi')
    db.addUser('Oya',"Kalıpsız","oyakalipsiz@gmail.com","oyakalipsiz","Yıldız Teknik Üniversitesi")

    db.initializeOrder()

    conn.commit()
    conn.close()

