# 預先建立質數表
WORD_NUM = 62
MAX_SIZE = 2000
prime = [True] * MAX_SIZE
prime[0] = False

for i in range(2, int(MAX_SIZE ** 0.5) + 1):
    if prime[i - 1]:
        # 從 2 到 MAX_SIZE/i 做標記
        for j in range(2, (MAX_SIZE // i) + 1):
            prime[i * j - 1] = False

# 讀入 n 筆測資
n = int(input())
for i in range(1, n+1):
    # 讀入字串 s
    s = input()
    # 計算每個字元的出現次數
    frequency = [0] * WORD_NUM
    for j in range(len(s)):
        # '0' - '9' => 0 - 9
        if '0' <= s[j] <= '9':
            frequency[ord(s[j]) - ord('0')] += 1
        # 'A' - 'Z' => 10 - 35
        elif 'A' <= s[j] <= 'Z':
            frequency[ord(s[j]) - ord('A') + 10] += 1
        # 'a' - 'z' => 36 - 61
        elif 'a' <= s[j] <= 'z':
            frequency[ord(s[j]) - ord('a') + 36] += 1
     # 輸出次數為質數的字元
    print("Case {}: ".format(i), end='')
     # 用來記錄是否有字元次數為質數
    empty = True
    for j in range(WORD_NUM):
        # 如果有字元次數為質數，則輸出
        if frequency[j] and prime[frequency[j] - 1]:
            empty = False
             # 轉換成字元並輸出
            if j < 10:
                print(chr(j + ord('0')), end='')
            elif j < 36:
                print(chr(j - 10 + ord('A')), end='')
            else:
                print(chr(j - 36 + ord('a')), end='')
    if empty:
        print("empty", end='\n')
    print(end='\n') 