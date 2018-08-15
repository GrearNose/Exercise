class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        problem url: https://leetcode.com/problems/trapping-rain-water/description/
        problem decription:
            there a row of danks with width of 1 and non-negative height
            (i.e. >=0), after rain, water can be trapped between them if any
            of them form a dent shape. given a row of danks with their height,
            compute how much water at most can be trapped.
        """
        reservoir = 0
        dank, ix_dank = -1, -1
        i = -1 # some lower version might complain no declaration before use.
        for i,h in enumerate(height):
            # Found a dank with height > 0,
            # set it as the left border of the dent to find.
            if ix_dank == -1 and h > 0:
                dank,ix_dank = h,i
            # Found a higher dank, try to compute the collumn of dent on its
            # left side, and then set it as the left border of a new dent to find.
            elif h > dank:
                reserve_seg  = [dank - hi for hi in height[ix_dank+1:i]]
                reservoir   += sum(reserve_seg)
                dank,ix_dank = h,i

        if ix_dank < i:   # the last bar is lower or equal to than h[ix_dank]
            if dank == h: # h is the height of last bar
                reserve_seg = [dank - hi for hi in height[ix_dank+1:]]
                reservoir  += sum(reserve_seg)
            else:         # the last bar is lower than h[ix_dank]
                # overturn this part of the row left side to right side,
                # and deal with it again with this func recursively.
                bars = height[ix_dank:][::-1]
                reservoir += self.trap(bars)

        return reservoir

def test():
    solu = Solution()
    # h1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    h1 = [2,0,2]
    r = solu.trap(h1)
    print(r)


if __name__ == '__main__':
    test()