A, B = map(int, input().split())

for i in range(A, B + 1):
    if i % 2 == 1:          # 2로 나누어 나머지가 1이면 홀수
        print(i, end=' ')   # 줄바꿈 대신 공백(' ')을 두고 이어서 출력