"""R. IÑIGO S. ARCANGEL
   DATALOG Lab01
   Feb. 9, 2020
   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code."""

def check(list):
    return all(i == list[0] for i in list) # It will check if there are same characters in a given list, will print false if there are no identical characters and print yes if there are.
print(check(['a', 'b', 'c'])) # First List
print(check([1, 1, 1])) # Second list


