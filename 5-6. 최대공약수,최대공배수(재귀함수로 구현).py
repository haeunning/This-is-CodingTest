# 유클리드 호제법 아이디어를 이용한 코드 구현
# 최대공약수
def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
# 최소공배수
def lcm(a, b):
    return (a * b) // gcd(a, b)