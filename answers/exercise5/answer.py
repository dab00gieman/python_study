weirdo_1 = {"shapes": "triangle", "sides": 3}
print(weirdo_1["shapes"])
print(weirdo_1.get("fast", "sluggish"))
weirdo_1["shapes"] = "square"
weirdo_1["x_position"] = 0
print(weirdo_1["shapes"])
del weirdo_1["shapes"]
print(weirdo_1["sides"])

fruits = {"apple", "banana", "orange", "almond", "apple"}
print(sorted(fruits))

m = {1, 2, 3}
n = {3, 4, 5}

print(m | n)
print(m & n)
print(m - n)

michael = {"michael.": "python && rust",}
print(michael["michael."])
print(michael.get("car"))

cars = {"bmw", "audi", "mercedes_benz", "koineggseg", "pagani", "audi", "bmw"}
print(sorted(cars))

