import numpy as np
import math

class Nuclei:

    def __init__(self, λ, n, Δt):
        self.total_nuclei = n**2
        self.decay_constant = λ
        self.actual_half_life = math.log(2) / self.decay_constant
        self.probability_of_decay = Δt * self.decay_constant
        self.time_step = Δt
        self.grid = []
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
                        generate random number and if it is less than probability of 
                        decay then change element to equal zero

        else
            print recorded time step ie the simulated number for half life
    """


    """
    def simulate_radioactive_decay(self):

        decayed_nuclei = 0
        recorded_time_step = 0

        # continue until half the nuclei have decayed
        while decayed_nuclei < (self.total_nuclei / 2):
            # iterate for each time step
            for iteration in range(2000):
                recorded_time_step += self.time_step
                print(recorded_time_step)

                for index, value in enumerate(self.grid):
                    if value == 1:
                        random_value = np.random.rand()
                        if random_value <= self.probability_of_decay:
                            print(f"mins : {recorded_time_step}")
                            self.grid[index] = 0
                            decayed_nuclei += 1
                            print(decayed_nuclei)

        else:
            print(decayed_nuclei)
            print(recorded_time_step)
            print(self)
    """
    def simulate_radioactive_decay(self):
        decayed_nuclei = 0
        recorded_time_step = 0
    # continue until half the nuclei have decayed
        while decayed_nuclei < (self.total_nuclei / 2):
            # iterate for each time step
            recorded_time_step += self.time_step
            #print(recorded_time_step)
            for index, value in enumerate(self.grid):
                if value == 1:
                    random_value = np.random.rand()
                    if random_value <= self.probability_of_decay:
                        print(f"mins : {recorded_time_step}")
                        self.grid[index] = 0
                        decayed_nuclei += 1
                        print(decayed_nuclei)
        else:
            print(decayed_nuclei)
            print(recorded_time_step)
            print(self)
                   



    
def main():
    
    print("Input the following: decay constant = λ [min^-1], square root of "
          "total array size N = √TotalSize, timestep = Δt [min]")
    λ = float(input("λ: "))
    n = int(input("N: "))
    Δt = float(input("Δt: "))

    """
    λ: 0.02775, N: 50, ∆t: 0.01
    """

    # probability_of_decay = Δt * decay_constant
    # half_life = math.log(2) / decay_constant

    # print(f"λ: {decay_constant}, N: {n}, ∆t: {Δt}")

    test_grid = Nuclei(λ, n, Δt)
    test_grid.simulate_radioactive_decay()
    print(test_grid)

if __name__ == "__main__":
    main()