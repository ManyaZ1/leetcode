class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        left_max = height[L]
        right_max = height[R]
        water = 0
        if left_max>right_max:
            current_bar=height[R]
        else:
            current_bar=height[L]
        while(L<R):
            #water+=(min(left_max,right_max)-current_bar)
            if height[L]>height[R]:
                R-=1
                right_max=max(right_max,height[R])
                water+=(right_max-height[R])
            else:
                L+=1
                left_max=max(left_max,height[L])
                water+=(left_max-height[L])
        return water
        
