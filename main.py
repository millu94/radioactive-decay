import numpy as py

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
    
def main():
    
    print("Input the following: decay constant = λ [min^-1], square root of "
          "total array size N = √TotalSize, timestep = Δt [min]")
    decay_constant = float(input("λ: "))
    n = int(input("N: "))
    Δt = float(input("Δt: "))

    """
    λ: 0.02775, N: 50, ∆t: 0.01
    """

    print(f"λ: {decay_constant}, N: {n}, ∆t: {Δt}")

    test_grid = Grid2D(n)
    print(test_grid)

if __name__ == "__main__":
    main()