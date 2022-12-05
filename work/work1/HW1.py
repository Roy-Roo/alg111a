import time

time_start = time.time() #開始計時

x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0

for a in range(0, 70):
    for b in range(0, 70):
        for c in range(0, 70):
            for d in range(0, 70):
                for e in range(0, 70):
                    if(5*a+7*b+9*c+2*d+1*e <= 250 and 18*a+4*b-9*c+10*d+12*e <= 285 and 4*a+7*b+3*c+8*d+5*e <= 211 and 5*a+13*b+16*c+3*d-7*e <= 315):
                        if(7*a+8*b+2*c+9*d+6*e >= 7*x1+8*x2+2*x3+9*x4+6*x5):
                            x1 = a
                            x2 = b
                            x3 = c
                            x4 = d
                            x5 = e
                        else: 
                            break
                    else:
                        break

time_end = time.time()    #結束計時
time_c= time_end - time_start   #執行所花時間

print(7*x1+8*x2+2*x3+9*x4+6*x5)
print([x1, x2, x3, x4, x5], sep = " , ")
print('time cost', time_c, 's')

