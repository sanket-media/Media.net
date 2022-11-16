from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ex
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
import random


def initialize(driverPath, site):
    d = webdriver.Chrome(driverPath)
    d.implicitly_wait(10)
    w = WebDriverWait(d, 10)
    d.maximize_window()
    d.delete_all_cookies()
    d.get("https://" + site["env"] + site["domain"] + "/?" + site["params"])
    return d, w

