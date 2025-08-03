import pandas as pd


def square_root(n):
    return n ** 0.5


def euclidean_distance(series_first, series_second):
    collector = ()
    for pair in zip(series_first, series_second):
        collector = collector + ((pair[0] - pair[1]) ** 2,)
    return square_root(sum(collector))


if __name__ == "__main__":
    s1 = pd.Series([2, 4, 6, 8])
    s2 = pd.Series([1, 3, 5, 7])

    print(euclidean_distance(s1, s2))
