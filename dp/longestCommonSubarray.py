import numpy as np

def findMaxSubarray(arr1, arr2):
    """
    Kinda just used the idea of https://www.geeksforgeeks.org/longest-common-subarray-in-the-given-two-arrays/
    """
    
    dp = [[{"number": 0, "index": 0} for i in range(len(arr2))] for j in range(len(arr1))]
    result = []
    
    for i, number1 in enumerate(arr1):
        for j, number2 in enumerate(arr2):
            if number2 == number1:
                if j-1 < 0 or i-1 < 0:
                    dp[j][i] = {
                        "number": number1,
                        "index": 1
                    }
                else:
                    dp[j][i] = {
                        "number": number1, 
                        "index": dp[j-1][i-1]["index"] + 1
                    }
    
    maxm = 0
    max_row = 0
    max_col = 0
    for (row,col), marker in np.ndenumerate(np.array(dp)):
        if marker["index"] > maxm:
            maxm = marker["index"]
            max_row = row
            max_col = col
    
    for i in reversed(range(maxm)):
        result.append(dp[max_row-i][max_col-i]["number"])
    
    return maxm, result
    

if __name__ == "__main__":
    A = [1, 2, 8, 2, 1, 2];
    B = [8, 2, 1, 2 ,4, 7 ];

    maxm, result = findMaxSubarray(A,B)
    print(maxm, result)