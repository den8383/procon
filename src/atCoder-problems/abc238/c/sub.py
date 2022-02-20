N = int(input())
#パターンに分ける
ans = 0
mod = 998244353
#def cul(x):
    #S = min(10 ** x - 1, N - (10 ** (x - 1) - 1))
    #T = min(10 ** x, N - (10 ** (x - 1) - 2))
    #return (S * T) // 2
ans = 0
l = 0
#print(ans)
while N >= 10 ** l:
    if N < 10 ** (l+1):
        K = N - 10 ** (l) + 1
        print((K * (K + 1)) // 2)
        ans += (K * (K + 1)) // 2
        ans %= mod
    else:
        K = 10 ** (l + 1) - 10 ** (l)
        ans += (K * (K + 1)) // 2
        ans %= mod
    l += 1
    #print(l,ans)
print(ans)
