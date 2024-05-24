class thi_sinh():
    def __init__(self,name,d_toan,d_ly,d_hoa):
        self.name=name
        self.d_toan=d_toan
        self.d_ly=d_ly
        self.d_hoa=d_hoa
    def nhap_thong_tin(self):
        self.name=input("Ten thi sinh: ")
        self.d_toan=float(input("Diem cua mon toan: "))
        self.d_ly=float(input("Diem cua mon hoa:"))
        self.d_hoa=float(input("Diem cua mon hoa: "))
    def in_thong_tin(self):
        print("Ho va ten {}".format(self.name))
        print("Diem cua mon Toan {}".format(self.d_toan))
        print("Diem cua mon Ly {}".format(self.d_ly))
        print("Diem cua mon Hoa {}".format(self.d_hoa))
    def tong_diem(self):
        return self.d_toan+self.d_hoa+self.d_ly
n=int(input("Nhap so danh sach hoc sinh: "))
ds=[]
for i in range(n):
    tts=thi_sinh("",0,0,0)
    tts.nhap_thong_tin()
    ds.append(tts)
dstt=sorted(ds,key=lambda tts: tts.tong_diem(),reverse=(True))
print("Danh sach trung tuyen: ")
for tst in dstt:
    if tst.tong_diem()>=20:
        tst.in_thong_tin()
        print("Tong diem: ",tst.tong_diem())


