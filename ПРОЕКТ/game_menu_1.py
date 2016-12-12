from tkinter import *
import PIL.Image, PIL.ImageTk, mainOOP
import sqlite3 as lite


### инициализация Tk ###

root=Tk()
root.geometry('1350x768+0+0')

class game_window():
    def __init__(self):
    
        connect_db=lite.connect('the_question')
        cursor_db=connect_db.cursor()
        self.pic=[]
        self.que=[]
        self.ans=[]
        self.numb=0
        self.text=StringVar()
        self.text1=StringVar()
        #############
        for i in range(0,10):
            '''извлечь картинку, вопрос, ответ'''
            self.pre_blowout_picture=cursor_db.execute('select picture from easy where id=?', str(i))
            self.blowout_picture=str(self.pre_blowout_picture.fetchone())
            self.blowout_picture=self.blowout_picture[2:-3]
            self.pic.append(self.blowout_picture)

            self.pre_blowout_question=cursor_db.execute('select question from easy where id=?', str(i))
            self.blowout_question=str(self.pre_blowout_question.fetchone())
            self.blowout_question=self.blowout_question[2:-3]
            self.que.append(self.blowout_question)

            self.pre_blowout_answer=cursor_db.execute('select answer from easy where id=?', str(i))
            self.blowout_answer=str(self.pre_blowout_answer.fetchone())
            self.blowout_answer=self.blowout_answer[2:-3]
            self.ans.append(self.blowout_answer)
        #############    
        self.image=PIL.Image.open(self.pic[self.numb])
        self.image_=PIL.ImageTk.PhotoImage(self.image)

        
        self.var1=IntVar()
        self.var1.set(0)

        self.canva=Canvas(root, width=480, height=480)
        self.canva.pack()

        self.img=self.canva.create_image(270, 250, image=self.image_)
          
        self.label1=Label(root, textvariable=self.text, font='Arial 15', bg='red').place(x=530, y=490, height=30, width=310)
        self.text.set(str(self.que[self.numb]))
        self.text1.set(str(self.ans[self.numb]))
        ####################
        self.rb1=Radiobutton(root, textvariable=self.text1, variable=self.var1, value=0, bg='blue', font='Arial 15').place(x=350, y=540, height=60, width=220)
        self.rb2=Radiobutton(root, text='вариант ответа 2', variable=self.var1, value=1, bg='blue', font='Arial 15').place(x=800, y=540, height=60, width=220)
        self.rb3=Radiobutton(root, text='вариант ответа 3', variable=self.var1, value=2, bg='blue', font='Arial 15').place(x=350, y=630, height=60, width=220)
        self.rb4=Radiobutton(root, text='вариант ответа 4', variable=self.var1, value=3, bg='blue', font='Arial 15').place(x=800, y=630, height=60, width=220)
        ####################
        self.b1=Button(root, text='Ответить', bg='blue', font='Arial 15')
        self.b1.place(x=610, y=540, height=150, width=150)
        self.b1.bind("<Button-1>",self.otvet)
        ####################
        self.b2=Button(root,text='NEXT', bg='green', font='Arial 17')
        self.b2.bind("<Button-1>", lambda event: self.e(event, self.img))
        self.b2.place(x=1100, y=540, height=150, width=150)
    ###
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

    ###   
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
#############################################################        
  

'''connect_db.commit()
cursor_db.close()
connect_db.close()'''
root.mainloop()



