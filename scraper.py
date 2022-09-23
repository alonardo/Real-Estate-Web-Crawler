from re import A
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl
from selenium.webdriver.common.by import By
import pandas as pd

book = openpyxl.load_workbook(r'C:\Users\aalon\OneDrive\Desktop\python\crawler\targets.xlsx')
sheet = book.active
v12 = sheet['V12']
v13 = sheet['V13']
x = v12.value


PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://www.loopnet.com/")
print(driver.title)


for row in range(1, sheet.max_row + 1):
    property = sheet.cell(row=row+1, column=22).value
    # property = property + ' utah'

    search = driver.find_element('name', 'geography')
    search.send_keys(property)
    time.sleep(4)
    search.send_keys(Keys.RETURN)
    search.submit
    try:
        # This checks to see if the property is on the market
        content = driver.find_element(By.CSS_SELECTOR, 'p.nearby-results__text strong')
        results = content.text
        print(property + '*******' + results)

    except:
        print('Property found!')
        content = driver.find_element(By.CSS_SELECTOR, '.ldp-header .ln-logo').click()
        
    finally:
        # This clicks the logo to return to search field
        content = driver.find_element(By.CSS_SELECTOR, '.main-header .logo').click()

    


