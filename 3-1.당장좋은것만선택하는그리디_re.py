#거스름돈-동전의 최소 개수
N = int(input())
count = 0
coins = [500,100,50,10]

for coin in coins:
    count += N//coin
    N %= coin

print(count)