from leadGen.resources import xpaths as x
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def pii(d, w, details):
    flags = {
        "email": False,
        "fname": False,
        "lname": False,
        "maleRadio": False,
        "phone": False,
        "doby": False,
        "dobm": False,
        "dobd": False,
        "address": False,
        "city": False,
        "state": False,
        "zip": False,
    }

    while False in flags.values():
        w.until(ec.visibility_of_element_located((By.XPATH, x.submitBtn)))
        elements = []
        for i in flags:
            if ~flags[i]:
                if d.find_element(By.XPATH, x.pii[i]):
                    elements += [i, d.find_element(By.XPATH, x.pii[i])]

        # for i in flags:
        #     if ~flags[i]:
        #         e = d.find_element(By.XPATH, x.pii[i])
        #         type = e.get_attribute("type")
        #
        #         if type in ['text', 'email', 'tel']:
        #             e.clear()
        #             e.send_keys(details[i])
        #             flags[i] = True
        #         elif type in ['select-one']:
        #             print('select')
        #             flags[i] = True
        #         elif type in ['radio']:
        #             print('gender')
        #             flags[i] = True
        #     d.find_element(By.XPATH, x.submitBtn).click()

