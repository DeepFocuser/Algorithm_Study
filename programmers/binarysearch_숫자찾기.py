# https://sangwoo0727.github.io/algorithm/Algorithm-Ublb/
def search_strlen(num): 
    length = len(str(num))
    res = 0 
    for i in range(1, length):
        res += i * (pow(10, i) - pow(10, i - 1))
    res += length * (num - pow(10, length - 1) + 1)
    return res

def solution1(n):

    left = 0
    right =100

    while left < right:
        mid = (left+right) // 2
        temp = search_strlen(mid)

        # print(left, right, temp)
        # lower bounder
        if temp < n:
            left = mid+1
        else: # temp >= n # n보다 같거나 큰값이 처음 나오는 위치 리턴
            right = mid
            answer = right      

    idx = search_strlen(answer) - n + 1
    answer = str(answer)
    return int(answer[-idx])

def solution2(n):

    answer = 0
    digit = 1
    nine = 9
    while n > digit*nine:
        n = n - (digit*nine)
        answer+=nine
        digit+=1
        nine*=10
    
    answer = (answer+1) + (n-1) // digit
    return int(str(answer)[(n-1)%digit])

print(solution1(189))
print(solution2(189))
