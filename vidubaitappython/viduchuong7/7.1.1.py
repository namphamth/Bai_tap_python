from tkinter import *
# Tạo một cửa sổ chính của ứng dụng
main = tk.Tk()
# Thêm các thành phần widget vào cửa sổ
label = tk.Label(main, text="Hello World!")
label.pack()
#Thêm tiêu đề cho cửa sổ
main.title("Wellcome to Uneti!")
#Đặt kích thước cửa sổ theo pixels
main.geometry('280x60')
# Bắt đầu vòng lặp chạy ứng dụng (lặp vô tận để hiển thị cửa sổ trên màn hình máy tính) 
main.mainloop()