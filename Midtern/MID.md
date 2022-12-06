# 期中專案



### 題目 : 

取自 CPE d261. 11000 (2022/05/24 考古題 第二題) https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/11000.pdf

https://github.com/Roy-Roo/alg111a/blob/main/Midtern/mid1.jpg



第一隻的母蜂不會死亡，母蜂可以生一隻公蜂，公蜂可以生一隻母蜂一隻公蜂，並且生完後就死亡，計算出N年後，有多少隻蜜蜂。





### 暴力法

* 本程式為原創

```c++
#include <iostream>
using namespace std;

int main()
{
	int n;
	
	while(cin >> n)
	{
		if(n == -1) break;
		
		long long w = 1, m = 0, x;
		
		for(int i=0; i<n; i++)
		{
			x = m;
			m = w + m;
			w = x + 1;
		}
		
		cout << m << " " << w+m << "\n";
	}
}
```







### 動態規劃

* 非原創，為複製貼上，以下為來源
* https://knightzone.studio/2012/10/20/1957/uva%EF%BC%9A12459%EF%BC%8Dbees-ancestors/



```c++
#include<iostream>
#include<cstdio>
using namespace std;

long long f[60],m[60];	/*創建兩個矩陣來存公蜂與母蜂*/

int main(){
  
	m[1] = 1LL,m[0] = 0LL;	/*母蜂先放入一隻不會死的，公蜂設為0*/
  	for( int i = 2 ; i < 60 ; i++ )		
    	m[i] = m[i-2] + m[i-1] + 1LL;	/*前面的值運算到現在並儲存*/
  	int n;
    while( scanf( "%d", &n ) && n != -1 )	/*偵測是不是結尾*/
    	printf("%lld %lld\n", m[n], m[n+1]);
    
  	return 0;
}
```

