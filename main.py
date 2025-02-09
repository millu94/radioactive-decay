import numpy as np
import math

class Nuclei:

    def __init__(self, λ, n, Δt):
        self.total_nuclei = n**2
        self.decayed_nuclei = 0
        self.decay_constant = λ
        self.actual_half_life = round(math.log(2) / self.decay_constant, 2)
        self.probability_of_decay = Δt * self.decay_constant
        self.time_step = Δt
        self.grid = []
        self.simulated_half_time = 0
        for i in range(n):
            one_row = [1]*n
            self.grid.append(one_row)

    def __str__(self):
        s = ""
        for row in self.grid:
            for point in row:
                s += f"{point} "
            s += "\n"
        return s
    
    """
    function to simulate radioactive decay

        while the number of decayed nuclei is less than half of N^2

            for each time step in total time (double actual half life)
                recorded time step += time step
                for each element in self.grid
                    if it equals zero
                        continue
                    else
                        generate random number and if it is less than 
                        probability of 
                        decay then change element to equal zero

        else
            print recorded time step ie the simulated number for half life
    """
        
    def simulate_radioactive_decay(self):
        
        # plenty of room for anomalies
        max_iteration = round((2 * self.actual_half_life) / self.time_step)
        
        print("Initial Nuclei: ", self.total_nuclei)
        print("Actual Half Life: ", self.actual_half_life, "mins")


        for iteration in range(max_iteration):
            
            # loop until decayed nuclei equal half of original number, then exit
            if self.decayed_nuclei >= self.total_nuclei / 2:
                self.simulated_half_life = round(iteration * self.time_step, 2)
                break

            for i, row in enumerate(self.grid):
                for j, value in enumerate(row):

                    random_number = np.random.rand()

                    if value == 1 and random_number < self.probability_of_decay:
                        self.grid[i][j] = 0
                        self.decayed_nuclei += 1.0
                    else:
                        continue

        print("Number of Remaining Nuclei: ", self.total_nuclei - self.decayed_nuclei)
        print("Simulated Half Life: ", self.simulated_half_life, "mins")
    
def main():
    
    print("Input the following: decay constant = λ [min^-1], square root of "
          "total array size N = √TotalSize, timestep = Δt [min]")
    λ = float(input("λ: "))
    n = int(input("N: "))
    Δt = float(input("Δt: "))


    
    # λ = 0.02775
    # n = 50
    # Δt = 0.01
    

    # probability_of_decay = Δt * decay_constant
    # half_life = math.log(2) / decay_constant

    # print(f"λ: {decay_constant}, N: {n}, ∆t: {Δt}")

    test_grid = Nuclei(λ, n, Δt)
    test_grid.simulate_radioactive_decay()
    print(test_grid)

if __name__ == "__main__":
    main()