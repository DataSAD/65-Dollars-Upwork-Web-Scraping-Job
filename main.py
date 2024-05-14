from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import re

links = []

with open('usa_states.txt', 'r') as f:
    raw_state_list = f.readlines()

state_list = []

for state in raw_state_list:
    state_list.append(state.replace('\n', ''))


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

for state in state_list:
    driver.get('https://quada.tradewing.com/members/companies')
    sleep(2)
    search_area = driver.find_element(By.CSS_SELECTOR, 'input[type="search"]')
    search_area.send_keys(state)
    sleep(2)

    element_count_string = driver.find_element(By.CSS_SELECTOR, 'p.css-2catvg').text
    element_count = int(re.search(r'\d+', element_count_string).group())
    page_count = int(element_count / 8) + 1

    if element_count != 0:
        for i in range(page_count):
            sleep(1)
            elements = driver.find_elements(By.CSS_SELECTOR, 'a.css-1hnz6hu')

            for element in elements:
                link = element.get_attribute('href')
                links.append(link)

            if i == page_count-1:
                break

            next_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Previous Page"]')
            next_button.click()


final_links_set = set(links)
print(len(final_links_set))

with open('final_links.txt', 'w') as f:
    for item in final_links_set:
        f.write(item + '\n')




