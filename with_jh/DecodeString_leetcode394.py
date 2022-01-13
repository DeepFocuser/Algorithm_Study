import re

class Solution:

    def decodeString(self, s: str) -> str:

        '''
        1. 숫자가 나오면 숫자를 하나로 합쳐주고 stack에 넣어준다.
        2. 알파벳이나 '['이 나오면 고대로 stack에 넣어준다.
        3. ']'이 나오면 '[' 전까지 stack.pop해주고 그 결과를 letter 변수에 문자를 더해준다.
        stack.pop의 결과가 '['가 나오면 반복문을 나온 다음에 '['옆에는 반드시 숫자가 있을 것이기 때문에 stack.pop을 해서 letter와 곱해준다.

        "23[ab32[de]]ef" 경우 32[de]를 먼저 decoding한 후 바깥쪽을 적용한다. -> stack을 잘 활용해야한다.
        '''

        stack = []
        p = 0
        while p < len(s):
            if s[p].isdigit():
                num = int(s[p])
                while True:
                    p += 1
                    if s[p].isdigit():
                        num = 10*num + int(s[p])
                    else:
                        break
                stack.append(num)

            elif s[p] == ']':
                letter = ''
                while True:
                    value = stack.pop()
                    if value == '[':
                        break
                    else:
                        letter = value + letter # 앞에 더해 주기 / 나중에 ''.join([e[::-1] for e in stack]) 이거 안하려고.
                stack.append(stack.pop()*letter)
                p+=1
            elif s[p] == '[' or s[p].isalpha(): # 순서대로 더해짐.
                stack.append(s[p])
                p+=1

        return ''.join(stack)

class Solution:
    def decodeString(self, s: str) -> str:
        while "[" in s: # or "]" in s
            s=re.sub('(\d+)\[([a-z]+)\]',lambda ele : int(ele.group(1))*ele.group(2), s)
            print(s)
        return s

if __name__ == "__main__":

    sol = Solution()
    print(sol.decodeString(s = "3[a]2[bc]"))
    print(sol.decodeString(s="23[ab32[de]]ef"))
    print(sol.decodeString(s="2[abc]3[cd]ef"))

