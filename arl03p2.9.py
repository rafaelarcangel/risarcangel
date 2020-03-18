"""R. IÑIGO S. ARCANGEL
   DATALOG Lab03
   Feb. 12, 2020
   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code."""

class Vector:
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d # Create d-dimensional vector of zeros
    def __len__(self): # Return the dimension of vector
        return len(self._coords)
    def __getitem__(self, j): #Return coordinator of vector
        return self._coords[j]
    def __setitem__(self, j, val): #Set coordinator of vector to given value
        self._coords[j] = val
    def __add__(self, other): #Return sum of two vectors
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __str__(self): # Produces string that represents vector
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'  # Produce string represention of vector
    def __sub__(self, other): #Return difference of two vectors
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
if __name__ == '__main__':
    v = Vector(5)  # Construct Five Dimensional Vector
    v[1] = 23 # based on use of __setitem__
    v[-1] = 45 # also based on use of __setitem__
    print(v[4]) #print via __getem__
    u = v + v # uses addition
    print(u) # print the vectors
    w = v - u # uses subtraction
    print(w) # print the vectors
    total = 0
    for entry in v:  # Iteration
        total += entry
