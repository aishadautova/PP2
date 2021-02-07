class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max = -101
 
        a = 0
        h = []
        h.append(a)
        
        for i in range(len(gain)):
            a += int(gain[i])
            h.append(a)
        
        for i in range(len(h)):
            if h[i] > max:
                max = h[i]
        
        return(max)