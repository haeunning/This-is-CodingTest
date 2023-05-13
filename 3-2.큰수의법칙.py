# N: 배열 속 숫자수, M : m개 더하기, K : 연속 가능 횟수

n,m,k = map(int,input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1] #가장 큰 수
second = data[n-2] #두번째로 큰 수

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m==0:
        break
    result += second
    m -= 1
print(result)