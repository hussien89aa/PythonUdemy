from functools import  reduce
listItems=[1,2,3,4,5,6,7,8,9,10]
print(listItems)
# without reduce
sum=0
for item in listItems:
    sum=sum+item
print(sum)

# with reduce

sum1= reduce(lambda  x,y:x+y,listItems)
print(sum1)