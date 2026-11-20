# 🧮 Project Euler: Algorithmic Mathematics & Complexity Optimization

Python implementations of Project Euler problems focused on **number theory, combinatorics, and asymptotic runtime optimization**—reducing naive $O(N)$ and $O(N^2)$ brute-force approaches down to $O(\log N)$ or $O(1)$.

## 📊 Complexity Optimization Summary

| Problem | Mathematical / Algorithmic Insight | Brute-Force | Optimized | Benchmark |
| :--- | :--- | :---: | :---: | :---: |
| **#001: Multiples of 3 or 5** | Arithmetic Progression + Inclusion-Exclusion Principle | $O(N)$ | **$O(1)$** | `0.004 ms` |
| **#002: Even Fibonacci Numbers** | Parity Recurrence Derivation ($E_k = 4E_{k-1} + E_{k-2}$) | $O(N)$ | **$O(\log N)$** | `0.006 ms` |
| **#005: Smallest Multiple** | Prime Factorization & Greatest Common Divisor ($\text{LCM}$) | $O(N \cdot M)$ | **$O(N \log \log N)$** | `0.012 ms` |
| **#010: Summation of Primes** | Sieve of Eratosthenes (Odd-Index Bitmasking) | $O(N\sqrt{N})$ | **$O(N \log \log N)$** | `42.1 ms` |

---

## 🧠 Featured Mathematical Proofs & Derivations

### 1. Problem 1 — Multiples of 3 or 5 ($O(N) \rightarrow O(1)$)
* **Naive Approach:** Loop from $1$ to $999$ checking `i % 3 == 0 or i % 5 == 0` ($O(N)$ time).
* **Mathematical Optimization:** Using the arithmetic series formula $S_k(n) = k \cdot \frac{m(m+1)}{2}$ where $m = \lfloor \frac{n-1}{k} \rfloor$, and applying the **Inclusion-Exclusion Principle**:
  $$\text{Sum} = S_3(N) + S_5(N) - S_{15}(N)$$
* **Result:** Constant $O(1)$ time regardless of whether $N = 10^3$ or $N = 10^{18}$.
* **Code:** [`solutions/problem_001.py`](solutions/problem_001.py)
