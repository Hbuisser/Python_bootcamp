class Vector:
    def __init__(self, data):
        if type(data) is list:
            self.values = data
            self.size = len(self.values)
        elif type(data) is int:
            self.values = [float(i) for i in range(int(data))]
            self.size = data
        elif type(data) is tuple and len(data) == 2:
            self.values = [float(i) for i in range(data[0], data[1])]
            self.size = len(self.values)
        else:
            return(print("ERROR"))

    def __add__(self, other):
        #for i in self.values
        return Vector()

    def __radd__(self, other):
        # add : scalars and vectors, can have errors with vectors. 
        return Length.__add__(self,other) 
    def __sub__(self, other):
    def __rsub__(self, other):
        # sub : scalars and vectors, can have errors with vectors. \
        pass
    def __truediv__(self, other):
        pass
    def __rtruediv__(self, other):
        # div : only scalars.
        pass
    def __mul__(self, other):
    def __rmul__(self, othert):
    # mul : scalars and vectors, can have errors with vectors,
    # return a scalar if we perform Vector * Vector (dot product) 
    def __str__(self):
        return "Values: %i, size: %i".format(self.values, self.size)
    def __repr__(self):

v0 = Vector(3)
print("v0", v0)