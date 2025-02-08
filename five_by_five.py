import numpy as np

class Grid2D:

    def __init__(self, n):
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
    
    def simulate_decay(self):

        decayed_nuclei = 0

        while decayed_nuclei < 13:
            for x in range(1000):
                for i, row in enumerate(self.grid):
                    for j, value in enumerate(row):
                        #print(x, i, j)
                        random_number = np.random.rand()
                        if value == 1 and random_number < 0.0002775:
                            self.grid[i][j] = 0
                            decayed_nuclei += 1
                            print(x)
                            if decayed_nuclei == 13:
                                return
                        else: 
                            continue

        print(decayed_nuclei)


def main():

    five_by_five = Grid2D(5)
    five_by_five.simulate_decay()
    print(five_by_five)


main()
