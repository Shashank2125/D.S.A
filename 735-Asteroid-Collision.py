class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        for asteroid in asteroids:
            while stack  and asteroid<0 and stack[-1]>0:
                if stack[-1]<abs(asteroid):
                    stack.pop()
                    continue
                elif stack[-1]==abs(asteroid):
                    stack.pop()
                    asteroid=0
                    break
                else:
                    asteroid=0
                    break
            if asteroid!=0:
                stack.append(asteroid)
        return stack


        