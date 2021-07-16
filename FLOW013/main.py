test_cases = int(input(""))
while test_cases:
    N = input("")
    sum = int(N.split()[0]) + int(N.split()[1]) + int(N.split()[2])
    if(sum==180):
        print("YES")
    else:
        print("NO")
    --test_cases