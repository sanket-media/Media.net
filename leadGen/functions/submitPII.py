# are all PII fields filled? NO -> execute the following, Yes --> continue
# fetch the available elements on the page
# enter the data and submit
# update the flags
# if all the elements are filled then wait the for the next page and then repeat the filling process or else proceed
#page_url = "https://qa-v1.freesamplesprousa.com/?cid=qa-slug1&test=1"

from leadGen.resources import xpath as x
from selenium.webdriver.common.by import By


def pii(d, w, details):
    flags = {
        "email":False,
        "fname":False,
        "lname":False,
        "gender":False,
        "phone":False,
        "doby":False,
        "dobm":False,
        "dobd":False,
        "address":False,
        "state":False,
        "zip":False,
    }

    while False in flags.values():
        for i in range(len(x.pii)):

