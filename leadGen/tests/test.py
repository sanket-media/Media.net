# url = 'https://qa-v1.freesamplesprousa.com/?cid=qa-slug1&test=1'

from leadGen.functions import functions as f
from leadGen.resources import contants as c
from leadGen.resources import xpaths as x
from leadGen.resources import environment as e
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import random
import logging
from datetime import datetime


# driverPath = 'D:\\chromedriver.exe'
# site = 'https://freesamplesprousa.com/?cid=vn1ws&test=1'
# site = "https://qa-v1.freesamplesprousa.com/?cid=qa-slug1&test=1&exp=Flow2-Duplicate-qa-v1-QA-Only"
# site = 'https://qa-v2.freesamplesprousa.com/?cid=qa-slug2&test=1'
# site = 'https://theamericansweepstakes.com/?cid=kejy4&test=1&exp=TAS-AutoLinkoutV3-OK-Wow-TCPA-on-Lander'
# site = "https://qa-v1.freesamplesprousa.com/?cid=qa-slug1&test=1"

# driver = webdriver.Chrome(driverPath)
# wait = WebDriverWait(driver, 10)
# driver.maximize_window()
# driver.delete_all_cookies()
# driver.get(site)

d,w = f.initialize(e.driverPath, e.fspu_live_full_tcpa['site'])
f.submitPII(d,w,c.ana)

