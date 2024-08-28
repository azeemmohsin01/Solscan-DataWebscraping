# Complete Program

# Important libraries to import
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
import time
import pandas as pd


# Part of the url of Solscan website
root = 'https://solscan.io/token/26f12PmBk77wQV1TzLe8XKkNBvMFggbuypxdtMLzNLzz?page='

# Command to open an empty chrome browser
driver = webdriver.Chrome()


# Creating dictionary to store different features of the data
data = {
    'Accounts' : [],
    'Token_Accounts' : [],
    'Quantities' : [],
    'Percentages' : [],
    'Values' : []
}

# loop referring to page numbers of the actual data
for i in range(1,21):

    # adjustment of url with respect to the page 
    url = f'{root}{i}#holders'
    
    # Command to direct to the respective url of page in already opened browser
    driver.get(url)

    # time to load the page to fetch complete data 
    time.sleep(10)
    
    # fetching the details of all the serial number and is stored in the accs variable
    serials = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div[5]/div/div[1]/div/div/div/div/table/tbody/tr/td[1]')
    
    # fetching all the accounts' data vertically and is stored in the accs variable
    accs = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div[5]/div/div[1]/div/div/div/div/table/tbody/tr/td[2]')
    
    # All token accounts details are fetched here vertically
    taccs = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div[5]/div/div[1]/div/div/div/div/table/tbody/tr/td[3]')
    
    # No. of tokens available in the respective token account
    quants = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div[5]/div/div[1]/div/div/div/div/table/tbody/tr/td[4]')
    
    # percentage of zigs on solscan
    perc = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div[5]/div/div[1]/div/div/div/div/table/tbody/tr/td[5]')
    
    # usdt worth of zigs are stored here
    vals = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div[5]/div/div[1]/div/div/div/div/table/tbody/tr/td[6]')

    # running the loop till the end of the serial of each page
    for i in range(len(serials)):

        # printing the serial number
        print(serials[i].text)

        # appending the account data into the list of dict
        data['Accounts'].append(accs[i].text)

        # printing the account number with respect to serial
        print(accs[i].text)

        # appending the token accounts data into the list of dict
        data['Token_Accounts'].append(taccs[i].text)

        # printing the token account number with respect to serial 
        print(taccs[i].text)

        # appending the token accounts data into the list of dict
        data['Quantities'].append(quants[i].text)

        # printing the number of zigs in the respective account
        print(quants[i].text)

        # appending the percentage of zigs in the list of dict
        data['Percentages'].append(perc[i].text)

        # printing the percentage of zigs
        print(perc[i].text)

        # appending the usdt worth of zigs in the list of dict
        data['Values'].append(vals[i].text)


# converting all data to pandas data frames 
df = pd.DataFrame(data)

# exporting whole data frame to solscan csv file
df.to_csv('solscan.csv')