# String Encode
# You are given a string that may contain sequences of consecutive characters.
# Create a function to shorten a string by including the character,
# then the number of times it appears. 


# str1 = "aaaabbcddd"
# expected1 = "a4b2c1d3"

# https://www.w3schools.com/python/python_dictionaries_access.asp
# Get the value of the "model" key:
""" thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"] """

# encoded_string = encode_string("aaaabbcccdddddfffffffff")
# Objective 1: Make a dict like this , "counter" is needed
# {'a': 4, 'b': 2, 'c': 3, 'd': 5, 'f': 9}
def encode_string(stringy_string):
    result = ""
    counter = {}
    for char in stringy_string:
        if char not in counter:
            counter[char] = 1
        else:
            counter[char] += 1
    print(counter)

#Objective 2: Concatinate the new dict, "result" is needed
    for key in counter:
    #   x = []     
    #   x += something           
    #   x = x + something  ===concatenation!
        # Objective 2a: get the key out in each step of the "for" loop
        result += key
        print(result)
        # Objective 2b: concatenate the value next to the key in each step of the "for" loop
        result += str(counter[key])        
        
    return result


encoded_string = encode_string("aaaabbcccdddddfffffffff")
print(encoded_string)