import math
can_coverage=5

def can_estimate(height,width):
    can_count=(height*width)/can_coverage
    can_count=math.ceil(can_count)
    print(f"You need {can_count} cans of paint to paint your wall!")

height=int(input("What is the height of the wall in sq.meters?: "))
width=int(input("What is the width of the wall in sq.meters?: "))

can_estimate(height,width)