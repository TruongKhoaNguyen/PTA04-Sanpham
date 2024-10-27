class QuanLyDiemHS:
    def __init__(self,_ht = "",_l = "",_tr = "",_dT = 0,_dV = 0,_dA = 0):
        self.hoten = _ht
        self.lop = _l
        self.truong = _tr
        self.toan = _dT
        self.van = _dV
        self.anh = _dA
    def show(self):
        print(self.__dict__)
    def average(self):
        return (self.toan + self.van + self.anh)/3
hs1 = QuanLyDiemHS("Nguyễn Thị A","Lop 7","Truong THCS A",9,8,4)
hs2 = QuanLyDiemHS("Trần Văn B","Lop 8","Truong THCS B",6,10,9)
hs3 = QuanLyDiemHS("Lý Thiên C","Lop 9","Truong THCS C",6,10,9)
max_aver = max(hs1.average(),hs2.average(),hs3.average())
lists = [hs1,hs2,hs3]
for i in range(len(lists)):
    if lists[i].average() == max_aver:
        lists[i].show()