def maxArea(height):
    largest_area = 0 
    h1 = len(height)-1
    h0 = 0
        
    while h0 < h1:
        area = min(height[h0], height[h1]) * (h1-h0)   # to find the area of the water, minimum height should be taken, otherwise the water will overflow.
        if area > largest_area:
            largest_area = area
        if height[h0] < height[h1]:
            h0+=1
        else:
            h1-=1
    return largest_area
