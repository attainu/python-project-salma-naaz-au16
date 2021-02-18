import math
def distance(x1,x2,y1,y2):
    #* Distance between two points (x1, y1) and(x2, y2) is sqrt((x1-x2)^2 + (y1-y2)^2)
    c1 = (x1 - x2)
    c2 = (y1 - y2)
    return (math.sqrt((c1*c1)+(c2*c2)))