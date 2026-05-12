# i=2
# if(i>18):
#     print("eligable")
# else:
#     print("not")
#     tota=0
#     a=4
#     while(i<=10)

# a=["navjot@gmail.com","Satnam@gmail.com","navjot@gmail.com","Armaan@gmail.com","Mannat@gmail.com"]
# b= set(a)
# print(b)


# b=float(input("Enter the Marks: "))
# if(90<=b):
#     print("Grade A")
# elif(80<=b and 90>b):
#     print("Grade b")
# elif(60<=b and 80>b):
#     print("Grade C")
# elif(33<=b and 60>b):
#     print("Grade B")
# else:
#     print("Faliure")

# # Functions with parameter
# def std_name():
#     print("Satnam")
# std_name()

# Satnam= lambda a : a*b
# print(Satnam(8,4))
# file = open("data.txt","r")
# s= file.read()
# print(s)
# file.close()

file = open("data.txt","w")
s= file.write("I'm 20 year old")
print(s)
file.close()