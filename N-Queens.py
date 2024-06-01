import random
import math
import tkinter as tk

# Colors
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE ='\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[0m'



# N-Queen problem using simulated annealing

N = 8  # Number of queens
E_MAX = 0  # Max number of attacks
INITIAL_TEMP = 1000  # Initial temperature
MIN_TEMP = 0.00000001
ALPHA = 0.99

def select_N(num):
    global N
    N = num


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

# Function to determine T_(k+1) given alpha and T_k
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
    print(BLUE+"Initial state: ", current_state)
    print("Initial state:\n")
    show_board(current_state)
    print("Cost: ", e)
    T = INITIAL_TEMP
    k = 0
    while e > E_MAX and T > MIN_TEMP:
        new_state = random.choice(neighbours(current_state))
        new_utility = utility(new_state)
        current_utility = utility(current_state)
        ap = acceptance_probability(current_utility, new_utility, T)
        if ap > random.random():
            current_state = new_state
            e = new_utility
        T = temp(T, ALPHA)
        k += 1
    return current_state

def show_board(state):
    for i in range(N):
        for j in range(N):
            if state[j] == i:
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print()
    print()
    

class Board:
    
    def __init__(self):
        self.window = tk.Tk() 
        self.window.title("N-Queens Problem")
        self.window.geometry(f"{str(50*N)}x{str(50*N)}")
        self.interface = tk.Canvas(self.window)
        self.interface.pack(fill="both", expand=True)
        self.queen = tk.PhotoImage(file="./Queen.png").subsample(7, 10)
        
    def __call__(self):
        self.window.mainloop()
        
    def draw_board(self):
        for i in range(N):
            for j in range(N):
                if (i + j) % 2 == 0:
                    self.interface.create_rectangle(i * 50, j * 50, (i + 1) * 50, (j + 1) * 50, fill="white")
                else:
                    self.interface.create_rectangle(i * 50, j * 50, (i + 1) * 50, (j + 1) * 50, fill="black")
                    
    def show_queens(self, positions):
        for i in range(N):
            for j in range(N):
                if positions[j] == i:
                    self.interface.create_image(i * 50, j * 50, image=self.queen, anchor="nw")        


if __name__ == "__main__":
    
    # To change the number N of queens, use the function select_N(number)
    # before using simulated_annealing()
    # The default vaue of N is 8
    
    print(CYAN,"\nSolution with 8 queens")
    solution = simulated_annealing()
    print(GREEN+"Solution:", solution)
    show_board(solution)
    print("Number of collisions:", utility(solution))
    window = Board()
    window.draw_board()
    window.show_queens(solution)
    window()
    
    print(CYAN,"\nSolution with 10 queens")
    select_N(10) # Change the number of queens to 10
    solution1 = simulated_annealing()
    print(GREEN+"Solution:", solution1)
    show_board(solution1)
    print("Number of collisions:", utility(solution1),RESET)
    window1 = Board()
    window1.draw_board()
    window1.show_queens(solution1)
    window1()
