length = float(input("Please enter the length of the garden in metres: "))
width = float(input("Please enter the width of the garden in metres: "))
area = (length-1)*(width-1)
cost = area*10
print("The area of your garden is: {0}".format(area))
print("The cost to lay grass on your garden is : £{0}".format(cost))

