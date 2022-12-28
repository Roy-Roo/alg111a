# 演算法期末報告

### 題目 : **2022/12/13 CPE** 第4題 ([10789 Prime Frequenc](https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/10789.pdf))

給定一個只包含字母數字（0-9，A-Z和a-z）的字符串，必須計算所有字符的頻率（字符出現的次數），並僅報告頻率為質數的字符。質數是一個只能被兩個不同整數整除的數。一些質數的例子是2，3，5，7，11等。



### 參考來源 :

* http://program-lover.blogspot.com/2009/04/prime-frequency.html

* ChatGPT



### 程式碼 : 

* 非原創，照著參考來源並詢問 ChatGPT 後從c++改寫成python
* 創建2000範圍內的質數表，及取得字元的ASCII碼ord函數為 ChatGPT 產生後直接複製貼上
* 使用埃拉托茨篩法建立質數表

```python
WORD_NUM = 62
MAX_SIZE = 2000
prime = [True] * MAX_SIZE
prime[0] = False

for i in range(2, int(MAX_SIZE ** 0.5) + 1):
    if prime[i - 1]:
        for j in range(2, (MAX_SIZE // i) + 1):
            prime[i * j - 1] = False

n = int(input())
for i in range(1, n+1):
    s = input()
    frequency = [0] * WORD_NUM
    for j in range(len(s)):
        if '0' <= s[j] <= '9':
            frequency[ord(s[j]) - ord('0')] += 1
        elif 'A' <= s[j] <= 'Z':
            frequency[ord(s[j]) - ord('A') + 10] += 1
        elif 'a' <= s[j] <= 'z':
            frequency[ord(s[j]) - ord('a') + 36] += 1
    print("Case {}: ".format(i), end='')
    empty = True
    for j in range(WORD_NUM):
        if frequency[j] and prime[frequency[j] - 1]:
            empty = False
            if j < 10:
                print(chr(j + ord('0')), end='')
            elif j < 36:
                print(chr(j - 10 + ord('A')), end='')
            else:
                print(chr(j - 36 + ord('a')), end='')
    if empty:
        print("empty", end='\n')
    print(end='\n')
```



### 輸出 : 

*  cpe標準測資

```
羅彥翔@MSI MINGW64 /d/大三/alg/FinalProject (master)
$ python final.py
3 
ABCC
Case 1: C
AABBBBDDDDD
Case 2: AD
ABCDFFFF
Case 3: empty
```



