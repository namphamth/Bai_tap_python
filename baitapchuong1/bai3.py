class Phan_So():
    def __init__(self,tu,mau):
        self.tu=tu
        self.mau=mau
    def nhap_phanso(self):
        self.tu=float(input("Tu so cua phan so: "))
        self.mau=float(input("Mau so cua phan so: "))
    def in_phanso(self):
        print("Phan so vua nhap la: ",self.tu,"/",self.mau)
ps=Phan_So(0,0)
ps.nhap_phanso()
if ps.mau==0:
    print("Phan so khong hop le")
else:
    ps.in_phanso()