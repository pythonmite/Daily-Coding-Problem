'''
    Company Name : Robinhood

    Problem Statement : 
    Write a program to calculate correlation (without any libraries except for math) for two lists X and Y.
    resource : https://corporatefinanceinstitute.com/resources/knowledge/finance/covariance/
'''
def mean(arr,n):
    n = len(arr)    
    sum = 0
    for i in range(0,n):
        sum += arr[i]
    mean = sum / n
    return mean

def solution(arr1,arr2):
    n = len(arr1)    
    sum = 0
    for i in range(0,n):
        sum +=(arr1[i]- mean(arr1,n)) * (arr2[i]- mean(arr2,n))
    
    covariance = sum / n-1
    return covariance
    

if __name__ == "__main__":
    arr1 = [1692,1978,1884,2151,2519]
    arr2 = [68,102,110,112,154]
    answer = solution(arr1,arr2)
    print(answer)
    # >>> 7284.839999999999