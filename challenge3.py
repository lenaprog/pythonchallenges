x = '121'

def isPalindrome(x):
    rev = ''.join(reversed(x))
    if x == rev:
        return True
    return False
    

isPalindrome(x)
