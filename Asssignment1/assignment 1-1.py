print("1. 1번째 n자리 정수 출럭")
x = input("n자리 정수를 입력하세요: ")
print("2. 2번째 n자리 정수 출력")
y = input("n자리 정수를 입력하세요: ")
print("3. 곱셈 결과 출력")

multi = int(x) * int(y)     #multi=x*y
multi_len = len(str(multi)) #length of multi
multi_fixed = multi_len        #변하지않는 multi_len
x_len = len(str(x))         #length of x
y_len = len(str(y))         #length of y

max_len = x_len     #두 자리수 중 더 큰거
if x_len < y_len:
    max_len = y_len
                    #max_len 정하기

if multi == 0:
    multi_len = max_len + 3

elif max_len == multi_len:
    multi_len += 3

x_void = multi_len - x_len
x_head = " " * x_void
y_void = multi_len - y_len - 1
cross = "X"
y_head = " " * y_void

print(x_head + x)       #x 출력
print("X" + y_head + y) #y 출력
#---------------------------
print("-" * multi_len)

if int(y) < 0:
    y_len -= 1

#y 각 자리 숫자 구하기
abs_y = abs(int(y))
num = []
for i in str(int(abs_y)):
    num.append(i)

#while문 시작
i = y_len
tail_len = 0

while i > 0:
    pos = int(num[i - 1])       #자리
    out = pos * int(x)          #숫자
    out_len = len(str(out))     #숫자 길이
    head_len = int(multi_len - out_len - tail_len) #전체 길이 - 숫자길이 - 뒷공백 길이
    out_head = " " * head_len   #앞 공백
    out_tail = " " * tail_len   #뒷 공백
    tail_len += 1               #뒷 공백 개수 증가

    print(out_head + str(out) + out_tail)   #각 줄 출력

    i -= 1
#while문 끝

#---------------------------
print("-" * multi_len)

front = " " * (multi_len - multi_fixed)
print(front + str(multi))