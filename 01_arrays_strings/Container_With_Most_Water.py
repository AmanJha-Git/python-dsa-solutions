class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            
            current_area = width * h
            max_water = max(max_water, current_area)
            
            # Move the pointer of the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water


if __name__ == "__main__":
    solver = Solution()
    
    print("--- Container With Most Water Simulator ---")
    user_input = input("Enter heights separated by spaces: ")
    
    test_heights = [int(x) for x in user_input.split()]
    
    output = solver.maxArea(test_heights)
    
    print(f"\nYour heights list: {test_heights}")
    print(f"Maximum water container area: {output}")
       
        