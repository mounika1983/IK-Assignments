def my_own_join(list1):
    str1 = ""
    for i in range(0, len(list1)):
        if (i != 0):
            str1 = str1 + " " + list1[i]

        else:
            str1 = str1 + list1[i]

    return str1

class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = s.split()
        list1.reverse()
        str1 = " ".join(list1)
        return str1


