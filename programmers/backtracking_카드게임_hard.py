'''
    제일 어려운 문제가 아닐까 싶다.
    backtracking에 대해서 공부하게 된 계기(n-queen 기초부터 )
    + word와 cards의 길이가 다른 경우에도 대응하는 코드를 생각하는데 한참 걸린... 
'''
from collections import defaultdict
def solution(word, cards):

    answer = 0
    word_length = len(word)
    cards_length = len(cards)
    if word_length > cards_length:
        return 0

    word_counter = defaultdict(int) # 1. 단어 개수 체크 변수 - 지금(2022-03-28) 생각해보니 이게 핵심1
    for w in word :
        word_counter[w]+=1 
    column_visitor = defaultdict(bool) # 2. 방문 여부 체크 변수

    def find(word_index=0, row=0):

        nonlocal answer # 3. nonlocal 키워드 유용 - 바깥 answer 사용하기
        if word_index == word_length:
            answer+=1
            return 

        if row == cards_length:
            return 

        for i, c in enumerate(cards[row]):

            if column_visitor[i] or word_counter[c]==0: 
                continue
            
            # 선택하는 경우
            column_visitor[i]=True
            word_counter[c]-=1
            find(word_index+1, row+1)
            column_visitor[i]=False
            word_counter[c]+=1

        # (2022-03-29) 아니 어렵다....
        # 핵심2 - 예제3 같은 경우를 대비해야 한다. / word의 길이와 cards의 길이가 다른 경우 -> 어려웠다.
        # word cards의 길이가 같은 경우는 아래 코드 필요 없고, 22,23번줄도 필요 없음
        find(word_index, row+1) # word 소비는 하지않고, row만 한개 늘림 - 22번,23번줄 필요 
    find()
    return answer

# 문제 cards에서 word를 가능하게 찾기 / 행단 문자 한개, 같은 열 안됨. 
print(solution(word = "APP" , cards = ["AVV", "XPP", "XPP"])) # 1 - 예제1
print(solution(word = "APPLE" , cards = ["LLZKE", "LCXEA", "CVPPS", "EAVSR", "FXPFP"])) # 3 - 예제2
print(solution(word = "BAB" , cards = ["ZZBZ", "BAZB", "XBXB", "XBAX"])) # 4 - 예제3 / 아 이것도 만만치 않네.


