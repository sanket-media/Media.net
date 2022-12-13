import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from leadGen.resources import contants as c
from selenium.webdriver.support import expected_conditions as ex

user = {
    "email": "phamanathon@gmail.com",
    "fname": "Anathon",
    "lname": "Pham",
    "zip": 89414,
    "gender": "Male",
    "address": "Access Road",
    "city": "Golconda",
    "state": "NV",
    "phone": 5048316700,
    "country": "USA",
    "doby": "2000",
    "dobm": "11",
    "dobd": "18"
}

d = webdriver.Chrome('D:\\chromedriver.exe')
wait = WebDriverWait(d, 10)
d.get('https://freesamplesprousa.com/?cid=vn1ws&test=1')

wait.until(ex.visibility_of_element_located((By.XPATH, "//input[@type='email' or @name='emailAddress']")))


mailBox = d.find_element(By.XPATH, c.pii['email'])
mailBox.send_keys(user['email'])
d.find_element(By.XPATH, c.submitBtn).click()
time.sleep(5)
d.find_element(By.XPATH, c.pii['fname']).clear()
d.find_element(By.XPATH, c.pii['fname']).send_keys(user["fname"])
d.find_element(By.XPATH, c.pii['lname']).clear()
d.find_element(By.XPATH, c.pii['lname']).send_keys(user["lname"])
d.find_element(By.XPATH, c.pii['zip']).clear()
d.find_element(By.XPATH, c.pii['zip']).send_keys(user["zip"])
wait.until(
    ex.visibility_of_element_located((By.XPATH, "//input[@id='zipcode' and @class='validated']")))
d.find_element(By.XPATH, c.pii['maleRadio']).click()
d.find_element(By.XPATH, c.submitBtn).click()

# pii2
wait.until(ex.visibility_of_element_located((By.XPATH, c.submitBtn)))
state = Select(d.find_element(By.XPATH, c.pii['state']))
state.select_by_value("NV")
d.find_element(By.XPATH, c.pii['address']).clear()
d.find_element(By.XPATH, c.pii['address']).send_keys(user["street"])
d.find_element(By.XPATH, c.pii['city']).clear()
d.find_element(By.XPATH, c.pii['city']).send_keys(user["city"])
d.find_element(By.XPATH, c.pii['phone']).send_keys(user["mob"])
d.find_element(By.XPATH, c.submitBtn).click()

# pii3
wait.until(ex.visibility_of_element_located((By.XPATH, c.psubmit)))
Select(d.find_element(By.XPATH, c.dobm)).select_by_value(user["dobm"])
Select(d.find_element(By.XPATH, c.dobd)).select_by_value(user["dobd"])
Select(d.find_element(By.XPATH, c.doby)).select_by_value(user["doby"])
d.find_element(By.XPATH, c.psubmit).click()
