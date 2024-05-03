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
        return generated



class Queens_8: 
    def __init__(self, init_state):
        self.state = init_state
        self.neghibours = []

    def objective_function(self, state):
        rows = set()
        cols = set()
        count = 0
        for row, col in state:
            rows.add(row)
            cols.add(col)
            for row2, col2 in state:
                delta_row = abs(row - row2)
                delta_col = abs(col - col2)
                if delta_row == delta_col:
                    count += 1
        count += len(state) - len(rows)
        count += len(state) - len(cols)

        return count


    def generate_neghibors(self, state):
        pass

    def hill_climbing(self, init_state):
        pass

    

tb = Table()
i_s = tb.generate_random()
gm = Queens_8(i_s)
print(gm.objective_function(i_s), i_s)
# print(tb.table)
        
        