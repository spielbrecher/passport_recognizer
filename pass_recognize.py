# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 21:14:23 2020

@author: Andy Jagello
"""

import cv2
import numpy as np
import pytesseract
import json
import create_passport_pattern as cpp

def image_to_grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)
    img_erode = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations=1)
    return img_erode

# x, y, x2, y2 in percentile math scale (0.3 = 30%)
def crop_area(image, coords):
    img_width = image.shape[1]
    img_height = image.shape[0]
    coord_x = img_width * float(coords[0])
    coord_y = img_height * float(coords[1])
    coord_x2 = img_width * float(coords[2])
    coord_y2 = img_height * float(coords[3])
    cropped = image[int(coord_y):int(coord_y2), int(coord_x):int(coord_x2)]
    return cropped

def crop_area_by_name(name, pass_pattern, image):
    coords = pass_pattern[name]
    cropped = crop_area(image, coords)
    return cropped

def resize_image(image, percent):
    #percent by which the image is resized
    scale_percent = percent
    src = image
    #calculate the 50 percent of original dimensions
    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)
    # dsize
    dsize = (width, height)
    # resize image
    resized = cv2.resize(src, dsize)
    return resized
    
def recogize(image_file):
    img = cv2.imread(image_file)
    # Загружаем шаблон паспорта
    pass_pattern = cpp.load_passport_pattern("passport_pattern_01.json")    
    # Первая страница паспорта    
    
    # crop Паспорт выдан
    cropped = crop_area_by_name("Issued", pass_pattern, img)
    issued = pytesseract.image_to_string(cropped, lang="rus")
    #cv2.imshow("Issued", cropped)
    #print(issued[:-1])
    
    # crop Дата выдачи
    cropped = crop_area_by_name("Date of issue", pass_pattern, img)
    date_of_issue = pytesseract.image_to_string(cropped);
    #cv2.imshow("Date of issue", cropped)    
    
    # crop Код подразделения
    cropped = crop_area_by_name("Department code", pass_pattern, img)
    cropped = image_to_grayscale(cropped)
    department_code = pytesseract.image_to_string(cropped);
    #cv2.imshow("Department code", cropped)
    
    # crop Номер паспорта
    #percent by which the image is resized
    scale_percent = 50
    src = img
    #calculate the 50 percent of original dimensions
    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)
    # dsize
    dsize = (width, height)
    # resize image
    resized = cv2.resize(src, dsize)
    (h, w) = resized.shape[:2]
    center = (w / 2, h / 2)
    # rotate the image by 90 degrees
    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated = cv2.warpAffine(resized, M, (h, w))
    cropped2 = rotated[150:200, 450:800]    
    # recognize pass number
    serie_number = pytesseract.image_to_string(cropped2);
    #cropped = crop_area_by_name("Number", pass_pattern, rotated)
    #cv2.imshow("Number", cropped2)
    # recognize pass number
    #serie_number = pytesseract.image_to_string(cropped);
    
    # Вторая страница паспорта
    
    # crop Фамилия
    #print("Surname") 
    cropped = crop_area_by_name("Surname", pass_pattern, img)   
    #cropped4 = img[1120:1190, 600:1300] 
    surname = pytesseract.image_to_string(cropped, lang="rus");
    #cv2.imshow("Surname", cropped)
    #print(surname[:-1])
    
    # crop Имя
    #print("Name")    
    cropped = crop_area_by_name("Name", pass_pattern, img)
    #cropped4 = img[1280:1350, 600:1300] 
    name = pytesseract.image_to_string(cropped, lang="rus");
    #cv2.imshow("Name", cropped)
    #print(name[:-1])
    
    # crop Отчество
    #print("Second Name")   
    cropped = crop_area_by_name("Second name", pass_pattern, img)
    #cropped4 = img[1350:1430, 600:1300] 
    second_name = pytesseract.image_to_string(cropped, lang="rus");
    #cv2.imshow("Second name", cropped)
    #print(second_name[:-1])
    
    # crop Пол
    #print("Sex")   
    cropped = crop_area_by_name("Sex", pass_pattern, img)
    #cropped4 = img[1440:1500, 530:700] 
    sex = pytesseract.image_to_string(cropped, lang="rus");
    #print(sex[:-1])
    #cv2.imshow("Sex", cropped)  
      
    # crop Дата рождения
    #print("Date of birth")  
    cropped = crop_area_by_name("Date of birth", pass_pattern, img)
    #cropped4 = img[1420:1500, 840:1200] 
    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)
    cropped = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations=0)   
    date_of_birth = pytesseract.image_to_string(cropped, lang="rus");
    #cv2.imshow("Date of birth", cropped)      
    
    # crop Место рождения
    #print("Place of birth")    
    cropped = crop_area_by_name("Place of birth", pass_pattern, img)
    #cropped4 = img[1520:1580, 600:1300] 
    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)
    cropped = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations=0)   
    place_of_birth = pytesseract.image_to_string(cropped, lang="rus");
    #print(place_of_birth[:-1])
    #cv2.imshow("Date of birth", cropped)
    
    # Сохраняем распознанные данные в json
        
    to_json = {
        "Number" : serie_number[:-1],
        "Issued" : issued[:-1],
        "Date of issue" : date_of_issue[:-1],
        "Department code" : department_code[:-1],
        "Surname" : surname[:-1],
        "Name" : name[:-1],
        "Second name" : second_name[:-1],
        "Sex" : sex[:-1],
        "Date of birth" : date_of_birth[:-1],
        "Place of birth" : place_of_birth[:-1]
        }
    f_personal_data = "personal_data.json"
    with open(f_personal_data, "w") as f:
        json.dump(to_json, f)
    return f_personal_data
    
# set path to tesseract.exe if not in PATH environment
pytesseract.pytesseract.tesseract_cmd = r'h:/soft/tesseract/tesseract.exe'
#image_file = "pass2.png"


#cv2.imshow("rotated", rotated)
#cv2.imshow("Resized", resized)
#cv2.imshow("Cropped", cropped4)
#cv2.imshow("Input", img)
#cv2.imshow("Enlarged", img_erode)


#cv2.waitKey(0)