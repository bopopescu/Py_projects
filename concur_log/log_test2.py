#844
class Test:
    def backspaceCompare(self, S, T):
        i, j = len(S)-1, len(T)-1

        while i >= 0 and j >= 0:
            if S[i] != T[j]:
                if S[i] != '#' and T[j] != '#':
                    return False
                cnt = 0
                while i >=0 and S[i] == '#':
                    i -= 1
                    cnt += 1
                if i - cnt > -1:
                    i -= cnt
                else:
                    i = -1
                cnt = 0
                while j >= 0 and T[j] == '#':
                    j -= 1
                    cnt += 1
                if j - cnt > -1:
                    j -= cnt
                else:
                    j = -1
                if i == -1 and j == -1:
                    return True
                elif i == -1:
                    cnt = 0
                    while j >= 0:
                        if T[j] == '#':
                            cnt +=1
                        else:
                            cnt -= 1
                    return cnt == 0
                elif j == -1:
                    cnt = 0
                    while i >= 0:
                        if S[i] == "#":
                            cnt += 1
                        else:
                            cnt -= 1
                    return cnt == 0

            else:
                i -= 1
                j -= 1
        return i == -1 and j == -1

if __name__ == "__main__":
    test = Test()
    assert test.backspaceCompare("a####","a#b#")== True, "wrong"
#
#242
class Solution():
    def isAnagram(self, s,t):
        return s.sort() == t.sort()
    def isAnagram(self, s,t):
        if len(s) != len(t):
            return False
        dict_s, dict_t = {}, {}
        for i in range(len(s)):
            if