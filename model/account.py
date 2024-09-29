class account:
    # ham khoi tao mot doi tuong
    def __init__(self,_user = "gmail.com" ,_pass = "XXXXX"):
        self.username = _user
        self.password = _pass
        self.LoadData()
    # ham in ra thong tin cua nguoi do
    def show(self):
        print(self.__dict__)
    # Save
    def SaveData(self):
        with open("DAT/account.txt","w") as file:
            dat = ""
            dat += self.username + ","
            dat += self.password
            # Write
            file.write(dat)
    # Load
    def LoadData(self):
        with open("DAT/account.txt","r") as file:
            dat = str(file.readline())
            self.username,self.password = dat.split(",")
    def RenamePass(self,new_P):
        self.password = new_P
        self.SaveData()
    def Checking(self,_user,_pass):
        if _user == self.username and _pass == self.password:
            print("Succeed !")
        else:
            print("Denied !")

ac1 = account()
ac1.show()
ac1.RenamePass("20336")
ac1.Checking("gmail.com","20336")