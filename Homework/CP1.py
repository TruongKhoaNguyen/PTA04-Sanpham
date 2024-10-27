class HocSinh:
    def __init__(self,_n = "",_ad = "",_h = 0.0,_w = 0.0,_edu = ""):
        self.ten = _n
        self.diachi = _ad
        self.cao = _h
        self.nang = _w
        self.hocluc = _edu
    def new_address(self,new):
        self.diachi = new
        print("Chuyển nhà đến :",new)
    def new_physic(self,nh,nw):
        self.cao = nh
        self.nang = nw
        print("Chiều cao mới :",nh," -  Cân nặng mới :",nw)
    def show(self):
        print(self.__dict__)
hs1 = HocSinh("Nguyễn Văn A","145/21 Q.4",1.62,45.5,"Tốt")
hs1.show()
hs1.new_address("123/87 Q.3")
hs1.new_physic(1.63,46.2)
hs1.show()

hs2 = HocSinh("Trần Thị B","741/12B Q.5",1.74,50.0,"Khá")
hs2.show()
hs2.new_address("985/35/2A Q.6")
hs2.new_physic(1.70,48.7)
hs2.show()