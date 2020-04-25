# Unzip the cast tuple into two names and heights tuples.

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
aux_heights = []
aux_names = []
names = True
heights = True
# define names and heights here
x = 0
for name, height in cast :
    aux_heights.append(height)
    aux_names.append(name)
    x = x + 1
heights = tuple(aux_heights)
names = tuple(aux_names)

print(names)
print(heights)