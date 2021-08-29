my_list_of_cubes = []
add_my_list_of_cubes = []
all_sum = 0

for i in range(1, 1001, 2):
    my_list_of_cubes.append(i ** 3)

for ind, val in enumerate(my_list_of_cubes):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += my_list_of_cubes[ind]

print(all_sum)

for m in my_list_of_cubes:
    add_my_list_of_cubes.append(m + 17)

all_sum = 0

for ind, val in enumerate(add_my_list_of_cubes):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += add_my_list_of_cubes[ind]

print(all_sum)