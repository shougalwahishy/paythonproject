x = 5
print (x >3 or x <4)

x = ["apple","banana"]
y = ["apple","banana"]
z = x
print (x is not z)
#returns false because z is the same object as x
print(x is not y)
#returns true because x is not the same object as y,
#even if they have the same content
print(x != y)
#to demonstrate the difference between "is not" and "!=":
#this comparison returns false because x is equal to y 
