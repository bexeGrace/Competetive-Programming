import random
import math

def simulated_annealing(initial_solution, objective_function, neighbor_function, temperature, cooling_rate, max_iterations):
    print(initial_solution)
    current_solution = initial_solution
    current_energy = objective_function(current_solution)
    best_solution = current_solution
    best_energy = current_energy
    
    for iteration in range(max_iterations):
        temperature *= cooling_rate
        if temperature < 0.001:
            print(iteration)
            break
        
        neighbor = neighbor_function(current_solution)
        curr = neighbor[0]
        for c_state in neighbor:
            val = objective_function(c_state)
            if val <= objective_function(curr):
                curr = c_state
        neighbor_energy = objective_function(curr)
        
        energy_difference = neighbor_energy - current_energy
        if energy_difference < 0 or random.random() < math.exp(-energy_difference / temperature):
            current_solution = curr
            current_energy = neighbor_energy
            
            if current_energy < best_energy:
                best_solution = current_solution
                best_energy = current_energy
    
    return best_solution, best_energy, iteration



# Example usage
initial_solution = ...
temperature = ...
cooling_rate = ...
max_iterations = ...


