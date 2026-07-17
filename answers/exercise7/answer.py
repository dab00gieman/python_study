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