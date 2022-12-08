'''You are given a task to find all of the whole numbers below 100 that are multiples of both 3 and 5.
Create an array of numbers below 100 that are multiples of both 3 and 5, and output it.'''

import numpy as np
arr=np.array([])
i=0
while i < 100:
    i+=1
    if i%3==0 and i%5 ==0:
        arr=np.append(arr,i)
print(arr)

'''
Answer from site
import numpy as np 
x = np.arange(1,100)

print(x[(x%3==0) & (x%5 ==0)])
'''