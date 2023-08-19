class Circle:
    pi = 3.14

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap

    def cevre(self):
        return 2 * self.pi * self.yaricap
    
    def alan(self):
        return self.pi * (self.yaricap ** 2)
    
c1 = Circle()
c2 = Circle(2)

print(f"c1 için alan: {c1.alan()} çevre: {c1.cevre()}")
print(f"c2 için alan: {c2.alan()} çevre: {c2.cevre()}")
