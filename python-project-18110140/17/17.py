class mt: 
    def __init__(self, first, second): 
        self.first = first 
        self.second = second 

    def add(self): 
        result = self.first + self.second 
        return result 

    def sub(self): 
        result = self.first - self.second 
        return result 

    def mul(self): 
        result = self.first * self.second 
        return result 

    def div(self): 
        result = self.first / self.second 
        return result 

a = mt(4,2)
print(a.first)
print(a.second)
print(a.add())
print(a.mul())