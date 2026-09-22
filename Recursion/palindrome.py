def is_palindrome(s):
    rev = ''.join(reversed(s))

    if s == rev:
        return True

    else:
        return False

print(is_palindrome("madam"))
print(is_palindrome("racecar")) 
print(is_palindrome("hello"))   
