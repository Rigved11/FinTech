marks=int(input("Enter marks:"))
if marks>=40:
   print("pass")
else:
   print("fail")

marks=int(input("Enter Marks(0-100):"))
if 0<=marks <=100:
   print("Marks are Valid")
else:
   print("Marks are Invalid")   

#if marks>0 and marks <100:
# print("marks are valid") 
# else:
# print("Invalid Marks")  

if marks>=85 and marks<=100:
   print("Excellent")
elif marks<=84 and marks<=60:
   print("Good")
elif marks<=59 and marks>=40:
   print("Average")
else:
   print("Fail")