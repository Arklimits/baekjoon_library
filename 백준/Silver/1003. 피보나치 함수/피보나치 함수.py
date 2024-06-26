import sys

dp = [[0, 0] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]

if __name__ == '__main__':
    t = int(sys.stdin.readline())

    for i in range(2, 41):
        if dp[i] == [0, 0]:
            dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
            dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

    for _ in range(t):
        n = int(sys.stdin.readline())

        print(*dp[n])
