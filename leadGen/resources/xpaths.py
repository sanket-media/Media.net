submitBtn = "//button[@type='submit']"

pii = {
    "email": "//input[@type='email' or @name='emailAddress']",
    "fname": "//input[@id='firstName']",
    "lname": "//input[@id='lastName']",
    "phone": "//input[@id='phoneNumber']",
    "gender": ("//input[@type='radio' and @value='", "']"),
    "maleRadio": "//input[@type='radio' and @value='Male']",
    "femaleRadio": "//input[@type='radio' and @value='female']",
    "zip": "//input[@id='zipcode']",
    "city": "//input[@id='cityName']",
    "address": "//input[@id='address']",
    "state": "//select[@id='stateCode']",
    "dobm": "//select[@id='dbodatemonth']",
    "dobd": "//select[@id='dbodateday']",
    "doby": "//select[@id='dbodateyear']"
}

emailBox = "//input[@type='email' or @name='emailAddress']",
fnameBox = "//input[@id='firstName']",
lnameBox = "//input[@id='lastName']",
phoneBox = "//input[@id='phoneNumber']",
gender = ("//input[@type='radio' and @value='", "']"),
maleRadio = "//input[@type='radio' and @value='Male']",
femaleRadio = "//input[@type='radio' and @value='female']",
zipBox = "//input[@id='zipcode']",
cityBox = "//input[@id='cityName']",
addressBox = "//input[@id='address']",
stateDDM = "//select[@id='stateCode']",
dobmDDM = "//select[@id='dbodatemonth']",
dobdDDM = "//select[@id='dbodateday']",
dobyDDM = "//select[@id='dbodateyear']"
