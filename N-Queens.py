import random
import math

# N-Queen problem using simulated annealing

N = 8  # Number of queens
E_MAX = 0  # Max number of attacks
INITIAL_TEMP = 1000  # Initial temperature

# Function to initialize the state of the board
def initialState():
    state = list(range(N))
    random.shuffle(state)
    return state

# Function to get the possible neighbours given a state 
def neighbours(state):
    neighbours = []
    for i in range(N):
        for j in range(i + 1, N):
            new_neighbour = state[:]
            new_neighbour[i], new_neighbour[j] = new_neighbour[j], new_neighbour[i]
            neighbours.append(new_neighbour)
    return neighbours

# Function to determine the number of collisions given a state
def utility(state):
    collisions = 0
    for i in range(N):
        for j in range(i + 1, N):
            if abs(i - j) == abs(state[i] - state[j]):
                collisions += 1
    return collisions

def temp(T, alpha):
    return T * alpha

# Function to determine the probability of accepting a neighbour
def acceptance_probability(utility, new_utility, temperature):
    if new_utility < utility:
        return 1.0
    else:
        return math.exp((utility - new_utility) / temperature)

def simulated_annealing():
    current_state = initialState()
    e = utility(current_state)
    T = INITIAL_TEMP
    k = 0
    while e > E_MAX and T > 1e-5:
        new_state = random.choice(neighbours(current_state))
        new_utility = utility(new_state)
        current_utility = utility(current_state)
        ap = acceptance_probability(current_utility, new_utility, T)
        if ap > random.random():
            current_state = new_state
            e = new_utility
        T = temp(T, 0.99)
        k += 1
    return current_state

if __name__ == "__main__":
    solution = simulated_annealing()
    print("Solution:", solution)
    print("Number of collisions:", utility(solution))
