""" Company Name : Stripe
    
    Problem Statement :
        Write a program to generate the partitions for a number n. A partition for n is a list of positive integers that sum up to n. For example: if n = 4, we want to return the following partitions: [1,1,1,1], [1,1,2], [2,2], [1,3], and [4]. Note that a partition [1,3] is the same as [3,1] so only the former is included. 
"""   
def partition(number):
    answer = []
    answer.append((number, ))
    for x in range(1, number):
        for y in partition(number - x):
            answer.append(tuple(sorted((x, ) + y)))
    return answer

if __name__ == '__main__':
    answer = partition(4)
    print(set(answer))