from leadGen.functions import functions as f
from leadGen.resources import contants as c
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from leadGen.functions import functions as f

driverPath = 'D:\\chromedriver.exe'
# site = "https://qa-v1.freesamplesprousa.com/?cid=qa-slug1&test=1&exp=Flow2-Duplicate-qa-v1-QA-Only"
# site = "https://qa-v1.freesamplesprousa.com/?cid=qa-slug1&test=1"
site = 'https://qa-v2.freesamplesprousa.com/?cid=qa-slug2&test=1'

d,w = f.initialize(driverPath, site)
f.submitPII(d,w,c.ana)
d