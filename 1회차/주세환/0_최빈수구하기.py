import sys

sys.stdin = open("_최빈수구하기.txt")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sagak = list(map(int, input().split()))
    line_s = []
    shout = []
    for i in sagak:
        line_s.append(sagak.count(i))
    for i in line_s:
            for  j in line_s:
                if i > 2 or i < 2 :
                    shout.append(sagak[j])
    print(shout)
# 수가 몇 번 있는지 카운트 한 후 
# 수가 2보다 작고 2보다 큰경우 값을 출력 할려고 했는데
# 마지막에서 막혔습니다...
# 딕셔너리 값 추가하는 방법이 생각이 안나서 결국 리스트로....