class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        current_s=""
        number=0
        for ch in s:
            if ch.isdigit():
                number=number*10+int(ch)
            elif ch=="[":
                stack.append((current_s,number))
                current_s=""
                number=0
            elif ch.isalpha():
                current_s+=ch
            elif ch=="]":
                previous,repeat=stack.pop()
                current_s=previous+(current_s*repeat)
        return current_s
        