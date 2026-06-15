"""Binary search utilities for sorted lists of integers.

This module supports arrays containing duplicate values and provides routines
for locating the first occurrence, last occurrence, and the full index range
of a target integer.
"""

from __future__ import annotations

from typing import Iterable, List, Optional, Tuple


def binary_search_first(numbers: Iterable[int], target: int) -> Optional[int]:
    """Return the first index of target in a sorted integer sequence.

    If the target is not found, return None.
    """
    nums = list(numbers)
    low = 0
    high = len(nums) - 1
    result: Optional[int] = None

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            result = mid
            high = mid - 1

    return result


def binary_search_last(numbers: Iterable[int], target: int) -> Optional[int]:
    """Return the last index of target in a sorted integer sequence.

    If the target is not found, return None.
    """
    nums = list(numbers)
    low = 0
    high = len(nums) - 1
    result: Optional[int] = None

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            result = mid
            low = mid + 1

    return result


def binary_search_range(numbers: Iterable[int], target: int) -> Tuple[Optional[int], Optional[int]]:
    """Return the first and last indices of target in a sorted integer sequence.

    If the target is not found, both values are None.
    """
    first_index = binary_search_first(numbers, target)
    if first_index is None:
        return None, None
    last_index = binary_search_last(numbers, target)
    return first_index, last_index


def binary_search_any(numbers: Iterable[int], target: int) -> Optional[int]:
    """Return any index of target in a sorted integer sequence.

    This is useful when any matching index is sufficient.
    """
    nums = list(numbers)
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid

    return None


def _demo() -> None:
    sample = [1, 1, 2, 2, 2, 3, 5, 5, 7]
    target = 2

    print("Sample list:", sample)
    print(f"Searching for {target}")
    print("First occurrence:", binary_search_first(sample, target))
    print("Last occurrence:", binary_search_last(sample, target))
    print("Range:", binary_search_range(sample, target))
    print("Any occurrence:", binary_search_any(sample, target))


if __name__ == "__main__":
    _demo()
