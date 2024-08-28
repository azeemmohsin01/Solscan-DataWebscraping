from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
import time
import pandas as pd

root = 'https://solscan.io/token/26f12PmBk77wQV1TzLe8XKkNBvMFggbuypxdtMLzNLzz?page='
driver = webdriver.Chrome()

data = {
    'Accounts' : [],
    'Token_Accounts' : [],
    'Quantities' : [],
    'Percentages' : [],
    'Values' : []
}

for i in range(1,21):

    url = f'{root}{i}#holders'
    
    driver.get(url)
    time.sleep(30)
    
    serials = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div[5]/div/div[1]/div/div/div/div/table/tbody/tr/td[1]')
    accs = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div[5]/div/div[1]/div/div/div/div/table/tbody/tr/td[2]')
    taccs = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div[5]/div/div[1]/div/div/div/div/table/tbody/tr/td[3]')
    quants = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div[5]/div/div[1]/div/div/div/div/table/tbody/tr/td[4]')
    perc = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div[5]/div/div[1]/div/div/div/div/table/tbody/tr/td[5]')
    vals = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div[5]/div/div[1]/div/div/div/div/table/tbody/tr/td[6]')

    for i in range(len(serials)):
        print(serials[i].text)
        data['Accounts'].append(accs[i].text)
        data['Token_Accounts'].append(taccs[i].text)
        data['Quantities'].append(quants[i].text)
        data['Percentages'].append(perc[i].text)
        data['Values'].append(vals[i].text)

df = pd.DataFrame(data)
df.to_csv('solscan.csv')