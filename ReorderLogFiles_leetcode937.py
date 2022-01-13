from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let_log =[]
        digit_log = []
        for log in logs:
            ele = log.split(" ")
            #if "".join(ele[1:]).isnumeric(): # 문자로그는 문자로만 , 숫자로그는 숫자로만
            if log.split()[1].isnumeric():
                digit_log.append(log)
            else:
                let_log.append(log)

        #let_log = sorted(let_log, key=lambda x: (x.split(" ")[1:], x.split(" ")[0])) # 오름차순
        let_log.sort(key=lambda x: (x.split(" ")[1:], x.split(" ")[0]))
        return let_log+digit_log

if __name__ == "__main__":
    sol=Solution()
    print(sol.reorderLogFiles(["dig1 8 1 5 1", "let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
    print(sol.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))

    '''
    Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    
    Input: logs = ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
    Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

    '''
