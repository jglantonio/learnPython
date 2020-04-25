multiples_3 = [x * 3 for x in range(20)]  # write your list comprehension here
print(multiples_3)

scores = {
    "Rick Sanchez": 70,
    "Morty Smith": 35,
    "Summer Smith": 82,
    "Jerry Smith": 23,
    "Beth Smith": 98
}

passed = [i for i,e in scores.items()if e > 65]  # write your list comprehension here
print(passed)
