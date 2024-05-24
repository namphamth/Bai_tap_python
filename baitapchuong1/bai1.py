class hinhchunnhat:
    def __init__(self,dai,rong):
        self.dai=dai
        self.rong=rong
    def nhap(self):
        self.dai=int(input("Chieu dai: "))
        self.rong=int(input("Chieu rong: "))
    def chuvi(self):
        return str((self.dai+self.rong)*2)
    def dientich(self):
        return str(self.dai*self.rong)
    def thongtin(self):
        print("Chieu dai cua hinh chu nhat la: {}".format(self.dai))
        print("Chieu rong cua hinh chu nhat la: {}".format(self.rong))
        print("Chu vi hinh chu nhat la: {}".format(self.chuvi()))
        print("Dien tich hinh chu nhat la {}".format(self.dientich()))


chunhat=hinhchunnhat(dai, rong)(0,0)
chunhat.nhap()
chunhat.thongtin()
        
        