import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

os.environ['PATH'] += r"C:/Users/azb/Downloads/Compressed/hromedriver_win"
driver = webdriver.Chrome(options=options)

driver.get('https://www.marshu.com/articles/calculate-addition-calculator-add-two-numbers.php')
driver.implicitly_wait(5)

try:
    no_button = driver.find_element(By.CLASS_NAME, 'at-cm-no-button')
    no_button.click()
except:
    print('No element with this class name. Skipping ....')

sum1 = driver.find_element(By.NAME, 'n01')
sum2 = driver.find_element(By.NAME, 'n02')

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(15)

btn = driver.find_element(By.CSS_SELECTOR, "input[onclick='findcalculatorcalculate(this.form)']")
btn.click()



