import random
import math


# N-Queen problem using simmulated annealing

N = 10 # Number of queens
E_MAX = 0 # Max number of attacks

# Function to initialize the state of the board
def initialState():
    state = []
    for num in range(N):
        state.append(num)
    print(state)
   
# Function to get the possible neighbours given a state 
def neighbours(state):
    neighbours = []
    for i in range(N):
        for j in range(i+1, N):
            new_neighbour = []
            for m in state:
                new_neighbour.append(m)
            new_neighbour[i] = state[j]
            new_neighbour[j] = state[i]
            neighbours.append(new_neighbour)
    return neighbours

# Function to determine the number of collisions given a state
def utility(state):
    collisions = 0
    for i in range(N):
        for j in range(i+1, N):
            if i+state[i] == j+ state[j]:
                collisions += 1
            if i-state[i] == j - state[j]:
                collisions += 1
    return collisions

# Function to determine the initial value of the temperature
def temp_estimation(state):
    neighbourhood = neighbours(state)
    utility_neigh = []
    for neighbour in neighbourhood:
        utility_neigh.append(utility(neighbour))
    # Calculate the mean
    mean = sum(utility_neigh)/len(utility_neigh)
    #Calculate the deviation of each point from the mean and square the result of each
    deviation = [(x-mean)**2 for x in utility_neigh]
    # Calculate the variance
    variance = sum(deviation)/len(utility_neigh)
    # Calculate the standard deviation
    std = variance ** 0.5
    
    return std

def temp(T, alpha):
    return T * alpha

# Function to determine the probability of accepting a neighbour
def acceptance_probability(utility, new_utility, temperature):
    if new_utility < utility:
        return 1.0
    else:
        return math.exp((utility - new_utility)/temperature) 
    
def simmulated_annealing():
    current_state = initialState()
    e = utility(current_state)
    k=0
    T = temp_estimation(current_state)
    k = 0
    while e > E_MAX and k < 100:
        new_state = random.choice(neighbours(current_state))
        new_utility = utility(new_state)
        current_utility = utility(current_state)
        ap = acceptance_probability(current_utility, new_utility, temp(i))
        if ap > random.random():
            current_state = new_state
            e = new_utility
        k += 1
    return current_state 
    
    
    
def cost(state):
    n = len(state)
    cost = 0
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j]:
                cost += 1
            if abs(state[i] - state[j]) == j - i:
                cost += 1
    return cost

def move(state):
    n = len(state)
    newState = []
    for i in range(n):
        newState.append(state[i])
    i = random.randint(0, n-1)
    j = random.randint(0, n-1)
    newState[i] = state[j]
    newState[j] = state[i]
    return newState

def simulatedAnnealing(n):
    current_state = initialState(n)
    t = 1.0
    tMin = 0.00001
    alpha = 0.9
    while t > tMin:
        i = 1
        while i <= 100:
            next = move(current_state)
            deltaE = cost(next) - cost(current_state)
            if deltaE < 0:
                current_state = next
            else:
                if random.random() < math.exp(-deltaE/t):
                    current_state = next
            i += 1
        t = t * alpha
    return current_state
    
    
    
if __name__ == "__main__":
    initialState(10)