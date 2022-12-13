import time
from leadGen.resources import xpaths as x
from leadGen.resources import environment as env
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
import random
import logging

logging.basicConfig(filename=env.logFile,
                    format='%(asctime)s: %(message)s')
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def initialize(driverPath, site, cookies=True):
    d = webdriver.Chrome(driverPath)
    # d.implicitly_wait(10)
    w = WebDriverWait(d, 10)
    d.maximize_window()
    if cookies:
        d.delete_all_cookies()
    # d.get("https://" + site["env"] + site["domain"] + "/?" + site["params"])
    d.get(site)
    return d, w


def submitPII(d, w, details):
    flags = {
        "email": False,
        "zip": False,
        "fname": False,
        "lname": False,
        "gender": False,
        "address": False,
        "city": False,
        "state": False,
        "phone": False,
        "doby": False,
        "dobm": False,
        "dobd": False
    }

    loopCount = 0
    while False in flags.values():
        if loopCount >= 5:
            raise Exception('Looping Limit Reached')
        elements = []
        # elementsFound = []
        # elementsNotPresent = []
        locators = ''
        submitBtn = w.until(ec.visibility_of_element_located((By.XPATH, x.submitBtn)))
        for i in flags:
            if not flags[i]:
                if i == 'gender':
                    locator = x.pii['gender'][0] + details['gender'] + x.pii['gender'][1]
                else:
                    locator = x.pii[i]
                try:
                    element = d.find_element(By.XPATH, locator)
                    elements += [((i, element))]
                    # elementsFound += [i]
                except:
                    if len(locators) == 0:
                        locators = locator
                    elif len(locators) > 0:
                        locators += ' | ' + locator
                    # elementsNotPresent += [i]
        # print(locators)

        for t in elements:
            key = t[0]
            element = t[1]
            type = element.get_attribute("type")
            if type in ['text', 'email', 'tel']:
                element.clear()
                element.send_keys(details[key])
                flags[key] = True
            elif type in ['select-one']:
                Select(element).select_by_value(details[key])
                flags[key] = True
            elif type in ['radio']:
                try:
                    element.click()
                except:
                    d.execute_script("arguments[0].click();", element)
                flags[key] = True

        # print("Fields present on page " + str((loopCount + 1)) + " -> ", elementsFound)
        # print("Fields not on page " + str((loopCount + 1)) + " -> ", elementsNotPresent)
        loopCount += 1
        submitBtn.click()
        try:
            alertMessage = d.switch_to_alert().text
            print(alertMessage)
        except:
            print('no alert in loop', loopCount)
        if locators:
            w.until(ec.visibility_of_any_elements_located((By.XPATH, locators)))
        elif False not in flags.values():
            break

    print('PII Submitted')


def answer(d, w,):
    pass