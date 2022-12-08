'''We have a report on the number of flu vaccinations in a class of 20 people.

It has the following numbers:
never: 5
once: 8
twice: 4
3 times: 3
Task 1
What is the mean number of times those people have been vaccinated?
Output the result using the print() statement.
'''

vac_nums = [0,0,0,0,0,
            1,1,1,1,1,1,1,1,
            2,2,2,2,
            3,3,3
            ]
#your code goes here
summ=sum(vac_nums)
print(summ/20)

'''
Task 2 Calculate and output the variance.
We will soon learn about easier ways to calculate the variance and other summary statistics using Python. For now, use Python code to calculate the result using the corresponding equation.
'''
vac_nums = [0,0,0,0,0,
            1,1,1,1,1,1,1,1,
            2,2,2,2,
            3,3,3
            ]
#your code goes here
x=0
i=0
mean=sum(vac_nums)/20
while i <20:
    x+=((vac_nums[i]-mean)**2)
    i+=1
print(x/20)