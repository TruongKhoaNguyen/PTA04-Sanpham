import webbrowser

class codechef():
    def __init__(self,_ln,_li,_p,_d,_lp):
        self.name = _ln
        self.link = _li
        self.problem = _p
        self.difficult = _d
        self.pro_link = _lp
    def openLesson(self):
        webbrowser.open(self.link)
    def openProblem(self):
        webbrowser.open(self.pro_link)

sheet1 = codechef("500 difficulty rating","https://www.codechef.com/practice/basic-programming-concepts","Puzzle Hunt","279","https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PUZHUNT")
#sheet1.openLesson()
sheet1.openProblem()