#!/usr/bin/python
# -*- coding: UTF-8 -*-
print ("02--------------------------------------------------------")
i = int(input('净利润:'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for idx in range(0, 6):
    if i > arr[idx]:
        r += (i - arr[idx]) * rat[idx]
        print((i - arr[idx] ) * rat[idx])
        i = arr[idx]
print (r)

print ("100--------------------------------------------------------")
i = ['a', 'b']
l = [1,  3]
print (dict([i,l]))

"""

i = int(input('净利润:'))
arr = [0,100,200,400,600,1000]
rat = [0,0.01,0.02,0.03,0.04,0.05,0.1]
result = 0
for idx in range(1,5):
#    print(idx, "  ", rat[idx], "   ", result)
    if i <= arr[idx]:
        result +=  ( i -arr[idx-1])  * rat[idx]
        print(idx, "  ", rat[idx], "   ", result)
        break
    else:
        result += (arr[idx] - arr[idx - 1]) * rat[idx]
        print(idx, "  ",rat[idx],"   ", result)
#        i = arr[idx]
print (result)
"""