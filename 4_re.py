# 보통 형식이 맞는지 확인하기 위해 정규식 사용
import re
# 영어 네 자리 중 세 자리만 알고 있는 상황 ca?e

p = re.compile("ca.e") 
# .은 하나의 문자를 의미
# ^은 문자열의 시작을 의미 (^de -> desk, destination)
# $은 문자열의 끝을 의미 (se$ -> case, base)

def print_match(m):
    if m:
        print(m.group()) # group은 일치하는 문자열만 반환
        print(m.string) # string은 입력받은 문자열을 반환
        print(m.start()) # start는 일치하는 문자열의 시작 idx
        print(m.end()) # end는 일치하는 문자열의 끝 idx
        print(m.span()) # span은 일치하는 문자열의 시작/끝 idx
    else:
        print("매칭되지 않음")
        
# m = p.match("case") # match는 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("good care") # search는 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall("careless") # findall은 일치하는 모든 것을 리스트 형태로 반환
# print(lst)

# 정규식 사용할 때
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열")
# 3. m = p.search("비교할 문자열")
# 4. lst = p.findall("비교할 문자열")

# 원하는 형태 : 정규식
# .은 하나의 문자를 의미 (ca.e -> case, cafe)
# ^은 문자열의 시작을 의미 (^de -> desk, destination)
# $은 문자열의 끝을 의미 (se$ -> case, base)