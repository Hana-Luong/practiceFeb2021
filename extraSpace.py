# Given a string that may have extra spaces at the start and the end,
# return a new string that has the extra spaces at the start and the end trimmed (removed)
# do not remove any other spaces.

# Input: "   hello world     "
# Output: "hello world"

string_length = len("   hello world     ") 

print(string_length)

# Needed to add the quote marks otherwise I got an error. However this returns 19#
# meaning it does count the empty space???
# you know, we need to keep the empty space between the two words
# 

# appears so. 

# according to some reading I did, Java will identify the unicode value, /u0020, and 
# use that to id the leading and trailing whitespavce and remove it thath way.
#  Not sure how we would implement that there tho

# WHAT ABOUT MAKING AN EMPTY DIC
# IF THE ELEMENTS ARE IN THE EMPTY DICT, MEANING IT IS AN EMPTY CHARACTER, REMOVE IT? 
#    If we do that, would Python identify the whitespace or just grab the first character we see? ~L
# We don't know
# Just give it a try to kill time


# Let communicate through writing only and turn off your mic so we don't get distracted!
def extraspaces(str3):
  new_string = ""
  for char in range(len(str3)):
    if str3[char] != "   ":
      new_string = new_string + str3[char]
  return new_string  

result = extraspaces("   Hello World   ")
print(result)

def strip(str4):
  for char in range(len(str4)):
    if str4[char] == "   ":
      str4.pop