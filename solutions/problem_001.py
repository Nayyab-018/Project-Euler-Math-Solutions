"""
Project Euler Problem 1: Multiples of 3 or 5
Mathematical Insight: Arithmetic Series + Inclusion-Exclusion Principle
Time Complexity: O(1) | Space Complexity: O(1)
"""
import time


def sum_divisible_by(k: int, limit: int) -> int:
    m = (limit - 1) // k
    return k * m * (m + 1) // 2


def solve(limit: int = 1000) -> int:
    return (
        sum_divisible_by(3, limit)
        + sum_divisible_by(5, limit)
        - sum_divisible_by(15, limit)
    )


if __name__ == "__main__":
    start = time.perf_counter()
    result = solve(1000)
    elapsed_ms = (time.perf_counter() - start) * 1000
    print(f"Answer: {result} | Runtime: {elapsed_ms:.4f} ms")
