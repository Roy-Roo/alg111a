def C(n, k):
    global selected
    selected = [0] * k
    combinations(0, 1, n, k)

def combinations(i, start, n, k):
  if i == k:
    print(selected)
  else:
    for j in range(start, n+1):
      selected[i] = j
      combinations(i + 1, j + 1, n, k)

C(5, 3)