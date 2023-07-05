#1 : 반복문
def factiorial_interative(n):
    result=1
    for i in range(1,n+1):
        result*=1
    return result

#2 : 재귀함수 n*(n-1)!
def factorial_recursive(n):
    if n<=1:
        return 1
    return n*factorial_recursive(n-1)