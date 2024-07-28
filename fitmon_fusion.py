"""
Dynamic Programming - Fitmon Fusion
Written by Choong Lee Ann
Version 1.0
"""

def fuse(fitmons):
    """
    This function takes a list of fitmons and returns the maximum cuteness score that can 
    be achieved by fusing all the fitmons. The function uses dynamic programming to solve
    the problem. The function creates a 2D array to store the cuteness score of the fitmons
    that can be fused. The function fills in the diagonal of the 2D array with the fitmons
    and then fills in the rest of the array with the cuteness score of the fitmons that can
    be fused. The function then returns the cuteness score of the final fitmon.
    Written by Choong Lee Ann

    Precondition: fitmons is a non-empty list, 
                adjacent fitmons have the same affinity, 
                only fitmon[0] and fitmon[N] have affinity of 0,
                affinity is a float between 0 and 1 not inclusive,
                cuteness is a non-zero positive integer
    Postcondition: an integer representing the maximum cuteness score that can be achieved by fusing the fitmons

    Input:
        fitmons: is a list of lists, where each list contains 3 integers, [a, b, c], where 
        a is the left affinity
        b is the cuteness, and 
        c is the right affinity of a fitmon
    Return:
        cuteness_score: an integer, the maximum cuteness score that can be achieved by fusing all the fitmons

    Time complexity: 
        Best case analysis: O(N^3), where N is the number of fitmons
        Worst case analysis: O(N^3)
    Space complexity: 
        Input space analysis: O(N)
        Aux space analysis: O(N^2)
    """
    N = len(fitmons)
    # create a 2D array 
    memo = [[0 for _ in range(N)] for _ in range(N)]

    # fill in the first diagonal of the memo matrix
    for i in range(N):
        memo[i][i] = fitmons[i]
    
    # number of fitmons to be fused
    for d in range(2, N+1):
        # starting index of fitmons to be fused
        for i in range(N-d+1):
            # ending index of fitmons to be fused
            j = i + d - 1
            cuteness = 0
            # index of fitmon to be fused
            for n in range(i, j):
                # get the largest cuteness score possible for the fitmon at position i,j 
                if int(((memo[i][n][2] * memo[i][n][1]) + (memo[n+1][j][0] * memo[n+1][j][1]))) > cuteness:
                    cuteness = int(((memo[i][n][2] * memo[i][n][1]) + (memo[n+1][j][0] * memo[n+1][j][1])))
                # set the fitmon with the highest cuteness score at position i,j
                memo[i][j] = [memo[i][n][0], cuteness, memo[n+1][j][2]]

    # get the cuteness score of the final fitmon
    cuteness_score = memo[0][N-1][1]
    return cuteness_score