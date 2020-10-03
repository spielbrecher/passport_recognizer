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
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)
    img_erode = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations=1)
    return img_erode

# x, y, x2, y2 in percentile math scale (0.3 = 30%)
def crop_area(image, coords):
    img_width = image.shape[1]
    img_height = image.shape[0]
    coord_x = img_width * coords[0]
    coord_y = img_height * coords[1]
    coord_x2 = img_width * coords[2]
    coord_y2 = img_height * coords[3]
    cropped = image[coord_y:coord_y2, coord_x:coord_x2]
    return cropped

def crop_area_by_name(name):
    


    
# set path to tesseract.exe if not in PATH environment
pytesseract.pytesseract.tesseract_cmd = r'h:/soft/tesseract/tesseract.exe'
image_file = "pass2.png"
img = cv2.imread(image_file)
#print("shape = ",img.shape)

# grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)
img_erode = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations=1)

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

# Загружаем шаблон паспорта
pass_pattern = cpp.load_passport_pattern("passport_pattern_01")

# Первая страница паспорта

# crop Паспорт выдан
cropped = img[200:250, 300:1300]    
issued = pytesseract.image_to_string(cropped);
print("length = ",len(issued))
for i in range(len(issued)-1):
    print(issued[i])
    
# crop Дата выдачи
cropped3 = img[400:500, 240:560]    
date_of_issue = pytesseract.image_to_string(cropped3);
print("length = ",len(date_of_issue))
for i in range(len(date_of_issue)-1):
    print(date_of_issue[i])

# crop Код подразделения
print("Код подразделения")    
cropped4 = img[400:480, 800:1200] 
gray = cv2.cvtColor(cropped4, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)
cropped4 = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations=0)   
department_code = pytesseract.image_to_string(cropped4);
print("length = ",len(date_of_issue))
for i in range(len(date_of_issue)-1):
    print(date_of_issue[i])

# crop Номер паспорта
# rotate the image by 90 degrees
M = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(resized, M, (h, w))
cropped2 = rotated[150:200, 450:800]
# recognize pass number
serie_number = pytesseract.image_to_string(cropped2);
print("length = ",len(serie_number))
for i in range(len(serie_number)-1):
    print(serie_number[i])


# Вторая страница паспорта

# crop Фамилия
print("Surname")    
cropped4 = img[1120:1190, 600:1300] 
gray = cv2.cvtColor(cropped4, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)
cropped4 = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations=0)   
surname = pytesseract.image_to_string(cropped4);
print("length = ",len(surname))
for i in range(len(surname)-1):
    print(surname[i])    

# crop Имя
print("Name")    
cropped4 = img[1280:1350, 600:1300] 
gray = cv2.cvtColor(cropped4, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)
cropped4 = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations=0)   
name = pytesseract.image_to_string(cropped4);
print("length = ",len(name))
for i in range(len(name)-1):
    print(name[i])    

# crop Отчество
print("Second Name")    
cropped4 = img[1350:1430, 600:1300] 
gray = cv2.cvtColor(cropped4, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)
cropped4 = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations=0)   
second_name = pytesseract.image_to_string(cropped4);
print("length = ",len(second_name))
for i in range(len(second_name)-1):
    print(second_name[i])    

# crop Пол
print("Sex")    
cropped4 = img[1440:1500, 530:700] 
gray = cv2.cvtColor(cropped4, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)
cropped4 = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations=0)   
sex = pytesseract.image_to_string(cropped4);
print("length = ",len(sex))
for i in range(len(sex)-1):
    print(sex[i])       
    
# crop Дата рождения
print("Date of birth")    
cropped4 = img[1420:1500, 840:1200] 
gray = cv2.cvtColor(cropped4, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)
cropped4 = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations=0)   
date_of_birth = pytesseract.image_to_string(cropped4);
print("length = ",len(date_of_birth))
for i in range(len(date_of_birth)-1):
    print(date_of_birth[i])
    
# crop Место рождения
print("Place of birth")    
cropped4 = img[1520:1580, 600:1300] 
gray = cv2.cvtColor(cropped4, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)
cropped4 = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations=0)   
place_of_birth = pytesseract.image_to_string(cropped4);
print("length = ",len(place_of_birth))
for i in range(len(place_of_birth)-1):
    print(place_of_birth[i])   
    
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

with open("personal_data.json", "w") as f:
    json.dump(to_json, f)

print(to_json)
#cv2.imshow("rotated", rotated)
#cv2.imshow("Resized", resized)
cv2.imshow("Cropped", cropped4)
#cv2.imshow("Input", img)
#cv2.imshow("Enlarged", img_erode)

cv2.waitKey(0)