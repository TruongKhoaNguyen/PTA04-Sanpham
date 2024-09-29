class person:
    # ham khoi tao mot doi tuong
    def __init__(self,_cP,_aP,fn,nn,bt,rl,ed):
        self.coverPicture = _cP
        self.avatarPicture = _aP
        self.fullname = fn
        self.nickname = nn
        self.birthday = bt
        self.relationship = rl
        self.education = ed
    # ham in ra thong tin cua nguoi do
    def show(self):
        print(self.__dict__)
    # Save
    def SaveData(self):
        with open("my_person.txt","w") as file:
            dat = ""
            dat += self.coverPicture + ","
            dat += self.avatarPicture + ","
            dat += self.fullname + ","
            dat += self.nickname + ","
            dat += self.birthday + ","
            dat += self.relationship + ","
            dat += self.education
            # Write
            file.write(dat)
    # Load
    def LoadData(self):
        with open("my_person.txt","r") as file:
            dat = str(file.readlines())
            self.coverPicture,self.avatarPicture,self.fullname,self.nickname,self.birthday,self.relationship,self.education = dat.split(",")

ps1 = person("null","null","Doraemon","Nobita","99/99/9999","Unkhown","Peashooter")
ps1.LoadData()
ps1.show()
#ps1.SaveData()