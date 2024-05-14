from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import openpyxl


my_dict = {'name': [], 'email': [], 'phone': [], 'address': []}

with open('final_links.txt', 'r') as f:
    links = f.readlines()


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)


for link in links:
    driver.get(link)

    sleep(2)

    view_more_button = driver.find_element(By.XPATH, '//button[text()="View More"]')
    view_more_button.click()

    try:
        street_address = driver.find_element(By.XPATH, '//p[text()="Street Address"]/following-sibling::p')
    except:
        street_address = ''

    try:
        city = driver.find_element(By.XPATH, '//p[text()="City"]/following-sibling::p')
    except:
        city = ''

    try:
        state = driver.find_element(By.XPATH, '//p[text()="State"]/following-sibling::p')
    except:
        state = ''

    try:
        zip_code = driver.find_element(By.XPATH, '//p[text()="Zip Code"]/following-sibling::p')
    except:
        zip_code = ''

    try:
        country = driver.find_element(By.XPATH, '//p[text()="Country"]/following-sibling::p')
    except:
        country = ''

    address = f'{street_address}, {city}, {state}, {zip_code}, {country}'
    my_dict['address'].append(address)

    try:
        name = driver.find_element(By.XPATH, '//p[text()="Name"]/following-sibling::p')
        my_dict['name'].append(name)
    except:
        name = ''
        my_dict['name'].append(name)

    try:
        email = driver.find_element(By.XPATH, '//p[text()="Email"]/following-sibling::p')
        my_dict['email'].append(email)
    except:
        email = ''
        my_dict['email'].append(email)

    try:
        phone = driver.find_element(By.XPATH, '//p[text()="Primary Phone"]/following-sibling::p')
        my_dict['phone'].append(phone)
    except:
        phone = ''
        my_dict['phone'].append(phone)

df = pd.DataFrame(my_dict)
df.to_excel('the_final_result.xlsx')



