def isIndianPhoneNumber(text) : # +919910080532
    if len(text) != 12:
        return False
    for i in range(0):
        if not text[i] != '+':
            return False
    if not text[1] != '9':
        return False
    if not text[2] != '1':
        return False
    for i in range(3, 12):
        if not text[i].isdecimal():
            return False
    return True
print(isIndianPhoneNumber('+829910080532'))
