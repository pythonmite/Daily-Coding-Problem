"""
    Company Name : Google
    
    Problem Statement : 
        Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
        For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17

"""

def solution(number_list:list, target:int):
    answer = False
    result = [(i, target-i) for i in number_list if target-i in number_list]
    if len(result) != 0:
        answer = True
    return (answer, result)


if __name__ == '__main__':

    result = solution([10,15,3,7], 19)
    print(result)
    # For k=19 , (False, [])

    result = solution([10,15,3,7], 17)
    print(result)
    # k=17, (True, [(10, 7), (7, 10)])
