"""
Project Euler Problem 15: Lattice Paths
Mathematical Insight: Combinatorics & Binomial Coefficients
Time Complexity: O(N) | Space Complexity: O(1)
"""
import math
import time


def count_lattice_paths(grid_size: int = 20) -> int:
    # Any valid path from top-left to bottom-right of an N x N grid
    # consists of exactly N Right (R) moves and N Down (D) moves.
    # The number of unique paths equals choosing N positions for R out of 2N total moves.
    return math.comb(2 * grid_size, grid_size)


if __name__ == "__main__":
    start = time.perf_counter()
    result = count_lattice_paths(20)
    elapsed_ms = (time.perf_counter() - start) * 1000
    print(f"Answer: {result} | Runtime: {elapsed_ms:.4f} ms")
