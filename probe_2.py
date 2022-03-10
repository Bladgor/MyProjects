cubs = [x ** 3 for x in range(1, 1000, 2)]
print(cubs)
total = 0
for elem in cubs:
    if sum(map(int, str(elem))) % 7 == 0:
        total += elem

print(total)

# print(len(cubs))
# # cub = sum(map(int, str(cubs)))
# # print(cub)
# # print(str(cubs))
# print(19 ** 3)
