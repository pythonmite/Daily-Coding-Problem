'''
    Company Name : Uber.
    
    Problem Statement : 
        Given a list of positive integers, return the maximum increasing subsequence, that is, the largest increasing subsequence within the array that has the maximum sum. Examples: if the input is [5, 4, 3, 2, 1] then return 5 (since no subsequence is increasing), if the input is [3, 2, 5, 7, 6] return 15 = 3 + 5 + 7, etc.
'''

def solution(arr):
    n = len(arr)
    new_list = []
    for i in range(n-1,0,-1):
        if arr[i] > arr[i-1]:
            new_list.append(arr[i])
    return (new_list)

if __name__ == '__main__':
    answer = solution([3, 2, 5, 7, 6])
    print(answer)
    # >>> 15 = 3 + 5 + 7