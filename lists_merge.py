from typing import List


def merge(first: List[int], second: List[int]) -> List[int]:
    """Merges two sorted lists into one sorted list."""
    result = []
    i = j = 0
    len_first, len_second = len(first), len(second)
    
    while i < len_first and j < len_second:
        if first[i] < second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1
    
    # Add remaining elements (if any)
    result.extend(first[i:])
    result.extend(second[j:])
    return result


def main() -> None:
    """Reads two lists from input, merges them, and prints the result."""
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    merged = merge(first, second)
    print(merged)


if __name__ == "__main__":
    main()