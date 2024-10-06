class car:
    def __init__(self,_hx = "Unname",_chn = "Unknown",_ms = "Unknown"):
        self.hangxe = _hx
        self.sochongoi = _chn
        self.mausac = _ms
    def show(self):
        print(self.__dict__)

xe1 = car()
xe1.show()

xe2 = car("Vinfast")
xe2.show()

xe3 = car("Vinfast",2)
xe3.show()

xe4 = car("Vinfast",2,"trang")
xe4.show()

exit()
# My baitap
class employee:
    def __init__(self,_n = "Unknown",_a = "Unknown",_m = "Unknown",_p = "Unknown"):
        self.ten = _n
        self.tuoi = _a
        self.luong = _m
        self.vitricongviec = _p
    def show(self):
        print(self.__dict__)

nhanvien1 = employee()
nhanvien1.show("Nguyen Van A",25,"5 trieu dong","Dong Nai")

nhanvien1 = employee()
nhanvien1.show("Tran Thi B",21,"3 trieu dong","Binh Duong")

#nhanvien3 ...