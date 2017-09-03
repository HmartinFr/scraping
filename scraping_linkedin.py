from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver.common.action_chains import ActionChains
import gspread
import pandas as pd
import time as time
import datetime
import random as random


import re
def remwithre(text, there=re.compile(re.escape('\n')+'.*')):
    return there.sub('', text)


def get_info(Nom):
    driver = webdriver.Chrome("C:/Users/NEL14886/Desktop/GH Linkedin/chromedriver.exe")
    driver.get("https://www.google.com/")
    cherche = driver.find_element_by_class_name("gsfi")
    cherche.send_keys("linkedin"+Nom)
    cherche.send_keys(Keys.ENTER)
    el =driver.find_elements_by_class_name("s")
    for i in el:
        if "linkedin" in i.text:
            if "-" in i.text:
                print(remwithre(i.text.replace(remwithre(i.text)+"\n",""))) 
    driver.close()