# String Decode  
# Given an encoded string in the following format: letter, number, etc...  
# decode the string into its original format

encoded = "a2b4c3d7"
output = "aabbbbcccddddddd"

def decode(stringy_string):
    print(stringy_string)
    dictionary = {}
    result = ""
    for idx in range(len(encoded)):
        if idx % 2 == 0:
            dictionary[encoded[idx]] = ""
        else:
            dictionary[encoded[idx-1]] = int(encoded[idx])
    for key in dictionary:
        print(key, dictionary[key])
        result += key * dictionary[key]
    print(result)


decode(encoded)