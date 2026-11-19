"""
Project Euler Solutions (Problems 1 - 10)
Author: Nayyab Faisal (GitHub: Nayyab-018)
Demonstrates mathematical optimization, number theory, and algorithmic efficiency in Python.
"""
import math


def problem_001(limit: int = 999) -> int:
    """Multiples of 3 or 5 using O(1) Arithmetic Series & Inclusion-Exclusion."""
    def sum_div(k: int) -> int:
        m = limit // k
        return k * m * (m + 1) // 2
    return sum_div(3) + sum_div(5) - sum_div(15)


def problem_002(limit: int = 4_000_000) -> int:
    """Even Fibonacci Numbers using recurrence E(n) = 4*E(n-1) + E(n-2)."""
    total, a, b = 0, 2, 8
    while a <= limit:
        total += a
        a, b = b, 4 * b + a
    return total


def problem_003(n: int = 600_851_475_143) -> int:
    """Largest Prime Factor via trial division up to sqrt(n)."""
    factor, last_factor = 2, 1
    while factor * factor <= n:
        if n % factor == 0:
            last_factor = factor
            while n % factor == 0:
                n //= factor
        factor += 1 if factor == 2 else 2
    return n if n > 1 else last_factor


def problem_004() -> int:
    """Largest Palindrome Product of two 3-digit numbers (utilizing divisibility by 11)."""
    best = 0
    for a in range(999, 99, -1):
        step = 1 if a % 11 == 0 else 11
        start = 999 if a % 11 == 0 else 990
        for b in range(start, a - 1, -step):
            prod = a * b
            if prod <= best:
                break
            s = str(prod)
            if s == s[::-1]:
                best = prod
    return best


def problem_005(n: int = 20) -> int:
    """Smallest Multiple: LCM(1..20) via math.lcm."""
    ans = 1
    for i in range(1, n + 1):
        ans = math.lcm(ans, i)
    return ans


def problem_006(n: int = 100) -> int:
    """Sum Square Difference using closed-form summation formulas."""
    square_of_sum = (n * (n + 1) // 2) ** 2
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    return square_of_sum - sum_of_squares


def problem_007(target: int = 10_001) -> int:
    """10,001st Prime using the Sieve of Eratosthenes."""
    limit = 120_000
    sieve = bytearray([1]) * limit
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(limit ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p : limit : p] = b"\x00" * len(range(p * p, limit, p))
    primes = [i for i, is_p in enumerate(sieve) if is_p]
    return primes[target - 1]


def problem_008(window: int = 13) -> int:
    """Largest Product in a 1000-digit Series using a sliding window."""
    series = (
        "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843"
        "8586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557"
        "6689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749"
        "3035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776"
        "6572733300105336788122023542180975125454059475224352584907711670556013604839586446706324415722155397"
        "5369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474"
        "8216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586"
        "1786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408"
        "0719840385096245544436298123098787992724428490918884580156166097919133875499200524063689912560717606"
        "0588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    )
    best = 0
    for i in range(len(series) - window + 1):
        chunk = series[i : i + window]
        if "0" in chunk:
            continue
        prod = math.prod(int(d) for d in chunk)
        if prod > best:
            best = prod
    return best


def problem_009(perimeter: int = 1000) -> int:
    """Special Pythagorean Triplet where a + b + c = 1000."""
    for a in range(1, perimeter // 3):
        numerator = perimeter * (perimeter - 2 * a)
        denominator = 2 * (perimeter - a)
        if numerator % denominator == 0:
            b = numerator // denominator
            c = perimeter - a - b
            if a < b < c:
                return a * b * c
    return 0


def problem_010(limit: int = 2_000_000) -> int:
    """Summation of all primes below two million via Sieve of Eratosthenes."""
    sieve = bytearray([1]) * limit
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(limit ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p : limit : p] = b"\x00" * len(range(p * p, limit, p))
    return sum(i for i, is_p in enumerate(sieve) if is_p)


if __name__ == "__main__":
    results = {
        1: problem_001(),
        2: problem_002(),
        3: problem_003(),
        4: problem_004(),
        5: problem_005(),
        6: problem_006(),
        7: problem_007(),
        8: problem_008(),
        9: problem_009(),
        10: problem_010(),
    }
    for num, ans in results.items():
        print(f"Problem {num:02d}: {ans}")
