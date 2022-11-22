from leadGen.resources import xpaths as x
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def pii(d, w, details):
    # flags = {
    #     "email": [False, "emailBox"],
    #     "fname": [False, "fnameBox"],
    #     "lname": [False, "lnameBox"],
    #     "male": [False, "maleRadio"],
    #     "female": [False, "femaleRadio"],
    #     # "gender": [False, "gender"],
    #     "phone": [False, "phoneBox"],
    #     "doby": [False, "dobyDDM"],
    #     "dobm": [False, "dobmDDM"],
    #     "dobd": [False, "dobdDDM"],
    #     "address": [False, "addressBox"],
    #     "city": [False, "cityBox"],
    #     "state": [False, "stateBox"],
    #     "zip": [False, "zipBox"],
    # }

    flags = {
        "email": False,
        "fname": False,
        "lname": False,
        # "gender": False,
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
            raise Exception('Loop has been run for total 5 times')
        elementsNotPresent = []
        submitBtn = w.until(ec.visibility_of_element_located((By.XPATH, x.submitBtn)))
        for i in flags:
            try:
                if ~flags[i] and d.find_element(By.XPATH, x.pii[i]):
                    element = d.find_element(By.XPATH, x.pii[i])
                    type = element.get_attribute("type")
                    if type in ['text', 'email', 'tel']:
                        element.clear()
                        element.send_keys(details[i])
                        flags[i] = True
                    elif type in ['select-one']:
                        print('select')
                        flags[i] = True
                    elif type in ['radio']:
                        print('gender')
                        flags[i] = True
            except:
                elementsNotPresent += [i]

        print(elementsNotPresent)
        submitBtn.click()
