import math

class Fare:
    def calculate_fare(self, x1,x2,y1,y2):
        return (math.sqrt(((y2 - y1)**2)+((x2 -x1)**2)))