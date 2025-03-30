# Time Complexity: O(n) 
# Space Complexity O(1)
def maxArea(height):
    # For left : max line closest to 0 
    # For right: max line closest to len(n)-1
    # if max line found closer in, we calculate candidate area anc check to see if its greater than current max area 

    i = 0 
    j = len(height) -1
    max_Area = 0

    while i<j: 
        current_Area = min(height[i],height[j])*(j-i)
        if current_Area > max_Area: 
            max_Area = current_Area 

        if height[i] >= height[j]: 
            j-=1
        else: 
            i+=1
    
    return max_Area