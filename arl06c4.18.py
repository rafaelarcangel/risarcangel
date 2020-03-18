"""R. IÑIGO S. ARCANGEL
   DATALOG Lab06
   March 4, 2020
   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code."""


input_str_1 = "aaeeaeebbd"
vowel = "AaEeIiOoUu"
def consonants(input_str): # defining consonants
    if input_str == '': # if nothing was inputted it will return 0
        return 0
    if input_str[0].lower() not in vowel and input_str[0].isalpha(): # checking if string characters is not in vowel
        return 1 + consonants(input_str[1:]) # If return was 0, it will already stop
    else:
        return consonants(input_str[1:])
def vowels(input_str): # defining vowels
    if input_str == '': # if nothing was inputted it will return 0
        return 0
    if input_str[0].lower() in vowel and input_str[0].isalpha(): # checking if string characters is in vowel
        return 1 + vowels(input_str[1:])
    else:
        return vowels(input_str[1:])
def total(input_str): # defining total
    if consonants(input_str) > vowels(input_str): # checking if consonant is greater than vowels
        print("There are more consonants than vowels") # print when there are more consonants than vowels
    else:
        print("There are more vowels than consonants") # print when there are more vowels than consonants

print("The number of consonants are: ", consonants(input_str_1))
print("The number of vowels are: ", vowels(input_str_1))
print("----------------------------------------------")
print(total(input_str_1))

