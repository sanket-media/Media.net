import time
from selenium.webdriver.support.select import Select
from leadGen.resources import xpaths as x
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def pii(d, w, details):
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
                    # if d.find_element(By.XPATH, locator):
                    element = d.find_element(By.XPATH, locator)
                    type = element.get_attribute("type")
                    if type in ['text', 'email', 'tel']:
                        element.clear()
                        element.send_keys(details[i])
                        flags[i] = True
                    elif type in ['select-one']:
                        Select(element).select_by_value(details[i])
                        flags[i] = True
                    elif type in ['radio']:
                        element.click()
                        flags[i] = True
                except:
                    locators += [locator]
                    elementsNotPresent += [i]

        print("Fields not on PII page " + str((loopCount + 1)) + " -> ", elementsNotPresent)
        loopCount += 1
        try:
            # time.sleep(10)
            submitBtn.click()
            message = d.switch_to_alert().text
            print(message)
        except:
            print('No Alert Present')
        if len(locators) > 0:
            multipleLocators = locators[0]
            for i in locators:
                multipleLocators += ' | ' + i
            w.until(ec.visibility_of_any_elements_located((By.XPATH, multipleLocators)))
