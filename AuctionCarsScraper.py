from selenium import webdriver
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os,time
from selenium.webdriver import Keys
import pyautogui
PATH = ".\chromedriver.exe"
# chromeOptions = Options()
# chromeOptions.add_argument("--disable-blink-features=AutomationControlled")
# chromeOptions.add_argument("load-extension=C:\Users\dhava\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.2_0")
driver = webdriver.Chrome(PATH) # ,chrome_options=chromeOptions)
listingIds = []
driver.get(f'https://foreclosureindia.com/bank-auctions/vadodara/1')
for pageNumber in range(1,20):
    url = f'https://foreclosureindia.com/bank-auctions/vadodara/{pageNumber}'
    driver.get(url)
    driver.maximize_window()
    for item in range(1,20):
        xpath = f'//*[@id="layout-content"]/div/div[3]/div/div/div[2]/table/tbody/tr[{item}]/td[3]'
        listing = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        itemTypeXpath = f'//*[@id="layout-content"]/div/div[3]/div/div/div[2]/table/tbody/tr[{item}]/td[3]'
        itemType = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, itemTypeXpath)))
        itemType = driver.find_element(By.XPATH,itemTypeXpath).get_attribute("innerHTML")
        print(itemType)
        if 'Vehicle' in itemType:
            listingIdXpath = f'//*[@id="layout-content"]/div/div[3]/div/div/div[2]/table/tbody/tr[{item}]/td[1]/h4'
            listingId = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, listingIdXpath)))
            listingId = driver.find_element(By.XPATH,listingIdXpath).get_attribute("innerHTML")
            print(listingId)
            listingIds.append(listingId)
        # nextButtonClassName = f'chevron angle right icon'
        # pyautogui.press("end")
        # nextButtonXpath = f'//*[@id="layout-content"]/div/div[3]/div/div/div[2]/table/tfoot/tr/th/div/a[9]'
        # nextButton = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, nextButtonXpath)))
        # nextButton = driver.find_element(By.XPATH, nextButtonXpath).click()
# listingIds.append(pageNumber)
print(listingIds)
f = open("./AuctionCarsVadodara.txt", "w")
f.write("")
f.close()
f = open("./AuctionCarsVadodara.txt", "a+")
for id in listingIds:
    f.write("https://foreclosureindia.com/auction/vadodara/"+str(id)+"\n")
f.close()
driver.quit()