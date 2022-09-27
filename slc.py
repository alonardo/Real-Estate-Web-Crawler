from re import A
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://slco.org/assessor/new/ParcelViewer/")
print(driver.title)

testing = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.CSS_SELECTOR, '.jimu-widget-splash .footer .jimu-btn'))
).click()

search = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.CSS_SELECTOR, '.jimu-widget-attributetable-switch.close'))
).click()


