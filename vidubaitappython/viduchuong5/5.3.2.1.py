# code for update operation
import sqlite3
# Kết nối đến cơ sở dữ liệu, tên cơ sở dữ lệu được truyền như một tham số của connect()
conn = sqlite3.connect('mydatabase.db')
# cập nhật bản ghi nhân viên từ bảng users
conn.execute("UPDATE users SET 'Tên' = 'Nguyễn Vân Anh' where id='1'")
conn.commit()
print("Tổng số dòng được cập nhật :", conn.total_changes)
cursor = conn.execute("SELECT * FROM users")
for row in cursor:
    print(row)
# Đóng kết nối sau khi hoàn tất công việc
conn.close() 