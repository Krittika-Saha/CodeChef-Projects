test_cases = int(input(""))
sums = []
for i in range(test_cases):
    add_input = input("")
    sums.append((int(add_input.split()[0]) + int(add_input.split()[1])))
for i in sums:
    print(i)
