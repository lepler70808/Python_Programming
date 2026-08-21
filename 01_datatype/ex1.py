# 변수
# 동적 타이핑 언어
a = 2
b = 3
print(a, end="")
print(b)
print(a, b, sep=",")

# a = 2, b = 3 -> a = (2, b) = 3 => syntax error
a = 2, b
print(type(a))
a = 2
b = 3
print(a, b)

x = y = z = 0

a, b = 2, 3  # 튜플 언패킹
print(a, b)

# 값 스왑
temp = a
a = b
b = temp
print(a, b)

a, b = b, a
print(a, b)

# 변수명 규칙 (C와 동일)
# 문자, 숫자, _ 만 가능
# 숫자로 시작 불가
# 대소문자 구분
# 예약어 사용 불가
name2 = "pororo"
_name = "pororo"
이름 = "뽀로로"
print(이름)

student_name = "크롱"
studentName = "크롱"
MAX_COUNT = 100
