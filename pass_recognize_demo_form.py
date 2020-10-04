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
        
        # elements
        self.e_number = None 
        self.e_issued = None 
        self.e_date_issued = None 
        self.e_department_code = None 
        self.e_surname = None 
        self.e_name = None 
        self.e_second_name = None 
        self.e_sex = None 
        self.e_date_birth = None 
        self.e_place_birth = None
        
        self.build_widgets()
        
    def build_widgets(self):
        pngFileName = "pass2.png"
        # set on form
        f1 = Frame()
        f1.pack(side = 'left')
        
        b_load = Button(f1, text="Загрузить", width=10, height=1)
        b_load.pack(side = "bottom")
        b_load.config(command=self.load_image)
        """
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
        """
        self.canvas = Canvas(f1,width=300,height=400)
        #imagesprite = self.canvas.create_image(150,200,image=self.image)
        self.canvas.pack(side = "bottom")              
        
        f2 = Frame()
        f2.pack(side = 'left')
        
        # set labels and edit boxes for passport features
        l_number = Label(f2, text="Серия и номер")
        self.e_number = Entry(f2, width=30)        
        
        l_issued = Label(f2, text="Выдан")        
        self.e_issued = Entry(f2, width=30)
        
        l_date_issued = Label(f2, text="Дата выдачи")
        self.e_date_issued = Entry(f2, width=30)
        
        l_department_code = Label(f2, text="Код подразделения")
        self.e_department_code = Entry(f2, width=30)
        
        l_surname = Label(f2, text="Фамилия")
        self.e_surname = Entry(f2, width=30)
        
        l_name = Label(f2, text="Имя")
        self.e_name = Entry(f2, width=30)
        
        l_second_name = Label(f2, text="Отчество")
        self.e_second_name = Entry(f2, width=30)
        
        l_sex = Label(f2, text="Пол")
        self.e_sex = Entry(f2, width=30)
        
        l_date_birth = Label(f2, text="Дата рождения")
        self.e_date_birth = Entry(f2, width=30)
        
        l_place_birth = Label(f2, text="Место рождения")
        self.e_place_birth = Entry(f2, width=30)
        
        l_number.pack()
        self.e_number.pack()
        
        l_issued.pack()
        self.e_issued.pack()
        
        l_date_issued.pack()
        self.e_date_issued.pack()
        
        l_department_code.pack()
        self.e_department_code.pack()
        
        l_surname.pack()
        self.e_surname.pack()
        
        l_name.pack()
        self.e_name.pack()
        
        l_second_name.pack()
        self.e_second_name.pack()
        
        l_sex.pack()
        self.e_sex.pack()
        
        l_date_birth.pack()
        self.e_date_birth.pack()
        
        l_place_birth.pack()
        self.e_place_birth.pack()

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
        f_personal_data = pass_recognize.recogize(file_name)        
        data = cpp.load_passport_pattern(f_personal_data)
        # Вставляем распознанные данные в Entry
        number = data["Number"]
        self.e_number.insert(string=number[:-1],index=0)
        issued = data["Issued"]
        self.e_issued.insert(string=issued[:-1],index=0)
        date_issued = data["Date of issue"]
        self.e_date_issued.insert(string=date_issued[:-1],index=0)
        department_code = data["Department code"]
        self.e_department_code.insert(string=department_code[:-1],index=0)
        surname = data["Surname"]
        self.e_surname.insert(string=surname[:-1], index=0)
        name = data["Name"]
        self.e_name.insert(string=name[:-1], index=0)
        second_name = data["Second name"]
        self.e_second_name.insert(string=second_name[:-1], index=0)
        sex = data["Sex"]
        self.e_sex.insert(string=sex[:-1], index=0)
        date_birth = data["Date of birth"]
        self.e_date_birth.insert(string=date_birth[:-1], index=0)
        place_birth = data["Place of birth"]
        self.e_place_birth.insert(string=place_birth[:-1], index=0)


root = Tk()
window = MainWindow()
root.resizable(False, False)
root.geometry('500x480')
root.title("Passport recognizer")





root.mainloop()
