length = float(input("Please enter the length of the swimming pool: "))
width = float(input("Please enter the width of the swimming pool: "))
shallow_depth = float(input("Please enter the depth of the shallowist part swimming pool: "))
deep_depth = float(input("Please enter the depth of the deepest part swimming pool: "))

surface_area = length*width
volume = surface_area*shallow_depth
volume2 = (surface_area*deep_depth)/2
print("The volume of the swimming pool is: {0} ".format(volume2))
