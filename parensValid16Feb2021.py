# Parens Valid
# Given a string that has parenthesis in it
# return whether the parenthesis are valid

# Input: "Y(3(p)p(3)r)s"
# Output: True

# Input: "N(0(p)3"
# Output: False

x= "((()))())("



def parens_valid(stringy):
    pairs =0
    for char in stringy:
        if char == "(":
            pairs +=1
            print(pairs)
        if char == ")":
            pairs -=1
            print(pairs)
        if pairs < 0:
            return False
    if pairs == 0:
        return True
    else:
        return False
        
#print(parens_valid("y(3(p)p(3)r)0s"))
print(parens_valid(x))