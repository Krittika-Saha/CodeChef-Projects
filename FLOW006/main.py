test_cases = int(input(""))
sums = []
for i in range(test_cases):
    add_input = input("")
    sum = 0
    for j in add_input:
        sum += int(j)
    sums.append(sum)
for q in sums:
    print(q)