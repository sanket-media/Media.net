# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# submitBtn = "//button[@type='submit']"
# email = "//input[@type='email' or @name='emailAddress']"
# fname = "//input[@id='firstName']"
# lname = "//input[@id='lastName']"
# phone = "//input[@id='phoneNumber']"
# gender = ("//input[@type='radio' and @value='", "']")
# maleRadio = "//input[@type='radio' and @value='Male']"
# femaleRadio = "//input[@type='radio' and @value='female']"
# zip = "//input[@id='zipcode']"
# city = "//input[@id='cityName']"
# address = "//input[@id='address']"
# state = "//select[@id='stateCode']"
# dobm = "//select[@id='dbodatemonth']"
# dobd = "//select[@id='dbodateday']"
# doby = "//select[@id='dbodateyear']"
#
# d = webdriver.Chrome("D:\\chromedriver.exe")
# d.get("https://qa-v1.freesamplesprousa.com/?cid=qa-slug1&test=1&exp=Flow2-Duplicate-qa-v1-QA-Only")
# time.sleep(5)
#
# print(d.find_element(By.XPATH, doby).get_attribute("type"))
# print(d.find_element(By.XPATH, dobm).get_attribute("type"))
# print(d.find_element(By.XPATH, dobd).get_attribute("type"))
# print(d.find_element(By.XPATH, state).get_attribute("type"))
# print(d.find_element(By.XPATH, maleRadio).get_attribute("type"))

from leadGen.resources import xpaths as x