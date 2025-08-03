import pandas as pd
import numpy as np


def square_root(n: float) -> float:
    """Вычисляет квадратный корень числа.
    
    Аргументы:
        n: Число для вычисления квадратного корня
        
    Возвращает:
        Квадратный корень входного числа
    """
    return n ** 0.5


def euclidean_distance(series1: pd.Series, series2: pd.Series) -> float:
    """Вычисляет евклидово расстояние между двумя pandas Series.
    
    Аргументы:
        series1: Первый pandas Series
        series2: Второй pandas Series
        
    Возвращает:
        Евклидово расстояние между двумя рядами
    """
    # Векторизованное вычисление более эффективно, чем цикл
    squared_diff = (series1 - series2) ** 2
    return square_root(squared_diff.sum())


def calculate_distances(df: pd.DataFrame, reference_series: pd.Series) -> pd.Series:
    """Вычисляет евклидовы расстояния от опорного ряда ко всем строкам в DataFrame.
    
    Аргументы:
        df: DataFrame, содержащий несколько рядов в строках
        reference_series: Опорный ряд для сравнения
        
    Возвращает:
        Ряд расстояний для каждой строки в DataFrame
    """
    return df.apply(lambda row: euclidean_distance(row, reference_series), axis=1)


def main():
    """Демонстрация вычисления расстояний."""
    # Пример данных
    s1 = pd.Series([2, 4, 6, 8])
    s2 = pd.Series([1, 3, 5, 7])
    
    # Создаем DataFrame с несколькими рядами
    data = {
        'A': [1, 3, 5, 7],
        'B': [2, 4, 6, 8],
        'C': [3, 6, 9, 12]
    }
    df = pd.DataFrame(data)
    
    # Вычисляем расстояние между двумя рядами
    print(f"Расстояние между s1 и s2: {euclidean_distance(s1, s2):.2f}")
    
    # Вычисляем расстояния от s1 до всех строк DataFrame
    distances = calculate_distances(df, s1)
    print("\nРасстояния от s1 до строк DataFrame:")
    print(distances)


if __name__ == "__main__":
    main()
