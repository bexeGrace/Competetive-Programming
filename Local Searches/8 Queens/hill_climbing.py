import random

class Table:
    def __init__(self, size = 8):
        self.size = size
        self.table = []
        for i in range(self.size):
            row = [0] * self.size
            self.table.append(row)

    def generate_random(self):
        generated = []
        rows = []
        cols = []

        while len(rows) != 8:
            row = random.randint(0, 7)
            if row not in rows:
                rows.append(row)

        while len(cols )!= 8:
            col = random.randint(0, 7)
            if col not in cols:
                cols.append(col)

        for i in range(len(rows)):
            generated.append((rows[i], cols[i]))

        return generated



class Queens_8: 
    def __init__(self, init_state):
        self.init_state = init_state

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


    def generate_neghibors(self, state: list):
        neghibors = []
        for i in range(len(state)):
            for j in range(len(state)):
                temp = state.copy()
                row, col = state[j]
                temp[j] = (row, (col + 1)%8)
                if temp not in neghibors:
                    neghibors.append(temp)

       
        
        return neghibors


    def hill_climbing(self, state, prev = None):
        neghibors = self.generate_neghibors(state)

        curr = state
        # print(neghibors)
        for c_state in neghibors:
            val = self.objective_function(c_state)
            if val < self.objective_function(curr):
                curr = c_state

        if curr == prev:
            if curr == 0:
                return curr, "Succesful"
            return curr, 'Failed', self.objective_function(curr)
        
        
        
        return self.hill_climbing(curr, state)
        
        
            

    

tb = Table()
i_s = tb.generate_random()
gm = Queens_8(i_s)
# print(gm.objective_function(i_s), i_s)
# print(gm.generate_neghibors(i_s), i_s)
print(gm.hill_climbing(i_s), i_s)
# print(tb.table)
        
        