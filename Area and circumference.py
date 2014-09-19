import math

radius = float(input("Please enter the radius of the circle in Centimetres: "))
circumference = (radius*2)*math.pi
area = (radius**2)*math.pi
print("The circumference of the circle is: {0}".format(circumference))
print("The area of the circle is: {0}".format(area))
