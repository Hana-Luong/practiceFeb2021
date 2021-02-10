stringy_string1 = 'radar' 
stringy_string2 = 'yes'

# Iterative Method (using a for loop)

def palindromeOrNot(aString):    
    for i in range(0, int(float(len(aString))/2)):            
        if aString[i] != aString[len(aString)-i-1]:
            return False
        return True

print(palindromeOrNot(stringy_string1))
print(palindromeOrNot(stringy_string2))


# Recursive Method
def isPalindrome(s):   
    # length of s
    l = len(s)     
    # if length is less than 2
    if l < 2:
        return True
 
    # If s[0] and s[l-1] are equal
    elif s[0] == s[l - 1]:        
        # Call is pallindrome form substring(1,l-1)
        return isPalindrome(s[1: l - 1])
 
    else:
        return False

# Another method 
# #https://www.w3schools.com/python/python_howto_reverse_string.asp
def isPalindromeOr(s):     
    # Using predefined function to 
    # reverse to string print(s)
    rev = ''.join(reversed(s))
 
    # Checking if both string are 
    # equal or not
    if (s == rev):
        return True
    return False

    # Another
    # https://www.w3schools.com/python/python_howto_reverse_string.asp
    #the slice statement [::-1] means start at the end of the string 
    # and end at position 0, move with the step -1, negative one, which means one step backwards.

def isPalindromeOrNo(s):
    return s == s[::-1]
 
s = "malayalam"
ans = isPalindrome(s)
 






 
