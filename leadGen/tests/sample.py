# values = []
# query = """insert into campaignmanager.phone_carrier_lookup (carrier, carrier_display_name) values """
# for i in range(1, 65):
#     values += [('verizon ' +str(i), 'verizon')]
#
# print (query + str(values) + ' ;')

l = ["//input[@id='firstName']", "//input[@id='lastName']", "//input[@type='radio' and @value='Male']",
       "//input[@id='phoneNumber']", "//select[@id='dbodateyear']", "//select[@id='dbodatemonth']",
       "//select[@id='dbodateday']", "//input[@id='address']", "//input[@id='cityName']", "//select[@id='stateCode']",
       "//input[@id='zipcode']"]

a = [1]
print(len(a))