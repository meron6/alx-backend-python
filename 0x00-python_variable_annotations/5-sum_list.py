#!/usr/bin/env python3
'''Task 5: Complex types - list of floats
'''
from typing import List

def sum_list(input_list: List[float]) -> float:
    '''Computes the sum of a list of floating-point numbers.
    '''
    return float(sum(input_list))

# Example usage:
if __name__ == "__main__":
    example_list = [1.1, 2.2, 3.3]
    result = sum_list(example_list)
    print(f"The sum of {example_list} is {result}")

