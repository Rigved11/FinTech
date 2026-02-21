numbers=[]
for i in range(5):
 num=int(input("Enter number:"))
 numbers.append(num)

total=sum(numbers)
mean=total/len(numbers)

print("Mean:",mean)    
print("Total:",total)    


#total = 0
#for i in range(5):
   # num = int(input("Enter number: "))
    #total = total + num
#print("Total:", total)
