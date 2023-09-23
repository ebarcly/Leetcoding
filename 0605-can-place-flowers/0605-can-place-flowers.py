class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0

        while i < len(flowerbed):
            if flowerbed[i] == 0:
                left_side = (i == 0) or flowerbed[i - 1] == 0
                right_side = (i == len(flowerbed) - 1) or flowerbed[i + 1] == 0

                if left_side and right_side:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n :
                        return True
                    i += 1
            i += 1
        return count >= n
            