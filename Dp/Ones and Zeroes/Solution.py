def findMaxForm(strs, m, n):
    if not strs:
        return 0

    # Convert strings to list of (#zeroes, #ones) pairs
    nums = [(s.count('0'), s.count('1')) for s in strs]
    nums.sort()
    if nums[0][0] > m:
        return 0

    # A[i][j] = Tuple (max formed strings, min used zeroes) in
    # examined first i strings and used j ones.
    A = []
    for i in range(len(strs) + 1):
        A.append([(0, 0)] * (n + 1))

    for i, (z, o) in enumerate(nums):
        for j in range(0, n + 1):
            # We just skip this string
            A[i + 1][j] = A[i][j]
            if j - o >= 0:
                (count, zz) = A[i][j - o]
                # We use the string if the usage of zeroes
                # is under limits and number of formed
                # strings can be increased.
                if zz + z <= m and A[i + 1][j][0] < 1 + count:
                    A[i + 1][j] = (1 + count, zz + z)
    print(A)
    return A[len(strs)][n][0]


findMaxForm({'01', '110'}, 5, 1)
