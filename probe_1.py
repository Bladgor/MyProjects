
n = 5
k = 2
index = 1

num_list = [x for x in range(1, n + 1)]
print(num_list)
i = 0
i = (i + k - 1) % (len(num_list))
print(i)
num_list.remove(i)

print(num_list)
