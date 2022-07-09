# draft
class Pair:
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
    
    def get(self):
        return self.t1, self.t2

    def swap(self):
        self.t1, self.t2 = self.t2, self.t1
    
    

a = 1
b = 2
pair1 = Pair(a, b)
print(pair1.get())
pair1.swap()
print(pair1.get())
print(a, b)