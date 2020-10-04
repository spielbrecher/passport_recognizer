# -*- coding: utf-8 -*-
"""
Just a simple form to demonstrate
Created on Sat Oct  3 23:53:03 2020

@author: Andy Jagello
"""

from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import pass_recognize
import create_passport_pattern as cpp

class MainWindow():
    def __init__(self):
        self.canvas = None
        self.b_load = None
        self.image = None 
        self.build_widgets()
        
    def build_widgets(self):
        pngFileName = "pass2.png"
        data = cpp.load_passport_pattern("personal_data.json")
        # set on form
        f1 = Frame()
        f1.pack(side = 'left')
        
        b_load = Button(f1, text="Загрузить", width=10, height=1)
        b_load.pack(side = "bottom")
        b_load.config(command=self.load_image)
        
        # open image from file
        pilImage = Image.open(pngFileName)
        scale_percent = 20
        src = pilImage
        #calculate the 50 percent of original dimensions
        width = int(src.width * scale_percent / 100)
        height = int(src.height * scale_percent / 100)
        # dsize
        dsize = (width, height)
        pilImage = pilImage.resize(dsize)
        self.image = ImageTk.PhotoImage(pilImage)
        self.canvas = Canvas(f1,width=300,height=400)
        imagesprite = self.canvas.create_image(150,200,image=self.image)
        self.canvas.pack(side = "bottom")              
        
        f2 = Frame()
        f2.pack(side = 'left')
        
        # set labels and edit boxes for passport features
        l_number = Label(f2, text="Серия и номер")
        e_number = Entry(f2, width=30)
        number = data["Number"]
        e_number.insert(string=number[:-1],index=0)
        
        l_issued = Label(f2, text="Выдан")        
        e_issued = Entry(f2, width=30)
        issued = data["Issued"]
        e_issued.insert(string=issued[:-1],index=0)
        
        
        l_date_issued = Label(f2, text="Дата выдачи")
        e_date_issued = Entry(f2, width=30)
        date_issued = data["Date of issue"]
        e_date_issued.insert(string=date_issued[:-1],index=0)
        
        l_department_code = Label(f2, text="Код подразделения")
        e_department_code = Entry(f2, width=30)
        department_code = data["Department code"]
        e_department_code.insert(string=department_code[:-1],index=0)
        
        l_surname = Label(f2, text="Фамилия")
        e_surname = Entry(f2, width=30)
        surname = data["Surname"]
        e_surname.insert(string=surname[:-1], index=0)
        
        l_name = Label(f2, text="Имя")
        e_name = Entry(f2, width=30)
        name = data["Name"]
        e_name.insert(string=name[:-1], index=0)
        
        l_second_name = Label(f2, text="Отчество")
        e_second_name = Entry(f2, width=30)
        second_name = data["Second name"]
        e_second_name.insert(string=second_name[:-1], index=0)
        
        l_sex = Label(f2, text="Пол")
        e_sex = Entry(f2, width=30)
        sex = data["Sex"]
        e_sex.insert(string=sex[:-1], index=0)
        
        l_date_birth = Label(f2, text="Дата рождения")
        e_date_birth = Entry(f2, width=30)
        date_birth = data["Date of birth"]
        e_date_birth.insert(string=date_birth[:-1], index=0)
        
        l_place_birth = Label(f2, text="Место рождения")
        e_place_birth = Entry(f2, width=30)
        place_birth = data["Place of birth"]
        e_place_birth.insert(string=place_birth[:-1], index=0)
        
        l_number.pack()
        e_number.pack()
        
        l_issued.pack()
        e_issued.pack()
        
        l_date_issued.pack()
        e_date_issued.pack()
        
        l_department_code.pack()
        e_department_code.pack()
        
        l_surname.pack()
        e_surname.pack()
        
        l_name.pack()
        e_name.pack()
        
        l_second_name.pack()
        e_second_name.pack()
        
        l_sex.pack()
        e_sex.pack()
        
        l_date_birth.pack()
        e_date_birth.pack()
        
        l_place_birth.pack()
        e_place_birth.pack()

    def load_image(self):
        file_name = askopenfilename()
        pilImage = Image.open(file_name)
        scale_percent = 20
        src = pilImage
        #calculate the 50 percent of original dimensions
        width = int(src.width * scale_percent / 100)
        height = int(src.height * scale_percent / 100)
        # dsize
        dsize = (width, height)
        pilImage = pilImage.resize(dsize)
        self.image = ImageTk.PhotoImage(pilImage)        
        self.canvas.create_image(150,200,image=self.image)
        # recognize
        


root = Tk()
window = MainWindow()
root.resizable(False, False)
root.geometry('500x480')
root.title("Passport recognizer")





root.mainloop()
