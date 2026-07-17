fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for m in range(5):
    print(m)

for m in range(2, 6):
    print(m)

for m in range(0, 10, 2):
    print(m)


count = 1
while count <= 5:
    print(count)
    count += 1

for num in range(10):
    if num == 5:
        break
    print(num)  


for num in range(5):
    if num == 2:
        continue
    print(num)

for num in range(5):
    print(num)
else:
    print("Loop finished successfully!")

squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(squares)

squares_dict = {x: x ** 2 for x in range(5)}
print(squares_dict)

for numb in range(1, 51):
    print(numb)

    nag = 1
    while nag <= 50:
        print(nag)
        nag += 1

for nut in range(16):
    if nut % 2 == 0:
        continue
    print(nut)

names = ["Alice", "Bob", "Charlie", "David", "Eve"]

for name in names:
    if name == "Charlie":
       print("Found Charlie!")
       break

