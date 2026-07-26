class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result=[]
        def backtrack(index,current):
            #base case
            if index==len(digits):
                result.append(current)
                return
            #get the digit from digits ex->digits[0]=2
            digit=digits[index]
            #get letter mapped to digits[n]
            letters=mapping[digit]
            #for every alphabet we backtrack and adjoin letters mapped under two numbers
            for letter in letters:
                backtrack(index+1,current+letter)
        backtrack(0,"")
        return result

        