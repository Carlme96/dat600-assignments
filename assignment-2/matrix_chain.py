def get_m_s(matrices):
    n = len(matrices)
    m = [[0]*x for x in range(n, 0, -1)]
    s = [[0]*x for x in range(n, 0, -1)]

    for l in range(1, n+1):
        for i in range(0, n-l):
            j = i+l
            ij = n-j-1
            m[i][ij] = float('inf')
            for k in range(i, j):
                ik = n-k-1
                q = m[i][ik] + m[k+1][ij] + matrices[i][0]*matrices[k][1]*matrices[j][1]
                if q < m[i][ij]:
                    m[i][ij] = q
                    s[i][ij] = k+1

    return m, s
                

def print_optimal_parentheses(s, i, j):
    if i == j:
        print(f"A{i+1}", end="")
    else:
        ij = len(s)-j-1
        print("(", end="")
        print_optimal_parentheses(s, i, s[i][ij]-1)
        print_optimal_parentheses(s, s[i][ij], j)
        print(")", end="")



if __name__ == "__main__":
    # Example usage
    matrices = [
        (10, 5),
        (5, 7),
        (7, 12),
        (12, 20),
        (20, 10)
    ]
    m, s = get_m_s(matrices)
    print_optimal_parentheses(s, 0, len(matrices)-1)