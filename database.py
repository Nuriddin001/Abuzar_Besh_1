import sqlite3


def create_categories_table():
    database = sqlite3.connect('abuzar_besh.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories(
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name VARCHAR(30) NOT NULL
    );
    ''')

    database.commit()
    database.close()


def insert_categories():
    database = sqlite3.connect('abuzar_besh.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO categories(category_name) VALUES
    ('Ovqatlar'),
    ('Ichimliklar'),
    ('Salad')
    ''')

    database.commit()
    database.close()


def create_products_table():
    database = sqlite3.connect('abuzar_besh.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    product_name VARCHAR(30) NOT NULL UNIQUE,
    price DECIMAL (12,2) NOT NULL,
    description VARCHAR(200),
    image TEXT,

    FOREIGN KEY(category_id) REFERENCES categories (category_id)
    );
    ''')

    database.commit()
    database.close()


def insert_products_table():
    database = sqlite3.connect('abuzar_besh.db')
    cursor = database.cursor()

    products = [
        (1, 'Besh barmoq', 70000, 'Ot go`shti va pishirilgan hamir', 'media/ovqatlar'),
        (1, 'Baliq 1kg', 160000, 'Xorazm sazan baliq', 'media/ovqatlar/baliq.jpg'),
        (1, 'Baliq 0,5kg', 80000, 'Xorazm sazan baliq', 'media/ovqatlar/baliq.jpg'),
        (1, 'Qazi', 25000, 'Bir bo`lak', 'media/ovqatlar/qazi.jpg'),
        (1, 'Hamir', 25000, 'Beshbarmoq hamiri', 'media/ovqatlar/hamir.jpg'),
        (1, 'Non', 6000, 'Patir non', 'media/ovqatlar/patir_non.jpg'),
        (2, 'Ko`k choy', 5000, '...', 'media/ichimliklar/kok_choy.jpg'),
        (2, 'Qora choy', 5000, '...', 'media/ichimliklar/qora_choy.jpg'),
        (2, 'Limon choy', 5000, '...', 'media/ichimliklar/limon_choy.jpg'),
        (2, 'Fanta 1,5 l', 18000, '...', 'media/ichimliklar/fanta1,5l.jpg'),
        (2, 'Fanta 1 l', 15000, '...', 'media/ichimliklar/fanta1l.jpg'),
        (2, 'Fanta 0,5 l', 10000, '...', 'media/ichimliklar/0,5fanta.jpg'),
        (2, 'Qimiz 1 l', 40000, '...', 'media/ichimliklar/qimiz.jpg'),
        (2, 'Coca-Cola 1,5 l', 18000, '...', 'media/ichimliklar/1,5cola.jpg'),
        (2, 'Coca-Cola 1 l', 15000, '...', 'media/ichimliklar/1lcola.jpg'),
        (2, 'Coca-Cola 0,5 l', 10000, '...', 'media/ichimliklar/0,5cola.jpg'),
        (2, 'Chortoq', 25000, '...', 'media/ichimliklar/chortoq075.jpg'),
        (2, 'Chortoq 0,5 l', 20000, '...', 'media/ichimliklar/chortoq0,5.jpg'),
        (2, 'Qimiz', 10000, '1 stakan', 'media/ichimliklar/qimiz.jpg'),
        (2, 'Suv 1 l', 5000, 'Gazli va Gazsiz', 'media/ichimliklar/oddiy_suv.jpg'),
        (2, 'Pepsi 1,5 l', 18000, '...', 'media/ichimliklar/pepsi1,5l.jpg'),
        (2, 'Pepsi 1 l', 15000, '...', 'media/ichimliklar/pepsi1l.jpg'),
        (2, 'Pepsi 0,5 l', 10000, '...', 'media/ichimliklar/pepsi0,5.jpg'),
        (2, 'Sok 1 l', 15000, '...', 'media/ichimliklar/sok1l.jpg'),
        (2, 'Milliy Cola 1 l', 15000, '...', 'media/ichimliklar/milliy_cola.jpg'),
        (2, 'Adrenalin', 18000, '...', 'media/ichimliklar/adrenlain.jpg'),
        (3, 'Chiroqchi', 25000, '...', 'media/salad/'),
        (3, 'Suzma', 20000, '...', 'media/salad/'),
        (3, 'Svejiy assarti', 25000, '...', 'media/salad'),
        (3, 'Achiq-chuchuk', 20000, '...', 'media/salad'),
        (3, 'Tuzlama', 25000, '...', 'media/salad'),

    ]

    cursor.executemany('''
        INSERT INTO products(category_id, product_name, price, description, image) 
        VALUES (?, ?, ?, ?, ?)
    ''', products)

    database.commit()
    database.close()


def get_all_categories():
    database = sqlite3.connect('abuzar_besh.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM categories
    ''')
    categories = cursor.fetchall()
    database.close()
    return categories


def get_products_by_category_id(category_id):
    database = sqlite3.connect('abuzar_besh.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT product_id,product_name
    FROM products WHERE category_id = ?
    ''', (category_id,))
    products = cursor.fetchall()
    database.close()
    return products

def get_product_detail(product_id):
    database = sqlite3.connect('abuzar_besh.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM products
    WHERE product_id = ?
    ''', (product_id,))
    product = cursor.fetchone()
    database.close()
    return product

# create_categories_table()
# insert_categories()
# create_products_table()
# insert_products_table()