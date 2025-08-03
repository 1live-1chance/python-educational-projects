import pandas as pd
import numpy as np
from pandas import Series


def square_root(n: float) -> float:
    """Вычисляет квадратный корень числа."""
    return n ** 0.5


def get_standard_deviation(series: Series) -> float:
    """
    Вычисляет стандартное отклонение для ряда данных.
    
    Args:
        series: Ряд данных
        
    Returns:
        Значение стандартного отклонения
    """
    arithmetic_mean = series.mean()
    squared_deviations = (series - arithmetic_mean) ** 2
    variance = squared_deviations.mean()
    return square_root(variance)


def normalize_column(column: Series) -> Series:
    """
    Нормализует данные в столбце (z-score нормализация).
    
    Args:
        column: Исходный столбец данных
        
    Returns:
        Нормализованный столбец
    """
    mean = column.mean()
    std = get_standard_deviation(column)
    return (column - mean) / std


def min_max_normalize(df: pd.DataFrame) -> pd.DataFrame:
    """
    Применяет min-max нормализацию к DataFrame.
    
    Args:
        df: Исходный DataFrame
        
    Returns:
        Нормализованный DataFrame
    """
    return df.apply(lambda x: ((x.max() - x) / (x.max() - x.min())).round(2))


def main() -> None:
    """Основная функция для выполнения и демонстрации работы."""
    # Создаем тестовый DataFrame
    source_df = pd.DataFrame(np.random.randint(1, 100, 16).reshape(4, 4))
    
    # Нормализуем каждый столбец
    normalized_df = pd.DataFrame()
    for column in source_df:
        normalized_df[column] = normalize_column(source_df[column])
    
    print("Исходный DataFrame:")
    print(source_df)
    
    print("\nZ-score нормализованный DataFrame:")
    print(normalized_df)
    
    print("\nMin-max нормализованный DataFrame:")
    print(min_max_normalize(normalized_df))


if __name__ == "__main__":
    main()
