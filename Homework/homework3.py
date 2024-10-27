class BankAccount:
    def __init__(self,_tnh = "",_tctk = "",_stk = "",_stttk = 0):
        self.tenNH = _tnh
        self.tenchuTK = _tctk
        self.soTK = _stk
        self.sotientrongTK = _stttk
    def ruttien(self,r):
        self.sotientrongTK -= r
        print("Rút :",r)
    def naptien(self,n):
        self.sotientrongTK += n
        print("Nạp :",n)
    def show(self):
        print(self.__dict__)
myaccount = BankAccount("Sacombank","Khoa","012345XXXX",80000000)
print("Tài khoản của bạn :")
myaccount.show()
myaccount.ruttien(10000000)
myaccount.naptien(5000000)
print("Tài khoản của bạn :")
myaccount.show()