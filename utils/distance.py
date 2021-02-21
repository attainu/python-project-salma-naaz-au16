import math

class Distance:
    
    def calculate_distance(self, x1,y1,x2,y2):
        # Distance between two points (x1, y1) and(x2, y2) is sqrt((x1-x2)^2 + (y1-y2)^2)
        c1 = (x1 - x2)
        c2 = (y1 - y2)
        return (math.sqrt((c1**2)+(c2**2)))