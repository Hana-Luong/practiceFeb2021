# For Hana's reference
#    for i in range(len(keys)):
#       direct[keys[i]] = values[i]


#FREQUENCY COUNTER

# An anagram is a word or phrase formed by rearranging the letters of a different word 
# or phrase, typically using all the original letters exactly once.
# Is there a quick way to determine if they aren't an anagram before spending more time?
# Given two strings return whether or not they are anagrams

# Input: "yes", "eys"
# Output: True

# Input: "yes", "eYs"
# Output: True

# Input: "no", "noo"
# Output: False

first_string = "yes"
second_string = "eYs"

def anagramOrNot(str1, str2):
  str1 = str1.lower()
  str2 = str2.lower()
  if(sorted(str1)== sorted(str2)):
    return True 
  else:
    return False

print(anagramOrNot(first_string, second_string))
print(anagramOrNot("nooo","ono"))


#https://www.geeksforgeeks.org/python-sorted-check-two-strings-anagram-not/
#https://stackoverflow.com/questions/39376164/how-to-treat-uppercase-and-lowercase-words-the-same-in-python

# Python3 program for the above approach
""" from collections import Counter """
 
# function to check if two strings are
# anagram or not
""" def check(s1, s2): """
   
    # implementing counter function
"""     if(Counter(s1) == Counter(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.") """
