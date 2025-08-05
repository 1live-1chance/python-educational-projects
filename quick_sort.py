def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    bigger = [digit for digit in arr if digit > arr[0]]
    less = [digit for digit in arr if digit < arr[0]]
    equal = [digit for digit in arr if digit == arr[0]]    

    return quick_sort(less) + equal + quick_sort(bigger)


def main():
    arr = [1, 2, 3, 4, 5, 6]
    print(quick_sort(arr))


if __name__ == "__main__":
    main()
