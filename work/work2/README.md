# HW 2 請列舉所有的組合 C(n,k) 種



參考 : https://gitlab.com/cccnqu111/alg/-/tree/master/08a-enumerate



### 系統式列舉

```python
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
```

* 輸出 : 

```
羅彥翔@MSI MINGW64 /d/大三/alg (master)
$ C:/Users/88693/AppData/Local/Microsoft/WindowsApps/python3.10.exe d:/大三/alg/work/work2/Cnk.py
[1, 2, 3]
[1, 2, 4]
[1, 2, 5]
[1, 3, 4]
[1, 3, 5]
[1, 4, 5]
[2, 3, 4]
[2, 3, 5]
[2, 4, 5]
[3, 4, 5]
```

### 隨機式列舉

```python
import random

randomnum1=random.randint(1,10)
randomnum2=random.randint(1,randomnum1)  

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

C(randomnum1, randomnum2)
```

* 輸出 : 

```
羅彥翔@MSI MINGW64 /d/大三/alg (master)
$ C:/Users/88693/AppData/Local/Microsoft/WindowsApps/python3.10.exe d:/大三/alg/work/work2/Cnkrandom.py
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 6]
[1, 2, 3, 4, 7]
[1, 2, 3, 5, 6]
[1, 2, 3, 5, 7]
[1, 2, 3, 6, 7]
[1, 2, 4, 5, 6]
[1, 2, 4, 5, 7]
[1, 2, 4, 6, 7]
[1, 2, 5, 6, 7]
[1, 3, 4, 5, 6]
[1, 3, 4, 5, 7]
[1, 3, 4, 6, 7]
[1, 3, 5, 6, 7]
[1, 4, 5, 6, 7]
[2, 3, 4, 5, 6]
[2, 3, 4, 5, 7]
[2, 3, 4, 6, 7]
[2, 3, 5, 6, 7]
[2, 4, 5, 6, 7]
[3, 4, 5, 6, 7]
```

```
羅彥翔@MSI MINGW64 /d/大三/alg (master)
$ C:/Users/88693/AppData/Local/Microsoft/WindowsApps/python3.10.exe d:/大三/alg/work/work2/Cnkrandom.py
[1, 2]
[1, 3]
[1, 4]
[1, 5]
[1, 6]
[2, 3]
[2, 4]
[2, 5]
[2, 6]
[3, 4]
[3, 5]
[3, 6]
[4, 5]
[4, 6]
[5, 6]
```

