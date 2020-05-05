'''
    Company Name : Robinhood

    Problem Statement : 
    Write a program to calculate correlation (without any libraries except for math) for two lists X and Y.
    resource : https://corporatefinanceinstitute.com/resources/knowledge/finance/covariance/
'''
def solution(X, Y=None):
    """ Calculate the covariance matrix for the dataset X """
    if Y is None:
        Y = X
    n_samples = np.shape(X)[0]
    covariance_matrix = (1 / (n_samples-1)) * (X - X.mean(axis=0)).T.dot(Y - Y.mean(axis=0))

    return np.array(covariance_matrix, dtype=float)
    
if __name__ == "__main__":
    import numpy as np
    arr1 = np.array([1692,1978,1884,2151,2519])
    arr2 = np.array([68,102,110,112,154])
    answer = solution(arr1,arr2)
    print(answer)
    # >>> 7284.839999999999