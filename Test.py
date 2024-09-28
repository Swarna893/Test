# Test


'''
3+4=7
1.charater(a,b,c,d,etc)
2.integer(1,2,3,4,etc)
3.floating point(1.78,6.98,etc)

sum --> +
sub --> -
multiplication --> *
division --> /
'''
print(":Summation:")
A = int(input("Enter the first value: "))
B = int(input("Enter the second value: "))
C = A+B
print("The sum value of the two numbers is", C)

print(":Multiplication Table:")
# 1 2 3 4 5 6 7 8 9 10

number = int(input("Enter the number: "))
for i in range(1,11):
  print(i,"x",number,"=",i*number)


print("MARKSHEET")
total_marks = 500
beng = int(input("Enter the marks of bengali: "))
eng = int(input("Enter the marks of english: "))
math = int(input("Enter the marks of math: "))
bio = int(input("Enter the marks of bio: "))
sci = int(input("Enter the marks of science: "))
total = beng+eng+math+bio+sci
print("Your total is: ", total)
percentage = (total/total_marks)*100
print("Your percentage is: ", percentage)
if percentage >= 90:
  print("Your grade is AA.")
elif percentage >= 80 and percentage < 90:
  print("Your grade is A+.")
elif percentage >= 70 and percentage < 80:
  print("Your grade is A.")
elif percentage >= 60 and percentage < 70:
  print("Your grade is B+.")
elif percentage >= 50 and percentage < 60:
    print("Your grade is B.")
elif percentage >= 40 and percentage < 50:
  print("Your grade is C+.")
elif percentage >= 30 and percentage < 40:
  print("Your grade is C.")
else:
  print("FAIL.....!!!!")
