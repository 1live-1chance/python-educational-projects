def factorial(n):
    """Вычисляет факториал числа n рекурсивно."""
    return n * factorial(n - 1) if n != 0 else 1


def binomial_coefficient(n, k):
    """
    Вычисляет биномиальный коэффициент C(n, k) = n! / (k! * (n - k)!).
    
    Args:
        n: Общее количество элементов
        k: Количество выбираемых элементов
        
    Returns:
        Биномиальный коэффициент
    """
    numerator = factorial(n)
    denominator = factorial(k) * factorial(n - k)
    return numerator // denominator  # Используем целочисленное деление


def binomial_theorem(n, a, b):
    """
    Раскрывает бином (a + b)^n по формуле бинома Ньютона.
    
    Args:
        n: Степень бинома
        a: Первый член бинома
        b: Второй член бинома
        
    Returns:
        Сумма всех членов разложения
    """
    terms = []
    for k in range(n + 1):
        coeff = binomial_coefficient(n, k)
        a_power = n - k
        b_power = k
        term = coeff * (a ** a_power) * (b ** b_power)
        terms.append(term)
    return sum(terms)


def main() -> int:
    """Основная функция для демонстрации работы кода."""
    # Пример: вычисление (2 + 2)^4 = 256
    print(binomial_theorem(4, 2, 2))
    return 0


if __name__ == "__main__":
    main()
