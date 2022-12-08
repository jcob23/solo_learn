'''he given code includes a list of heights for various basketball players.
You need to calculate and output how many players are in the range of one standard deviation from the mean.'''

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
mean=sum(players)/10
x=0
i=0
j=0
height=0
while i <10:
    x+=((players[i]-mean)**2)
    i+=1
Standard_deviation=(x/10)**0.5
while j<10:
    if(players[j]<=mean+Standard_deviation and players[j]>= mean-Standard_deviation):
        height+=1
    j+=1
print(height)