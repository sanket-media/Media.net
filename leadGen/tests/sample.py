flags = {
        "done": False,
        "email": [False, "emailBox"],
        "fname": [False, "fnameBox"],
        "lname": [False, "lnameBox"],
        "male": [False, "maleRadio"],
        "female": [False, "femaleRadio"],
        # "gender": [False, "gender"],
        "phone": [False, "phoneBox"],
        "doby": [False, "dobyDDM"],
        "dobm": [False, "dobmDDM"],
        "dobd": [False, "dobdDDM"],
        "address": [False, "addressBox"],
        "city": [False, "cityBox"],
        "state": [False, "stateBox"],
        "zip": [False, "zipBox"],
    }

# while False in flags.values():
#         elements = []
#         for i in flags:
#                 if i != 'done' and ~flags[i][0]:
#                         print(i)

print(flags["email"][1])