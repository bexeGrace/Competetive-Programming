import random

class Table:
    def __init__(self, size = 8):
        self.size = size
        self.table = []
        for i in range(self.size):
            row = [0] * self.size
            self.table.append(row)

    def generate_random(self):
        generated = set()
        for i in range(8):
            row = random.randint(0, 7)
            col = random.randint(0, 7)
            while (row, col) in generated:
                row = random.randint(0, 7)
                col = random.randint(0, 7)
            generated.add((row, col))
            self.table[row][col] = 1
        return self.table



class Queens_8: 
    def __init__(self, init_state: Table):
        self.init_state = init_state
        self.neghibours = []

    def generate_neghibors(self, state):
        pass

    def hill_climbing(self, init_state):
        pass

    

tb = Table()
print(tb.generate_random())
# print(tb.table)
        
        