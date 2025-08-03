def factorial(n):
    return n * factorial(n - 1) \
        if n != 0 else 1


def binomial_coefficient(n, k):
    numerator = factorial(n)
    denominator = factorial(k) * factorial(n - k)
    return numerator / denominator


def binomial_theorem(n, a, b):
    terms = []
    for k in range(n + 1):
        coeff = binomial_coefficient(n, k)
        a_power = n - k
        b_power = k
        term = coeff * a ** a_power * b ** b_power
        terms.append(term)
    return sum(terms)


def main() -> int:
    print(binomial_theorem(4, 2, 2))
    return 0


if __name__ == "__main__":
    main()