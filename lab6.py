def lcs_all(X, Y):
    m = len(X)
    n = len(Y)

    # 1. Build the DP table (Same as your original Lab 6 code)
    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    # 2. Recursive function to trace ALL paths backward
    def get_all_lcs(i, j):
        # Base case: If we reach the top or left edge of the table, return an empty string
        if i == 0 or j == 0:
            return {""}

        # Condition 1: If characters match, they are part of the LCS
        if X[i-1] == Y[j-1]:
            # Get the strings from the diagonal cell and append the matching character
            return {seq + X[i-1] for seq in get_all_lcs(i-1, j-1)}
        
        # Condition 2: If characters do NOT match, we check the table to see where the max value came from
        res = set() # We use a set to automatically prevent duplicate strings
        
        # If moving UP gives the same max length, branch out and explore the UP path
        if L[i-1][j] == L[i][j]:
            res.update(get_all_lcs(i-1, j))
            
        # If moving LEFT gives the same max length, branch out and explore the LEFT path
        if L[i][j-1] == L[i][j]:
            res.update(get_all_lcs(i, j-1))
            
        return res

    # 3. Retrieve all unique LCS strings starting from the bottom-right corner
    all_lcs_set = get_all_lcs(m, n)
    
    return L[m][n], list(all_lcs_set)

# --- Output Execution ---
string1 = "PARIJAT"
string2 = "TAJIRAP"
length, sequences = lcs_all(string1, string2)

print(f"String 1: {string1}")
print(f"String 2: {string2}")
print(f"Length of LCS: {length}")
print(f"All Longest Common Subsequences: {sequences}")