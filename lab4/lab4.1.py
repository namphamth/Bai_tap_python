import sqlite3
#Tạo Cơ Sở Dữ Liệu và Bảng Sản Phẩm: Khởi tạo CSDL product.db và tạo bảng product có nội dung sau
def create_database_and_table():
    
    path = '/Users/nguyenxuanty/Documents/Baitappython/product.db'
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS product (
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL
        PRICE REAL NOT NULL
        Amount INTEGER NOT NULL
    );
    """
    cursor.execute(create_table_query)
    conn.comit()
    conn.close()
    print('Cơ sở dữ liệu đã tạo thành công')