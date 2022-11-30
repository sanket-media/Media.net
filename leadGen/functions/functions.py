from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ex
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
import random


def initialize(driverPath, site, cookies = True):
    d = webdriver.Chrome(driverPath)
    d.implicitly_wait(10)
    w = WebDriverWait(d, 10)
    d.maximize_window()
    if cookies:
        d.delete_all_cookies()
    # d.get("https://" + site["env"] + site["domain"] + "/?" + site["params"])
    d.get(site)
    return d, w


