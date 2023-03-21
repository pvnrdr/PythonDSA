class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def __gt__(self,other_circle):
        if self.radius > other_circle.radius:
            return True
        else:
            return False


if __name__ == "__main__":
    radius_1 = int(input("Enter the radius 1 for the circle"))
    radius_2 = int(input("Enter the radius 2 for the other circle"))
    circle_1 = Circle(radius_1)
    circle_2 = Circle(radius_2)
    print(circle_1.radius > circle_2.radius)
