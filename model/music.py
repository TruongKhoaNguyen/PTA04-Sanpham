import webbrowser    # HAM MO TREN MANG

class music():
    def __init__(self,_l,_n,_a,_s,_d):
        self.link = _l
        self.name = _n
        self.artist = _a
        self.stream = _s
        self.duration = _d
    def open(self):
        webbrowser.open(self.link)

# ms1 = music("https://www.youtube.com/watch?v=0tU54gOwKKs","DASH - GEOMETRY DASH 2.2","MDK","529K views","1m 35s")
# ms1.open()

# ms2 = music("https://open.spotify.com/artist/6eEYfyl229fn2DAqq0fdhl","Dash Full Version","MDK","Unknown","3m 11s")
# ms2.open()

ms3 = music("D: \TRUONG_KHOA\MIND_X_Truong_Khoa\Python_ADVANCE\Dash.mp3","Dash in GD","MDK","Unknown","3m 11s")
ms3.open()