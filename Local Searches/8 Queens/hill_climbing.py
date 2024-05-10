import random
import copy

from simulated_annealing import simulated_annealing 

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
    
    def generate_successors(self, state):
        successors = []

        for i, (queen_row, queen_col) in enumerate(state):
            # Create a copy of the current state
            new_state = copy.deepcopy(state)
            # Remove the queen from its current position
            new_state.pop(i)
            # Try placing the queen in each row of its column
            for row in range(self.size):
                # Check if placing the queen in this row is valid
                if all((row != q_row and
                        abs(row - q_row) != abs(queen_col - q_col))
                       for q_row, q_col in new_state):
                    # If valid, add the new position to the successors
                    new_state.append((row, queen_col))
                    successors.append(new_state)
                    # Create a fresh copy of the state for the next iteration
                    new_state = copy.deepcopy(state)

        return successors



class Queens_8: 
    def __init__(self, init_state):
        self.init_state = init_state

    def objective_function(self, state):
        rows = set()
        cols = set()
        count = 0
        # print(state)
        for row, col in state:
            rows.add(row)
            cols.add(col)
            for row2, col2 in state:
                if row2==row or col==col2:
                    continue
                delta_row = abs(row - row2)
                delta_col = abs(col - col2)
                if delta_row == delta_col:
                    count += 1
        count += len(state) - len(rows)
        count += len(state) - len(cols)

        return count





    def generate_neighbors(self, state: list):
        neighbors = []
        for i in range(len(state)):
            for row in range(8):
                if row != state[i][0]:
                    temp = state.copy()
                    temp[i] = (row, state[i][1])  # Only change the row number
                    neighbors.append(temp)
        return neighbors
    


    def hill_climbing(self, state):

        prev = None

        curr = state
        while True:
            neghibors = self.generate_neighbors(curr)

            # print(neghibors)
            prev = curr
            for c_state in neghibors:
                val = self.objective_function(c_state)
                if val <= self.objective_function(curr):
                    curr = c_state
            

            if self.objective_function(curr) == self.objective_function(prev):
                if self.objective_function(curr) == 0:
                    return curr, "Succesful"
                else:
                    curr = Table.generate_random(Table)
                    prev = None


    def simulated_annealing(self, temperature=100, cooling_rate=0.99, max_iterations=1000):
        best_solution, best_energy, i = simulated_annealing(Table.generate_random(Table), self.objective_function, self.generate_neighbors, temperature, cooling_rate, max_iterations)
        print("Best Solution:", best_solution)
        print("Best Energy:", best_energy)
        print('Max iteration: ', i)
                    
        
        
        
            

    

tb = Table()
i_s = tb.generate_random()
gm = Queens_8(i_s)
# a= gm.objective_function([(1, 5), (6, 1), (4, 4), (0, 2), (2, 7), (7, 3), (3, 0), (5, 6)])
# print(a)
# print(tb.generate_successors(i_s))
# print(gm.objective_function(i_s), i_s)
# print(gm.generate_neghibors(i_s), i_s)
# print(gm.hill_climbing(i_s), i_s)
gm.simulated_annealing()
# print(tb.table)
        
        