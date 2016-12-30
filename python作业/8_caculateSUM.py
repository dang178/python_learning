#__*__coding:utf-8__*__
sum_odd=0
sum_even=0
for i in range(1,101):
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
print("100内的偶数和："+str(sum_even)+",奇数和："+str(sum_odd))
