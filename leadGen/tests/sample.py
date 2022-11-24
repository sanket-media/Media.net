xp = dict(gender=("//input[@type='radio' and @value='", "']"))

details = {'gender': 'Male'}


print (xp['gender'][0] + details['gender'] + xp['gender'][1])
