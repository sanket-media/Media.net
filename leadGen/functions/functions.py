from leadGen.resources import xpaths as x
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
import random


def initialize(driverPath, site, cookies=True, env='staging'):
    d = webdriver.Chrome(driverPath)
    d.implicitly_wait(10)
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
        "fname": False,
        "lname": False,
        "gender": False,
        "phone": False,
        "doby": False,
        "dobm": False,
        "dobd": False,
        "address": False,
        "city": False,
        "state": False,
        "zip": False
    }
    loopCount = 0
    while False in flags.values():
        if loopCount >= 5:
            raise Exception('Looping Limit Reached')
        elementsFound = []
        elementsNotPresent = []
        locators = []
        multipleLocators = ''
        submitBtn = w.until(ec.visibility_of_element_located((By.XPATH, x.submitBtn)))
        for i in flags:
            if ~flags[i]:
                if i == 'gender':
                    locator = x.pii['gender'][0] + details['gender'] + x.pii['gender'][1]
                else:
                    locator = x.pii[i]
                try:
                    element = d.find_element(By.XPATH, locator)
                    elementsFound += [i]
                    type = element.get_attribute("type")
                    if type in ['text', 'email', 'tel']:
                        element.clear()
                        element.send_keys(details[i])
                        flags[i] = True
                        print('Interaction done ', i)
                    elif type in ['select-one']:
                        Select(element).select_by_value(details[i])
                        flags[i] = True
                        print('Interaction done ', i)
                    elif type in ['radio']:
                        element.click()
                        flags[i] = True
                        print('Interaction done ', i)
                except:
                    locators += [locator]
                    elementsNotPresent += [i]

        print("Fields present on PII page " + str((loopCount + 1)) + " -> ", elementsFound)
        print("Fields not on PII page " + str((loopCount + 1)) + " -> ", elementsNotPresent)
        loopCount += 1
        submitBtn.click()
        try:
            message = d.switch_to_alert().text
            print(message)
        except:
            print('No Alert Present')
        if len(locators) > 0:
            multipleLocators = locators[0]
            for i in locators:
                multipleLocators += ' | ' + i
            w.until(ec.visibility_of_any_elements_located((By.XPATH, multipleLocators)))
    print('PII bhar diya')
