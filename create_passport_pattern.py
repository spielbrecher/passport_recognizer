# -*- coding: utf-8 -*-
"""
Create passport pattern in json

Created on Sat Oct  3 18:29:24 2020

@author: Andy Jagello
"""

import json

to_json = {
    "Number" : (0.31, 0.07, 0.55, 0.01),
    "Issued" : (0.21, 0.10,	0.90, 0.12),
    "Date of issue" : (0.17, 0.20, 0.39, 0.25),
    "Department code" : (0.55, 0.20, 0.83, 0.24),
    "Surname" : (0.41, 0.55, 0.90, 0.58),
    "Name" : (0.41, 0.63, 0.90, 0.67),
    "Second name" : (0.41, 0.66, 0.90, 0.70),
    "Sex" : (0.37, 0.71, 0.48, 0.74),
    "Date of birth" : (0.58, 0.70, 0.83, 0.74),
    "Place of birth" : (0.41, 0.75, 0.90, 0.78)
    }

with open("passport_pattern_01.json", "w") as f:
    json.dump(to_json, f)

def load_passport_pattern(path):
    passport_pattern = json.load(open(path))
    return passport_pattern
