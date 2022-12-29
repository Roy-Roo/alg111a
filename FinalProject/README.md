# 演算法期末報告

### 題目 : **2022/12/13 CPE** 第2題 ([10789 Prime Frequenc](https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/10789.pdf))

* **問題** : 

  給你一個只有數字及英文字母（0-9、A-Z及a-z）的字串，你需要計算每一個字元出現的頻率，並且判斷哪一個字元出現的頻率是質數。所謂的質數是指可以被 1 和自己整除的數，例如：2、3、5、7、11…等。

* **輸入 **: 

​		輸入的第一列有一個整數 T （1＜T＜201），代表以下有多少組測試資料。每組測試資料一列。每組測試資料		只有數字及英文字母，測試資料的長度大於 0 且小於 2001 。

* **輸出** : 

​		對於每組測資請輸出一列，內容是出現頻率是質數的字元；輸出的順序必需依照 ASCII 值由小到大排列。請參		考 sample input 及 sample output。如果沒有任何字元的出現頻率是質數，請輸出 empty 。



### 參考來源 :

* http://program-lover.blogspot.com/2009/04/prime-frequency.html

* [ChatGPT](https://chat.openai.com/chat)



### 程式碼 : 

* 非原創，將參考來源放進 ChatGPT 後讓其從c++改寫成python，看懂了，修改輸出格式符合cpe的輸出，添加註解後繳交
* 使用埃拉托茨篩法建立質數表

```python
WORD_NUM = 62 # 紀錄出現過的0~9、A~Z、a~z
MAX_SIZE = 2000 # 題目指定的範圍2001以內
prime = [True] * MAX_SIZE # 用於記錄小於MAX_SIZE的自然數是否為質數，長度為MAX_SIZE的bool陣列
prime[0] = False # 1不是質數

# 埃拉托茨篩法建立質數表
# 埃拉托色尼篩法的原理是，只需要將小於等於待求質數的平方根的整數的合數標記為合數即可。因此，只需要迴圈到MAX_SIZE的平方根的整數加1就可以求出所有小於MAX_SIZE的質數。

for i in range(2, int(MAX_SIZE ** 0.5) + 1): # i會在2到MAX_SIZE的平方根的整數加1之間
    if prime[i - 1]: # prime數組的第i-1個元素的值為True
        for j in range(2, (MAX_SIZE // i) + 1): # j會在2到MAX_SIZE除以i的整數加1之間
            prime[i * j - 1] = False # prime的第i*j-1個元素設置為False

n = int(input()) # 輸入有幾串字串
for i in range(1, n+1): # i從第1串字串開始跑到n+1個字串
    s = input() # 輸入字串
    frequency = [0] * WORD_NUM # 將frequency設為長度為WORD_NUM的陣列，並且將所有元素的值初始化為0
    for j in range(len(s)): # j在字串S的長度內迴圈
        if '0' <= s[j] <= '9': # 確認s陣列中的第j位是否為0~9
            frequency[ord(s[j]) - ord('0')] += 1 # 用ord函式取得ASCII碼，減掉0的ascii碼後，便是該字元在frequency陣列中的位置，該位置的元素+1
        elif 'A' <= s[j] <= 'Z': # 確認s陣列中的第j位是否為A~Z
            frequency[ord(s[j]) - ord('A') + 10] += 1 # 用ord函式取得ASCII碼，減掉A的ascii碼後，再+10(0~9)便是該字元在frequency陣列中的位置，該位置的元素+1
        elif 'a' <= s[j] <= 'z': # 確認s陣列中的第j位是否為a~z
            frequency[ord(s[j]) - ord('a') + 36] += 1# 用ord函式取得ASCII碼，減掉A的ascii碼後，再+36(0~9、A~Z)便是該字元在frequency陣列中的位置，該位置的元素+1
    print("Case {}: ".format(i), end='') # 顯示Case i,i為1~n+1
    empty = True # bool，用於記錄frequency中是否有質數出現的次數
    for j in range(WORD_NUM): # j為1~62(0~9、A~Z、a~z)
        if frequency[j] and prime[frequency[j] - 1]:  # 如果該字元出現過且頻率為質數
            empty = False # 設定為出現過字元且頻率為質數
            if j < 10: # 該字元為0~9
                print(chr(j + ord('0')), end='') # j加上0的ASCII碼後根據出現的ASCII碼印出數字
            elif j < 36: # 該字元為A~Z
                print(chr(j - 10 + ord('A')), end='') # j減掉10(0~9)後加上A的ASCII碼根據出現的ASCII碼印出字母
            else: # 該字元為a~z
                print(chr(j - 36 + ord('a')), end='') # j減掉36(0~9、A~Z)後加上a的ASCII根據出現的ASCII碼印出字母
    if empty: # 沒有出現過頻率為質數的字元
        print("empty", end='\n') # 顯示empty
    print(end='\n') # 根據cpe的輸出規定要跳行
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



