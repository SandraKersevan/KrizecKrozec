from tkinter import *

class Krizec_krozec():
    def __init__(self,master):

        self.canvas = Canvas(master,width=300,height=300,background="white")
        self.canvas.grid(row=1,column=2,columnspan=2)
        self.canvas.create_line(100,0,100,300)
        self.canvas.create_line(200,0,200,300)
        self.canvas.create_line(0,100,300,100)
        self.canvas.create_line(0,200,300,200)

        self.koordinate = ()
        self.koordinate2 = ()
        self.na_vrsti_krizec = True
        self.canvas.bind("<Button-1>", self.obmocje)
        self.polje = 0
        self.slovar = {1: ' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

        #Meni
        menu = Menu(master)
        master.config(menu=menu)

        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        
        file_menu.add_command(label="Nova igra", command=self.nova)
        file_menu.add_command(label="Shrani", command=self.shrani)
        file_menu.add_command(label="Odpri", command=self.odpri)
        file_menu.add_separator()
        file_menu.add_command(label="Izhod", command=master.destroy)



    def odpri(self):
        ime = filedialog.askopenfilename()
        if ime == "":
            return
        with open(ime, encoding="utf8") as f:
            self.nova()
            sez = []
            for v in f:
                for i in v:
                    if i != '\n':
                        sez+=[i]
            self.polje = 1
            for k in range(0,len(sez)):
                if self.polje == 1:
                    self.koordinate = (20,20,80,80)
                    self.koordinate2 = (80,20,20,80)
                elif self.polje == 4:
                    self.koordinate = (20,120,80,180)
                    self.koordinate2 = (80,120,20,180)
                elif self.polje == 7:
                    self.koordinate = (20,220,80,280)
                    self.koordinate2 = (80,220,20,280)
                elif self.polje == 2:
                    self.koordinate = (120,20,180,80)
                    self.koordinate2 = (180,20,120,80)
                elif self.polje == 5:
                    self.koordinate = (120,120,180,180)
                    self.koordinate2 = (180,120,120,180)
                elif self.polje == 8:
                    self.koordinate = (120,220,180,280)
                    self.koordinate2 = (180,220,120,280)
                elif self.polje == 3:
                    self.koordinate = (220,20,280,80)
                    self.koordinate2 = (280,20,220,80)
                elif self.polje == 6:
                    self.koordinate = (220,120,280,180)
                    self.koordinate2 = (280,120,220,180)
                elif self.polje == 9:
                    self.koordinate = (220,220,280,280)
                    self.koordinate2 = (280,220,220,280)

                if sez[k] == 'X':
                    self.slovar[self.polje] = 'X'
                    self.krizec()
                elif sez[k] == 'O':
                    self.slovar[self.polje] = 'O'
                    self.krozec()
                self.polje += 1

                if self.zmaga() == True:
                    self.canvas.create_text(150,150,anchor=CENTER,text="Game over!",font=("ComicSans",40),fill="red")
                    self.canvas.bind("<Button-1>",self.ustavi)
                    
                

    def shrani(self):
        ime=filedialog.asksaveasfilename()
        if ime == "":
            return
        with open(ime,"wt",encoding="utf8") as f:
            print("{0}{1}{2}\n{3}{4}{5}\n{6}{7}{8}".format(
                str(self.slovar[1]),str(self.slovar[2]),str(self.slovar[3]),
                str(self.slovar[4]),str(self.slovar[5]),str(self.slovar[6]),
                str(self.slovar[7]),str(self.slovar[8]),str(self.slovar[9])),
                file=f)

                

    def nova(self):
        self.canvas.delete(ALL)
        self.canvas.create_line(100,0,100,300)
        self.canvas.create_line(200,0,200,300)
        self.canvas.create_line(0,100,300,100)
        self.canvas.create_line(0,200,300,200)
        self.slovar = {1: ' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
        self.canvas.bind("<Button-1>", self.obmocje)
        
        
    def krizec(self):
        self.canvas.create_line(self.koordinate)
        self.canvas.create_line(self.koordinate2)

        
    def krozec(self):
        self.canvas.create_oval(self.koordinate)


    def obmocje(self,event):
#1 stolpec
        if event.x < 100 and event.y < 100:
            if self.slovar[1] == ' ':
                self.polje = 1
                self.koordinate = (20,20,80,80)
                self.koordinate2 = (80,20,20,80)
                if self.na_vrsti_krizec:
                    self.slovar[self.polje] = 'X'
                else:
                    self.slovar[self.polje] = 'O'
            else: return
        elif event.x < 100 and 100 < event.y < 200:
            if self.slovar[4] == ' ':
                self.polje = 4
                self.koordinate = (20,120,80,180)
                self.koordinate2 = (80,120,20,180)
                if self.na_vrsti_krizec:
                    self.slovar[self.polje] = 'X'
                else:
                    self.slovar[self.polje] = 'O'
            else: return
        elif event.x < 100 and event.y > 200:
            if self.slovar[7] == ' ':
                self.polje = 7
                self.koordinate = (20,220,80,280)
                self.koordinate2 = (80,220,20,280)
                if self.na_vrsti_krizec:
                    self.slovar[self.polje] = 'X'
                else:
                    self.slovar[self.polje] = 'O'
            else: return

# 2 stolpec
        elif 100 < event.x < 200 and event.y < 100:
            if self.slovar[2] == ' ':
                self.polje = 2
                self.koordinate = (120,20,180,80)
                self.koordinate2 = (180,20,120,80)
                if self.na_vrsti_krizec:
                    self.slovar[self.polje] = 'X'
                else:
                    self.slovar[self.polje] = 'O'
            else: return
        elif 100 < event.x < 200 and 100 < event.y < 200:
            if self.slovar[5] == ' ':
                self.polje = 5
                self.koordinate = (120,120,180,180)
                self.koordinate2 = (180,120,120,180)
                if self.na_vrsti_krizec:
                    self.slovar[self.polje] = 'X'
                else:
                    self.slovar[self.polje] = 'O'
            else: return
        elif 100 < event.x < 200 and event.y > 200:
            if self.slovar[8] == ' ':
                self.polje = 8
                self.koordinate = (120,220,180,280)
                self.koordinate2 = (180,220,120,280)
                if self.na_vrsti_krizec:
                    self.slovar[self.polje] = 'X'
                else:
                    self.slovar[self.polje] = 'O'
            else: return

#3 stolpec    
        elif event.x > 200 and event.y < 100:
            if self.slovar[3] == ' ':
                self.polje = 3
                self.koordinate = (220,20,280,80)
                self.koordinate2 = (280,20,220,80)
                if self.na_vrsti_krizec:
                    self.slovar[self.polje] = 'X'
                else:
                    self.slovar[self.polje] = 'O'
            else: return
        elif event.x > 200  and 100 < event.y < 200:
            if self.slovar[6] == ' ':
                self.polje = 6
                self.koordinate = (220,120,280,180)
                self.koordinate2 = (280,120,220,180)
                if self.na_vrsti_krizec:
                    self.slovar[self.polje] = 'X'
                else:
                    self.slovar[self.polje] = 'O'
            else: return
        elif event.x > 200 and event.y > 200:
            if self.slovar[9] == ' ':
                self.polje = 9
                self.koordinate = (220,220,280,280)
                self.koordinate2 = (280,220,220,280)
                if self.na_vrsti_krizec:
                    self.slovar[self.polje] = 'X'
                else:
                    self.slovar[self.polje] = 'O'
            else: return
#Poseben primer:
        elif event.x == 100 or event.x == 200 or event.y == 100 or event.y == 200:
            return

        if self.na_vrsti_krizec:
            self.krizec()
            if self.zmaga() == True:
                self.na_vrsti_krizec = False
        else:
            self.krozec()
            if self.zmaga() == True:
                self.na_vrsti_krizec = True
        self.na_vrsti_krizec = not self.na_vrsti_krizec

        if self.zmaga() == True:
            self.canvas.create_text(150,150,anchor=CENTER,text="Game over!",font=("ComicSans",40),fill="red")
            self.canvas.bind("<Button-1>",self.ustavi)


    def zmaga(self):
        if self.slovar[1] == self.slovar[2] == self.slovar[3] and self.slovar[1] != ' ':
            self.canvas.create_line(20,50,280,50,fill="red",width=2)
            return True
        elif self.slovar[4] == self.slovar[5] == self.slovar[6] and self.slovar[4] != ' ':
            self.canvas.create_line(20,150,280,150,fill="red",width=2)
            return True
        elif self.slovar[7] == self.slovar[8] == self.slovar[9] and self.slovar[7] != ' ':
            self.canvas.create_line(20,250,280,250,fill="red",width=2)
            return True
        elif self.slovar[1] == self.slovar[4] == self.slovar[7] and self.slovar[1] != ' ':
            self.canvas.create_line(50,20,50,280,fill="red",width=2)
            return True
        elif self.slovar[2] == self.slovar[5] == self.slovar[8] and self.slovar[2] != ' ':
            self.canvas.create_line(150,20,150,280,fill="red",width=2)
            return True
        elif self.slovar[3] == self.slovar[6] == self.slovar[9] and self.slovar[3] != ' ':
            self.canvas.create_line(250,20,250,280,fill="red",width=2)
            return True
        elif self.slovar[1] == self.slovar[5] == self.slovar[9] and self.slovar[1] != ' ':
            self.canvas.create_line(20,20,280,280,fill="red",width=2)
            return True
        elif self.slovar[3] == self.slovar[5] == self.slovar[7] and self.slovar[3] != ' ':
            self.canvas.create_line(280,20,20,280,fill="red",width=2)
            return True


    def ustavi(self,evet):
        return "break"

    

root = Tk()
aplikacija = Krizec_krozec(root)
root.title("Križec krožec")
root.mainloop()
