import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import lxml
import time
import random
from pprint import pprint

# 啟動seleium, browser is chrome

# selenium設定
URL = 'https://insider.espn.com/nba/hollinger/statistics/_/page/' # page/後方加Number
# chrome_driver_path = 'C:\development\chromedriver.exe'
chrome_driver_path = 'C:\development\chromedriver119\chromedriver.exe'

# 設定使用selenium設定選項
options = webdriver.ChromeOptions()

# 讓Browser不要自動關閉
options.add_experimental_option(name='detach', value=True)

# 驅動路徑
service = ChromeService(executable_path=chrome_driver_path)
players = []
pers = []
result = []

# 啟用driver
driver = webdriver.Chrome(service=service, options=options)

try:
    for i in range(1, 9):
        driver.get(URL+f'{i}')
        soup = BeautifulSoup(driver.page_source, 'lxml')

        data = soup.select('#my-players-table > div.mod-container.mod-table.mod-no-header > div.mod-content > table tr.oddrow, tr.evenrow')

        for j in range(0, len(data)):
            tds = data[j].select('td')
            if len(tds) > 1:
                player = tds[1].getText()
                per = tds[11].getText()
                info = {f'{player}': per}
                result.append(info)

        time.sleep(random.randint(0, 5))

finally:
    driver.quit()

pprint(result)
with open('result.txt', mode='w') as file:
    json.dump(result, file)





