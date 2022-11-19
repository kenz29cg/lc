# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = int(1);
        high = int(n);
        while(low <= high):
            mid = (high + low) / 2; 
            if (guess(mid) == 0):
                return mid;
            elif (guess(mid) > 0):
                low = mid + 1;
            else:
                high = mid - 1;
        return -1;
