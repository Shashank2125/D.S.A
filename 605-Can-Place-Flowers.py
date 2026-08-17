class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        plant = 0

        if n == 0:
            return True

        for i in range(len(flowerbed)):

            if flowerbed[i] == 0:
                left = (i == 0 or flowerbed[i - 1] == 0)
                right = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

                if left and right:
                    flowerbed[i] = 1
                    plant += 1

                    if plant >= n:
                        return True

        return False