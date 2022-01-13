import time

class Solution1:

    # 시간초과 코드
    def longestPalindrome(self, s: str) -> str:

        candidate = ''
        if s == s[::-1]:
            return s

        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if len(candidate) >= j - i + 1:
                    continue
                if s[i:j] == s[i:j][::-1]:
                    candidate = s[i:j]

        return candidate

class Solution2:
    
    # 힌트 얻고 작성해본 코드
    def longestPalindrome(self, s: str) -> str:

        candidate = {}
        if s == s[::-1]:
            return s
        else:
            for i in range(len(s)):
                # 2개씩 끊어서 오른쪽으로 한칸씩 이동후 양옆으로 확장하기 / 힌트 얻음
                ls, le=i, i+2
                while ls >= 0 and le<=len(s) and s[ls] == s[le-1]:
                    candidate[s[ls:le]]=1
                    ls-=1
                    le+=1

                # 1개씩 끊어서 오른쪽으로 한칸씩 이동후 양옆으로 확장하기
                ls, le = i, i+1
                while ls >= 0 and le<=len(s) and s[ls] == s[le-1]:
                    candidate[s[ls:le]]=1
                    ls-=1
                    le+=1

        return sorted(candidate.keys(), key=len)[-1]


# 어떤 이가.. 작성한.. 어렵다
class Solution3:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        i,l=0,0
        for j in range(len(s)):
            if s[j-l: j+1] == s[j-l: j+1][::-1]:
                i, l = j-l, l+1
                # print(s[i: i+l])
            elif j-l > 0 and s[j-l-1: j+1] == s[j-l-1: j+1][::-1]:
                i, l = j-l-1, l+2
                # print(s[i: i+l])
        return s[i: i+l]

if __name__ == "__main__":

    # s consist of only digits and English letters.
    start = time.time()
    sol = Solution1()
    # print(sol.longestPalindrome(s = "babad"))
    # print(sol.longestPalindrome(s = "cbbd"))
    # print(sol.longestPalindrome(s = "a"))
    # print(sol.longestPalindrome(s = "ac"))
    # print(sol.longestPalindrome(s = "bb"))
    print(sol.longestPalindrome(s = "xdxtfdaarvvznrptwicdldmrmwbdrmyppvamdvofujthfcmkcugvodmlvubgvodectwzparprifwgwfvddlrfdnrpspirtyvxqvbqiglugbmzoyzcfkvbjdrdqqxxzutebgoacczuhopvzjfrnfsylgfgkbmbjqqyggtdjcvjbvpspkjcezanajjzabfidndfdpkuamwvxrbpxzoivlnkwdxedtfnmvicmzebwktpktokibeycbpqzejddwnvimmbzupyxwmrgdbmcujadfexcchdkfvkxsdwkuwuxzhpnjgmqbmidcwywjgcsbydixyxcclcbrzjvrmlrzgmbviifllouykovscaufvxovwmmgubshtoizbwtcpqzwchtkmkjfneuybfglywfrorhmfdgvjdsmegtoytsivnuaceszpfsxgddbweckgziahkslykgdkztmpapnoyawqtyrdcuzaxcohohapektyfbfhrsdnjbgjvwvqpcikdnlkdogsinkfpymkkdburnbksnqfjgjlacqpfqlhsjhhoccdkrjipqwzsxmpjughaqchzlrqkogkryqkuuxhzchovebzgeekuflcgvxugnxcvugqlstmnljlvxonkybmzjmnsvvwfztcplgikptnppbzeygbmdsyimsntveojwsejmastiovbctdkdlfvpyzihhxishtveflnmamlnzqroxknrrkkfpveyzvvasdznykygrpbfkbinrrvheekeumlvlgalqelspvpiydqkwduckimyhpzsxlcpkbvgwmwnasdxuupdhcmxjoushcvcnjyrmuemuydyywpvzhkxsqszaqhnbhjwsokkpployomoawtr"))
    print("sol1 time :",time.time()-start)

    start = time.time()
    sol = Solution1()
    # print(sol.longestPalindrome(s = "babad"))
    # print(sol.longestPalindrome(s = "cbbd"))
    # print(sol.longestPalindrome(s = "a"))
    # print(sol.longestPalindrome(s = "ac"))
    # print(sol.longestPalindrome(s = "bb"))
    print(sol.longestPalindrome(s = "xdxtfdaarvvznrptwicdldmrmwbdrmyppvamdvofujthfcmkcugvodmlvubgvodectwzparprifwgwfvddlrfdnrpspirtyvxqvbqiglugbmzoyzcfkvbjdrdqqxxzutebgoacczuhopvzjfrnfsylgfgkbmbjqqyggtdjcvjbvpspkjcezanajjzabfidndfdpkuamwvxrbpxzoivlnkwdxedtfnmvicmzebwktpktokibeycbpqzejddwnvimmbzupyxwmrgdbmcujadfexcchdkfvkxsdwkuwuxzhpnjgmqbmidcwywjgcsbydixyxcclcbrzjvrmlrzgmbviifllouykovscaufvxovwmmgubshtoizbwtcpqzwchtkmkjfneuybfglywfrorhmfdgvjdsmegtoytsivnuaceszpfsxgddbweckgziahkslykgdkztmpapnoyawqtyrdcuzaxcohohapektyfbfhrsdnjbgjvwvqpcikdnlkdogsinkfpymkkdburnbksnqfjgjlacqpfqlhsjhhoccdkrjipqwzsxmpjughaqchzlrqkogkryqkuuxhzchovebzgeekuflcgvxugnxcvugqlstmnljlvxonkybmzjmnsvvwfztcplgikptnppbzeygbmdsyimsntveojwsejmastiovbctdkdlfvpyzihhxishtveflnmamlnzqroxknrrkkfpveyzvvasdznykygrpbfkbinrrvheekeumlvlgalqelspvpiydqkwduckimyhpzsxlcpkbvgwmwnasdxuupdhcmxjoushcvcnjyrmuemuydyywpvzhkxsqszaqhnbhjwsokkpployomoawtr"))
    print("sol2 time :",time.time()-start)

    start = time.time()
    sol = Solution3()
    # print(sol.longestPalindrome(s = "babad"))
    # print(sol.longestPalindrome(s = "cbbd"))
    # print(sol.longestPalindrome(s = "a"))
    # print(sol.longestPalindrome(s = "ac"))
    # print(sol.longestPalindrome(s = "bb"))
    print(sol.longestPalindrome(s = "xdxtfdaarvvznrptwicdldmrmwbdrmyppvamdvofujthfcmkcugvodmlvubgvodectwzparprifwgwfvddlrfdnrpspirtyvxqvbqiglugbmzoyzcfkvbjdrdqqxxzutebgoacczuhopvzjfrnfsylgfgkbmbjqqyggtdjcvjbvpspkjcezanajjzabfidndfdpkuamwvxrbpxzoivlnkwdxedtfnmvicmzebwktpktokibeycbpqzejddwnvimmbzupyxwmrgdbmcujadfexcchdkfvkxsdwkuwuxzhpnjgmqbmidcwywjgcsbydixyxcclcbrzjvrmlrzgmbviifllouykovscaufvxovwmmgubshtoizbwtcpqzwchtkmkjfneuybfglywfrorhmfdgvjdsmegtoytsivnuaceszpfsxgddbweckgziahkslykgdkztmpapnoyawqtyrdcuzaxcohohapektyfbfhrsdnjbgjvwvqpcikdnlkdogsinkfpymkkdburnbksnqfjgjlacqpfqlhsjhhoccdkrjipqwzsxmpjughaqchzlrqkogkryqkuuxhzchovebzgeekuflcgvxugnxcvugqlstmnljlvxonkybmzjmnsvvwfztcplgikptnppbzeygbmdsyimsntveojwsejmastiovbctdkdlfvpyzihhxishtveflnmamlnzqroxknrrkkfpveyzvvasdznykygrpbfkbinrrvheekeumlvlgalqelspvpiydqkwduckimyhpzsxlcpkbvgwmwnasdxuupdhcmxjoushcvcnjyrmuemuydyywpvzhkxsqszaqhnbhjwsokkpployomoawtr"))
    print("sol3 time :",time.time()-start)
    '''
    Output: "bab"
    Note: "aba" is also a valid answer.
    
    Output: "bb"
    Output: "a"
    Output: "a"
    Output: "a"
    Output: "bb"
    '''