numbers = [3, 6, 2, 4, 3, 6, 8, 9]
new_list = []

for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            new_list.append(numbers[i])
            print(numbers[i], "is the duplicate numbers")

print(new_list)

num = [4,9,15,21,34,57,68,91]

for i in range(len(num)):
    if num[i] ==68:
        print(i)
