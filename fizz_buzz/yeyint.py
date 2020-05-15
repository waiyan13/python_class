a = int(input("number:"))
b = a%3
c = a%5
if (b==0 and c==0):
	print("FizzBuzz")
elif(c==0):
	print("buzz")
else:
	print("none")