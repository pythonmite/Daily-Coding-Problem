"""
    Company Name : Uber
    
    Problem Statement : 
        Given an array of integers, return a new array such that each element at index i of the new array is the product of all 
        the numbers in the original array except the one at i.

        For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
        If our input was [3, 2, 1], the expected output would be [2, 3, 6]

"""
import numpy as np


def solution(numbers:list):
    result = list(map(lambda x: np.prod(numbers[:x] + numbers[x+1:]), range(len(numbers))))
    return result


if __name__ == '__main__':
    print(solution(numbers=[1, 2, 3, 4, 5]))
    # [120, 60, 40, 30, 24]
    print(solution(numbers=[3,2,1]))
    # [2,3,6]
 
