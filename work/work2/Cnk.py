def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def combinations(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))

n = 0
k = 0
print("範例 : C(3, 2)")
for i in range(1, 4):
    for j in range(1, i+1):
        if j == i:
            break
        if n < i:
            n = i
        if k < j:
            k = j
        print(f"[{i}, {j}]")
print(f"C(3, 2) = {combinations(n, k)}")
