input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]))-int(ord('a'))+1 #아스키코드로 변환해서 소문자 위치값 구하기

steps = [(-2,1),(-2,-1),(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_col = column + step[1]
    if next_row > 0 and next_row < 8 and next_col > 0 and next_col < 8:
        result += 1

print(result)