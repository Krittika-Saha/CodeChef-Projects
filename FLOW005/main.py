from itertools import combinations
test_cases = int(input(""))
answers = []
for i in range(test_cases):
    values = int(input(""))
    notes = [1, 2, 5, 10, 50, 100]
    len_of_k = []
    for j in range(6):
        comb = list(combinations(notes, j))
        for k in comb:
            sum = 0
            for l in k:
                sum += l
            if sum == values:
                len_of_k.append(len(k))
    answers.append(min(len_of_k))
for q in answers:
    print(q)
