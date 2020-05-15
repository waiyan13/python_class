# # # # # # # a=int(input("What is your fucking number: "))
# # # # # # # b=a%3
# # # # # # # c=a%5
# # # # # # # if(b==0 and c==0):
# # # # # # # 	print("FizzBuzz")
# # # # # # # elif(b==0):
# # # # # # # 	print("Fizz")
# # # # # # # elif(c==0):
# # # # # # # 	print("Buzz")
# # # # # # # else:
# # # # # # # 	print("Chit Lay Yuu Nay Lr?")
# # # # # # a=[0,1,2]
# # # # # # print(a)
# # # # # a=[3,4,5,6,7,8]
# # # # # a.append(9)
# # # # # print(a[-2])
# # # # a=int(input("What is your fucking age: "))
# # # # b=[5,15,17,20]
# # # # if(a>18):
# # # # 	print(b[-1])
# # # # elif(a<=18 and a>15):
# # # # 	print(b[-2])
# # # # elif(a<=15 and a>10):
# # # # 	print(b[1])
# # # # else:
# # # # 	print(b[0])
# # # a=float(input("Your weight in kg: "))
# # # b=float(input("Your height in metre: "))
# # # c=a/b**2
# # # if(c<18.5):
# # # 	print("Underweight")
# # # elif(c>=18.5 and c<=24.9):
# # # 	print("Normal")
# # # elif(c>=25.0 and c<=29.9):
# # # 	print("Overweight")
# # # else:
# # # 	print("Very Overweight")
# # a=float(input("Your Weight in lbs: "))
# # b=float(input("Your Height in in: "))
# # c=a/b**2*703
# # if(c<18.5):
# # 	print("Underweight")
# # elif(c>=18.5 and c<=24.9):
# #  	print("Normal")
# # elif(c>=25.0 and c<=29.9):
# #  	print("Overweight")
# # else:
# #  	print("Very Overweight")
# a=[1,2,3,4,5]
# for x in a:
# 	if(x%2==0):
# 		print(x)
a=[1,2,3]
b=[4,5]
c=[]
c.append(a)
c.append(b)
for x in c:
	for y in x:
		print(y)