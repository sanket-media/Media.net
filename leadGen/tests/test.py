import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from leadGen.functions import common as c
from leadGen.functions import submitPII

details = {
    "email": "tasteyuri@gmail.com",
    "fname": "Yuri",
    "lname": "Charles",
    "gender": "Male",
    "phone": "5418316780",
    "doby": "2000",
    "dobm": "11",
    "dobd": "18",
    "address": "Access",
    "city": "Golconda",
    "state": "NV",
    "zip": "89414",
}

site = "https://qa-v1.freesamplesprousa.com/?cid=qa-slug1&test=1&exp=Flow2-Duplicate-qa-v1-QA-Only"
# site = "https://qa-v1.freesamplesprousa.com/?cid=qa-slug1&test=1"
d = webdriver.Chrome("D:\\chromedriver.exe")
d.get(site)
w = WebDriverWait(d, 20)
submitPII.pii(d, w, details)
