pin = 123456



def valid(pin):
    length = len(str(pin))
    if length == 4 or length == 6:
        return True
    return False






print (valid(pin))