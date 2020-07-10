

import os
import time
import shutil
from tkinter import *
from tkinter import messagebox


def mus():
    ver = 'v0.4.0 beta'
    return ver


def save_():

    
    def return_():
        save.withdraw()


    def na():
        name = n.get()
        py = p.get()
        speed = s.get()
        level = lv.get()
        lvl = ll.get()
        track = tr.get()
        mr = int(m.get())
        pure = int(pu.get())
        late = int(la.get())
        early = int(ea.get())
        lp = int(lap.get())
        ep = int(eap.get())
        lost = int(lo.get())
        far = late + early
        score = int((pure + far / 2) / (pure + far + lost) * 10000000 + pure - lp - ep)
        if score > 9900000:
            exx = 'EX+'
        else:
            if score > 9800000:
                exx = 'EX'
            else:
                if score > 9500000:
                    exx = 'AA'
                else:
                    if score > 9200000:
                        exx = 'A'
                    else:
                        if score > 8900000:
                            exx = 'B'
                        else:
                            if score > 8600000:
                                exx = 'C'
                            else:
                                exx = 'D'
        arc = {'標題':name,
               '日期':time.strftime('%Y/%m/%d'),
               '時間':time.strftime('%X'),
               '偏移率':py,
               '速度':speed,
               '難度':level,
               'LVL':lvl,
               '評級':exx,
               '評分':score,
               '通關狀態':track,
               'MAX RECALL':mr,
               'PURE':pure,
               'FAR':far,
               'LOST':lost,
               'LATE':late,
               'EARLY':early,
               'LATE PURE':lp,
               'EARLY PURE':ep}
        re = open('music/arcaea.arc','a')
        for x,y in arc.items():
            if x == '標題':
                name = x + ": " + y
            if x == '日期':
                date = x + ": " + y
            if x == '時間':
                time_ = x + ": " + y
            if x == '偏移率':
                py = x + ": " + y
            if x == '速度':
                speed = x + ": " + y
            if x == '難度':
                x_level = x
                y_level = y
            if x == 'LVL':
                y_lvl = y
            if x == '評級':
                exx = x + ": " + y
            if x == '評分':
                score = x + ": " + str(y)
            if x == '通關狀態':
                track = x + ": " + y
            if x == 'MAX RECALL':
                mr = x + ": " + str(y)
            if x == 'PURE':
                pure = x + ": " + str(y)
            if x == 'FAR':
                far = x + ": " + str(y)
            if x == 'LOST':
                lost = x + ": " + str(y)
            if x == 'LATE':
                late = x + ": " + str(y)
            if x == 'EARLY':
                early = x + ": " + str(y)
            if x == 'LATE PURE':
                lp = x + ": " + str(y)
            if x == 'EARLY PURE':
                ep = x + ": " + str(y)
        level = x_level + ": " + y_level + " " + y_lvl
        for i in [name,date,time_,py,speed,level,exx,score,track,mr,pure,far,lost,late,early,lp,ep,""]:
            re.write(i + "\n")
        re.close()
        return_()

    
    save = Toplevel(ttk)
    save.title("Arcaea")
    Label(save,text = "v0.4.0").grid()
    Label(save,text = "標題").grid()
    Label(save,text = "偏移率").grid()
    Label(save,text = "速度").grid()
    Label(save,text = "難度").grid()
    Label(save,text = "通關狀態").grid()
    Label(save,text = "MAX RECALL").grid()
    Label(save,text = "PURE").grid()
    Label(save,text = "LATE").grid()
    Label(save,text = "EARLY").grid()
    Label(save,text = "LATE PURE").grid()
    Label(save,text = "EARLY PURE").grid()
    Label(save,text = "LOST").grid()
    n = Entry(save)
    p = Entry(save)
    s = Spinbox(save,from_ = 1,to = 6.5,increment = 0.1)
    lv = StringVar()
    lv.set("")
    l = OptionMenu(save,lv,"Beyond","Future","Present","Past")
    ll = StringVar()
    ll.set("")
    le = OptionMenu(save,ll,"11","10+","10","9+","9","8","7","6","5","4","3","2","1")
    tr = StringVar()
    tr.set("")
    t = OptionMenu(save,tr,"PURE MEMORY","FULL RECALL","TRACK COMPLETE","TRACK LOST")
    m = Entry(save)
    pu = Entry(save)
    la = Entry(save)
    ea = Entry(save)
    lap = Entry(save)
    eap = Entry(save)
    lo = Entry(save)
    p.insert(0,"0")
    n.grid(row = 1,column = 1)
    p.grid(row = 2,column = 1)
    s.grid(row = 3,column = 1)
    l.grid(row = 4,column = 1)
    le.grid(row = 4,column = 2)
    t.grid(row = 5,column = 1)
    m.grid(row = 6,column = 1)
    pu.grid(row = 7,column = 1)
    la.grid(row = 8,column = 1)
    ea.grid(row = 9,column = 1)
    lap.grid(row = 10,column = 1)
    eap.grid(row = 11,column = 1)
    lo.grid(row = 12,column = 1)
    Button(save,text = "確定",command = na).grid()
    Button(save,text = "返回",command = return_).grid(row = 13,column = 1)
	

def load():
    if not os.path.exists('music/arcaea.arc'):
        messagebox.showerror(os.path.abspath("MusicGame.py"),"暫無遊玩記錄")
    else:
        look = Toplevel(ttk)
        look.title("Read")
        bar = Scrollbar(look)
        bar.grid(row = 0,column = 1,sticky = 'n' + 's')
        re = open('music/arcaea.arc')
        rea = re.read()
        re.close()
        re = Text(look,yscrollcommand = bar.set)
        re.insert("end",rea)
        re.configure(state = "disabled")
        re.grid(row = 0)
        bar.config(command = re.yview)


def del_():
    shutil.rmtree("music")
    ttk.quit()


if not os.path.exists('music'):
    os.makedirs('music')


ttk = Tk()
ttk.title("MusicGame")


music = Frame(ttk)
music.grid()
version = Label(music,text = mus()).grid()
arcaea = Button(music,text = "arcaea",command = save_,width = 6).grid()
read = Button(music,text = "read",command = load,width = 6).grid()
delete = Button(music,text = "del",command = del_,width = 6).grid()
ttk.mainloop()

