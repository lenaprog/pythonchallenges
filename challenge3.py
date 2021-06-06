x = 'Anna'

def isPalindrome(x):
    print(reversed(x))
    rev = ''.join(reversed(x)).lower()
    print(rev)
    return x.lower() == rev
     #   return True
    #return False
    
    

print(isPalindrome(x))
