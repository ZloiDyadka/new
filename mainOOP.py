from tkinter import *
import PIL.Image, PIL.ImageTk
import sqlite3 as lite
root=Tk()
root.title('Культурные загадки')
root.geometry('1350x768+0+0')
class main_menu():
    def __init__(self):
        '''Картинки'''
        fn0="fon.png"
        fn1="Play.png"
        fn2="Setting.png"
        fn3="Quit.png"
        fn4="4.png"
        #########
        '''Подготовка картинок'''
        self.src_img=PIL.Image.open(fn0)
        self.img0=PIL.ImageTk.PhotoImage(self.src_img)
        ###
        self.src_img1=PIL.Image.open(fn1)
        self.img1=PIL.ImageTk.PhotoImage(self.src_img1)
        ###
        self.src_img2=PIL.Image.open(fn2)
        self.img2=PIL.ImageTk.PhotoImage(self.src_img2)
        ###
        self.src_img3=PIL.Image.open(fn3)
        self.img3=PIL.ImageTk.PhotoImage(self.src_img3)
        ###
        self.src_img4=PIL.Image.open(fn4)
        self.img4=PIL.ImageTk.PhotoImage(self.src_img4)
        ###
        '''создаем холст и на нем размещаем картинку с фоном'''
        self.canvas1=Canvas(root, width=1360, height=765)
        self.canvas1.create_image(100,20,image=self.img0,anchor="center")
        self.canvas1.pack()
        '''создаем рамку'''
        self.f1=Frame(root)
        self.f1.place(x=510,y=30,height = 700, width = 400)
        '''создаем холст и на нем размещаем картинку с фоном рамки'''
        self.canvas2=Canvas(self.f1, width=400, height=700)
        self.canvas2.create_image(0,0,image=self.img4,anchor="center")
        self.canvas2.pack()
        '''размещаем кнопки на рамке'''
        self.b1=Button(self.f1,image=self.img1, command=self.mod_win)
        self.b1.place(x=50,y=40,width=300,height=90)
        #self.b1.bind("<Button-1>",game_menu_1.game_window())
        
        self.b2=Button(self.f1,image=self.img2)
        self.b2.place(x=50,y=300,width=300,height=90)
        
        self.b3=Button(self.f1,image=self.img3, command=root.destroy)
        self.b3.place(x=50,y=550,width=300,height=90)
    def mod_win(self):
        
        wdw=Toplevel()
        wdw.geometry('1300x750+0+0')
        connect_db=lite.connect('the_question')
        cursor_db=connect_db.cursor()
        self.pic=[]
        self.que=[]
        self.ans=[]
        self.numb=1
        self.text=StringVar()
        self.text1=StringVar()
        #############
        for i in range(0,6):
            '''извлечь картинку, вопрос, ответ'''
            self.pre_blowout_picture=cursor_db.execute('select image from images where id_image=?', str(i))
            self.blowout_picture=str(self.pre_blowout_picture.fetchone())
            self.blowout_picture=self.blowout_picture[2:-3]
            self.pic.append(self.blowout_picture)

            self.pre_blowout_question=cursor_db.execute('select question from questions where id_question=?', str(i))
            self.blowout_question=str(self.pre_blowout_question.fetchone())
            self.blowout_question=self.blowout_question[2:-3]
            self.que.append(self.blowout_question)

            self.pre_blowout_answer=cursor_db.execute('select answer from answer where id_answers=?', str(i))
            self.blowout_answer=str(self.pre_blowout_answer.fetchone())
            self.blowout_answer=self.blowout_answer[2:-3]
            self.ans.append(self.blowout_answer)
        #############
           
        self.image=PIL.Image.open(self.pic[self.numb])
        self.image_=PIL.ImageTk.PhotoImage(self.image)
        
        
        self.var1=IntVar()
        self.var1.set(0)
        
        self.canva=Canvas(wdw, width=480, height=480)
        self.canva.pack()
       
        self.img=self.canva.create_image(270, 250, image=self.image_)
          
        self.label1=Label(wdw, textvariable=self.text, font='Arial 15', bg='red').place(x=530, y=490, height=30, width=310)
        self.text.set(str(self.que[self.numb]))
        self.text1.set(str(self.ans[self.numb]))
        ####################
        self.rb1=Radiobutton(wdw, textvariable=self.text1, variable=self.var1, value=0, bg='yellow', font='Arial 15').place(x=350, y=540, height=60, width=220)
        self.rb2=Radiobutton(wdw, text='Франсиско Гойя', variable=self.var1, value=1, bg='yellow', font='Arial 15').place(x=800, y=540, height=60, width=220)
        self.rb3=Radiobutton(wdw, text='Донатело', variable=self.var1, value=2, bg='yellow', font='Arial 15').place(x=350, y=630, height=60, width=220)
        self.rb4=Radiobutton(wdw, text='Рафаэль', variable=self.var1, value=3, bg='yellow', font='Arial 15').place(x=800, y=630, height=60, width=220)
        ####################
        self.b1=Button(wdw, text='Ответить', bg='blue', font='Arial 15')
        self.b1.place(x=610, y=540, height=150, width=150)
        self.b1.bind("<Button-1>",self.otvet)
        ####################
        self.b2=Button(wdw,text='NEXT', bg='green', font='Arial 17')
        self.b2.bind("<Button-1>", lambda event: self.e(event, self.img))
        self.b2.place(x=1100, y=540, height=150, width=150)
    def otvet(self, event):
        ''' изменить текст кнопки'''
        self.v=self.var1.get()
        if self.v==0:
            self.b1['text']='верно'
            self.b1['bg']='green'

        elif self.v==1:
            self.b1['text']='неверно'
            self.b1['bg']='red'

        elif self.v==2:
            self.b1['text']='неверно'
            self.b1['bg']='red'

        elif self.v==3:
            self.b1['text']='неверно'
            self.b1['bg']='red'
    def e(self, event, img):
        '''извлечь номер вопроса из списка вопросов '''
        global image_
        self.numb+=1
        self.canva.delete(self.img)
        self.image=PIL.Image.open(self.pic[self.numb])
        self.image_=PIL.ImageTk.PhotoImage(self.image)
        self.img=self.canva.create_image(270, 250, image=self.image_)
        self.text.set(str(self.que[self.numb]))
        self.text1.set(str(self.ans[self.numb]))
        self.b1['text']='Ответить'
        self.b1['bg']='blue'
        root.update()
a=main_menu()
root.mainloop()

