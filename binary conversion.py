number = int(input("enter a number:"))
remainder = 0
x = ""
n = number 

while n > 0: 
    remainder = (n%2)
    x = str(remainder) + x
    n = n//2
  
print(x, "is the binary of", number) 