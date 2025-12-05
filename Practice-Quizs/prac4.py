number = [4, -1, 7, -2, -6, 8]

count = 0

for num in number:
    if num <0:
        count += 1

print("number of -v values:", count)